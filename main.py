from flask import Flask , render_template, request, redirect,url_for,flash
from database import get_products, insert_stock ,insert_products, get_sales, get_stock,insert_sales,generate_password


app = Flask(__name__)

app.secret_key = 'yuewhjfjsyugsjvjfs'

@app.route('/')
def home():
    name= "Ancy Niya"
    return render_template('index.html',x=name)

@app.route('/products')
def products():
    products= get_products()
    return render_template('products.html', products = products)

@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method == "POST": 
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']

        new_product = [product_name,buying_price,selling_price]
        insert_products[new_product]

        flash("Products added successfully","success")
    return redirect(url_for['products'])

@app.route('/sales')
def sales():
    sales= get_sales()
    products= get_products()
    return render_template('sales.html', sales = sales,products=products)


@app.route('/make_sale',methods=['GET','POST'])
def make_sale():
    if request.method == 'POST':
        pid = request.form['pid']
        quantity = request.form['quantity']

        new_sale = (pid, quantity)
        insert_sales(new_sale)

        flash("Sale made successfully",'success')

    return redirect(url_for('sales'))

@app.route('/stock')
def stock():
    stock = get_stock()
    products = get_products()
    return render_template('stock.html', stock=stock,products=products)


@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method == 'POST':
        pid = request.form['pid']
        stock_quantity = request.form['s_quantity']

        new_stock = (pid,stock_quantity)

        insert_stock(new_stock)
        flash("Stock has been inserted succesfully",'success')
    return redirect(url_for('stock'))
    


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


app.run(debug=True)