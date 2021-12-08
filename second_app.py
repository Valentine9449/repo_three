from flask import Flask, request, session, redirect

second_app = Flask(__name__)
second_app.secret_key = '4a5bc1c65d6f28ef795171cb69144e3658fec03fa2f128fdbf867556cca842c4'


@second_app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect('/index')
    elif 'username' not in session:
        return '''
               <form method='POST'>
                 <input name="username">
                 <input name="password">
                 <input type="submit">
             </form>
        '''
    return redirect('/index')


@second_app.route("/")
@second_app.route("/index")
def index():
    if 'username' in session:
        if 'visits' in session:
            session['visits'] = session.get('visits') + 1
        else:
            session['visits'] = 1
        return f"<h1>Пользователь зашел в систему как {session['username']}</h1>" + \
               "Total visits: {}".format(session.get('visits'))
    return redirect('/login')


@second_app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('visits', None)
    return 'Пользователь вышел'


if __name__ == '__main__':
    second_app.run(debug=True)
