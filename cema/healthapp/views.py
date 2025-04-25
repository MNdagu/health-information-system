from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from rest_framework import viewsets

from .models import HealthProgram, Client, Enrollment
from .serializers import HealthProgramSerializer, ClientSerializer, EnrollmentSerializer

# Create your views here.

# Home View
def home_view(request):
    context = {
        'programs_count': HealthProgram.objects.count(),
        'clients_count': Client.objects.count(),
        'enrollments_count': Enrollment.objects.count(),
    }
    return render(request, 'healthapp/home.html', context)

# Health Program Views
class HealthProgramListView(ListView):
    model = HealthProgram
    template_name = 'healthapp/program_list.html'
    context_object_name = 'programs'

class HealthProgramCreateView(CreateView):
    model = HealthProgram
    fields = ['name', 'description']
    template_name = 'healthapp/program_form.html'
    success_url = reverse_lazy('program-list')

# Client Views
class ClientListView(ListView):
    model = Client
    template_name = 'healthapp/client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Client.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(email__icontains=query) |
                Q(phone_number__icontains=query)
            )
        return Client.objects.all()

class ClientDetailView(DetailView):
    model = Client
    template_name = 'healthapp/client_detail.html'
    context_object_name = 'client'

class ClientCreateView(CreateView):
    model = Client
    fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'email']
    template_name = 'healthapp/client_form.html'
    success_url = reverse_lazy('client-list')

# Enroll Client in Program
def enroll_client(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        program_id = request.POST.get('program')
        if program_id:
            program = get_object_or_404(HealthProgram, pk=program_id)
            Enrollment.objects.create(client=client, program=program)
            messages.success(request, f'{client} has been enrolled in {program}')
        else:
            messages.error(request, 'Please select a program')
        return redirect('client-detail', pk=pk)

    enrolled_ids = client.programs.values_list('id', flat=True)
    available_programs = HealthProgram.objects.exclude(id__in=enrolled_ids)
    return render(request, 'healthapp/enroll_client.html', {
        'client': client,
        'available_programs': available_programs
    })

# API ViewSets
class HealthProgramViewSet(viewsets.ModelViewSet):
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
