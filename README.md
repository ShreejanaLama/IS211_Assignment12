# IS211_Assignment12 - Student Tracker Web App

This is a simple web application built using Flask. It helps a teacher keep track of students, quizzes, and quiz results for a class.

---

## Features
- Teacher can login
- View and add students
- View and add quizzes
- View and add quiz results
- See quiz scores for each student

---

## How to Run the Project

1. **Install Flask**

First, make sure Flask is installed. You can install it by running:

Bash:

pip install flask

2. **Create the Database**

Run the following command to create the database and add some sample data:

Bash:

python init_db.py


3. **Start the Web App**

Run the Flask app by typing:

Bash:

python app.py

4. **Open the App**

Go to your browser and open:

```
http://127.0.0.1:5000/
```

---

## Login Information
- Username: `admin`
- Password: `password`

Make sure you type it exactly the same (all lowercase).

---

## Files in the Project

```
IS211_Assignment13/
├── app.py               # Main Flask app
├── init_db.py            # Script to create database
├── schema.sql            # Database schema
├── README.md             # This instruction file
├── templates/            # Folder with all HTML templates
│   ├── add_quiz.html
│   ├── add_result.html
│   ├── add_student.html
│   ├── dashboard.html
│   ├── login.html
│   └── view_student_results.html
└── hw13.db               # Database file (created after running init_db.py)
```


---

## Important Notes
- Run `init_db.py` first before you run the app.
- The database is stored in the file `hw13.db`.
- Only the username `admin` and password `password` will work for logging in.

---
Thank You

Shreejana Ghalan Lama
