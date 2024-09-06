FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app/. .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD ["gunicorn", "dropbox_like_service.wsgi:application", "--bind", "0.0.0.0:8000"]

# CMD ["python", "dropbox_like_service/manage.py", "runserver", "0.0.0.0:8000"]
# ENTRYPOINT ["sh", "entrypoint.sh"]