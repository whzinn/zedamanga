import pyrebase


Config = {
    "apiKey": "AIzaSyAYaMOb-La3_s59XIl9qwGAV0Lc4TLH9yQ",
  "authDomain": "casca-de-bala-d6970.firebaseapp.com",
  "databaseURL": "https://casca-de-bala-d6970-default-rtdb.firebaseio.com",
  "projectId": "casca-de-bala-d6970",
  "storageBucket": "casca-de-bala-d6970.firebasestorage.app",
  "messagingSenderId": "368205644481",
  "appId": "1:368205644481:web:1fc77663987f1b3cbe4a40",
  "measurementId": "G-Q9YYJ3SVKG"
}

firebase = pyrebase.initialize_app(Config)

db = firebase.database()
def cobranca(key, code, uid):
    data = {"key": f"{key}", "code": f"{code}"}
    db.child("cobrancas").child(f"{uid}").set(data)