# COM4008 Programming Concepts: Flask and Web Connectivity

This content is designed as three linked VLE information pages. Lecture 10 brings together Python functions, imports and data processing to create a small web application.

---

# 10.1 Getting Started with Flask

## On this page

- Web applications and the request-response cycle
- Installing Flask in a virtual environment
- Creating a minimal Flask application
- Running the development server
- Routes and view functions
- Returning responses

## Learning outcomes

By the end of this page, you should be able to:

- distinguish between a web browser, web server and web application;
- describe the basic HTTP request-response cycle;
- install Flask in an isolated Python environment;
- create and run a minimal Flask application;
- connect a URL to a Python function using a route;
- recognise the purpose of common HTTP status-code groups.

## From Python program to web application

Until now, most of our programs have communicated through the terminal or a notebook. A web application uses the same programming ideas, but communicates with a browser.

A simplified interaction is:

1. The user visits a URL or submits a form.
2. The browser sends an HTTP **request** to a server.
3. Flask selects the Python function associated with that URL.
4. Python performs any required processing.
5. Flask sends an HTTP **response** back to the browser.
6. The browser displays the returned HTML and applies its CSS.

The browser is the **client**. Flask runs on the **server side**. During development, both can run on the same computer, but they still have different roles.

## What is Flask?

Flask is a lightweight Python web framework. It supplies the core tools needed to connect URLs, Python functions, templates and HTTP requests without deciding every detail of the application's structure.

Flask is installed separately from Python's standard library. For a new project, create and activate a virtual environment before installing it:

```text
python3 -m venv .venv
source .venv/bin/activate
python -m pip install Flask
```

On Windows, activation commonly uses:

```text
.venv\Scripts\activate
```

A virtual environment keeps this project's packages separate from other Python projects. Your editor must use the same environment in which Flask was installed.

## A minimal Flask application

Create a file named `app.py`:

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello from Flask!</h1>"
```

There are four important ideas here:

- `from flask import Flask` imports the Flask class.
- `Flask(__name__)` creates the application and helps Flask locate related resources.
- `@app.route("/")` associates the root URL with the function below it.
- `home()` is a **view function**. Its returned value becomes part of the HTTP response.

The decorator belongs immediately above the function it registers.

## Running the development server

From the folder containing `app.py`, run:

```text
flask --app app run --debug
```

Open the address shown in the terminal, commonly:

```text
http://127.0.0.1:5000/
```

`127.0.0.1` and `localhost` refer to your own computer. The number after the colon is the port used by the development server.

Debug mode reloads the application after many code changes and provides useful diagnostic information. The Flask development server and interactive debugger are for development only; they must not be exposed as a production service.

To stop the server, return to its terminal and press `Ctrl+C`.

## Adding routes

Each route identifies a URL path:

```python
@app.route("/")
def home():
    return "<h1>Home</h1>"


@app.route("/about")
def about():
    return "<h1>About this application</h1>"
```

Visiting `/about` calls `about()`. The Python function name and URL do not have to match, but clear names make the program easier to follow.

A route can also contain a value:

```python
@app.route("/hello/<name>")
def hello(name):
    return f"<h1>Hello, {name}!</h1>"
```

This is useful for learning how routing works. In a real application, avoid inserting untrusted content directly into hand-built HTML. Templates provide automatic escaping for ordinary displayed values and are introduced on the next page.

## Responses and status codes

An HTTP response includes content and a status code. Common groups are:

| Range | Meaning | Example |
|---|---|---|
| `200`–`299` | Successful response | `200 OK` |
| `300`–`399` | Redirection | `302 Found` |
| `400`–`499` | Problem with the request | `404 Not Found` |
| `500`–`599` | Server-side failure | `500 Internal Server Error` |

If no route matches the requested URL, Flask normally returns a `404` response. If a view function fails unexpectedly, the result is normally a `500` response.

## Pause and predict

Before running the code, study these two routes:

```python
@app.route("/")
def home():
    return "Home page"


@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"
```

Predict what the browser will display for each address:

1. `http://127.0.0.1:5000/`
2. `http://127.0.0.1:5000/hello/Aisha`
3. `http://127.0.0.1:5000/hello`
4. `http://127.0.0.1:5000/about`

Which requests should produce content, and which should produce a `404` response? Run the application and test your predictions.

## Common mistakes

- **`ModuleNotFoundError: No module named 'flask'`:** Flask is not installed in the environment running the application.
- **The application cannot be found:** run the command from the project folder and name the correct module after `--app`.
- **The port is already in use:** stop the other server or choose another port, for example `--port 5001`.
- **A page returns 404:** check the spelling of the route and the URL.
- **Changes do not appear:** confirm that debug mode is enabled, save the file and refresh the browser.
- **Two functions have the same name:** every view function should have a distinct endpoint name.
- **The decorator is separated from its function:** place `@app.route(...)` immediately above the function it registers.
- **The development server is treated as deployment:** debug mode is a local development aid, not a production hosting method.

## Check your understanding

1. What is the difference between a browser and a server?
2. What does `@app.route("/")` do?
3. Why is Flask's debug server unsuitable for production?
4. What do status codes `404` and `500` indicate?

## Apply your learning

1. Create and run the minimal application.
2. Add a `/course` route that returns the module title.
3. Add a route with a variable, such as `/student/<name>`.
4. Create a `/topics/<number>` route and investigate how Flask supplies the URL value to Python.
5. Deliberately visit a route that does not exist and use the browser or developer tools to identify its status code.

## Page summary

Flask connects incoming HTTP requests to Python view functions. A route identifies the URL pattern, the view function performs the relevant work, and its return value contributes to the response. Flask's debug server makes this cycle easy to investigate locally, but it is not a production server.

**Next:** Continue to **10.2 HTML and CSS — The Front End**.

---

# 10.2 HTML and CSS — The Front End

## On this page

- The roles of HTML and CSS
- Creating Flask templates
- Rendering a template from Python
- Linking pages with `url_for()`
- Serving CSS from the static folder
- Displaying Python data with Jinja
- Template inheritance

## Learning outcomes

By the end of this page, you should be able to:

- explain the separate roles of HTML, CSS and Python in a Flask application;
- create and render an HTML template;
- connect a style sheet from Flask's static folder;
- generate links using named Flask endpoints;
- display Python values safely in a Jinja template;
- reduce repeated HTML using a base template.

## The front end

The **front end** is the part presented in the user's browser. In this lecture:

- **HTML** describes the content and structure of a page;
- **CSS** controls its visual presentation;
- **Python and Flask** decide what data and page should be returned.

Keeping these concerns separate makes an application easier to read and maintain.

## A useful project structure

Flask looks in conventional locations for templates and static files:

```text
lecture10-app/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── about.html
└── static/
    └── style.css
```

The folder names `templates` and `static` are significant and should be spelt exactly as shown.

## Creating an HTML template

Create `templates/index.html`:

```html
<!doctype html>
<html lang="en-GB">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>COM4008 Flask application</title>
  </head>
  <body>
    <header>
      <h1>COM4008 Flask application</h1>
    </header>

    <main>
      <p>This page was returned by a Python application.</p>
    </main>
  </body>
</html>
```

Elements such as `header`, `main`, headings and paragraphs give the page meaningful structure. Correct structure also helps accessibility and styling.

## Rendering the template

Update `app.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
```

`render_template()` finds the file in `templates`, processes any Jinja template instructions and returns the resulting HTML.

## Adding CSS

Create `static/style.css`:

```css
body {
  background-color: #f7f4fb;
  color: #25212b;
  font-family: Arial, sans-serif;
  line-height: 1.6;
  margin: 0 auto;
  max-width: 60rem;
  padding: 2rem;
}

h1 {
  color: #4c247d;
}
```

A CSS declaration uses a colon between a property and value, and usually ends with a semicolon:

```css
property: value;
```

In the template's `head`, link to the style sheet:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

Flask serves files from `static`. `url_for()` generates the appropriate URL and is preferable to manually assembling file paths.

## Linking to another route

Add another route:

```python
@app.route("/about")
def about():
    return render_template("about.html")
```

In a template, link to the route by its endpoint—the view function name:

```html
<nav aria-label="Main navigation">
  <a href="{{ url_for('home') }}">Home</a>
  <a href="{{ url_for('about') }}">About</a>
</nav>
```

If a route URL changes later, links generated from its endpoint can remain correct.

## Passing Python data to HTML

A route can pass named values into a template:

```python
@app.route("/")
def home():
    topics = ["Routes", "Templates", "Forms"]
    return render_template(
        "index.html",
        student_name="Aisha",
        topics=topics,
    )
```

Jinja uses double braces to output an expression:

```html
<h2>Welcome, {{ student_name }}</h2>
```

Statement tags control template behaviour:

```html
<ul>
  {% for topic in topics %}
    <li>{{ topic }}</li>
  {% endfor %}
</ul>
```

Jinja comments are not included in the rendered page:

```html
{# This comment is processed on the server. #}
```

For HTML templates, Flask configures Jinja to escape ordinary inserted values automatically. This prevents characters in a value from being interpreted as HTML in many common cases. Do not mark user-controlled content as safe merely to make it render differently.

## Avoiding repeated HTML

A base template can contain the shared page structure. Create `templates/base.html`:

```html
<!doctype html>
<html lang="en-GB">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}COM4008 Flask{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  </head>
  <body>
    <nav aria-label="Main navigation">
      <a href="{{ url_for('home') }}">Home</a>
      <a href="{{ url_for('about') }}">About</a>
    </nav>

    <main>
      {% block content %}{% endblock %}
    </main>
  </body>
</html>
```

Then `index.html` can extend it:

```html
{% extends "base.html" %}

{% block title %}Home — COM4008 Flask{% endblock %}

{% block content %}
  <h1>Welcome, {{ student_name }}</h1>
  <p>This content is unique to the home page.</p>
{% endblock %}
```

Template inheritance removes duplication while allowing each page to supply its own title and content.

## Pause and trace the data

Study this route and template fragment without running them:

```python
@app.route("/topics")
def topics():
    course_topics = ["Routes", "Templates", "Forms"]
    return render_template("topics.html", topics=course_topics)
```

```html
<ul>
  {% for topic in topics %}
    <li>{{ topic }}</li>
  {% endfor %}
</ul>
```

Identify:

1. the Python variable that exists only inside the view function;
2. the name made available to the template;
3. the Jinja statement that repeats the HTML;
4. the expression that outputs one value;
5. the final HTML you expect the browser to receive.

## Common mistakes

- **Using `template` instead of `templates`:** Flask searches the `templates` folder by convention.
- **Putting CSS in the templates folder:** style sheets and images normally belong in `static`.
- **Writing CSS with `=`:** CSS declarations use `property: value;`.
- **Opening the template file directly:** visit the Flask route so that Jinja instructions are processed on the server.
- **Hard-coding every URL:** use `url_for()` with an endpoint name to generate application links.
- **Confusing endpoint and template names:** `url_for('about')` refers to the `about()` view function, not to `about.html`.
- **Using a Python variable that was not passed to the template:** include it as a named argument to `render_template()`.
- **Copying the complete page structure into every template:** use template inheritance for shared navigation and layout.
- **Marking untrusted content as safe:** keep automatic escaping enabled for user-controlled values.

## Check your understanding

1. What separate jobs do HTML, CSS and Python perform?
2. Why are the folder names `templates` and `static` important?
3. What is the difference between `{{ ... }}` and `{% ... %}`?
4. Why is `url_for()` preferable to manually assembled links?
5. What problem does template inheritance solve?

## Apply your learning

1. Create the project structure shown above.
2. Render an `index.html` template from the root route.
3. Add a CSS file and confirm that it changes the page.
4. Create an `/about` route and link both pages using `url_for()`.
5. Pass a dictionary from Python and display its keys and values in an HTML table.
6. Move the common document structure and navigation into `base.html`.
7. Inspect the page source in the browser and compare the final HTML with the original Jinja template.

## Page summary

HTML gives a web page structure, CSS controls its presentation, and Flask renders templates using server-side data. Jinja expressions display values, statement tags provide controlled template logic, and inheritance removes repeated page structure. Flask's conventional `templates` and `static` folders keep presentation resources organised.

**Previous:** Return to **10.1 Getting Started with Flask**.  
**Next:** Continue to **10.3 Python as a Server-Side Script**.

---

# 10.3 Python as a Server-Side Script

## On this page

- Server-side processing
- GET and POST requests
- Reading query-string and form data
- Validating input on the server
- Returning calculated results
- Separating processing from presentation
- State, persistence and security

## Learning outcomes

By the end of this page, you should be able to:

- explain what server-side processing means;
- distinguish between common uses of GET and POST;
- read query-string and submitted form values in Flask;
- validate input before processing it;
- return calculated data to an HTML template;
- separate reusable Python logic from Flask routes;
- explain why global variables are unsuitable for storing web-application data.

## What happens on the server?

HTML and CSS are interpreted by the browser. Python normally runs on the server and can:

- validate submitted data;
- perform calculations;
- read files or databases;
- call another service;
- choose which template to render;
- decide which status or redirect response to return.

The browser receives the result, not the application's Python source code.

## GET requests and query strings

GET is normally used to retrieve a representation of a resource. Extra values can be included in the URL as a query string:

```text
/greet?name=Aisha
```

Flask exposes query-string values through `request.args`:

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/greet")
def greet():
    name = request.args.get("name", "visitor").strip()

    if not name:
        name = "visitor"

    return render_template("greet.html", name=name)
```

The URL can be bookmarked and shared, so query strings are useful for searches and filters. They must not be used for passwords or other secrets because URLs can appear in browser history, logs and shared links.

## POST requests and forms

POST is commonly used when submitting data that changes state or should not be encoded in the URL. Create `templates/add.html`:

```html
{% extends "base.html" %}

{% block title %}Add two numbers{% endblock %}

{% block content %}
  <h1>Add two numbers</h1>

  <form method="post">
    <div>
      <label for="first">First number</label>
      <input id="first" name="first" type="number" step="any" required>
    </div>

    <div>
      <label for="second">Second number</label>
      <input id="second" name="second" type="number" step="any" required>
    </div>

    <button type="submit">Calculate</button>
  </form>

  {% if result is not none %}
    <p>The result is <strong>{{ result }}</strong>.</p>
  {% endif %}

  {% if error %}
    <p role="alert">{{ error }}</p>
  {% endif %}
{% endblock %}
```

The `name` attributes become the keys sent in the request. Labels make the controls easier to understand and use.

The route accepts both methods and reads POST values from `request.form`:

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/add", methods=["GET", "POST"])
def add_numbers():
    result = None
    error = None

    if request.method == "POST":
        first_text = request.form.get("first", "").strip()
        second_text = request.form.get("second", "").strip()

        try:
            first = float(first_text)
            second = float(second_text)
            result = first + second
        except ValueError:
            error = "Enter two valid numbers."

    return render_template("add.html", result=result, error=error)
```

The GET request displays the empty form. A POST request submits it for processing. Browser-side controls such as `required` improve usability, but the server must still validate every value: a request can be created without using your form.

## Separating the processing logic

Keep reusable calculations independent of Flask where possible. Create `data_processing.py`:

```python
def add_values(first, second):
    return first + second
```

Import and call it from `app.py`:

```python
from data_processing import add_values

# Inside the route, after validation:
result = add_values(first, second)
```

This separation has several benefits:

- the calculation can be tested without running a web server;
- the route concentrates on HTTP input and output;
- the same logic can be reused elsewhere;
- presentation remains in the template.

## Avoid global mutable data

It may be tempting to write:

```python
numbers = []
```

and append form values to it. This is unreliable for web applications. The list may be shared between users, disappear when the application restarts, behave unexpectedly with the debug reloader, or differ between multiple server processes.

For a calculation that uses only the current form, keep values local to the request. When information must persist, use an appropriate mechanism such as a database or carefully configured user session.

## Redirecting after a successful change

When a POST request changes stored data, applications commonly redirect to a GET page after success:

```python
from flask import redirect, url_for

return redirect(url_for("results"))
```

This **Post/Redirect/Get** pattern helps prevent a browser refresh from repeating the form submission. The simple calculator above does not change stored state, so rendering its result directly is acceptable for this introductory example.

## A complete mental model

When the user submits the calculator form:

1. The browser creates a POST request containing named form values.
2. Flask matches `/add` to `add_numbers()`.
3. The route retrieves strings from `request.form`.
4. Python validates and converts those strings.
5. A Python function performs the calculation.
6. Flask renders a template with the result or an error message.
7. The browser receives and displays the resulting HTML.

That cycle is the central connection between front-end forms and server-side Python.

## Security boundaries

This lecture introduces connectivity, not a complete production security model. Remember:

- never trust input merely because it came from your own form;
- never place passwords or secrets in a URL;
- never store passwords as plain text;
- do not disable template escaping for user-controlled content;
- state-changing forms in real applications need protection against cross-site request forgery;
- authentication, sessions, database design and production deployment require further study.

A login system is therefore a valuable later project, but it should not be treated as a small extension to this first Flask application.

## Pause and diagnose

Consider this incomplete route:

```python
@app.route("/divide", methods=["GET", "POST"])
def divide():
    if request.method == "POST":
        first = float(request.form["first"])
        second = float(request.form["second"])
        result = first / second

    return render_template("divide.html", result=result)
```

Before running it, identify what could happen when:

1. the page is first requested with GET;
2. either form field is missing;
3. a value cannot be converted to `float`;
4. the second value is zero;
5. two different users submit the form.

Rewrite the route so that it validates the values and always supplies defined template variables.

## Common mistakes

- **Assuming form values are already numbers:** values retrieved from `request.form` are strings and require validation and conversion.
- **Using `request.form["name"]` without considering missing data:** `.get()` allows the application to handle an absent key deliberately.
- **Trusting `required` as security:** browser validation improves usability, but the server must validate every request.
- **Using GET for passwords or secrets:** query-string values can appear in URLs, histories and logs.
- **Forgetting to permit POST:** a route handling a submitted form must include the appropriate method.
- **Using global lists for user data:** globals can leak state between users, vanish on restart and differ between processes.
- **Putting calculation and HTML construction inside one large route:** separate processing functions and templates make the code easier to test.
- **Ignoring predictable exceptions:** invalid numbers and division by zero should produce helpful feedback rather than a server error.
- **Building login functionality with plain-text passwords:** secure authentication requires password hashing, sessions, CSRF protection and careful deployment.

## Check your understanding

1. When would GET be more appropriate than POST?
2. Why does Flask initially receive form values as strings?
3. Why must the server validate input even when the HTML form uses `required`?
4. What is wrong with using a module-level list to hold every user's data?
5. What responsibilities belong in the route, processing function and template?

## Apply your learning

1. Build the two-number calculator.
2. Add a choice of arithmetic operation: addition, subtraction, multiplication or division.
3. Handle division by zero with a useful error message.
4. Move the arithmetic functions into `data_processing.py`.
5. Add a results page and use a redirect after storing a result in an appropriate persistence layer.
6. Test missing, blank, non-numeric and zero values, recording the response produced in each case.
7. Explain the complete request-response journey of one successful submission in your own words.

## Page summary

Server-side Python receives HTTP input, validates and converts it, performs processing, and passes a result to a response or template. GET commonly retrieves information; POST commonly submits information for processing or change. Request-local values, separate processing functions and deliberate error handling provide a sounder foundation than shared global data.

**Previous:** Return to **10.2 HTML and CSS — The Front End**.  
**Next step:** Complete the Lecture 10 Flask application and test the complete browser–server request cycle.

---

# Suggested lecture flow

For this introductory lecture, the three-page sequence is deliberately cumulative:

1. **Getting started with Flask:** establish the request-response model and create routes.
2. **HTML and CSS:** move presentation into templates and static files.
3. **Python as a server-side script:** submit, validate and process browser input.

The external-API material from Lecture 9 can still be revisited as an optional integration exercise: a Flask route could call an API and pass selected results to a template. Database-backed authentication is better reserved for later teaching because secure passwords, sessions and CSRF protection introduce several new concepts at once.

## Further reading

- [Flask installation](https://flask.palletsprojects.com/en/stable/installation/)
- [Flask quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Flask tutorial: templates](https://flask.palletsprojects.com/en/stable/tutorial/templates/)
- [Flask tutorial: static files](https://flask.palletsprojects.com/en/stable/tutorial/static/)
- [Flask web security guidance](https://flask.palletsprojects.com/en/stable/web-security/)
