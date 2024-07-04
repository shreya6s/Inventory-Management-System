import MySQLdb
from flask import Flask,redirect,url_for,render_template,request
from datetime import datetime  # Import the datetime module
import os

from flask import Flask, render_template
from flask_mysqldb import MySQL

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# ... your configuration ...

toolbar = DebugToolbarExtension(app)


app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_mysql_user'  # Replace with your MySQL user
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'testdb'


mysql = MySQL(app)



def create_db_connection():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )


picFolder = os.path.join('static','pics')
app.config['UPLOAD_FOLDER'] = picFolder



# on load page
@app.route('/')
def welcome():
  
    image2 = os.path.join(app.config['UPLOAD_FOLDER'],'image2.jpg')
    return render_template('login.html',user_image=image2)

@app.route('/home')
def home():

        image1 = os.path.join(app.config['UPLOAD_FOLDER'],'image1.png')
        image2 = os.path.join(app.config['UPLOAD_FOLDER'],'image2.jpg')
        return render_template('home.html',lala=image2, img5 =image1)

@app.route('/updateStock')
def addStock():
    return render_template('updateStock.html')

@app.route('/submitupStock',methods=['POST','GET'])
def submitupStock():
    if request.method=='POST':
        product_name=request.form['ProductName']
        quantity=request.form['Quantity']
        addorsub = request.form['AddorSub']

        cur = mysql.connection.cursor()
        if addorsub == 'add':
            cur.execute("UPDATE product SET Quantity = Quantity + %s WHERE ProductName = %s", (quantity, product_name))
        elif addorsub == 'sub':
            cur.execute("UPDATE product SET Quantity = Quantity - %s WHERE ProductName = %s", (quantity, product_name))
        mysql.connection.commit()
        cur.close()
        return render_template('updateStock.html',info='Stock Updated')

        

@app.route('/removeStock')
def removeStock():
    return render_template('removeStock.html')

@app.route('/submitremStock',methods=['POST','GET'])
def submitremStock():
    if request.method=='POST':
        product_name=request.form['ProductName']
        
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM product WHERE ProductName = %s", (product_name,))
        mysql.connection.commit()
        cur.close()
        return render_template('removeStock.html',info='Stock Removed')


@app.route('/addStock')
def updateStock():
    return render_template('addStock.html')

@app.route('/submitStock',methods=['POST','GET'])
def submitStock():
    if request.method=='POST':
        product_code=request.form['ProductCode']
        product_name=request.form['ProductName']
        weight=request.form['PackedWeight']
        quantity=request.form['Quantity']
        refrigerated=request.form['Refrigerated']


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO product (ProductCode, ProductName, PackedWeight, Quantity, Refrigerated) VALUES (%s, %s, %s, %s, %s)",
                    (product_code, product_name, weight, quantity, refrigerated))
        mysql.connection.commit()
        cur.close()
        return render_template('addStock.html',info='Stock Inserted')
        
@app.route('/provadd')
def provadd():
    return render_template('provadd.html')

@app.route('/submitprovadd',methods=['POST','GET'])
def submitprovadd():
    if request.method=='POST':
        providerid=request.form['ProviderID']
        orderid=request.form['OrderID']
        providername=request.form['ProviderName']
        provideraddress=request.form['ProviderAddress']
        orderitem=request.form['OrderItem']
        quantity=request.form['Quantity']
        orderdate=request.form['OrderDate']
        newdate = datetime.strptime(orderdate, '%Y-%m-%d')

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO product VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (providerid, orderid, providername, provideraddress, orderitem, quantity, newdate))
        mysql.connection.commit()
        cur.close()
        return render_template('provadd.html',info='Provider Inserted')



@app.route('/submit',methods=['POST','GET'])
def submit():
    
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
    
    
    a = get_user(username,password)
    if a:
         
         image1 = os.path.join(app.config['UPLOAD_FOLDER'],'image1.png')
         image2 = os.path.join(app.config['UPLOAD_FOLDER'],'image2.jpg')
         return render_template('home.html',lala=image2, img5 =image1)
    else:
        image2 = os.path.join(app.config['UPLOAD_FOLDER'],'image2.jpg')
        return render_template('login.html',user_image=image2,info='Invalid username')


def get_user(user_id,password):
    cursor = mysql.connection.cursor()
    # SQL statement to select a user by ID
    select_user_query = "SELECT * FROM login WHERE name = %s AND pass = %s"
    cursor.execute(select_user_query, (user_id, password))
    user_data = cursor.fetchone()  # Fetch the first row
    cursor.close()
    #return render_template('login.html',info='user id ==='+user_id)
    return user_data
    


# after login page



@app.route('/product')
def product():
    cursor = mysql.connection.cursor()

    # SQL statement to select all rows from the table
    select_all_rows_query = "SELECT * FROM product"
    cursor.execute(select_all_rows_query)

    rows = cursor.fetchall()  # Fetch all rows

    cursor.close()
    print(rows)
    image1 = os.path.join(app.config['UPLOAD_FOLDER'],'image1.png')
    return render_template('product.html',img5 =image1, rows=rows)
    
@app.route('/provider')
def provider():
    cursor = mysql.connection.cursor()

    # SQL statement to select all rows from the table
    select_all_rows_query = "SELECT * FROM provider"
    cursor.execute(select_all_rows_query)

    rows = cursor.fetchall()  # Fetch all rows

    cursor.close()
    print(rows)

    image1 = os.path.join(app.config['UPLOAD_FOLDER'],'image1.png')
    return render_template('prov.html',img5 =image1, rows=rows)

@app.route('/customer')
def customer():
    cursor = mysql.connection.cursor()

    # SQL statement to select all rows from the table
    select_all_rows_query = "SELECT * FROM customer"
    cursor.execute(select_all_rows_query)

    rows = cursor.fetchall()  # Fetch all rows

    cursor.close()
    print(rows)

    image1 = os.path.join(app.config['UPLOAD_FOLDER'],'image1.png')
    return render_template('customer.html',img5 =image1, rows=rows)


if __name__=='__main__':
    app.run(debug=True)