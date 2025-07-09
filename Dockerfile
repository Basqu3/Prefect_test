FROM python:3.9

WORKDIR /app

# Update system packages to reduce vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY hello.py .

# Set environment variables for Prefect
ENV PREFECT_API_URL=http://prefect-server:4200/api

CMD ["python", "hello.py"]