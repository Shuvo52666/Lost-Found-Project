
# Lost & Found — Community Based Platform

Lost & Found is a community-based web application developed with Django. It helps users report missing belongings, share found items, search posts within their communities, and contact post owners through an organized communication system.

The platform provides community management, lost and found posts, image uploads, optional ownership-verification questions, contact requests, messaging, notifications, and post moderation.

## Features

### 1. Accounts and Profiles

- User registration, login, and logout.
- User profile management.
- Profile picture upload, update, and removal.
- Authentication for protected actions.

### 2. Community Creation and Joining

- Create and manage communities.
- Join existing communities through the available membership workflow.
- Display community descriptions, membership information, and administrators.
- Allow community administrators to access post-management features.

### 3. Lost and Found Feed

- Create Lost or Found posts.
- Add captions, descriptions, and item images.
- Browse posts in a community-based feed.
- Search posts by keywords.
- Filter posts by Lost or Found status.
- Read and write comments.
- Send contact requests to post owners.
- Report inappropriate posts.

### 4. Ownership Verification

- Add optional verification questions when creating a post.
- Submit answers when requesting contact with a post owner.
- Allow post owners to review incoming contact requests.
- Require approval before unrestricted conversation when applicable.

### 5. Messaging and Notifications

- Access conversations and contact requests through the Inbox.
- Track unread messages and request activity.
- Receive notifications for relevant activities.
- Notify community administrators about reported posts.
- Support real-time messaging and notification updates through Socket.IO where correctly configured.

**Note:** Real-time messaging depends on the Socket.IO client, ASGI configuration, event handlers, and server connection working together. Test message delivery with two separate accounts before claiming that real-time functionality works completely.

### 6. Reports and Moderation

- Allow users to report inappropriate posts.
- Allow community administrators to review and manage posts in their communities.
- Restrict moderation actions through server-side permission checks.
- Prevent unauthorized users from accessing administrative actions.

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, Django 5.2 |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| Real-time communication | Socket.IO |
| ASGI server | Uvicorn |
| Image processing | Pillow |
| Static file serving | WhiteNoise |
| Version control | Git and GitHub |

## Project Structure

The project contains six custom Django applications.

```text
Lost-Found-Project/
|
|-- accounts/
|   |-- migrations/
|   |-- admin.py
|   |-- forms.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|
|-- communities/
|   |-- migrations/
|   |-- admin.py
|   |-- forms.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|
|-- newsfeed/
|   |-- migrations/
|   |-- admin.py
|   |-- forms.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|
|-- verification/
|   |-- migrations/
|   |-- admin.py
|   |-- forms.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|
|-- messaging/
|   |-- migrations/
|   |-- admin.py
|   |-- forms.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|
|-- notifications/
|   |-- migrations/
|   |-- admin.py
|   |-- context_processors.py
|   |-- models.py
|   |-- services.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|
|-- config/
|   |-- asgi.py
|   |-- settings.py
|   |-- socketio.py
|   |-- urls.py
|   |-- wsgi.py
|
|-- templates/
|   |-- accounts/
|   |-- messaging/
|   |-- newsfeed/
|   |-- notifications/
|   |-- verification/
|
|-- static/
|   |-- css/
|       |-- style.css
|
|-- tests/
|-- .env.example
|-- requirements.txt
|-- manage.py
|-- README.md
```

### Application Responsibilities

| Application | Responsibility |
|---|---|
| accounts | User authentication and profile management |
| communities | Community creation, membership, and administration |
| newsfeed | Lost and found posts, comments, reports, and moderation |
| verification | Ownership-verification questions and contact-request workflow |
| messaging | Inbox, conversations, and message management |
| notifications | Notification records, unread counts, and notification services |
| config | Project settings, URL routing, and ASGI/WSGI configuration |

## Installation and Setup

### Prerequisites

Install the following software before running the project:

- Python
- Git
- A terminal such as Windows PowerShell
- A code editor such as VS Code or PyCharm

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/Shuvo52666/Lost-Found-Project.git
cd Lost-Found-Project
```

Run the remaining commands from the project directory containing `manage.py`.

### 2. Create and Activate a Virtual Environment

Create a virtual environment:

```powershell
py -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

For Git Bash, use:

```bash
source .venv/Scripts/activate
```

### 3. Install Dependencies

Install the packages listed in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `.env.example` to a new file named `.env` in the project root.

Configure the following variables in `.env`:

```dotenv
DJANGO_SECRET_KEY=replace-with-a-new-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_CSRF_TRUSTED_ORIGINS=
```

Use a unique secret key for your local environment. Never commit your private `.env` file or production credentials to GitHub.

The example above is for local development only. Production deployments require secure settings, an appropriate secret key, and `DJANGO_DEBUG=False`.

### 5. Check and Prepare the Database

Run the Django system check:

```bash
python manage.py check
```

Review the migration status:

```bash
python manage.py showmigrations
```

Apply database migrations:

```bash
python manage.py migrate
```

Create an administrator account if needed:

```bash
python manage.py createsuperuser
```

The project uses SQLite by default. If you need to preserve an existing database and user accounts, back up and restore the original `db.sqlite3` file before running migrations. Uploaded media must be backed up separately.

### 6. Start the Application

Start the ASGI application using Uvicorn:

```bash
python -m uvicorn config.asgi:application --reload
```

Open the website in your browser:

http://127.0.0.1:8000/

The ASGI configuration is used for the project's Socket.IO integration.

## How the Application Works

### Create a Lost or Found Post

1. Register or log in.
2. Create or join a community.
3. Open the community feed.
4. Select the option to create a post.
5. Choose Lost or Found.
6. Enter the item's caption and description.
7. Upload an image if desired.
8. Add optional verification questions when available.
9. Publish the post.

### Search and Interact with Posts

1. Browse the community feed.
2. Search using keywords or filter by Lost or Found.
3. Read or write comments.
4. Send a contact request to the owner of an eligible post.
5. Report inappropriate content when necessary.

### Contact and Verification Workflow

```text
User discovers a post
        |
        v
User selects Message / Contact
        |
        v
Answers optional verification questions
        |
        v
Contact request reaches the post owner
        |
        v
Owner reviews the request
        |
        v
Owner accepts or rejects the request
        |
        v
Conversation proceeds when approved
```

### Community Moderation Workflow

```text
User reports a post
        |
        v
Community administrator reviews the report
        |
        v
Administrator opens post management
        |
        v
Administrator decides on the appropriate action
```

Permissions must be enforced in Django views, not only by hiding buttons in HTML templates.

## Requirements.txt

The `requirements.txt` file contains the Python packages needed by the application.

| Package | Purpose |
|---|---|
| Django | Web framework, authentication, and ORM |
| Pillow | Image processing |
| python-socketio | Real-time communication |
| python-engineio | Socket.IO communication engine |
| Uvicorn | ASGI server |
| python-dotenv | Environment variable loading |
| qrcode | QR code generation |
| WhiteNoise | Static file serving |
| asgiref | Asynchronous and synchronous application support |

The exact dependency versions are defined in `requirements.txt`.

## Common Development Commands

Check the project configuration:

```bash
python manage.py check
```

Create migration files after model changes:

```bash
python manage.py makemigrations
```

Apply database migrations:

```bash
python manage.py migrate
```

Run the test suite:

```bash
python manage.py test
```

Start the ASGI server:

```bash
python -m uvicorn config.asgi:application --reload
```

## Troubleshooting

### TemplateDoesNotExist

Check that the requested template exists in the `templates` directory and that the `TEMPLATES` setting includes the correct directory.

### Uploaded Images Do Not Appear

Check the `MEDIA_URL` and `MEDIA_ROOT` settings, the image field configuration, and the media URL configuration used during development.

### Socket.IO Messaging Does Not Update

Check that:

- The Socket.IO client library loads successfully.
- Uvicorn is running the project's ASGI application.
- The browser reports a successful Socket.IO connection.
- The backend emits the expected event names.
- The recipient's event listener and conversation identifiers match the backend payload.

Test using two separate accounts and inspect browser console errors.

### Environment Variable Errors

Check that `.env` is located in the project root and contains the variables expected by `config/settings.py`. Restart the server after changing environment variables.

### Existing Users Cannot Log In

Verify that the application is connected to the correct SQLite database. Creating a new superuser does not restore existing user accounts. Back up the original database before replacing or migrating it.

## Security Considerations

- Require authentication for protected actions.
- Check community membership where required.
- Validate post ownership and administrator permissions on the server.
- Use CSRF protection for forms that modify data.
- Validate uploaded images and limit upload sizes where appropriate.
- Protect verification answers and private conversations from unauthorized access.
- Keep secret keys and credentials out of version control.
- Disable debugging and configure secure hosts and HTTPS for production.

## Team Contribution Workflow

The project is developed by a three-member team.

Recommended workflow:

1. Pull the latest changes before starting work.
2. Create a branch for each feature or fix.
3. Make focused commits with meaningful messages.
4. Run relevant checks and tests.
5. Coordinate merges with the other team members.

Examples of meaningful commit messages:

```text
feat(newsfeed): add lost and found filters
feat(messaging): improve contact request workflow
feat(verification): add ownership questions
feat(notifications): update unread notification count
fix(moderation): restrict post management to community admins
fix(profile): support profile picture removal
```

## Future Improvements

Potential future enhancements include:

- More reliable real-time messaging and notifications.
- Improved search, filtering, and pagination.
- More comprehensive automated tests.
- Accessibility and mobile interface improvements.
- Production deployment and continuous integration.

These are potential improvements, not claims that the features are already implemented.

## GitHub Repository

https://github.com/Shuvo52666/Lost-Found-Project

---

**Lost & Found — Connecting communities to reunite people with their belongings.**
