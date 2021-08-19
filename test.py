import pyrebase 
from  pyrebase.pyrebase import Storage
a = {
    "apiKey": "AIzaSyBVr3gx5xnzFNypRcKc0n-69miPnyXLYks",
    "authDomain": "note-management-system.firebaseapp.com",
    "databaseURL": "https://note-management-system.firebaseio.com",
    "projectId": "note-management-system",
    "storageBucket": "note-management-system.appspot.com",
    "messagingSenderId": "644251894279",
    "appId": "1:644251894279:web:a110969bd85480dfab60a2",
    "measurementId": "G-YJ1PMBM442",
}

firbase = pyrebase.initialize_app(a)
storage = firbase.storage()
path_on_cloud = "Files/Ranuga/a.py"
path_local = "test.py"
storage.child(path_on_cloud).put(path_local)
path_on_cloud = "Files/Ranuga/"
print(storage.child(path_on_cloud).list_files())
