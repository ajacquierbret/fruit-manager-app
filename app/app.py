from flask import Flask, render_template, url_for, request
import mysql.connector

app = Flask(__name__)

config = {
    'user': 'mzEfYUETPz',
    'password': 'XQmgGcWPkP',
    'host': 'remotemysql.com',
    'port': '3306',
    'database': 'mzEfYUETPz'
    }  
connection = mysql.connector.connect(**config)

@app.route('/add', methods=['POST'])
def addFruit():
    fruitName = request.form['name']
    cursor = connection.cursor()
    query = 'INSERT INTO fruits_list (id, name) VALUES(%s, %s)'
    cursor.execute(query, (0, str(fruitName)))
    return getAllFruits()

@app.route('/delete', methods=['POST'])
def deleteFruit():
    fruitId = request.form['entry_id']
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM fruits_list WHERE  id = {fruitId}')
    return getAllFruits()
    
@app.route('/')
def getAllFruits():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM fruits_list')
    results = cursor.fetchall()
    return render_template('index.html', fruits=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
