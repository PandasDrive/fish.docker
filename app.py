from flask import Flask, render_template
import os
from dotenv import load_dotenv

# Load the variables from our .env file
load_dotenv()

app = Flask(__name__)

# Get the title from the environment variables
APP_TITLE = os.getenv('APP_TITLE')

@app.route('/')
def hello_fishing_app():
    # Pass the title variable into our HTML template
    return render_template('index.html', title=APP_TITLE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)