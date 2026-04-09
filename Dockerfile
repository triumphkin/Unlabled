# Use an official, lightweight Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your simulation code into the container
COPY . .

# --- CHOOSE YOUR RUN COMMAND ---

# OPTION A: If your simulation just runs in the terminal (CLI)
# CMD ["python", "app.py"] 

# Expose the port Streamlit uses
EXPOSE 8501

# Run the Streamlit command instead of standard Python
# (Make sure to change "main.py" if your file is actually named "app.py")
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]