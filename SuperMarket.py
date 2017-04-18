from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash
import DatabaseConnection
import transaction

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

    if DatabaseConnection.exec_staff_login(username, password):
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

    (is_valid, user_tuple) = DatabaseConnection.exec_customer_login(username, password)
    user_id = user_tuple[0][0]
    if is_valid:
        return redirect(url_for('customer', user_id=user_id))

    flash("The account does not exist, check it again.")
    return redirect('/customer_login')


@app.route('/customer/<user_id>', methods=['GET'])
def customer_form(user_id=None):
    items = DatabaseConnection.exec_show_items()
    return render_template("customer.html", user_id=user_id, items=items)


@app.route('/customer/<user_id>', methods=['POST'])
def customer(user_id=None):
    order_list = request.form['items[]']
    # TODO transaction.process purchase(user_id, order_list)

    return redirect(url_for('customer', user_id=user_id))


@app.route('/customer_information/<user_id>')
def customer_information(user_id=None):
    # TODO customer_info = fetch_all_information_from_customer(user_id)
    return render_template('customer_information.html', user_id=user_id)


@app.route('/customer_complain/<user_id>', methods=['GET'])
def complain_form(user_id=None):
    return render_template('customer_complain.html', user_id=user_id)


@app.route('/customer_complain/<user_id>', methods=['POST'])
def complain(user_id=None):
    # TODO complain_list = request.form['']
    # transaction.process_complain(user_id, complain_list)
    return render_template('customer.html', user_id=user_id)


@app.route('/supplier')
def supplier(username=None):
    return render_template("supplier.html")


@app.route('/staffone/<username>')
def staffone(username=None):
    return render_template("staffone.html", username=username, time=time)


@app.route('/registeration', methods=['GET'])
def registeration_form():
    return render_template('registeration.html')


@app.route('/registeration', methods=['POST'])
def registeration():
    username = request.form['username']
    password = request.form['password']
    retype_password = request.form['retype_password']
    email = request.form['email']

    if retype_password != password:
        flash("The password is not consistent!")
        return redirect('/registeration')

    is_valid = DatabaseConnection.exec_register_customer(username, password, email)
    if is_valid:
        return redirect('/customer_login')
    else:
        flash("The username has been registered, Please Try again")
        return redirect('/registeration')


#
# @app.route()
# def logout():
#     pass


if __name__ == '__main__':
    app.run(debug=True)
