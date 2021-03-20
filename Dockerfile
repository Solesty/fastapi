FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

COPY ./app/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt



# FROM python:3.8.1-slim-buster

# ENV WORKDIR=/usr/src/app
# ENV USER=app
# ENV APP_HOME=/home/app/web
# ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# # WORKDIR $WORKDIR

# RUN pip install --upgrade pip
# COPY ./app/requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# RUN adduser --system --group $USER
# RUN mkdir $APP_HOME
# # WORKDIR $APP_HOME

# # COPY . $APP_HOME
# COPY ./app $APP_HOME
# RUN chown -R $USER:$USER $APP_HOME
# USER $USER