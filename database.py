import psycopg2

conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='2303',dbname='myduka')

cur = conn.cursor()

def get_products():
    cur.execute('select * from products')
    products = cur.fetchall()
    return products

#def insert_products(product_values):
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


stock_data = get_stock()
print(stock_data)

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

