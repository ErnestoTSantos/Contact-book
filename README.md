# Contact Book

This is a Django application for managing contacts. It provides a RESTful API for creating, reading, updating, and deleting contacts.

## Getting Started

To run the application, you need to have Docker and Docker Compose installed on your system. Then, run the following command:

```
docker-compose up
```

This will start the application and its dependencies (database, web server, etc.) in Docker containers.

You can access the API at `http://localhost:8000/api/contacts/`.

## API Documentation

The API documentation is available at `http://localhost:8000/api/docs/`. It provides a user-friendly interface for exploring the API endpoints and their parameters.

## Development

To develop the application, you need to have Python 3.8 and Poetry installed on your system. Then, run the following commands:

```
poetry install
poetry run python manage.py runserver
```

This will install the dependencies and start the development server.

## Testing

To run the tests, run the following command:

```
poetry run pytest
```

This will run the test suite and report any failures or errors.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.