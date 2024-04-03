# Messaging System

## Table of Contents
1. [Description](#description)
2. [Installation Instructions](#installation-instructions)
3. [Operating Instructions](#operating-instructions)

## Description
The Messaging System is a REST API backend system responsible for handling messages between users. It is built using Django and utilizes tokens for authentication to manage requests for logged-in users.

## Installation Instructions
To install and set up the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/ShovalElhaiany/messaging-system.git
    cd messaging-system
    ```

2. Run the provided PowerShell script (run.ps1) or execute the following commands manually:
    ```powershell
    .\run.ps1
    ```

    The script automates the following commands:
    ```bash
    py -m venv .venv
    .venv/scripts/activate
    python.exe -m pip install --upgrade pip
    pip install -r requirements.txt
    python manage.py migrate
    python load_data.py
    python manage.py runserver
    ```

## Operating Instructions
To operate the Messaging System, follow these instructions:

### Admin Details
- Username: Admin
- Password: 1234

### Postman Collection
A Postman collection file is attached to the project. You can import it into Postman and start using it.

The collection contains 6 requests:
1. Get Token
2. Create Message
3. Get Message
4. Get All Messages
5. Get Unread Messages
6. Delete Message

Send the requests in the following order:
1. Get Token
   - Only after receiving the token can you send the rest of the requests.
   
2. Add the token to the header of subsequent requests with the key "Authorization" and the token value.
   - Example value: `Token ae4f8d4ddaa173ad34cd4a42f4a043fcb83ca8c4`

Good luck!
