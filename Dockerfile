### Base Image 지정
FROM python:3.10.12

MAINTAINER paulracooni "paulracooni@gmail.com"

# App 설치
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# App 실행
WORKDIR /app/moa_django
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]