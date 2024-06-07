from flask import request
from flask import Flask, request, jsonify
from api import *
app = Flask(__name__)

@app.route("/tables", methods=["GET"])
def get_tables():
    tables = Database.get_all_table_names()
    return jsonify(tables)

@app.route("/books", methods=["GET"])
def get_books():
    books = Book.get_all()
    return jsonify(books)

@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    book = Book.create(
        data['name'],
        data['publication_year'],
        data['pages'],
        data['id_publisher'],
        data['id_category']
    )
    return jsonify(book), 201

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.get_by_id(book_id)
    return jsonify(book)

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    book = Book.update(
        book_id,
        data['name'],
        data['publication_year'],
        data['pages'],
        data['id_publisher'],
        data['id_category']
    )
    return jsonify(book)

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.delete(book_id)
    return jsonify(book)

@app.route("/transaction", methods=["POST"])
def transaction():
    data = request.get_json()
    bought_data = data.get("bought")
    inventory_data = data.get("inventory")
    queries = []
    bought_query = "INSERT INTO bought (book_number, customer_number, purchase_date, price, quantity) VALUES (%s, %s, %s, %s, %s);"
    bought_params = (bought_data["book_number"], bought_data["customer_number"],
                     bought_data["purchase_date"], bought_data["price"], bought_data["quantity"])
    queries.append((bought_query, bought_params))

    inventory_query = "UPDATE storeinventory SET quantity = quantity - %s WHERE id_inventory = %s;"
    inventory_params = (
        inventory_data["quantity"], inventory_data["id_inventory"])
    queries.append((inventory_query, inventory_params))
    try:
        execute_transaction(queries)
        return jsonify({"message": "Transaction executed successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/query", methods=["POST"])
def execute_query():
    data = request.get_json()
    query = data.get("query")

    try:
        cur = get_db_connection().cursor()
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/useraccounts", methods=["GET"])
def get_user_accounts():
    user_accounts = UserAccount.get_all()
    return jsonify(user_accounts)


@app.route("/publishers", methods=["GET"])
def get_publishers():
    publishers = Publisher.get_all()
    return jsonify(publishers)


@app.route("/categories", methods=["GET"])
def get_categories():
    categories = Category.get_all()
    return jsonify(categories)


@app.route("/customers", methods=["GET"])
def get_customers():
    customers = Customer.get_all()
    return jsonify(customers)


@app.route("/onlinestores", methods=["GET"])
def get_online_stores():
    online_stores = OnlineStore.get_all()
    return jsonify(online_stores)


@app.route("/wishlistitems", methods=["GET"])
def get_wishlist_items():
    wishlist_items = WishlistItem.get_all()
    return jsonify(wishlist_items)


@app.route("/wishlists", methods=["GET"])
def get_wishlists():
    wishlists = Wishlist.get_all()
    return jsonify(wishlists)


@app.route("/reviews", methods=["GET"])
def get_reviews():
    reviews = Review.get_all()
    return jsonify(reviews)


@app.route("/storeinventory", methods=["GET"])
def get_store_inventory():
    store_inventory = StoreInventory.get_all()
    return jsonify(store_inventory)


@app.route("/boughts", methods=["GET"])
def get_boughts():
    boughts = Bought.get_all()
    return jsonify(boughts)


@app.route("/wrotes", methods=["GET"])
def get_wrotes():
    wrotes = Wrote.get_all()
    return jsonify(wrotes)


@app.route("/staff", methods=["GET"])
def get_staff():
    staff = Staff.get_all()
    return jsonify(staff)


@app.route("/authors", methods=["GET"])
def get_authors():
    authors = Author.get_all()
    return jsonify(authors)


@app.route("/stores", methods=["GET"])
def get_stores():
    stores = Store.get_all()
    return jsonify(stores)


@app.route("/stores/<int:store_id>", methods=["PUT"])
def update_store(store_id):
    data = request.get_json()
    store = Store.update(store_id, data['name'], data['location'])
    return jsonify(store)


@app.route("/stores", methods=["POST"])
def create_store():
    data = request.get_json()
    store = Store.create(data['name'], data['location'])
    return jsonify(store), 201


@app.route("/stores/<int:store_id>", methods=["DELETE"])
def delete_store(store_id):
    store = Store.delete(store_id)
    return jsonify(store)


if __name__ == "__main__":
    app.run(debug=True)
