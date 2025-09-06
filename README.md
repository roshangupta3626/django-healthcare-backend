Django Healthcare Backend

A secure and scalable healthcare backend API built with Django, Django REST Framework, and PostgreSQL.
Supports JWT authentication, patient/doctor management, and patient-doctor mappings.
Features

User authentication with JWT

CRUD APIs for patients and doctors

Assign doctors to patients

PostgreSQL with Django ORM

⚙️ Setup
git clone https://github.com/your-username/django-healthcare-backend.git
cd django-healthcare-backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

API Endpoints

POST /api/auth/register/ – Register

POST /api/auth/login/ – Login (JWT)

POST /api/patients/ – Add patient

POST /api/doctors/ – Add doctor

POST /api/mappings/ – Assign doctor to patient

⚡ Built with Django + DRF + PostgreSQL
