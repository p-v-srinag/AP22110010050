import time
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_average', methods=['POST'])
def calculate_average():
    try:
        numbers = request.form.get('numbers')
        start_time = time.time()
        number_list = [float(n.strip()) for n in numbers.split(',') if n.strip()]
        if not number_list:
            return render_template('index.html', error="Please enter valid numbers.")
        avg = sum(number_list) / len(number_list)
        end_time = time.time()
        execution_time = (end_time - start_time) 

        return render_template('index.html', average=avg, execution_time=f"{execution_time:.2f} ms")

    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
