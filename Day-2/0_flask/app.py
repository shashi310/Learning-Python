from flask import Flask, render_template
from snacks import Snack, SnackInventory

app = Flask(__name__)
inventory = SnackInventory()

@app.route('/')
def index():
    snacks = inventory.snacks
    return render_template('index.html', snacks=snacks)

if __name__ == '__main__':
    app.run(debug=True)
