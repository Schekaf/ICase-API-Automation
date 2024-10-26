import pytest


@pytest.fixture(scope="function")
def pet_payload():
    return {
        "id": 0,  # The API will assign an ID, but you can initialize it as 0.
        "category": {
            "id": 0,  # You can leave this as 0 for a test or specify a valid category ID.
            "name": "Cats"  # You can put a relevant name for your test.
        },
        "name": "Ketty",  # The name of the pet.
        "tags": [
            {
                "id": 0,  # Similar to category ID, this can be set to 0 or a valid tag ID.
                "name": "A Cute Cat"  # You can replace this with a relevant tag name.
            }
        ],
        "status": "available"  # The status of the pet.
    }