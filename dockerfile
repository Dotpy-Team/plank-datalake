FROM python:3.11.9-slim AS builder

EXPOSE 8000
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Cria o usuário app
RUN useradd -ms /bin/bash app

# Usa o usuário app
USER app

CMD ["python", "plank_datalake/manage.py", "runserver", "0.0.0.0:8000"]
