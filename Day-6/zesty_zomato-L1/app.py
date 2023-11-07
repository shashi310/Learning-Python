from flask import Flask,jsonify,request
import json

app= Flask(__name__ )

#loading the json files
with open('dishes.json','r') as f:
    dishes=json.load(f)

with open('orders.json','r') as f:
    orders=json.load(f)

#saving the current Json data
def save_data():
    # Save dishes and orders back to JSON files
    with open('dishes.json', 'w') as f:
        json.dump(dishes, f)

    with open('orders.json', 'w') as f:
        json.dump(orders, f)


@app.route('/get-dishes',methods=['GET'])
def get_dishes():
    return jsonify({'message':dishes})


@app.route('/add-dish', methods=['POST'])
def add_dish():
    data=request.get_json()
    dishes.append(data)
    save_data()
    return jsonify({'message':'Dish added successfully'})

@app.route('/update-dish/<int:dish_id>', methods=['PUT'])
def update_dish(dish_id):
    for dish in dishes:
        if dish['dish_id']==dish_id:
            dish.update(request.get_json())
            save_data()
            return jsonify({'message': 'Dish updated successfully'})
    return jsonify({'message': 'Dish not found'})

@app.route('/delete-dish/<int:dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    for dish in dishes:
        if dish['dish_id']==dish_id:
            dishes.remove(dish)
            save_data()
            return jsonify({'message': 'Dish deleted'})
    return jsonify({'message': 'Dish not found'})

@app.route('/get_dish/<int:dish_id>', methods=['GET'])
def get_dish(dish_id):
    for dish in dishes:
        if dish['dish_id']==dish_id:
            return jsonify({'message': dish})
    return jsonify({'message': 'Dish not found'})

if __name__ == '__main__':
    app.run(debug=True)
