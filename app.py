from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

db = sqlite3.connect(':memory:', check_same_thread=False)
db.execute("CREATE TABLE users (id INTEGER, username TEXT, secret TEXT)")
db.execute("INSERT INTO users VALUES (1, 'admin', 'FLAG{SQL_INJECTION_SUCCESS}')")
db.execute("INSERT INTO users VALUES (2, 'alice', 'alice_password_123')")

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title> Vulnerability Lab </title>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
        body { 
            background-color: #0d1117; 
            color: #c9d1d9; 
            font-family: 'Press Start 2P', cursive;
            display: flex; flex-direction: column; align-items: center; padding: 50px;
        }
        .container { 
            background-color: #161b22; 
            padding: 30px; border-radius: 15px; 
            border: 1px solid #30363d; box-shadow: 0 8px 32px rgba(0,0,0,0.5);
            width: 400px;
        }
        h1 { color: #58a6ff; text-align: center; border-bottom: 1px solid #30363d; padding-bottom: 10px; }
        h2 { font-size: 1rem; color: #79c0ff; margin-top: 15px; }
        input { 
            width: 100%; padding: 10px; margin: 10px 0; 
            background: #0d1117; border: 1px solid #30363d; 
            color: #58a6ff; border-radius: 5px; box-sizing: border-box;
        }
        .btn { 
            width: 100%; background-color: #238636; color: white; 
            border: none; padding: 10px; border-radius: 5px; cursor: pointer; font-weight: bold;
        }
        .btn:hover { background-color: #2ea043; }
        .result { 
            margin-top: 15px; padding: 10px; background: #0d1117; 
            border-left: 4px solid #58a6ff; font-size: 0.9rem; word-wrap: break-word;
        }
        .footer { margin-top: 30px; font-size: 0.7rem; color: #8b949e; }
    </style>
</head>
<body>
    <div class="container">
        <h1> Vulnerability Lab </h1>
        
        <!-- Секция XSS -->
        <h2> Search portal </h2>
        <form action="/search" method="GET">
            <input type="text" name="name" placeholder="Search users...">
            <input type="submit" class="btn" value="Search">
        </form>
        {% if search_term %}
        <div class="result">Last search: {{ search_term | safe }}</div>
        {% endif %}

        <!-- Секция SQLi -->
        <h2> Admin login </h2>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" class="btn" value="Login">
        </form>
        {% if login_result %}
        <div class="result">{{ login_result }}</div>
        {% endif %}
    </div>
    <div class="footer">Educational Security Lab v1.0</div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/search')
def search():
    name = request.args.get('name', '')
    return render_template_string(HTML_TEMPLATE, search_term=name)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    query = f"SELECT * FROM users WHERE username = '{username}'"
    try:
        cursor = db.execute(query)
        user = cursor.fetchone()
        if user:
            res = f"Welcome, {user[1]}! Secret: {user[2]}"
        else:
            res = "Login failed:( "
    except Exception as e:
        res = f"DB Error: {str(e)}"
    return render_template_string(HTML_TEMPLATE, login_result=res)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
