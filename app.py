from flask import Flask, render_template, redirect, url_for, request, jsonify
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return "Hello World!"

@app.route('/about')
def welcome():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Invalid credentials. Please try again."
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)
