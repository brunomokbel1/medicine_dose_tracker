from flask import Flask, render_template, request, jsonify
app = Flask(__name__, template_folder='template')

# Render the sign-up page
@app.route('/')
def signup_form():
    return render_template('sign-up_2.html')

# Handle the form submission
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    # Here you would typically save the user data to a database
    # For this example, we'll just return the data as JSON
    return jsonify({"message": "User signed up successfully!", "username": username})

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port = 5000)
