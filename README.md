
# GraphQL User Management

![Build Status](https://github.com/your-username/graphql-user-management/actions/workflows/python-app.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A GraphQL-based user management system built with Python and Flask. This project allows you to create, update, delete, and fetch users using GraphQL queries and mutations.

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

- **Create User**: Add new users to the system.
- **Update User**: Modify existing user details.
- **Delete User**: Remove users from the system.
- **Fetch Users**: Retrieve a list of all users.
- **Fetch User by ID**: Get details of a specific user by ID.

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

2. **Access the GraphQL interface**:

   Open your browser and navigate to `http://localhost:5000/graphql`.

## Running Tests

1. **Ensure that the virtual environment is activated**.

2. **Run the tests using `unittest`**:

   ```sh
   python -m unittest discover tests
   ```

## Continuous Integration

This project uses GitHub Actions for continuous integration. The workflow is defined in the 

python-app.yml

 file. It runs the tests on every push and pull request to the `main` branch.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bugfix.
3. **Make your changes** and commit them with a descriptive message.
4. **Push your changes** to your fork.
5. **Create a pull request** to the `main` branch of the original repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

