from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
from bson import ObjectId 

PORT = 3001
APP_URL = f"http://127.0.0.1:{PORT}"

client = MongoClient("mongodb://localhost:27017/")
db = client["anaslmsdb"]
products_collection = db["products"]

app = Flask(__name__)


@app.route("/")
def index():
    product_list = products_collection.find()
    return render_template("index.html", product_list=product_list)


@app.route("/add-product", methods=["GET", "POST"])
def addproduct():
    if request.method == "POST":

        product_data = {
            "name": request.form["name"],
            "price": request.form["price"],
            "quantity": request.form["quantity"],
        }

        products_collection.insert_one(product_data)

        return redirect(url_for("index"))

    return render_template("addproduct.html")


@app.route("/edit-product/<id>", methods=["GET", "POST"])
def editproduct(id):

    if request.method == "POST":
        updated_product_data = {
            "name": request.form["name"],
            "price": request.form["price"],
            "quantity": request.form["quantity"],
        }

        products_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": updated_product_data}
        )

        return redirect(url_for("index"))

    product = products_collection.find_one({"_id": ObjectId(id)})
    return render_template("editproduct.html", p=product)


@app.route("/delete-product/<id>")
def deleteproduct(id):
    products_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=PORT)