from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_unregisters_student_from_activity():
    original_participants = activities["Gym Class"]["participants"][:]

    response = client.delete(
        "/activities/Gym Class/signup",
        params={"email": "john@mergington.edu"},
    )

    assert response.status_code == 200
    assert "john@mergington.edu" not in activities["Gym Class"]["participants"]
    assert response.json()["message"] == "Removed john@mergington.edu from Gym Class"

    activities["Gym Class"]["participants"] = original_participants
