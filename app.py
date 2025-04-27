# Directory Structure:
# IS211_Assignment13/
# ├─ app.py
# ├─ hw13.db
# ├─ schema.sql
# └─ templates/
#    ├─ login.html
#    ├─ dashboard.html
#    ├─ add_student.html
#    ├─ add_quiz.html
#    ├─ add_result.html
#    └─ view_student_results.html

# ---------- app.py ----------

from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret'
DATABASE = 'hw13.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid Credentials'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    cur = get_db().cursor()
    students = cur.execute('SELECT * FROM students').fetchall()
    quizzes = cur.execute('SELECT * FROM quizzes').fetchall()
    return render_template('dashboard.html', students=students, quizzes=quizzes)

@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    error = None
    if request.method == 'POST':
        fname = request.form['first_name']
        lname = request.form['last_name']
        if fname and lname:
            conn = get_db()
            conn.execute('INSERT INTO students (first_name, last_name) VALUES (?, ?)', (fname, lname))
            conn.commit()
            return redirect(url_for('dashboard'))
        else:
            error = 'Both fields are required.'
    return render_template('add_student.html', error=error)

@app.route('/quiz/add', methods=['GET', 'POST'])
def add_quiz():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    error = None
    if request.method == 'POST':
        subject = request.form['subject']
        num_questions = request.form['num_questions']
        date = request.form['date']
        if subject and num_questions and date:
            conn = get_db()
            conn.execute('INSERT INTO quizzes (subject, num_questions, quiz_date) VALUES (?, ?, ?)', (subject, num_questions, date))
            conn.commit()
            return redirect(url_for('dashboard'))
        else:
            error = 'All fields are required.'
    return render_template('add_quiz.html', error=error)

@app.route('/student/<int:student_id>')
def view_student_results(student_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    cur = get_db().cursor()
    results = cur.execute('SELECT quiz_id, score FROM results WHERE student_id = ?', (student_id,)).fetchall()
    return render_template('view_student_results.html', results=results, student_id=student_id)

@app.route('/results/add', methods=['GET', 'POST'])
def add_result():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    db = get_db()
    students = db.execute('SELECT id, first_name, last_name FROM students').fetchall()
    quizzes = db.execute('SELECT id, subject FROM quizzes').fetchall()
    error = None
    if request.method == 'POST':
        student_id = request.form['student_id']
        quiz_id = request.form['quiz_id']
        score = request.form['score']
        if student_id and quiz_id and score:
            db.execute('INSERT INTO results (student_id, quiz_id, score) VALUES (?, ?, ?)', (student_id, quiz_id, score))
            db.commit()
            return redirect(url_for('dashboard'))
        else:
            error = 'All fields are required.'
    return render_template('add_result.html', students=students, quizzes=quizzes, error=error)

@app.route('/')
def home():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)