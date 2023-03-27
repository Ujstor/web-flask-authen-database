from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be longer than 3 chara.', category='error')
        elif len(firstName) <2:
            flash('Name must be longer than 1 chara.', category='error')
        elif password1 != password2:
            flash('Passwords dont match.', category='error')
        elif len(password1) < 1:
            flash('Passwords must be at least 7 chara.', category='error')
        else:
            flash('Account created')

            #add user to database

    return render_template("sign_up.html")
