from flask import Flask, render_template, request, redirect, url_for
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
    students_list = students_collection.find()

    return render_template("index.html", students_list=students_list)

@app.route("/add-student", methods=["GET", "POST"])
def addstudent():
    if request.method == "POST":

        student_data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "contact": request.form["contact"],
            "course": request.form["course"],
        }

        students_collection.insert_one(student_data)

        return redirect(url_for("index"))
    
    return render_template("add-student.html")


if __name__ == "__main__":
    app.run(debug=True,port=PORT)

