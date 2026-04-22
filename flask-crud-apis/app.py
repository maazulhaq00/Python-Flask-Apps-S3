from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId 

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

@app.route("/edit-student/<id>", methods=["GET", "POST"])
def editstudent(id):

    if request.method == "POST":
        updated_student_data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "contact": request.form["contact"],
            "course": request.form["course"],
        }

        students_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_student_data})

        return redirect(url_for("index"))

    student = students_collection.find_one({"_id": ObjectId(id)})
    return render_template("edit-student.html", student=student )

@app.route("/delete-student/<id>")
def deletestudent(id):
    students_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True,port=PORT)

