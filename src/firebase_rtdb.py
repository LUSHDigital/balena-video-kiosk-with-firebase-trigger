import os
import base64
import pyrebase

databaseURL = os.environ['DBURL']
fbCredentials = os.environ['DBCRED']

with open("firebase-adminsdk.json", "wb") as fh:
    fh.write(base64.b64decode(fbCredentials))

config = {
  "apiKey": "apiKey",
  "authDomain": "lens-kiosk.firebaseapp.com",
  "databaseURL": databaseURL,
  "storageBucket": "lens-kiosk.appspot.com",
  "serviceAccount": "firebase-adminsdk.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

stores = db.child("stores").get()

print(stores.val())