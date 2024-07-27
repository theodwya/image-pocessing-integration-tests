"""
Integration test for the image processing API.
"""

import os
import time
import requests

BASE_URL = "http://localhost:8000"  # Update if running on different host/port


def test_upload_and_process_image():
    """
    Test the upload and processing of an image file.
    """
    # Ensure the test image exists
    test_image_path = "test_images/sample1.jp2"
    assert os.path.exists(test_image_path)

    # Upload an image
    with open(test_image_path, "rb") as image_file:
        response = requests.post(
            f"{BASE_URL}/ipload/",
            files={"file": ("sample1.jp2", image_file, "image/jp2")},
            data={"operation": "decode"}
        )

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == "File uploaded successfully"
    task_id = response_data["task_id"]

    # Wait for the task to complete
    time.sleep(5)  # Wait for 5 seconds (adjust as needed)

    # Verify the output image exists
    output_image_path = f"output/sample1_output.jp2"
    assert os.path.exists(output_image_path)

    # Wait for the image to be processed
    time.sleep(5)

    # Get the processed image
    response = requests.get(f"{BASE_URL}/download")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/jpeg"
    assert response.headers["Content-Disposition"] == "attachment; filename=processed_image.jpg"
    assert response.content

    # Delete the processed image
    response = requests.delete(f"{BASE_URL}/delete")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Processed image deleted successfully"}

    # Get the processed image again
    response = requests.get(f"{BASE_URL}/download")
    assert response.status_code == 404
    assert response.json() == {"error": "Processed image not found"}

    # Delete the processed image again
    response = requests.delete(f"{BASE_URL}/delete")
    assert response.status_code == 404
    assert response.json() == {"error": "Processed image not found"}
