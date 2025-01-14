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
- Redis (for production)

### Frontend
- TailwindCSS
- AlpineJS
- WebSocket

### Database
- SQLite (development)

## Prerequisites

- Python 3.8+
- Node.js 14+
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

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Install Node.js dependencies:
```bash
npm install
```

5. Create `.env` file in the project root:
```env
SECRET_KEY=your-django-secret-key
DEBUG=True
GOOGLE_OAUTH2_KEY=your-google-oauth2-client-id
GOOGLE_OAUTH2_SECRET=your-google-oauth2-client-secret
```

6. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Create superuser (admin):
```bash
python manage.py createsuperuser
```

## Google OAuth2 Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google+ API
4. Go to the Credentials page
5. Create OAuth 2.0 Client ID credentials
6. Add authorized redirect URIs:
   - Development: `http://localhost:8000/social-auth/complete/google-oauth2/`
   - Production: `https://yourdomain.com/social-auth/complete/google-oauth2/`
7. Copy the Client ID and Client Secret to your `.env` file

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
- Main application: `http://localhost:8000`
- Admin interface: `http://localhost:8000/admin`

## Development

### Project Structure
```
chat_project/
├── chat/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── chat/
│   │       ├── login.html
│   │       ├── profile.html
│   │       ├── home.html
│   │       └── room.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── consumers.py
│   ├── models.py
│   ├── routing.py
│   ├── urls.py
│   └── views.py
├── chat_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
├── templates/
│   └── base.html
├── .env
├── .gitignore
├── manage.py
└── requirements.txt
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Acknowledgments

- Django documentation
- Channels documentation
- TailwindCSS documentation
- Google OAuth2 documentation
