from flask import Flask, session, render_template, request, redirect
import pyrebase
import firebase_admin
from firebase_admin import firestore, credentials

app = Flask(__name__)

config = {
    'apiKey': "AIzaSyDyXhTxo6x3hTQTIp2_G1ZlL_w-jvFqbQE",
    'authDomain': "pioneerhacks-6a057.firebaseapp.com",
    'projectId': "pioneerhacks-6a057",
    'storageBucket': "pioneerhacks-6a057.appspot.com",
    'messagingSenderId': "114861868300",
    'appId': "1:114861868300:web:05d401a83d5e328d5db529",
    'measurementId': "G-TTWEJKD5PC",
    'databaseURL': ''
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'secret'

cred = credentials.Certificate("./pioneerhacks-6a057-firebase-adminsdk-8a13u-c8adfd5fce.json")
default_app = firebase_admin.initialize_app(cred)


@app.route('/', methods=['POST', 'GET'])
def home():
    if 'user' in session:
        return render_template('home.html')
    return render_template('first_page.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'user' in session:
        return render_template('home.html')

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
            return render_template('home.html')
        except:
            return render_template('login.html')
    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    db = firestore.client()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = email

            preferences = {
                "Precipitation": request.form.get('precipitation'),
                "Temperature": request.form.get('temperature'),
                "Humidity": request.form.get('humidity'),
                "Wind": request.form.get('wind'),
                "Cloud Cover": request.form.get('cloudcover'),
                "Visibility": request.form.get('visibility')
            }
            db.collection(u'Users').document(email).set(preferences)
            return render_template('home.html')
        except:
            return render_template('signup.html')
    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')


if __name__ == '__main__':
    app.run(port=1111)
