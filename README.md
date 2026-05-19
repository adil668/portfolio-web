# Personal Portfolio Website

A modern Django-powered personal portfolio website for a software engineer, AI engineer, or full-stack developer. The project uses a Start Bootstrap Creative-inspired one-page layout with a fixed navbar, masthead hero, orange accent section styling, project grid overlays, skill progress bars, services, contact form, and responsive styling.

## Project Information

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Django project:** `portfolio_site`
- **Django app:** `main`
- **Templates:** `templates/main/home.html`
- **Static files:** `static/css`, `static/js`, `static/images`

## Features

- Modern glassmorphism-inspired UI
- Start Bootstrap Creative-inspired one-page design
- Full-screen masthead with local visual background
- Sticky responsive navigation
- Mobile hamburger menu
- Smooth scrolling
- Scroll reveal animations
- Animated skill progress bars
- Project cards with hover effects
- Services section
- Experience and education timeline
- Contact form UI with JavaScript feedback
- Login page using Django authentication
- Signup page using Django user creation
- Optional WAMP/MySQL database connection
- Footer with social links and back-to-top button

## Folder Structure

```text
.
├── main/
│   ├── __init__.py
│   ├── apps.py
│   ├── forms.py
│   ├── urls.py
│   └── views.py
├── portfolio_site/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── files/
│   │   └── .gitkeep
│   ├── images/
│   │   ├── creative-masthead.svg
│   │   ├── portfolio-1.svg
│   │   ├── portfolio-2.svg
│   │   ├── portfolio-3.svg
│   │   └── profile-placeholder.svg
│   └── js/
│       └── main.js
├── templates/
│   └── main/
│       └── home.html
├── manage.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/adil668/portfolio-web.git
cd portfolio-web
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv env
env\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open the site in your browser:

```text
http://127.0.0.1:8000/
```

## Login and Signup Pages

The project includes Django authentication pages:

```text
http://127.0.0.1:8000/login/
http://127.0.0.1:8000/signup/
```

After signup, the new user is automatically logged in and redirected to the portfolio homepage. The navbar changes based on authentication status.

## WAMP/MySQL Setup

SQLite is still the default database so the project can run immediately. To connect the site to WAMP Server, use MySQL from WAMP and enable the MySQL settings with environment variables.

### 1. Start WAMP

Start WAMP Server and make sure the icon is green. This means Apache and MySQL are running.

### 2. Create the database

Open phpMyAdmin:

```text
http://localhost/phpmyadmin/
```

Create a database named:

```text
portfolio_web
```

Default WAMP credentials are commonly:

```text
Username: root
Password: empty
Host: 127.0.0.1
Port: 3306
```

If your WAMP uses different credentials, use those in the environment variables below.

### 3. Install MySQL dependency

```bash
pip install -r requirements.txt
```

If `mysqlclient` fails to install on Windows, install the required MySQL/MariaDB development connector or use a prebuilt wheel that matches your Python version.

### 4. Enable WAMP/MySQL for this Django project

PowerShell:

```powershell
$env:USE_WAMP_MYSQL="True"
$env:WAMP_DB_NAME="portfolio_web"
$env:WAMP_DB_USER="root"
$env:WAMP_DB_PASSWORD=""
$env:WAMP_DB_HOST="127.0.0.1"
$env:WAMP_DB_PORT="3306"
```

Command Prompt:

```cmd
set USE_WAMP_MYSQL=True
set WAMP_DB_NAME=portfolio_web
set WAMP_DB_USER=root
set WAMP_DB_PASSWORD=
set WAMP_DB_HOST=127.0.0.1
set WAMP_DB_PORT=3306
```

### 5. Create Django tables in MySQL

```bash
python manage.py migrate
```

### 6. Run the site with WAMP/MySQL enabled

```bash
python manage.py runserver
```

## Personalization Guide

### Change name, title, email, and hero content

Edit:

```text
templates/main/home.html
```

Look for text such as:

- `Alex Morgan`
- `hello@example.com`
- Hero introduction
- CTA button text
- Social links in the footer

Replace them with your real details.

### Change skills, projects, services, and timeline

Edit:

```text
main/views.py
```

You can update:

- `skills`
- `projects`
- `services`
- `timeline`

This keeps portfolio data organized in one place and avoids hardcoding repeated content directly in the template.

### Add your resume

Add your resume file here:

```text
static/files/resume.pdf
```

The Download Resume button already points to this location. The file is ignored by Git by default so you can keep personal versions local if needed.

### Replace the profile image

Current placeholder:

```text
static/images/profile-placeholder.svg
```

To use your own image:

1. Add an image to `static/images/`
2. Update the image path in `templates/main/home.html`

Example:

```html
<img src="{% static 'images/my-profile.jpg' %}" alt="Profile image">
```

### Update colors and design

Edit:

```text
static/css/styles.css
```

The main color variables are at the top of the file:

```css
:root {
    --bg: #08111f;
    --accent: #6ee7b7;
    --accent-two: #60a5fa;
    --accent-three: #f472b6;
}
```

### Update animations and interactions

Edit:

```text
static/js/main.js
```

Useful areas to customize:

- Typing animation roles
- Scroll reveal behavior
- Contact form message
- Active navbar logic

## Useful Commands

Run server:

```bash
python manage.py runserver
```

Run server on a specific port:

```bash
python manage.py runserver 127.0.0.1:8000
```

Check Django project health:

```bash
python manage.py check
```

Apply database migrations:

```bash
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Run with WAMP/MySQL in PowerShell:

```powershell
$env:USE_WAMP_MYSQL="True"
python manage.py migrate
python manage.py runserver
```

Open Django shell:

```bash
python manage.py shell
```

Collect static files for deployment:

```bash
python manage.py collectstatic
```

View Git status:

```bash
git status
```

Commit changes:

```bash
git add .
git commit -m "Describe your change"
```

Push changes:

```bash
git push
```

## Deployment Notes

Before deploying publicly:

- Set `DEBUG = False` in `portfolio_site/settings.py`
- Replace the development `SECRET_KEY`
- Configure `ALLOWED_HOSTS`
- Use environment variables for sensitive settings
- Run `python manage.py collectstatic`
- Use a production server such as Gunicorn, Uvicorn, or a managed hosting platform

## License

This project is ready to customize for a personal portfolio. Add your preferred license if you plan to share or reuse it publicly.
