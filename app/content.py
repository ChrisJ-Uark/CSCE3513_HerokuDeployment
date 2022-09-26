import os
import psycopg2
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def run():
    rRows = queryDB()
    return render_template("index.html", rows=rRows)
    
def queryDB():
    try:                                
        DATABASE_URL = os.environ['DATABASE_URL']
        print(DATABASE_URL)

        conn = psycopg2.connect(DATABASE_URL, sslmode='require')

        print(conn)
                                
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM test")
        rows = cursor.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
            print("Error:")
            print(error)
    finally:
        pass
    if conn is not None:
        conn.commit()
        cursor.close()
        conn.close()
        return rows