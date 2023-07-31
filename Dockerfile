# Use a Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy local contents into the container at /app
COPY img /app/img
COPY pages /app/pages
COPY models /app/models
COPY Project_Description.py /app

# Expose port 8501 for Streamlit
EXPOSE 8501

# Specify the command to run when the container starts
CMD ["streamlit", "run", "Project_Description.py"]
