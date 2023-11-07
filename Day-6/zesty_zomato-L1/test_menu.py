# def test_add_dish():
#     #code
#     pass

# def test_update_dish():
#     #code
#     pass

# def test_delete_dish():
#     #code
#     pass

# def test_get_dish():
#     #code
#     pass

# test_menu.py
from test_helpers import send_json_request


def test_add_dish(client):
    response = send_json_request(client, 'POST', '/add_dish', {"id": 5, "name": "Hot Dog", "price": 5, "available": True})
    assert response.status_code == 200
    assert response.json == {'message': 'Dish added successfully'}

# def test_add_dish(client):
#     response = client.post('/add_dish', json={"id": 5, "name": "Hot Dog", "price": 5, "available": True})
#     assert response.status_code == 200
#     assert response.json == {'message': 'Dish added successfully'}
    
# def test_update_dish(client):
#     response = client.put('/update_dish/2', json={"id": 2, "name": "Cheeseburger", "price": 10, "available": True})
#     assert response.status_code == 200
#     assert response.json == {'message': 'Dish updated successfully'}
    
# def test_delete_dish(client):
#     response = client.delete('/delete_dish/1')
#     assert response.status_code == 200
#     assert response.json == {'message': 'Dish deleted successfully'}
    
# def test_get_dish(client):
#     response = client.get('/get_dish/3')
#     assert response.status_code == 200
#     assert response.json == {'dish': {'id': 3, 'name': 'Pasta', 'price': 12, 'available': True}}
    

# def test_get_nonexistent_dish(client):
#     response = client.get('/get_dish/10')
#     assert response.status_code == 200
#     assert response.json == {'message': 'Dish not found'}
    


