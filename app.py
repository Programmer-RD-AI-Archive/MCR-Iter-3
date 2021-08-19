from flask import *
import pyrebase
from firebase import firebase
import os
import shutil

app = Flask(__name__)
app.debug = True
app.secret_key = "RANUGA"
firebaseconfig = {
    "apiKey": "AIzaSyBVr3gx5xnzFNypRcKc0n-69miPnyXLYks",
    "authDomain": "note-management-system.firebaseapp.com",
    "databaseURL": "https://note-management-system.firebaseio.com",
    "projectId": "note-management-system",
    "storageBucket": "note-management-system.appspot.com",
    "messagingSenderId": "644251894279",
    "appId": "1:644251894279:web:a110969bd85480dfab60a2",
    "measurementId": "G-YJ1PMBM442",
}
firebase_ = pyrebase.initialize_app(firebaseconfig)
storage = firebase_.storage()
firebase_db = firebase.FirebaseApplication(
    "https://note-management-system.firebaseio.com/", None
)


def get_notes():
    try:
        result = firebase_db.get("/note-management-system/Notes", "")
        print(result)
        a = []
        for c in result:
            print(result[c])
            a.append(result[c])
        print(a)
        if a == []:
            return []
        else:
            return a
    except:
        return []


def new_note(title, description, filenames):
    path_local = []
    for m in filenames:
        path_local.append(
            "/home/indika/Projects/Reminder/Learning/Project/Info/" + title + "/" + m
        )
    print(path_local)
    for x in path_local:
        print(x)
        path_on_cloud = f"Files/{title}/{m}"
        print(path_local)
        storage.child(path_on_cloud).put(x)
    data = {"title": title, "description": description}
    firebase_db.post("/note-management-system/Notes", data)
    shutil.rmtree("/home/indika/Projects/Reminder/Learning/Project/Info/" + title)
    return True


@app.route("/")
def home():
    return render_template("home.html", info="Information and Data \n Programming")


@app.route("/Children", methods=["POST", "GET"])
@app.route("/Children/", methods=["POST", "GET"])
def children():
    info = get_notes()
    return render_template("children.html", infos=info)


@app.route("/Teacher", methods=["POST", "GET"])
@app.route("/Teacher/", methods=["POST", "GET"])
def teacher():
    if request.method == "POST":
        title = request.form["T"]
        description = request.form["D"]
        if title == "" or description == "":
            return "Title or Description is Blank ! "
        else:
            files = request.files.getlist("file")
            os.mkdir("/home/indika/Projects/Reminder/Learning/Project/Info/" + title)
            a = []
            for file in files:
                a.append(file.filename)
                file.save(
                    os.path.join(
                        "/home/indika/Projects/Reminder/Learning/Project/Info/" + title,
                        file.filename,
                    )
                )
            print(a)
            reuslt = new_note(title=title, description=description, filenames=a)
            if reuslt is True:
                return "New Note Added ! "
            else:
                return "An error occured ! "
    else:
        info = get_notes()
        return render_template("teacher.html", infos=info)


if __name__ == "__main__":
    app.run(host="192.168.1.7")
