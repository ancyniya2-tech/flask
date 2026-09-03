from flask import Flask , render_template
from database import get_products
from database import get_sales
from database import get_stock

app = Flask(__name__)

@app.route('/')
def home():
    name= "Ancy Niya"
    return render_template('index.html',x=name)

@app.route('/products')
def products():
    products= get_products()
    return render_template('products.html', products = products)

@app.route('/sales')
def sales():
    sales= get_sales()
    return render_template('sales.html', sales = sales)

@app.route('/stock')
def stock():
    stock = get_stock()
    return render_template('stock.html', stock=stock)

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