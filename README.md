# Image Processing API Integration Tests

## Overview

This project contains integration tests for the Image Processing API. Integration testing is crucial as it verifies the entire application workflow, ensuring that different components work together as expected. These tests are designed to simulate real-world scenarios where users interact with the API to perform CRUD (Create, Read, Update, Delete) operations on images. The tests cover uploading, retrieving, updating, and deleting images while verifying that the image processing tasks are handled correctly by the backend.

## Why Integration Testing is Important

Integration testing is an essential phase of the software development lifecycle. It ensures that:
- Different modules and services within the application work together seamlessly.
- The API endpoints correctly handle requests and responses, providing the expected output.
- The application behaves as intended in a real-world environment, improving reliability and robustness.
- Any issues arising from the interaction between various components are identified and resolved early.

By having a separate, modularized integration testing package, we can:
- Maintain a clear separation of concerns, making the test suite easier to manage and update.
- Run tests independently from the main application, ensuring that the core functionality is not disrupted during testing.
- Facilitate continuous integration and continuous deployment (CI/CD) processes by providing automated testing capabilities.

## Project Structure

The project is organized as follows:

```
image-processing-integration-tests/
├── .gitignore
├── requirements.txt
├── test_images/
│   ├── sample1.jp2
│   └── sample2.jp2
├── tests/
│   └── test_integration.py
└── venv/
```

- **.gitignore**: Specifies files and directories to be ignored by Git.
- **requirements.txt**: Lists the dependencies required for the integration tests.
- **test_images/**: Contains sample images used for testing.
- **tests/**: Contains the integration test scripts.
- **venv/**: Virtual environment for managing dependencies.

## Prerequisites

- **Python 3.9** or later
- **Virtual Environment**: It's recommended to use a virtual environment to manage dependencies.
- **Main Application**: The Image Processing API should be running locally or on a server accessible by the tests.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/theodwya/image-pocessing-integration-tests
   cd image-processing-integration-tests
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure the Main Application is Running**:
   Start the main Image Processing API application. If using Docker, navigate to the main application directory and run:
   ```bash
   docker-compose up --build
   ```

## Running the Tests

To run the integration tests, use the following command:
```bash
pytest --cov=app tests/
```

## Integration Tests

### Test Upload and Process Image

This test uploads an image to the API and verifies that the image is processed correctly.

```python
def test_upload_and_process_image():
    ...
```

### Test Retrieve Image

This test retrieves an image from the API to verify that the image retrieval functionality works as expected.

```python
def test_get_image():
    ...
```

### Test Update Image

This test updates an existing image to verify that the image update functionality works as expected.

```python
def test_update_image():
    ...
```

### Test Delete Image

This test deletes an image to verify that the image deletion functionality works as expected.

```python
def test_delete_image():
    ...
```

## Contributing

We welcome contributions to enhance the integration tests. Please fork the repository, make your changes, and submit a pull request.


## Contact

For questions or feedback, please open an issue on the [GitHub repository](https://github.com/theodwya/image-pocessing-integration-tests).

