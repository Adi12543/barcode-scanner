from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Sample product data
products = {
    '23045701': {'Product ID': '23045701', 'Product Name': 'Product 1', 'Product Description': 'This is product 1', 'Price': 100},
    'DEF456': {'Product ID': 'DEF456', 'Product Name': 'Product 2', 'Product Description': 'This is product 2', 'Price': 200},
    'GHI789': {'Product ID': 'GHI789', 'Product Name': 'Product 3', 'Product Description': 'This is product 3', 'Price': 300},
    
}

# Sample cart data
cart = []

@app.route('/')
def index():
    return render_template('index.html', products=products, cart=cart)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    scanned_code = request.form['scanned_code']
    if scanned_code in products:
        cart.append(products[scanned_code])
        return jsonify({'cart': cart})
    else:
        return jsonify({'error': 'Product not found'}), 404

@app.route('/delete_from_cart', methods=['POST'])
def delete_from_cart():
    item_id = request.form['item_id']
    for item in cart:
        if item['Product ID'] == item_id:
            cart.remove(item)
            return jsonify({'cart': cart})
    return jsonify({'error': 'Item not found in cart'}), 404

@app.route('/buy', methods=['GET', 'POST'])
def buy():
    # Implement payment processing logic here
    return 'Payment processing...'

if __name__ == '__main__':
    app.run(debug=True)