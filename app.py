from flask import Flask, jsonify, request, render_template_string
import random

app = Flask(__name__)

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Random Number Generator</title>
</head>
<body>
    <h1>Random Number Generator</h1>
    <h2>Generate a Random Number</h2>
    <form action="/generate" method="post">
        <label for="min">Min:</label>
        <input type="number" id="min" name="min" value="1" required><br><br>
        <label for="max">Max:</label>
        <input type="number" id="max" name="max" value="100" required><br><br>
        <button type="submit">Generate</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML_TEMPLATE

@app.route('/generate', methods=['POST'])
def generate_number():
    min_value = int(request.form.get('min', 1))
    max_value = int(request.form.get('max', 100))
    
    if min_value >= max_value:
        return "Invalid range! Min must be less than Max.", 400
    
    number = random.randint(min_value, max_value)
    return f"<h1>Generated Random Number: {number}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
