from flask import Flask, request , render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/math', methods=['POST'])
def math_ops():
    if request.method == 'POST':
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = None
        
        if ops == 'add':
            r = num1 + num2
            result = f"The sum of {num1} and {num2} is {r}"
        
        if ops == 'subtract':
            r = num1 - num2
            result = f"The result of subtracting {num2} from {num1} is {r}"
        
        if ops == 'multiply':
            r = num1 * num2
            result = f"The product of {num1} and {num2} is {r}"
        
        if ops == 'divide':
            if num2 != 0:
                r = num1 / num2
                result = f"The result of dividing {num1} by {num2} is {r}"
            else:
                result = "Error: Cannot divide by zero!"
        
        if result is None:
            result = "Error: Invalid operation!"

        return render_template('results.html', result=result)

if __name__=="__main__":
    app.run(host="0.0.0.0")
