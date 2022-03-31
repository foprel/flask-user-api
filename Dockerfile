# syntax=docker/dockerfile:1

FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy source code
COPY . .

# Install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]