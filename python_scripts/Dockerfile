FROM python:3.10.8-alpine3.16
ARG nt_import_src="C:\Users\14sur\Documents\GitHub\nt_import"

RUN mkdir /opt/tomcat
RUN mkdir /opt/tomcat/uploadedFile
RUN mkdir /opt/tomcat/unHandlerErrors
RUN mkdir /notes
RUN chmod -R 777 /opt/tomcat/uploadedFile
RUN chmod -R 777 /notes
RUN chmod -R 777 /opt/tomcat/unHandlerErrors

RUN apk update
RUN apk add git
RUN apk add vim
RUN apk add --no-cache --upgrade bash
RUN apk add gcc
RUN apk add musl-dev
RUN apk add linux-headers
RUN pip3 install psutil
RUN pip3 install six
WORKDIR /app
RUN git clone https://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@github.com/noteunlimited/nt_import.git
WORKDIR /app/nt_import
RUN mkdir ./logs
RUN mkdir ./logs/run
RUN chmod -R 777 ./logs
RUN chmod -R 777 ./logs/run
RUN pip3 install -r requirements.txt 
COPY . .
RUN pip3 install -r requirements_app.txt 
RUN sed -i "s|localhost|nt-database|g" ./settings/database.py 

CMD [ "python3", "app.py"]
# ENTRYPOINT [ "python3", "-u", "/app/nt_import/nt_importd.py", "/app/nt_import/logs/run/nt_importd.pid","/app/nt_import/logs/nt_importd.log","start"]
