from flask import Flask, render_template, url_for, request
import mysql.connector

# Creates a flask app
app = Flask(__name__)

# Fill the necessary config fields for the DB connexion
config = {
    'user': 'mzEfYUETPz',
    'password': 'XQmgGcWPkP',
    'host': 'remotemysql.com',
    'port': '3306',
    'database': 'mzEfYUETPz'
    }

# Connects to the database
connection = mysql.connector.connect(**config)

# The "Add" route (When a user adds a fruit)
@app.route('/add', methods=['POST'])
def addFruit():
    fruitName = request.form['name']
    cursor = connection.cursor()
    query = 'INSERT INTO fruits_list (id, name) VALUES(%s, %s)' # Prepared query to prevent SQL-injection
    cursor.execute(query, (0, str(fruitName)))
    return getAllFruits()

# The "Delete" route (When a user deletes a fruit)
@app.route('/delete', methods=['POST'])
def deleteFruit():
    fruitId = request.form['entry_id']
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM fruits_list WHERE  id = {fruitId}')
    return getAllFruits()

# Display every fruit stored in the database on 'index.html'
@app.route('/')
def getAllFruits():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM fruits_list')
    results = cursor.fetchall()
    return render_template('index.html', fruits=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
