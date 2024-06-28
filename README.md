# Django Blog

This project is a blogging platform built using the Django framework.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

Django Blog is a simple and powerful blogging platform designed to help you create and manage your blog posts efficiently. The application leverages the power of Django to provide a robust backend and a clean, user-friendly interface.

## Features

- **Post Management:** Create, update, and delete blog posts with ease.
- **Categories and Tags:** Organize your posts into categories and tags for better navigation.
- **Responsive Design:** A responsive design that works on both desktop and mobile devices.

## Installation

To get started with Django Blog, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/burakozcn01/django-blog.git
    cd django-blog
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run database migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

6. **Start the development server:**
    ```sh
    python manage.py runserver
    ```

7. Open your web browser and navigate to `http://127.0.0.1:8000` to see the application in action.

## Usage

- **Create a Post:** Start by creating a new blog post from the admin panel.
- **Add Categories and Tags:** Organize your posts into categories and tags for better navigation.
- **View Posts:** Access and read blog posts from the main page.
---

Thank you for using Django Blog! If you have any questions or feedback, please feel free to open an issue or contact us.
