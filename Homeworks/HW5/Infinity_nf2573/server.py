from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 2
data = [
    {
        "id": 1,
        "name": "michael scott"
    },
    {
        "id": 2,
        "name": "jim halpert"
    },
]

current_id = 4
sales = [
    {
        "id": 1,
        "salesperson": "James D. Halpert",
        "client": "Shake Shack",
        "reams": 1000
    },
    {
        "id": 2,
        "salesperson": "Stanley Hudson",
        "client": "Toast",
        "reams": 4000
    },
    {
        "id": 3,
        "salesperson": "Michael G. Scott",
        "client": "Computer Science Department",
        "reams": 10000
    }
]

clients = [
    "Shake Shack",
    "Toast",
    "Computer Science Department",
    "Teacher's College",
    "Starbucks",
    "Subsconsious",
    "Flat Top",
    "Joe's Coffee",
    "Max Caffe",
    "Nussbaum & Wu",
    "Taco Bell",
]

# ROUTES

@app.route('/')
def hello_world():
   return render_template('welcome.html')   

@app.route('/infinity')
def infinity():
    return render_template('log_sales.html', clients=clients, sales=sales)  

@app.route('/people')
def people():
    return render_template('people.html', data=data)


# AJAX FUNCTIONS

@app.route('/delete_sale')
def delete_sale():
    global sales

    sale_id = request.form.get('id')
    if not sale_id.isdigit():
        return jsonify({"error": "Invalid ID"}), 400

    sale_id = int(sale_id)

    # Filter out the sale with the matching ID
    sales = [sale for sale in sales if sale["id"] != sale_id]

    return jsonify(sales=sales)

@app.route('/save_sale', methods=['POST'])
def save_sale():
    global current_id, sales, clients

    salesperson = request.form.get('salesperson')
    client = request.form.get('client')
    reams = request.form.get('reams')

    if not salesperson or not client or not reams.isdigit() or int(reams) <= 0:
        return jsonify({"error": "Invalid data"}), 400

    reams = int(reams)  # Convert to integer
    current_id += 1  # Assign new unique ID

    new_sale = {
        "id": current_id,
        "salesperson": salesperson,
        "client": client,
        "reams": reams
    }

    sales.insert(0, new_sale)

    if client not in clients:
        clients.append(client)

    return jsonify(sales=sales, clients=clients)


# ajax for people.js
# @app.route('/add_name', methods=['GET', 'POST'])
# def add_name():
#     global data 
#     global current_id 

#     json_data = request.get_json()   
#     name = json_data["name"] 
    
#     # add new entry to array with 
#     # a new id and the name the user sent in JSON
#     current_id += 1
#     new_id = current_id 
#     new_name_entry = {
#         "name": name,
#         "id":  current_id
#     }
#     data.append(new_name_entry)

#     #send back the WHOLE array of data, so the client can redisplay it
#     return jsonify(data = data)

 


if __name__ == '__main__':
   app.run(debug = True, port=5001)




