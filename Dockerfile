# Base image 
FROM python:3.9

# workdir
WORKDIR /app

# Copy command
COPY . /app


# run command
RUN pip install -r requirements.txt

# port
EXPOSE 5000



# command
CMD ["python", "./app.py"]