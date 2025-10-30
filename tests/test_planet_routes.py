def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_succeeds(client, one_planet):
    response = client.get(f"/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Earth",
        "description": "Home planet"   
    }

def test_create_one_planet(client):
    response = client.post("/planets", json={
        "name": "Venus",
        "description": "A planet"
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Venus",
        "description": "A planet"
    }