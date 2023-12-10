from flask import Flask, render_template


appFlask(__name__)

app.secret_key = '56fyj58'


@app.route('/')
def home():
    return render_template('index.html'

@app.route('/login')
def log_user():
    return render_template('login.html')

@app.route('/register')
def register_user():
    return render_template('register.html')

@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/auth/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password ']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template('profile.html', email=session['email'])

@app.route('/auth/register', methods=['Post'])
def register_user():
    email = request.form['email']
    password = request.form['password ']

    User.register(email, password)
    User.register(email, password)
    return render_template('profile.html', email=session['email'])


if __name__ == '__main__':
    app.run(debug=True)
