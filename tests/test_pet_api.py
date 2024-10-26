from random import random

import pytest
import requests
from tests.fixtures.pet_fixtures import pet_payload

BASE_URL = "https://petstore.swagger.io/v2"
PET_ENDPOINT = f"{BASE_URL}/pet"


# POST /pet - Add New Pet

def test_add_new_pet_success(pet_payload):
    response = requests.post(PET_ENDPOINT, json=pet_payload)
    assert response.status_code == 200
    assert response.json()["name"] == pet_payload["name"]


def test_add_new_pet_invalid_data():
    invalid_payload = {
        "id": "invalid_id",
        "name": 123  # Name should be a string
    }
    response = requests.post(PET_ENDPOINT, json=invalid_payload)
    assert response.status_code == 500


# GET /pet/{petId} - Find Pet by ID

def test_get_pet_by_id_success(pet_payload):
    new_pet_response = requests.post(PET_ENDPOINT, json=pet_payload)
    pet_id = new_pet_response.json()["id"]
    response = requests.get(f"{PET_ENDPOINT}/{pet_id}")
    assert response.status_code == 200
    assert response.json()["id"] == pet_id


def test_get_pet_by_id_not_found():
    non_existent_id = 999999
    response = requests.get(f"{PET_ENDPOINT}/{non_existent_id}")
    assert response.status_code == 404


# PUT /pet - Update Existing Pet

def test_update_pet_success(pet_payload):
    # First, create a pet
    requests.post(PET_ENDPOINT, json=pet_payload)
    updated_payload = pet_payload.copy()
    updated_payload["name"] = "UpdatedCatName"

    response = requests.put(PET_ENDPOINT, json=updated_payload)
    assert response.status_code == 200
    assert response.json()["name"] == "UpdatedCatName"


def test_update_pet_invalid_data(pet_payload):
    # First, check a not existing pet
    non_existent_id = 999999
    no_pet_response = requests.get(f"{PET_ENDPOINT}/{non_existent_id}")
    assert no_pet_response.status_code == 404
    invalid_payload = {
        "id": non_existent_id,
        "name": "Catty"
    }
    response = requests.put(PET_ENDPOINT, json=invalid_payload)
    assert response.status_code == 400


# POST /pet/{petId}/uploadImage - Upload Image for Pet

def test_upload_pet_image_success(pet_payload):
    # First, create a pet to ensure it exists
    new_pet = requests.post(PET_ENDPOINT, json=pet_payload)
    pet_id = new_pet.json()["id"]

    files = {'file': ('test_image.jpg', open('assets/pets.jpg', 'rb'), 'image/jpeg')}
    response = requests.post(f"{PET_ENDPOINT}/{pet_id}/uploadImage", files=files)
    assert response.status_code == 200
    assert "message" in response.json()  # Checking if there's a response message


def test_upload_pet_image_invalid_pet():
    # First, check a not existing pet
    non_existent_id = 999999
    no_pet_response = requests.get(f"{PET_ENDPOINT}/{non_existent_id}")
    assert no_pet_response.status_code == 404
    files = {'file': ('test_image.jpg', open('assets/pets.jpg', 'rb'), 'image/jpeg')}
    response = requests.post(f"{PET_ENDPOINT}/{non_existent_id}/uploadImage", files=files)
    assert response.status_code == 404


# Create Pet (POST /pet)
def test_create_pet_success(pet_payload):
    response = requests.post(PET_ENDPOINT, json=pet_payload)
    assert response.status_code == 200
    assert response.json()["name"] == pet_payload["name"]


def test_create_pet_invalid_data():
    invalid_payload = {"id": "invalid", "name": 123}
    response = requests.post(PET_ENDPOINT, json=invalid_payload)
    assert response.status_code == 400  # Expecting a bad request due to invalid data


# GET /pet/findByStatus - Find Pets by Status
def test_find_pets_by_status_success(pet_payload):
    requests.post(PET_ENDPOINT, json=pet_payload)
    status = pet_payload["status"]
    response = requests.get(f"{PET_ENDPOINT}/findByStatus?status={status}")
    assert response.status_code == 200
    assert all(pet["status"] == status for pet in response.json())


def test_find_pets_by_status_invalid_status():
    invalid_status = "unknown_status"
    response = requests.get(f"{PET_ENDPOINT}/findByStatus?status={invalid_status}")
    assert response.status_code == 400


# DELETE /pet/{petId} - Delete Pet by ID
def test_delete_pet_success(pet_payload):
    new_pet = requests.post(PET_ENDPOINT, json=pet_payload)
    pet_id = new_pet.json()["id"]
    response = requests.delete(f"{PET_ENDPOINT}/{pet_id}")
    assert response.status_code == 200
    assert response.json()["message"] == str(pet_id)


def test_delete_pet_not_found():
    # First, check a not existing pet
    non_existent_id = 999999
    no_pet_response = requests.get(f"{PET_ENDPOINT}/{non_existent_id}")
    assert no_pet_response.status_code == 404
    response = requests.delete(f"{PET_ENDPOINT}/{non_existent_id}")
    assert response.status_code == 404
