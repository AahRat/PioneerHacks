from flask import Flask, session, render_template, request, redirect
import pyrebase

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


@app.route('/', methods=['POST', 'GET'])
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
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = email
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
