# BreyTrainer Project Documentation

This project is a web-based platform for Breyner Riveros, designed to offer personalized fitness training and nutritional guidance. It utilizes a Django-powered backend with Django Rest Framework (DRF) to serve content to a static frontend.

## Project Architecture

The application follows a standard decoupled architecture:
* Backend: Python 3.x and Django Framework.
* API: Django Rest Framework for handling data requests.
* Database: SQLite3 for local development and simplified data management.
* Frontend: HTML5, Tailwind CSS, and JavaScript, consuming data from the API.

## Features

* Dynamic Site Configuration: Most of the site content (titles, subtitles, images, and links) can be updated directly through the Django Admin panel without code changes.
* Blog Management: Create and edit blog posts using a Rich Text Editor (CKEditor).
* Routines and Nutrition: Specific modules to post fitness routines (including video support) and nutritional advice.
* Responsive Design: Optimized for both desktop and mobile devices.

## Requirements

The project relies on the following dependencies:
* Django >= 4.0
* djangorestframework >= 3.13
* django-cors-headers >= 3.13
* whitenoise >= 6.0
* Pillow >= 9.0
* django-ckeditor >= 6.5.1
* gunicorn >= 20.1.0

## Setup and Installation

### 1. Environment Preparation
It is recommended to use a virtual environment to manage dependencies:

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

### 2. Dependency Installation
Install the required packages using pip:

pip install -r requirements.txt

### 3. Database Configuration
Apply migrations to initialize the database schema:

python manage.py migrate

### 4. Create Administrative User
Create a superuser to access the management dashboard:

python manage.py createsuperuser

### 5. Start Development Server
Run the local server to test the application:

python manage.py runserver

The application will be accessible at http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin/.

## API Endpoints

The system exposes several RESTful endpoints:
* /api/posts/: Returns a list of all publications (Blogs, Routines, and Nutrition).
* /api/config/: Returns the current site-wide configurations (titles, images, contact info).

## Project Structure

* breytrainer/: Core project settings and URL routing.
* api/: Manages publications and core business logic models.
* site_config/: Handles the singleton-style model for global site settings.
* frontend/: Contains static HTML templates and assets.
* media/: Directory for user-uploaded files (images and videos).

## Content Management Instructions

1. Log in to the Admin Panel.
2. Navigate to the "Site Configurations" section to update main page texts and links.
3. Use the "Posts" section within the "Api" app to add new content. 
4. When adding a Post, select the appropriate "Post Type" (Blog, Routine, or Nutrition) to ensure it appears in the correct section of the frontend.

## License

This project is intended for personal use by Breyner Riveros. All rights reserved.
