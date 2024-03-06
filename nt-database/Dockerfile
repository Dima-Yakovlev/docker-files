FROM mysql:5.7
# Copy the database initialize script: 
# Contents of /docker-entrypoint-initdb.d are run on mysqld startup
# ADD  docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/
COPY my.cnf /etc/my.cnf
# Default values for passwords and database name. Can be overridden on docker run
# ENV MYSQL_ROOT_PASSWORD=my-secret-pw # Not defaulted for security reasons!
ENV MYSQL_DATABASE=nt
ENV MYSQL_USER=notes
ENV MYSQL_PASSWORD=notes