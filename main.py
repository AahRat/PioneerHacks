from flask import Flask, session, render_template, request, redirect
import pyrebase
import firebase_admin
from firebase_admin import firestore, credentials
from weather import value_cleaner
from formula import weather_formula

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
    db = firestore.client()
    if 'user' in session:
        email = session.get('user')
        preferences = db.collection('Users').document(email).get().to_dict()
        location = 'Sunnyvale'
        real_weather = value_cleaner(location)
        index_number = weather_formula(preferences, real_weather)
        print(index_number)
        # index_number = 50
        return render_template('homepageIndex.html', Index=index_number, Temperature=real_weather[0], Humidity=real_weather[1], Precipitation=real_weather[6], Wind=real_weather[3], CloudCover=real_weather[4], Visibility=real_weather[5])
    return render_template('first_page.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    db = firestore.client()
    if 'user' in session:
        email = session.get('user')
        preferences = db.collection('Users').document(email).get().to_dict()
        location = 'Sunnyvale'
        real_weather = value_cleaner(location)
        index_number = weather_formula(preferences, real_weather)
        print(index_number)
        return render_template('homepageIndex.html', Index=index_number, Temperature=real_weather[0], Humidity=real_weather[1], Precipitation=real_weather[6], Wind=real_weather[3], CloudCover=real_weather[4], Visibility=real_weather[5])

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email

            preferences = db.collection('Users').document(email).get().to_dict()
            location = 'Sunnyvale'
            real_weather = value_cleaner(location)
            index_number = weather_formula(preferences, real_weather)
            print(index_number)
            return render_template('homepageIndex.html', Index=index_number, Temperature=real_weather[0],
                                   Humidity=real_weather[1], Precipitation=real_weather[6], Wind=real_weather[3],
                                   CloudCover=real_weather[4], Visibility=real_weather[5])

        except:
            return render_template('login.html')
    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    db = firestore.client()
    if request.method == 'POST':
        print("GOT HERE")
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            print("GOT HERE2")
            user = auth.create_user_with_email_and_password(email, password)
            print("GOT HERE3")
            session['user'] = email
            print("CREATED ACCOUNT")
            preferences = {
                "Precipitation": request.form.get('precipitation'),
                "Temperature": int(request.form.get('temperature')),
                "Humidity": int(request.form.get('humidity')),
                "Wind": int(request.form.get('wind')),
                "Cloud Cover": int(request.form.get('cloudcover')),
                "Visibility": int(request.form.get('visibility'))
            }
            db.collection(u'Users').document(email).set(preferences)
            print("SET PREFERENCES")

            preferences = db.collection('Users').document(email).get().to_dict()
            location = 'Sunnyvale'
            real_weather = value_cleaner(location)
            index_number = weather_formula(preferences, real_weather)
            print(index_number)

            return render_template('homepageIndex.html', Index=index_number, Temperature=real_weather[0],
                                   Humidity=real_weather[1], Precipitation=real_weather[6], Wind=real_weather[3],
                                   CloudCover=real_weather[4], Visibility=real_weather[5])

        except:
            return render_template('signup.html')
    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')


if __name__ == '__main__':
    app.run(port=1111)
