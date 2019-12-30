FROM python:3.7

EXPOSE 5000

# Sets the working directory
WORKDIR /app

# Install packages specified in requirements.txt
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy necessary folders and files
COPY templates /app/templates
COPY static /app/static

# Run app.py when the container launches
COPY app.py /app
CMD python3 app.py