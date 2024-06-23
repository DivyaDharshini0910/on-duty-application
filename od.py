from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Varshini@30'
app.config['MYSQL_DB'] = 'od'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/get_od', methods=['POST'])
def get_od():
    roll_num = request.form['roll_num']
    name = request.form['name']
    clas = request.form['class']
    reason = request.form['reason']
    dates = request.form['dates']
    nod = request.form['nod']

    cursor = mysql.connection.cursor()
    query = "INSERT INTO od_claimed (roll_num, name, class, dates, reason, nod) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (roll_num, name, clas, dates, reason, nod))
    mysql.connection.commit()

    flash('OD claimed successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)