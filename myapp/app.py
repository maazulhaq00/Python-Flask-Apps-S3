from flask import Flask, render_template

app = Flask(__name__)

my_port = 3333
app_url = f"http://127.0.0.1:{my_port}"

@app.route("/")
def index():
    name = "Faraz Sami"
    return render_template("index.html", visitor_name=name)

@app.route("/services")
def services():
    return render_template("services.html", app_url=app_url )

@app.route("/contact-us")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=my_port)