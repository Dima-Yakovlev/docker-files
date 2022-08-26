FROM tomcat:8.5.82-jdk8-temurin-jammy
MAINTAINER Dima Yakovlev <14urup91@gmail.com>

# tomcat-users.xml sets up user accounts for the Tomcat manager GUI
# and script access for Maven deployments
ADD tomcat/tomcat-users.xml $CATALINA_HOME/conf/

# ADD tomcat/catalina.sh $CATALINA_HOME/bin/
ADD tomcat/run.sh $CATALINA_HOME/bin/run.sh
RUN chmod +x $CATALINA_HOME/bin/run.sh

RUN cp -avT $CATALINA_HOME/webapps.dist/manager $CATALINA_HOME/webapps/manager

# add MySQL JDBC driver jar
ADD tomcat/mysql-connector-java-5.1.36-bin.jar $CATALINA_HOME/lib/

# create mount point for volume with application

RUN mkdir /opt/tomcat
RUN mkdir /opt/tomcat/uploadedFile
RUN mkdir /notes
RUN chmod -R 777 /opt/tomcat/uploadedFile
RUN chmod -R 777 /notes
# add tomcat jpda debugging environmental variables
#ENV JPDA_OPTS="-agentlib:jdwp=transport=dt_socket,address=8000,server=y,suspend=n"
ENV JPDA_ADDRESS="8000"
ENV JPDA_TRANSPORT="dt_socket"

# start tomcat8 with remote debugging
EXPOSE 8080
CMD ["run.sh"]