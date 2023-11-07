from flask import Flask, jsonify, request

app = Flask(__name__)
weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}



@app.route("/", methods=['GET'])
def welcome():
    return jsonify({"message": "welcome to the backend of  weather app!"})


@app.route("/weather/<string:city>")
def weather(city):
    if city in weather_data:
        return jsonify({"Weather_data": weather_data[city]})
    else:
        return jsonify({"message": "Invalid city"})


@app.route("/weather", methods=['POST'])
def postWeather():
    if(request.method == 'POST'):
        data = request.get_json()
        try:
            city = str(data['city'])
            temperature = int(data['temperature'])
            weather = data['weather']
            if weather in ['Cloudy', 'Sunny', 'Rainy', 'Hot']:
                weather_data[city] = {
                    "temperature": temperature,
                    "weather": weather
                }
                return jsonify({"message": "Data added!"})
            else:
                return jsonify({"message": "Please write correct weather"})
        except KeyError:
            return jsonify({"message": "Please write correct data format"})
        

@app.route('/weather/<string:city>', methods=["PUT", "DELETE"])
def putWeather(city):
    try:
        if(request.method == 'PUT'):
            data = request.get_json()
            
            if(weather_data[city] and data['temperature'] and data['weather'] and data['weather'] in ['Cloudy', 'Sunny', 'Rainy', 'Hot']):
                weather_data[city]['weather'] = data['weather']
                weather_data[city]['temperature'] = data['temperature']
                return jsonify({"message": "Data updated!"})
            else:
                return jsonify({"message": "Invalid Data"})
            
        elif(request.method == 'DELETE'):
            if(city in weather_data):
                weather_data.pop(city)
                return jsonify({"message": "Data deleted!"}) 
            else:
                return jsonify({"message": "City not found"}) 
    except:
        return jsonify({"message": "Something is wrong"})



if __name__ =='__main__':
    app.run(debug=True)