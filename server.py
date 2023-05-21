from flask import Flask, render_template, request, session, redirect, url_for

# Create a new Flask application instance
app = Flask(__name__)

# Set a secret key for the application. This is used to encrypt session data.
app.secret_key = 'your_secret_key'

# Define a route for the root URL (`/`). This function returns the `index.html` template.


@app.route('/')
def index():
    return render_template('index.html')

# Define a route for the `/result` URL with the `POST` method. This function stores the form data in the session and returns the `result.html` template with the form data.


@app.route('/result', methods=['POST'])
def result():
    session['form_data'] = request.form
    return render_template('result.html', form_data=session['form_data'])


# Check if the script is being run directly (as opposed to being imported as a module). If it is, run the Flask application with debugging enabled.
if __name__ == '__main__':
    app.run(debug=True)
