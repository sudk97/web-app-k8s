import psycopg2
from flask import Flask, render_template
 
app = Flask(__name__)
conn = psycopg2.connect(host="web-app-postgresql", user="postgres", password="user")
cursor = conn.cursor()

## When app runs for the first time on a new pv, configure empty database and table
conn.autocommit = True
cursor.execute('CREATE TABLE IF NOT EXISTS views (row integer, count integer)')
cursor.execute('INSERT INTO views (row, count) VALUES (1, 0)')

@app.route('/')
def hello_world():
    ## Fetch visit count from database
    try:
        cursor.execute("select * from views where row = 1")
        result = cursor.fetchall()
    except:
        result = [(1,0)]
    
    ## Add to visit count
    cursor.execute("UPDATE views SET count = count + 1 WHERE row = 1")

    ## Render HTML
    return render_template('index.html', data=str(result[0][1]))
 
# main driver function
if __name__ == '__main__':
 
    app.run(host='0.0.0.0', port=80)