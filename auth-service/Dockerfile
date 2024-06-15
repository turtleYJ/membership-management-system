FROM python:3.9-slim

WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install debugpy

COPY . .

# CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
CMD ["python", "app.py"]