from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase
import random
import string

# Your web app's Firebase configuration
firebaseConfig = {
  "apiKey": "AIzaSyAF7o6ScO48KZ2oUYyP-iAl5euoMwPYk-E",
  "authDomain": "meet-first-project-d6147.firebaseapp.com",
  "projectId": "meet-first-project-d6147",
  "storageBucket": "meet-first-project-d6147.appspot.com",
  "messagingSenderId": "85564189860",
  "appId": "1:85564189860:web:765d5d7c56248f3b924a31",
  "databaseURL": "https://meet-first-project-d6147-default-rtdb.europe-west1.firebasedatabase.app/"
}


# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'super-secret-key'

# Routes

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['full_name']
        username = request.form['username']
        user = {"full name": full_name, "email": email, "Username": username}
        try:
            user = auth.create_user_with_email_and_password(email, password)
            user_id = user['localId']
            db.child("user").child(user_id).set({
                "email": email,
                "password": password,
                "username": username
            })
            session['user'] = user
            return redirect(url_for('index'))
        except:
            return "Failed to create account. Try again."
    return render_template('signup.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            if 'quotes' not in session:
                session['quotes'] = []
            return redirect(url_for('home'))
        except:
            return "Invalid login credentials"
    return render_template('signin.html')


@app.route('/home', methods=['GET', 'POST'])

def home():
    if 'user' in session:
        if request.method == 'POST':
            # Create a dictionary with quote details
            quote = {
                'text': request.form['quote'],
                'said_by': request.form['said_by'],
                'uid': session['user']['localId']  # Add user ID to the quote
            }

            # Add quote to the Firebase database under "Quotes" with a random key
            random_key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            db.child("Quotes").child(random_key).set(quote)

            return redirect(url_for('thanks'))
        return render_template('home.html')
    return redirect(url_for('signin'))

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/display')
def display():
    if 'user' in session:
        # Get all quotes from the database and convert them into a dictionary
        quotes_data = db.child("Quotes").get().val()
        return render_template('display.html', quotes=quotes_data)
    return redirect(url_for('signin'))


@app.route('/signout')
def signout():
    session.pop('user', None)
    session.pop('quotes', None)
    return redirect(url_for('signin'))



if __name__ == '__main__':
    app.run(debug=True)

