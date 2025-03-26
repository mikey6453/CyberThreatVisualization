FROM python:3.10-slim

WORKDIR /code

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project files
COPY ../requirements.txt .

