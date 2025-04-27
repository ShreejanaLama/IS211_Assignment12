import sqlite3

def create_database():
    connection = sqlite3.connect('hw13.db')
    cursor = connection.cursor()

    # Create tables
    cursor.executescript('''
    DROP TABLE IF EXISTS students;
    DROP TABLE IF EXISTS quizzes;
    DROP TABLE IF EXISTS results;

    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    );

    CREATE TABLE quizzes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        num_questions INTEGER NOT NULL,
        quiz_date TEXT NOT NULL
    );

    CREATE TABLE results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        quiz_id INTEGER NOT NULL,
        score INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
    );
    ''')

    # Insert starter data
    cursor.execute('''
    INSERT INTO students (first_name, last_name)
    VALUES (?, ?)
    ''', ('John', 'Smith'))

    cursor.execute('''
    INSERT INTO quizzes (subject, num_questions, quiz_date)
    VALUES (?, ?, ?)
    ''', ('Python Basics', 5, '2015-02-05'))

    cursor.execute('''
    INSERT INTO results (student_id, quiz_id, score)
    VALUES (?, ?, ?)
    ''', (1, 1, 85))

    # Commit and close
    connection.commit()
    connection.close()
    print("Database 'hw13.db' created and populated successfully!")

if __name__ == '__main__':
    create_database()
