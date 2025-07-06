# Create Comment Microservice

This project is a Python-based backend service for managing comments. It utilizes Flask to expose RESTful APIs and MongoDB as its database.

## Folder Structure

The project is organized into the following main folders:

-   **`.github/workflows/`**: Contains GitHub Actions workflow configurations for Continuous Integration and Continuous Deployment (CI/CD). This includes Docker image building, testing, and deployment to environments like AWS EC2.
-   **`conections/`**: This directory is responsible for managing database connections. Currently, it includes modules to connect to a MongoDB instance.
    -   `mongo.py`: Handles the connection logic to the MongoDB database using environment variables for configuration.
-   **`services/`**: This folder houses the business logic of the application. Each service typically corresponds to a specific domain or feature.
    -   `functions.py`: Contains core functions, such as `create_comment`, which handles the logic for creating new comments in the database.
-   **`tests/`**: Includes test scripts to ensure the reliability and correctness of the application's APIs and functionalities.
    -   `route_test.py`: An example script for testing API endpoints, including authentication and data posting.
    -   `test_create_comment.py`: (Likely) Contains unit or integration tests specifically for the comment creation functionality.

Other notable files:

-   **`main.py`**: The entry point of the Flask application. It defines the API routes (e.g., `/create-comment`) and handles incoming requests.
-   **`dockerfile`**: Defines the instructions to build a Docker image for the application, enabling containerized deployment.
-   **`requirements.txt`**: Lists the Python dependencies required to run the project.

## Backend Design Pattern

The backend appears to follow a **Service-Oriented Architecture (SOA)** or a **Microservice** approach. Key characteristics include:

-   **Layered Architecture**:
    -   **Presentation Layer (API Endpoints)**: `main.py` uses Flask to define and handle HTTP requests.
    -   **Service Layer (Business Logic)**: `services/functions.py` encapsulates the core business operations.
    -   **Data Access Layer**: `conections/mongo.py` abstracts the database interaction.
-   **Modularity**: Functionalities are separated into distinct services and connection modules.

## Communication Architecture

-   **RESTful API**: The service exposes endpoints via HTTP. For example, the `/create-comment` endpoint allows clients to post new comments.
-   **JSON**: Data is exchanged in JSON format for requests and responses.
-   **Token-Based Authentication (JWT)**: API endpoints like `/create-comment` are secured using JSON Web Tokens (JWT). Clients must provide a valid Bearer token in the `Authorization` header. The token is decoded and validated to identify the user.

## Folder Pattern

The project uses a **feature-based** or **component-based** folder pattern. Related code for specific functionalities (like database connections or service logic) is grouped into dedicated directories (e.g., `conections/`, `services/`).

## API Endpoints

### Create Comment

-   **Endpoint**: `/create-comment`
-   **Method**: `POST`
-   **Description**: Creates a new comment for a publication.
-   **Authentication**: Required. A valid JWT Bearer token must be included in the `Authorization` header.
    ```
    Authorization: Bearer <your_jwt_token>
    ```
-   **Request Body**: JSON
    ```json
    {
        "Id_publication": "string (MongoDB ObjectId)",
        "Comment": "string"
    }
    ```
    -   `Id_publication`: The ID of the publication to which the comment belongs.
    -   `Comment`: The text content of the comment.

-   **Responses**:
    -   **`201 Created`**: Comment created successfully.
        ```json
        {
            "message": "Comment created successfully"
        }
        ```
    -   **`400 Bad Request`**: Missing `Id_publication` or `Comment` in the request.
        ```json
        {
            "error": "Missing data"
        }
        ```
    -   **`401 Unauthorized`**:
        -   Token missing or invalid format:
            ```json
            {
                "error": "Token missing or invalid"
            }
            ```
        -   Invalid token data (e.g., missing `user_id`):
            ```json
            {
                "error": "Invalid token data"
            }
            ```
        -   Token expired:
            ```json
            {
                "error": "Token expired"
            }
            ```
        -   Invalid token signature or structure:
            ```json
            {
                "error": "Invalid token"
            }
            ```
    -   **`500 Internal Server Error`**: General server error or failure during comment creation.
        ```json
        {
            "error": "Server error: <specific_error_message>"
        }
        ```
        ```json
        {
            "error": "Failed to create comment: <specific_error_message>"
        }
        ```
