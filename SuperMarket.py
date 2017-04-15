from flask import Flask, render_template, request, redirect, url_for, flash

from datetime import datetime

time = str(datetime.now())

app = Flask(__name__)
app.secret_key = 'asfasfasfasqwerqwr'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/supplier_login', methods=['GET'])
def supplier_login_form():
    return render_template('supplier_login.html')


@app.route('/supplier_login', methods=['POST'])
def supplier_login():
    username = request.form['username']
    password = request.form['password']

    if username == 'supplier' and password == 'password':
        return redirect(url_for('supplier', username=username))

    flash("The account does not exist, please retype it!")
    return redirect('/supplier_login')


@app.route('/staff_login', methods=['GET'])
def staff_login_form():
    return render_template('staff_login.html')


@app.route('/staff_login', methods=['POST'])
def staff_login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'password':
        return redirect(url_for('staffone', username=username))


    flash("The account does not exist, please retype it!")
    return redirect('/staff_login')


@app.route('/customer_login', methods=['GET'])
def customer_login_form():
    return render_template('customer_login.html')


@app.route('/customer_login', methods=['POST'])
def customer_login():
    username = request.form['username']
    password = request.form['password']

    if username == 'customer' and password == 'password':
        return redirect(url_for('customer', username=username))

    flash("The account does not exist, check it again.")
    return redirect('/customer_login')


@app.route('/customer/<username>')
def customer(username=None):
    return render_template("customer.html", username=username)


@app.route('/supplier/<username>')
def supplier(username=None):
    return render_template("supplier.html", username=username,)


@app.route('/staffone/<username>')
def staffone(username=None):
    return render_template("staffone.html", username=username, time=time)


@app.route('/registeration')
def registeration():
    return render_template('registeration.html')


if __name__ == '__main__':
    app.run(debug=True)
