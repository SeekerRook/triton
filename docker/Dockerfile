FROM openjdk:slim
COPY --from=python:3.6 / /
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
RUN mv /code/app/index.html .

CMD ["/bin/bash","-c","/code/app/init.sh"]
