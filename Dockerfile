
FROM python:3.10-slim

# Set the working directory
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000


CMD ["python", "app.py"]
