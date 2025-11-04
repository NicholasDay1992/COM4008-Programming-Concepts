from flask import Flask, render_template, request

app = Flask(__name__)

numbers = []

@app.route('/', methods=['GET', 'POST'])
def home():
    total = None

    if request.method == 'POST':
        try:
            num = float(request.form['number'])
            numbers.append(num)
            total = sum(numbers)
        except ValueError:
            total = "Invalid input. Please enter a number."

    return render_template('index.html', numbers=numbers, total=total)

if __name__ == '__main__':
    app.run(debug=True)