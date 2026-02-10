from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Создаем базу данных в памяти для теста
db = sqlite3.connect(':memory:', check_same_thread=False)
db.execute("CREATE TABLE users (id INTEGER, username TEXT, secret TEXT)")
db.execute("INSERT INTO users VALUES (1, 'admin', 'FLAG{SQL_INJECTION_SUCCESS}')")
db.execute("INSERT INTO users VALUES (2, 'alice', 'alice_password_123')")

# Шаблон страницы (в реальном проекте это отдельные HTML файлы)
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>Vulnerability Lab</title></head>
<body style="font-family: sans-serif; padding: 20px;">
    <h1>🔍 User Search Portal</h1>
    
    <h3>1. Search User (Reflected XSS)</h3>
    <form method="GET" action="/search">
        <input type="text" name="name" placeholder="Enter username">
        <input type="submit" value="Search">
    </form>
    <p>Last searched: {{ search_term | safe }}</p>

    <hr>

    <h3>2. Admin Login (SQL Injection)</h3>
    <form method="POST" action="/login">
        <input type="text" name="username" placeholder="Username"><br><br>
        <input type="password" name="password" placeholder="Password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, search_term="None")

# ❌ Уязвимость XSS: ввод пользователя выводится через | safe без фильтрации
@app.route('/search')
def search():
    name = request.args.get('name', '')
    return render_template_string(HTML_TEMPLATE, search_term=name)

# ❌ Уязвимость SQL Injection: ввод вставляется напрямую в строку запроса
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    # Это "плохой" код. Правильно использовать "?" вместо f-строк.
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    try:
        cursor = db.execute(query)
        user = cursor.fetchone()
        if user:
            return f"Welcome back, {user[1]}! Your secret: {user[2]}"
        else:
            return "Login failed."
    except Exception as e:
        return f"Database Error: {str(e)}"

if __name__ == "__main__":
    app.run(port=5000)
