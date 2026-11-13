from flask import Flask, render_template
from data_processing import process_data  # Import your script
# First Flask App
app = Flask(__name__)

@app.route('/')
def home():
    result = process_data()  # Call the function from the script
    return render_template('home.html', result=result)
 
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
