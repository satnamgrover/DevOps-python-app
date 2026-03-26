from flask import Flask, render_template, request, redirect
from database import get_users, add_user

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users')
def users():
    user_list = get_users()
    return render_template('users.html', users=user_list)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        add_user(name, email)
        return redirect('/users')
    return render_template('add_user.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
