from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import os

app = Flask(__name__, template_folder="templates")
app.secret_key = 'your_secret_key'
DATA_FILE = 'data/users.xlsx'

# Ensure data folder and Excel file exist
if not os.path.exists('data'):
    os.makedirs('data')
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=['Name', 'Department', 'Year', 'Section', 'Username', 'Password'])
    df.to_excel(DATA_FILE, index=False)

@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', username=session['username'])

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        year = request.form['year']
        section = request.form['section']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return "Passwords do not match!"

        df = pd.read_excel(DATA_FILE)
        new_user = pd.DataFrame([[name, department, year, section, username, password]],
                                columns=['Name', 'Department', 'Year', 'Section', 'Username', 'Password'])
        df = pd.concat([df, new_user], ignore_index=True)
        df.to_excel(DATA_FILE, index=False)
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        df = pd.read_excel(DATA_FILE)
        user = df[(df['Username'] == username) & (df['Password'] == password)]
        
        if not user.empty:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Invalid credentials!"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('exit_page'))

@app.route('/exit')
def exit_page():
    return render_template('exit.html')

if __name__ == '__main__':
    app.run(debug=True)