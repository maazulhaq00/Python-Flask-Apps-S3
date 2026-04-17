from flask import Flask, render_template

app = Flask(__name__)


PORT= 3001
APP_URL = f"http://127.0.0.1:{PORT}"

@app.route("/")
@app.route("/<name>")
def index(name="User"):
    return render_template("index.html", visitor_name=name)

@app.route("/shop")
def shop():
    # products = ["Tsirt", "Jeans", "Trousers", "Shirts", "Cap"]

    products = [
        {
            "name": "T-shirt",
            "price": 1400,
            "desc": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Placeat iure voluptate sint molestiae veniam nulla similique aperiam autem quaerat, reiciendis beatae! Harum, eligendi nam fuga illum excepturi maxime autem? Eligendi.",
            "imgUrl": "https://nolson.nl/cdn/shop/files/3_4.jpg?v=1772113380",
            "onSale" : True,
            "isFeatured": True
        },
        {
            "name": "Jeans",
            "price": 2000,
            "desc": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Placeat iure voluptate sint molestiae veniam nulla similique aperiam autem quaerat, reiciendis beatae! Harum, eligendi nam fuga illum excepturi maxime autem? Eligendi.",
            "imgUrl": "https://nolson.nl/cdn/shop/files/3_4.jpg?v=1772113380",
            "onSale" : False,
            "isFeatured": True
        },
        {
            "name": "Trousers",
            "price": 1800,
            "desc": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Placeat iure voluptate sint molestiae veniam nulla similique aperiam autem quaerat, reiciendis beatae! Harum, eligendi nam fuga illum excepturi maxime autem? Eligendi.",
            "imgUrl": "https://nolson.nl/cdn/shop/files/3_4.jpg?v=1772113380",
            "onSale" : False,
            "isFeatured": False
        },
        {
            "name": "Shirt",
            "price": 1750,
            "desc": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Placeat iure voluptate sint molestiae veniam nulla similique aperiam autem quaerat, reiciendis beatae! Harum, eligendi nam fuga illum excepturi maxime autem? Eligendi.",
            "imgUrl": "https://nolson.nl/cdn/shop/files/3_4.jpg?v=1772113380",
            "onSale" : True,
            "isFeatured": False
        }
    ]

    return render_template("shop.html", products=products)

@app.route("/hello/<name>/<age>")
def greet(name, age):
    return f"<h3>Hello {name}, you are {age} years old</h3>"

@app.route("/isOld/<age>")
def isOld(age):
    return render_template("isOld.html", age=int(age))

if __name__ == "__main__":
    app.run(debug=True, port=PORT)