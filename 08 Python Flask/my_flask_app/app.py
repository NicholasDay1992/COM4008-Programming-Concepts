from flask import Flask, render_template
# First Flask App
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

'''    
@app.route('/about')
def about():
    return "This is the About page."
''' 

if __name__ == '__main__':
    app.run(debug=True)
