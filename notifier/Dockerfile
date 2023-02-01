# Dockerfile to create image with cron services
FROM ubuntu:latest







#Install Cron & python
RUN apt-get update
RUN apt-get -y install cron
RUN apt-get -y install wget
RUN apt-get -y install python3 
RUN apt-get -y install curl 


# Add the script to the Docker Image
ADD script.sh /root/script.sh
ADD notify.py /root/notify.py
# Give execution rights on the cron scripts
RUN chmod 0644 /root/script.sh
# Add the cron job
RUN crontab -l | { cat; echo "0 9 * * * bash /root/script.sh"; } | crontab -

# Run the command on container startup
CMD cron ; bash