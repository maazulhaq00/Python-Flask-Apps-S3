from flask import Flask, render_template
from pymongo import MongoClient

PORT=5001
APP_URL=f"http://127.0.0.1:{PORT}"

client = MongoClient("mongodb://localhost:27017/")
db = client["maazlmsdb"]
students_collection = db["students"]
# teacher_collection = db["teachers"]


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add-student")
def addstudent():
    return render_template("add-student.html")


if __name__ == "__main__":
    app.run(debug=True,port=PORT)

