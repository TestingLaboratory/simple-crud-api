FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY booker /app/booker

COPY shell_scripts /app/shell_scripts
RUN chmod -R +x ./shell_scripts

ENTRYPOINT ["/bin/sh", "./shell_scripts/run_app.sh", "booker", "8089"]