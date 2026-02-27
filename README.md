# Django Web App - Blog Application

A simple yet functional blog application built with Django. This project demonstrates core Django concepts including models, views, templates, URL routing, and the Django admin panel.

## Features

- **Blog Posts**: Create, read, and manage blog posts
- **Comments**: Readers can leave comments on posts
- **Admin Panel**: Manage posts and comments through Django's admin interface
- **Responsive Design**: Bootstrap 5 for mobile-friendly UI
- **User Authentication**: Built-in user authentication support

## Project Structure

```
django web app/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── db.sqlite3            # SQLite database (created after migration)
├── myproject/            # Django project configuration
│   ├── settings.py       # Project settings
│   ├── urls.py           # Root URL configuration
│   ├── wsgi.py           # WSGI configuration
│   └── asgi.py           # ASGI configuration
├── blog/                 # Blog application
│   ├── models.py         # Post and Comment models
│   ├── views.py          # View logic
│   ├── urls.py           # Blog URL patterns
│   ├── forms.py          # Comment form
│   ├── admin.py          # Admin configuration
│   └── tests.py          # Unit tests
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── home.html         # Home page
│   └── blog/
│       ├── post_list.html   # Blog posts listing
│       └── post_detail.html # Individual post detail
└── static/               # Static files (CSS, JS, images)
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Navigate to the project directory:**
   ```powershell
   cd "c:\Users\cctar\Documents\django web app"
   ```

2. **Create a virtual environment:**
   ```powershell
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   ```powershell
   # On Windows
   venv\Scripts\Activate.ps1
   
   # If you get an execution policy error, run:
   # Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

5. **Run migrations:**
   ```powershell
   python manage.py migrate
   ```

6. **Create a superuser (admin account):**
   ```powershell
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

7. **Run the development server:**
   ```powershell
   python manage.py runserver
   ```

8. **Access the application:**
   - **Home page**: http://127.0.0.1:8000/
   - **Blog**: http://127.0.0.1:8000/blog/
   - **Admin panel**: http://127.0.0.1:8000/admin/

## Usage

### Creating Blog Posts

1. Go to the admin panel (http://127.0.0.1:8000/admin/)
2. Log in with your superuser credentials
3. Click "Posts" and "Add Post"
4. Fill in the title, content, and select an author
5. Click "Save"

### Leaving Comments

1. View a blog post
2. Scroll down to the "Leave a Comment" section
3. Enter your name and comment text
4. Click "Post Comment"

## Available Management Commands

```powershell
# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver

# Run tests
python manage.py test

# Create a backup of the database
python manage.py dumpdata > backup.json

# Create a new app
python manage.py startapp myapp

# Open the Django shell
python manage.py shell
```

## Customization

### Modify Models

Edit [blog/models.py](blog/models.py) to add more fields or models. After changes, run:
```powershell
python manage.py makemigrations
python manage.py migrate
```

### Change Settings

Edit [myproject/settings.py](myproject/settings.py) to configure:
- Database settings
- Installed apps
- Static files location
- Templates directory
- Time zone
- Language

### Add New Pages

1. Create a view in [blog/views.py](blog/views.py)
2. Create an HTML template in `templates/blog/`
3. Add a URL pattern in [blog/urls.py](blog/urls.py)

## Deployment Considerations

For production deployment:

1. **Set DEBUG to False** in settings.py
2. **Change the SECRET_KEY** to a secure random value
3. **Use a proper database** (PostgreSQL, MySQL) instead of SQLite
4. **Configure ALLOWED_HOSTS** with your domain name
5. **Use a production server** (Gunicorn, uWSGI)
6. **Use a reverse proxy** (Nginx, Apache)
7. **Enable HTTPS** with SSL/TLS certificates
8. **Collect static files**: `python manage.py collectstatic`

## Troubleshooting

### Port 8000 already in use:
```powershell
python manage.py runserver 8001
```

### Virtual environment not activating:
- Check PowerShell execution policy
- Use Command Prompt instead: `venv\Scripts\activate.bat`

### Database errors:
```powershell
python manage.py migrate --run-syncdb
```

### Module not found errors:
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

## Learning Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django for Beginners](https://djangoforbeginners.com/)
- [Real Python Django Tutorials](https://realpython.com/tutorials/django/)

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, refer to the Django documentation or community forums.
