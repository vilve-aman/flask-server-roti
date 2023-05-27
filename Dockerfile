FROM python:3.10-slim
WORKDIR ./flask_app
COPY . .
RUN apt-get update
RUN #apt-get install build-essential
RUN pip install requirements.txt
RUN ls
ENTRYPOINT ["make", "run_app" ]