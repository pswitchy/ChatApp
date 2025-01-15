# Real-Time Chat Application

A feature-rich real-time chat application built with Django, Channels, and modern frontend technologies. The application supports Google Authentication, real-time messaging, file sharing, and user status tracking.

## Features

### Authentication & User Management
- Google OAuth2 integration for seamless sign-in
- User profile management
- Online/offline status tracking
- Last seen timestamps

### Chat Functionality
- Real-time messaging using WebSocket
- File attachment support
- Message read receipts
- Chat history
- Message timestamps
- Desktop notifications
- Typing indicators

### User Interface
- Responsive design for all devices
- Modern UI with TailwindCSS
- Collapsible sidebar for mobile view
- User-friendly interface
- Real-time status indicators

## Technology Stack

### Backend
- Django 5.0.1
- Channels 4.0.0
- Django Channels
- Social Auth App Django
  
### Frontend
- TailwindCSS
- AlpineJS
- WebSocket

### Database
- SQLite (development)

## Prerequisites

- Python 3.8+
- JavaScript
- Google OAuth2 credentials

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (admin):
```bash
python manage.py createsuperuser
```

## Running the Project

1. Start the development server:
```bash
python manage.py runserver
```

2. In a new terminal, start the Tailwind CSS build process:
```bash
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
```

3. Access the application:
- Main application: `http://127.0.0.1:8000`

## Working of Application

![Screenshot 2025-01-14 162904](https://github.com/user-attachments/assets/e35c3ad0-d0a8-4fce-b4e2-5ed676bda45f)


![Screenshot 2025-01-14 162921](https://github.com/user-attachments/assets/453e81b4-03a4-4f41-b8ca-af37454fc045)



![Screenshot 2025-01-14 162605](https://github.com/user-attachments/assets/18bfa253-3d55-4598-81fa-eb9436a0df6b)



![Screenshot 2025-01-14 162632](https://github.com/user-attachments/assets/e31e4c14-5a37-4541-a3da-c7b43819d842)


  
![Screenshot 2025-01-14 163055](https://github.com/user-attachments/assets/2af4501b-f118-4948-8be3-7f8a4565572d)




![Screenshot 2025-01-14 163118](https://github.com/user-attachments/assets/c0bf022c-26c3-409b-96f0-975a7f821ffc)
