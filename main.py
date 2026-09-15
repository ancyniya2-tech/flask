from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_products, insert_stock, insert_products, get_sales, get_stock, insert_sales, available_stock,check_user_exists,insert_user
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = 'yuewhjfjsyugsjvjfs'


@app.route('/')
def home():
    name = "Ancy Niya"
    return render_template('index.html', x=name)


@app.route('/products')
def products():
    products = get_products()
    return render_template('products.html', products=products)


@app.route('/add_products', methods=['GET', 'POST'])
def add_products():
    if request.method == "POST":
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']

        new_product = [product_name, buying_price, selling_price]
        insert_products[new_product]

        flash("Products added successfully", "success")
    return redirect(url_for['products'])


@app.route('/sales')
def sales():
    sales = get_sales()
    products = get_products()
    return render_template('sales.html', sales=sales, products=products)


@app.route('/make_sale', methods=['GET', 'POST'])
def make_sale():
    if request.method == 'POST':
        pid = request.form['pid']
        quantity = request.form['quantity']

        new_sale = (pid, quantity)

        check_stock = available_stock(pid)

        if check_stock < float(quantity):
            flash(f"Insufficient stock to complete sale, only{check_stock} remaining","danger")
            return redirect(url_for('sales'))

        insert_sales(new_sale)

        flash("Sale made successfully", 'success')

    return redirect(url_for('sales'))


@app.route('/stock')
def stock():
    stock = get_stock()
    products = get_products()
    return render_template('stock.html', stock=stock, products=products)


@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        pid = request.form['pid']
        stock_quantity = request.form['s_quantity']

        new_stock = (pid, stock_quantity)

        insert_stock(new_stock)
        flash("Stock has been inserted succesfully", 'success')
    return redirect(url_for('stock'))


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', method=['GET','POST'])
def register():
    if request.method == 'POST':

        full_name = request.form['full_name']
        email = request.form['Email']
        phone_number = request.form['Phone number']
        password = request.form['Password']

        existing_user=check_user_exists(email)
        if existing_user:
            flash("User with this email already exists,Login instead","danger")
            return(redirect(url_for('register')))
        hashed_password = bcrypt.generate_password_hash(password).decode('uft-8')

        new_user = (full_name,email,phone_number,hashed_password)
        insert_user(new_user)
        flash("User created successfully","success")
        return redirect(url_for('login'))

    return render_template('register.html')


app.run(debug=True)
