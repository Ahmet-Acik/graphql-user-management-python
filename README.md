

# GraphQL User Management

![Build Status](https://github.com/your-username/graphql-user-management/actions/workflows/python-app.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A comprehensive user management system built with Python, Flask, and Graphene. It exposes a GraphQL API for creating, updating, deleting, and fetching users. The project includes robust unit and integration tests, and is ready for local development and CI/CD.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Continuous Integration](#continuous-integration)
- [Contributing](#contributing)
- [License](#license)


## Features

- **Create User**: Add new users with full details (name, email, address, phone, roles).
- **Update User**: Modify any user field, including address and roles.
- **Delete User**: Remove users by ID.
- **Fetch Users**: Retrieve all users with full details.
- **Fetch User by ID**: Get details of a specific user.
- **GraphQL Playground**: Interactive browser interface at `/graphql` for testing queries and mutations.
- **Input Validation**: Ensures required fields and valid email formats.
- **Comprehensive Testing**: Unit and integration tests for all major features.

## Getting Started

### Prerequisites

- Python 3.9
- pip (Python package installer)

### Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/ahmet-acik/graphql-user-management.git
   cd graphql-user-management
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```sh
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```sh
     source venv/bin/activate
     ```

4. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt
   ```


## Running the Application

1. **Start the Flask application**:

   ```sh
   python app.py
   ```

   By default, the app runs on port 5000. If you encounter port conflicts, you can change the port in `app.py`:
   ```python
   if __name__ == "__main__":
       app.run(debug=True, port=5050)
   ```

2. **Access the GraphQL Playground**:

   Open your browser and navigate to `http://localhost:5000/graphql` (or the port you set). You can interactively test queries and mutations here.

3. **Troubleshooting**:
   - If you get a 403 Forbidden error, ensure no other process is using the port (use `lsof -i :5000`).
   - Make sure your Flask app is running and you see `* Running on http://127.0.0.1:5000/` in the terminal.
   - For port issues, kill conflicting processes and restart Flask.


## Running Tests

1. **Activate your virtual environment**.

2. **Run all tests (unit and integration):**
   ```sh
   python -m unittest discover tests
   ```

3. **Run only integration tests:**
   ```sh
   python -m unittest tests/test_app_integration.py
   ```

4. **Test output:**
   - Unit tests use mocks and do not require the Flask app to be running.
   - Integration tests require the Flask app to be running and will send real HTTP requests to `/graphql`.
   - All test logs and errors are printed to the console for easy debugging.


## Continuous Integration

This project uses GitHub Actions for CI. The workflow is defined in `python-app.yml` and runs all tests on every push and pull request to the `main` branch.


## Contributing

Contributions are welcome! Please:
- Fork the repository.
- Create a new branch for your feature or bugfix.
- Make your changes and commit with a descriptive message.
- Push your changes to your fork.
- Create a pull request to the `main` branch.


## License

This project is licensed under the MIT License. See the LICENSE file for details.

