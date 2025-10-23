from flask import Flask
import os

# Create the app instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_fishing_app():
    return 'Hello, Fishing App!'

# Run the app
if __name__ == '__main__':
    # '0.0.0.0' makes it accessible on your network (and inside Docker)
    app.run(debug=True, host='0.0.0.0', port=5000)