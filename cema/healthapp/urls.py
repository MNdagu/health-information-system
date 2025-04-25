from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router for the API
router = DefaultRouter()
router.register(r'programs', views.HealthProgramViewSet, basename='api-program')
router.register(r'clients', views.ClientViewSet, basename='api-client')
router.register(r'enrollments', views.EnrollmentViewSet, basename='api-enrollment')

# URL patterns for the web interface
urlpatterns = [
    # Web views
    path('', views.home_view, name='home'),
    path('programs/', views.HealthProgramListView.as_view(), name='program-list'),
    path('programs/create/', views.HealthProgramCreateView.as_view(), name='program-create'),
    path('clients/', views.ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
    path('clients/create/', views.ClientCreateView.as_view(), name='client-create'),
    path('clients/<int:pk>/enroll/', views.enroll_client, name='client-enroll'),

    # API endpoints
    path('api/', include(router.urls)),
]