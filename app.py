#This line of code is a part of the Flask web framework in Python. It's used to import specific functionalities and modules necessary for building web applications
from flask import Flask, render_template, request, redirect, url_for, session
#more explanation about Flask,render_template, request, redirect, url_for, session in README.md

app = Flask(__name__)
app.secret_key = 'your_secret_key'

#This code block is a Python list of dictionaries representing a menu for a coffee shop
#dictionary contains information about a specific item on the menu, including its ID, name, and price.
menu_items = [
    {'id': 1, 'name': 'Hot Cappuccino', 'price': 135.0},
    {'id': 2, 'name': 'Hot Americano', 'price': 140.0},
    {'id': 3, 'name': 'Hot Latte', 'price': 210.0},
    {'id': 4, 'name': 'Hot Espresso', 'price': 190.0},
    {'id': 5, 'name': 'Iced Cappuccino', 'price': 170.0},
    {'id': 6, 'name': 'Iced Americano', 'price': 160.0},
    {'id': 7, 'name': 'Iced Milky Latte', 'price': 155.0},
]

@app.route('/')
def index():# This is the Python function that will be executed when the user visits the root URL. It's named 'index'
    return render_template('index.html', menu_items=menu_items)# This provides the 'menu_items' data to the 'index.html' template. It allows the HTML template to access and utilize the 'menu_items' data.
    #This line serves the HTML content to be displayed in the user's browser.

@app.route('/add_to_cart/<int:item_id>')
def add_to_cart(item_id):
    cart = session.get('cart', [])
    cart.append(menu_items[item_id - 1])
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/remove_from_cart/<int:item_id>')
def remove_from_cart(item_id):
    cart = session.get('cart', [])
    if item_id - 1 < len(menu_items):
        cart.remove(menu_items[item_id - 1])
    session['cart'] = cart
    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    total_price = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/place_order', methods=['POST'])
def place_order():
    cart = session.get('cart', [])
    # Here you can implement the logic to place the order, save it in a database, etc.
    total_price = sum(item['price'] for item in cart)
    session.pop('cart', None)
    return render_template('confirmation.html', cart=cart,total_price=total_price)

if __name__ == '__main__':
    app.run(debug=True)
