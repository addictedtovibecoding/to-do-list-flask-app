# To-Do List Application

## Overview
This To-Do List application is a simple web app that allows users to create, manage, and track their tasks. It features a frontend built with HTML, CSS, and JavaScript, utilizing Bootstrap for styling and responsiveness. The backend is developed using Flask, a Python web framework, to handle RESTful API requests for managing tasks.

## File Structure
The application consists of two primary files:
1. `index.html` - The frontend HTML and JavaScript code.
2. `app.py` - The backend Flask application.

---

## index.html

This file contains the HTML structure, styling, and JavaScript functionality for the To-Do List application.

### Key Sections

- **HTML Structure**: 
  - The document is structured with a `<!DOCTYPE html>` declaration, used to define the content as an HTML5 document.
  - The `<head>` section includes metadata, Bootstrap CSS for styling, and a custom style for the app.
  - The `<body>` section houses the main content, including a header, task input form, and navigation tabs for pending and completed tasks.

- **Styling**:
  - CSS styles are applied directly within a `<style>` tag. The styles define the layout, color schemes, animations, and hover effects for buttons and task items.
  - A dark mode can be toggled on and off.

- **JavaScript Functionality**:
  - JavaScript code handles functionality such as task creation, completion status updates, and deletion of tasks.
  - Uses the Fetch API to communicate with the Flask backend endpoints for adding, fetching, updating, and deleting tasks.
  - Notifications are displayed to inform users about the success of their actions (e.g., adding a task).

### Key Features

- **Task Management**: Users can add new tasks, toggle their completion status, and delete old tasks.
- **Responsive Design**: The app is responsive and adapts to different screen sizes using Bootstrap.
- **Dark Mode**: Users can switch between light and dark themes for better visibility based on preference.

---

## app.py

This file defines the Flask application and contains the backend logic to manage tasks via API endpoints.

### Key Sections

- **Flask Application Setup**: 
  - The application is initialized with `Flask(__name__)`.
  - An in-memory list named `tasks` is used to store the task objects temporarily.

- **Routes**:
  - **Index Route (`/`)**: Renders the `index.html` page for the user interface. 
  - **Task Management API (`/api/tasks`)**: This route supports `GET` and `POST` methods.
    - **GET**: Retrieves all tasks in JSON format.
    - **POST**: Accepts a new task from the request body, creates a new task object, assigns it an ID, and adds it to the `tasks` list.
  - **Task Update and Deletion Route (`/api/tasks/<int:task_id>`)**: This route supports `PUT` and `DELETE` methods.
    - **PUT**: Updates the completion status of a specific task based on the provided `task_id`.
    - **DELETE**: Removes the task with the specified `task_id` from the `tasks` list.

### Key Features

- **RESTful API**: The application follows a REST architecture, allowing CRUD (Create, Read, Update, Delete) operations on tasks.
- **Easy Task Management**: Users can manage tasks seamlessly using HTTP requests.

---

## Installation Instructions

### Prerequisites
- Python 3.x installed on your operating system. You can download it from [python.org](https://www.python.org/downloads/).
