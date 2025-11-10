import pytest
from app import app  # on importe notre application Flask

# 🔧 Fixture : crée un "client" pour tester l'application sans la lancer réellement
@pytest.fixture
def client():
    app.config["TESTING"] = True  # active le mode test
    return app.test_client()      # renvoie un client de test Flask

# 🏠 Test de la page d'accueil
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

# ❤️ Test de la route /health
def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"

# 🧾 Test de la route /version
def test_version(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert "version" in response.get_json()

# 🚫 Test d'une route inexistante
def test_not_found(client):
    response = client.get("/route-inexistante")
    assert response.status_code == 204
