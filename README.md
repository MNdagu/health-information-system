# CEMA Health Information System

CEMA HIS is a Django-based health information system that allows healthcare providers to manage programs, clients, and program enrollments.

## Features

- Health Program Management
  - Create and list health programs
  - Track program descriptions and enrollment status
- Client Management
  - Register new clients with personal information
  - Search clients by name, email, or phone number
  - View detailed client profiles
- Enrollment Management
  - Enroll clients in health programs
  - Track enrollment status and dates
  - View client enrollment history
- REST API
  - Full API support for programs, clients, and enrollments
  - Browse API endpoints at `/healthapp/api/`

## Technology Stack

- Python 3.10
- Django 5.2
- Django REST Framework
- Bootstrap 5.3
- SQLite

## Project Structure

```
cema/
├── healthapp/           # Main application
│   ├── templates/      # HTML templates
│   ├── models.py       # Database models
│   ├── views.py        # View controllers
│   ├── urls.py         # URL routing
│   └── serializers.py  # API serializers
└── cema/               # Project configuration
    ├── settings.py     # Django settings
    └── urls.py         # Main URL routing
```

## API Endpoints

- `/healthapp/api/programs/` - Health programs
- `/healthapp/api/clients/` - Client information
- `/healthapp/api/enrollments/` - Program enrollments