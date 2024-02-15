from flask import redirect, render_template, url_for, request
from form_1 import db, User, app
import bcrypt 
"""
Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". 
При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
"""


@app.route("/", methods = ["POST", "GET"])
def main_page():
    name = request.args.get("name")
    print(name)
    return render_template("main.html")

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("good")

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


@app.route("/sing-up", methods = ["POST", "GET"])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        new_user = User(name=name, surname = surname, email = email, password = hash_password(password))
        print(name, surname, password, 22)
        db.session.add(new_user)
        db.session.commit()
        return render_template('index.html', user = name)
    return render_template("sign_up.html", user = User)

