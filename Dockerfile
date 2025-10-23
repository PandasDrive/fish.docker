# 1. Start from an official Python base image
# We'll use Python 3.10-slim, which is a lightweight version
FROM python:3.10-slim

# 2. Set the "working directory" inside the container
# This is where our app's files will live
WORKDIR /app

# 3. Copy our requirements file in first
# (This helps Docker cache our packages)
COPY requirements.txt .

# 4. Install the Python packages
RUN pip install -r requirements.txt

# 5. Copy the rest of our application code into the container
COPY . .

# 6. Expose the port our app runs on
# Our app.py uses port 5000
EXPOSE 5000

# 7. Define the command to run when the container starts
# This runs "python app.py"
CMD ["python", "app.py"]