import pytest
from unittest.mock import patch, MagicMock
from io import BytesIO
from main import app as flask_app

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

def test_create_comment_success(client):
    mock_token = "mocktoken"
    mock_user_id = "123"
    data = {
        "Id_publication": "64ac123456789abcdef01234",
        "Comment": "Nice publication!"
    }

    with patch("main.jwt.decode") as mock_jwt_decode, \
         patch("services.functions.conection_mongo") as mock_conection_mongo:

        mock_jwt_decode.return_value = {"user_id": mock_user_id}
        
        mock_db = MagicMock()
        mock_comments_collection = MagicMock()
        mock_db.__getitem__.return_value = mock_comments_collection
        mock_conection_mongo.return_value = mock_db

        response = client.post(
            "/create-comment",
            headers={"Authorization": f"Bearer {mock_token}"},
            json=data
        )

        assert response.status_code == 201
        assert response.json["message"] == "Comment created successfully"
