FROM bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8

# Clear the existing sources and add new ones
RUN echo "" > /etc/apt/sources.list && \
    echo "deb http://archive.debian.org/debian stretch main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb http://archive.debian.org/debian-security stretch/updates main contrib non-free" >> /etc/apt/sources.list

# Update package lists (ignore expiry errors)
RUN apt-get update -o Acquire::Check-Valid-Until=false

# Install Python 3
RUN apt-get install -y python3
