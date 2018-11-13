FROM python:3
COPY . /app
WORKDIR /app
RUN pip3 install pipenv
RUN apt-get update && apt-get install -y \
    python3-dev \
 && rm -rf /var/lib/apt/lists/*
RUN pipenv install
EXPOSE 8006
CMD ["python", "service.py"]
