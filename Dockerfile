FROM python:3-onbuild
COPY ./app /usr/src/app
CMD ["gunicorn","app:app"]
EXPOSE 80
