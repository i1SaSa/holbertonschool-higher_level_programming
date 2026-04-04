import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            products = []

    elif source == 'csv':
        try:
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                products = [{"id": int(row['id']), "name": row['name'],
                             "category": row['category'], "price": float(row['price'])}
                            for row in reader]
        except (FileNotFoundError, KeyError):
            products = []

    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            if product_id:
                cursor.execute(
                    "SELECT * FROM Products WHERE id = ?", (product_id,))
            else:
                cursor.execute("SELECT * FROM Products")

            rows = cursor.fetchall()
            products = [dict(row) for row in rows]
            conn.close()
        except sqlite3.Error as e:
            return render_template('product_display.html', error=f"Database error: {e}")

    if source != 'sql' and product_id:
        products = [p for p in products if p['id'] == product_id]

    if product_id and not products:
        return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
