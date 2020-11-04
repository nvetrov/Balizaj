FROM python:3.7
ENV PYTHONUNBUFFERED=1
ENV app_port 8080
EXPOSE ${app_port}

COPY . /srv/www/Balizaj
WORKDIR /srv/www/Balizaj

RUN pip install -r requirements.txt
CMD python ./${WORKDIR}/manage.py runserver 0.0.0.0:${app_port}