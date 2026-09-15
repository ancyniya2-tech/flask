import psycopg2

conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='2303',dbname='myduka')

cur = conn.cursor()

def get_products():
    cur.execute('select * from products')
    products = cur.fetchall()
    return products

def insert_products(product_values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",product_values)
    conn.commit()




def get_sales():
    cur.execute("SELECT * FROM sales")
    sales = cur.fetchall()
    return sales


def insert_sales(sales_values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",sales_values)
    conn.commit()



def get_stock():
    cur.execute("Select * from stock")
    stock = cur.fetchall()
    return stock


def insert_stock(stock_values):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",stock_values)
    conn.commit()



#sales per day
#SELECT date(sales.created_at) as day, sum(products.selling_price * sales.quantity) FROM sales inner join products on sales.pid = products.id group by day;

def get_sales_per_day():
    cur.execute(""" 
        SELECT date(sales.created_at) as day, sum(products.selling_price * sales.quantity) FROM 
        sales inner join products on sales.pid = products.id group by day;
""")
    sales_per_day = cur.fetchall()
    return sales_per_day
    

#Profits per product
#SELECT products.name, sum(products.selling_price - products.buying_price * sales.quantity) as total_profit FROM products inner join sales on products.id = sales.pid group by products.name;

def get_profits_per_product():
    cur.execute(""" 
        SELECT products.name, sum(products.selling_price - products.buying_price * sales.quantity) as total_profit FROM 
        products inner join sales on products.id = sales.pid group by products.name;
""")
    profits_per_product = cur.fetchall()  
    return profits_per_product


def available_stock(pid):
    cur.execute("select sum(stock.stock_quantity) from stock where pid = %s",(pid,))
    total_stock = cur.fetchone()[0] or 0

    cur.execute("select sum(sales.quantity) from sales where pid = %s",(pid,))
    total_sold = cur.fetchone()[0] or 0

    return total_stock - total_sold

check_stock  = available_stock(1)
print(check_stock)

def check_user_esist(email):
    cur.execute("select * from user where users.email = %s,"(email,))
    user = cur.fetchone()
    return user

def insert_user(user_details):
    cur.execute["insert into users(full_name,email,phone_number,password)values(%s,%s,%s,%s)",user_details]
    conn.commit