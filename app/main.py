from flask import Flask, jsonify, request
import json

app = Flask(__name__)

DATA = "data/item.json"

def hello():
    return jsonify(messages="API rodando com sucesso")

data = {
    id:int,
    'name': str,
    'price': float
}

def read_json():

    with open(DATA, "r") as f:
        return json.load(f)
    
def append_item(parm):

    try:
        with open(DATA, "w") as f:
            json.dump(parm, f)
    except Exception as e:
        return e


@app.get("/", )
def run():
    return hello()

@app.route('/items', methods=['GET'])

def item():
    return read_json()

@app.route('/items/add', methods=['POST'])
def add():

    data = request.get_json()

    print(
        "------------------------------------------------"
        )
    
    print(data)

    print(
        "------------------------------------------------"
        )
    
    items = read_json()
    items.append(data)
    append_item(items)

    return jsonify(data)

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

