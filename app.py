from flask import Flask, request, render_template

app = Flask(__name__)

def is_xss_attack(input):
    # Simplified XSS validation function
    xss_characters = ['<', '>', '&', '"', "'"]
    return any(char in input for char in xss_characters)

def is_sql_injection(input):
    # Enhanced SQL injection validation function
    sql_keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'DROP', 'UNION', '--', "'", ' OR ', ' AND ']
    return any(keyword in input.upper() for keyword in sql_keywords)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_term = request.form['search']
        if is_sql_injection(search_term):
            return render_template('index.html', message='SQL Injection detected. Please enter a valid search term.')
        if is_xss_attack(search_term):
            return render_template('index.html', message='XSS detected. Please enter a valid search term.')
        return render_template('result.html', term=search_term)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
