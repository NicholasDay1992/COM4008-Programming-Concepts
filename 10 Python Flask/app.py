from flask import Flask, render_template, request
#from data_processing import process_data  # Import your script

app = Flask(__name__)

@app.route('/')
def home():
    #result = process_data()  # Call the function from the script
    return render_template('index.html')#, result=result)


@app.route("/search")
def search():
    query = request.args.get("query", "")  # get ?query=... from URL
    return render_template("search.html", query=query)


if __name__ == '__main__':
    app.run(debug=True)