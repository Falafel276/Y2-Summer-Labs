from flask import Flask, render_template
import random 

app = Flask(__name__)

# Route for the home page

@app.route('/home')
def home():
    return render_template('home.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
