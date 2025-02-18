from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = 'mi clave secreta'

@app.route('/')
def index():
    username = None
    if 'username' in session:
        username = session['username']
    return render_template('home.html', username=username)
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)   