# 📝 To-Do App with Role-Based Access Control

This is a Django-based To-Do application that supports user roles (Admin, Manager, and User).  
The application allows task management based on roles:

- **Admin**: Can manage users and assign roles via the admin panel.
- **Manager**: Can create, update, and delete tasks.
- **User**: Can only view tasks assigned to them.

---

## 🚀 Features

- Role-based access control
- Admin panel to manage users and roles
- Task creation, update, and deletion for managers
- Task viewing for general users
- User authentication (Login/Logout)

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/todo-app.git
   cd todo-app

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


pip install -r requirements.txt


python manage.py migrate


python manage.py createsuperuser


python manage.py runserver


Visit: http://127.0.0.1:8000/admin/

Login with your superuser credentials.

From the admin panel, you can:

Add new users

Assign them roles (e.g., Manager, User)

Manage tasks
