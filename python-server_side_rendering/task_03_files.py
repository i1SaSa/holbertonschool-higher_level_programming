import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products = json.load(f)
        except FileNotFoundError:
            products = []

    elif source == 'csv':
        try:
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                products = [row for row in reader]
                for p in products:
                    p['id'] = int(p['id'])
        except FileNotFoundError:
            products = []

    if product_id:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
