import pyrebase

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

email = 'test@gmail.com'
password = '123456'

# user = auth.create_user_with_email_and_password(email, password)
# print(user)

user = auth.sign_in_with_email_and_password(email, password)

# info = auth.get_account_info(user['idToken'])
# print(info)

# auth.send_email_verification(user['idToken'])

auth.send_password_reset_email(email)
