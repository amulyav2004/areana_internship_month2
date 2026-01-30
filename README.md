# Social Media Platform

A modern, feature-rich social media platform built with Django.

## Features
- **User Authentication**: Sign up, login, and profile management.
- **Posting system**: Create, view, archive, and delete posts with image support.
- **Interactions**: Like posts and comment on them.
- **Social Graph**: Follow/Unfollow other users.
- **Modern UI**: Built with Bootstrap 5 and customized for a premium feel.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML5, Vanilla CSS, Bootstrap 5
- **Database**: SQLite3 (Development) / PostgreSQL (Production ready)
- **Icons**: Bootstrap Icons

## Project Structure
- `social_platform/`: Core configuration.
- `users/`: User profiles and authentication.
- `posts/`: Post management, likes, and comments.
- `friends/`: User connections and followers.
- `notifications/`: User activity alerts.
- `api/`: RESTful API endpoints.
- `templates/`: Global HTML templates.
- `static/`: Static assets (CSS, JS, Images).

## Setup Instructions

### Prerequisites
- Python 3.10+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/arena_internship_month2.git
   cd arena_internship_month2
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update the values in `.env`

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Docker
To run with Docker:
```bash
docker-compose up --build
```

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License.
