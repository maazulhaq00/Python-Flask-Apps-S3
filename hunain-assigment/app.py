from flask import Flask,render_template,request,redirect,url_for
from pymongo import MongoClient
from bson import ObjectId 


PORT=5001
APP_URL=f"http://127.0.0.1:{PORT}"
client = MongoClient("mongodb://localhost:27017/")
db = client["pythonapp"]
product_collection = db["products"]

app = Flask(__name__)

@app.route("/")
def index():
    product_list = product_collection.find()
    return render_template("index.html", products=product_list)

@app.route("/add-product", methods=["GET","POST"])
def addproduct():
    if request.method == "POST":
        products = {
            "name": request.form["name"],
            "price": request.form["price"],
            "description": request.form["description"],
        }
        product_collection.insert_one(products)
        return redirect(url_for("index"))
    
    return render_template("add-product.html")


@app.route("/delete-product/<id>")
def deleteproduct(id):
    product_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))

@app.route("/edit-product/<id>",methods=["GET","POST"])
def editproduct(id):
        if request.method == "POST":
            updated_products = {
            "name": request.form["name"],
            "price": request.form["price"],
            "description": request.form["description"],
        }
            product_collection.update_one({"_id":ObjectId(id)},{"$set":updated_products})
            return redirect(url_for("index"))
        
        product = product_collection.find_one({"_id": ObjectId(id)})
        return render_template("edit-product.html", product=product )

if __name__ == "__main__":
    app.run(debug=True,port=PORT)