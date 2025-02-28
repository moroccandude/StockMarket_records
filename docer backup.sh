pull image

docker image pull IMAGE

create constainer for IMAGE with -it interactive mode with terminal (bash)
docker contrainer create -it IMAGE bash

runi t

docker container run start -i Name_con

# Stop services only
docker-compose stop

# Stop and remove containers, networks..
docker-compose down 

# Down and remove volumes
docker-compose down --volumes 

# Down and remove images
docker-compose down --rmi <all  | local> 

 1  hdfs dfs mkdir /user/folder
    2  hdfs dfs -mkdir /user/folder
    3  hdfs dfs -mkdir /user/folder/samil
    4  hdfs dfs -put /yy.yaml /user/folder/samil
    5  history
  remove dir
  /user/etudiant/crypto/raw/YYYY=2025/MM=02/DD=23
remove none empty file :
hdfs dfs -rm -r /path/to/directory

By default, HDFS moves deleted files to the trash (.Trash directory in the user's home directory). To permanently delete a file or directory (bypassing the trash), use the -skipTrash option:
hdfs dfs -rm -r -skipTrash /path/to/directory
----------Tu peux envoyer un fichier vers HDFS avec la commande put :

hdfs dfs -put /chemin/local/fichier.txt /chemin/hdfs/
----
6. Using Docker to Remove Files from HDFS

docker exec -u root namenode hdfs dfs -rm -r /path/to/directory

    
Generic options supported are:
-conf <configuration file>        specify an application configuration file
-D <property=value>               define a value for a given property
-fs <file:///|hdfs://namenode:port> specify default filesystem URL to use, overrides 'fs.defaultFS' property from configurations.
-jt <local|resourcemanager:port>  specify a ResourceManager
-files <file1,...>                specify a comma-separated list of files to be copied to the map reduce cluster
-libjars <jar1,...>               specify a comma-separated list of jar files to be included in the classpath
-archives <archive1,...>          specify a comma-separated list of archives to be unarchived on the compute machines



------------------------------------------------
To run docker daemon on Linux (from CLI),
sudo service docker start
sudo systemctl status docker
sudo systemctl start docker
sudo systemctl enable docker //will run after booting

Find the Process ID (PID) Using the Port

sudo lsof -i :PORT


------
# Comment fonctionne le groupe Docker ?
# Le fichier socket Docker (/var/run/docker.sock) est la clé de communication entre les clients Docker et le démon Docker. Par défaut, ce fichier appartient à l'utilisateur root et au groupe docker. Cela signifie que si tu fais partie de ce groupe, tu peux accéder à Docker sans avoir besoin de privilèges d'administrateur.



----
convert JSON STR -> python Object
json.load()


---
Declare a as a global variable within the function using the global keyword
a = "" 
arr = [12, 82, 8, 21, 92]

def fun():
    global a  
    ....

> check if docker what .socket used 
docker context ls
> switch btw them 
docker context use nameSocket

->logging configuration which might be specified in a file called `logging_config.py` 
AIRFLOW__LOGGING__LOGGING_CONFIG_CLASS = airflow.logging_config.DEFAULT_LOGGING_CONFIG

->file path en namenode not on airflow webservice
2029240f6d1128be89ddc32729463129  coingecko_raw.json  hh.json  pymp-aw11511k  pymp-fqk8c7u4  tmp7gcz89_m  tmpgd7_oni9  xx.json
(airflow)docker  exec -u root namenode hdfs dfs -put -f coingecko_raw.json /user/etudiant/crypto/raw/YYYY=2025/MM=02/DD=25 
put: `coingecko_raw.json': No such file or directory



------------------

the error message about SASL encryption is a security warning from Hadoop. It's related to how data is transferred between nodes in the cluster.


Function	   | Input       |    Type	Use Case
json.load()	 | File object |	Reading from JSON files
json.loads() |	String	   |  Parsing JSON strings



--------------------
strip()
What it does: Removes characters from both ends of the string

Default: Removes whitespace (spaces, tabs, newlines)

Syntax: string.strip([chars])
-----------
lstrip() (Left Strip)
What it does: Removes characters from the beginning (left side) only

Default: Removes whitespace

Syntax: string.lstrip([chars])
-------------------------
rstrip() (Right Strip)
What it does: Removes characters from the end (right side) only

Default: Removes whitespace

Syntax: string.rstrip([chars])

chmod +x mapper.py reducer.py #make them executables



-----------------------------
 trying python on Debian 9 (Stretch) for running | The default repositories are outdated (Debian 9 reached EOL in 2022), causing apt to fail to locate python3.
 
 > Edit the sources.list File
# Configure repositories (if not already done)
echo "" > /etc/apt/sources.list
cat <<EOF >> /etc/apt/sources.list
deb http://archive.debian.org/debian stretch main contrib non-free
deb http://archive.debian.org/debian-security stretch/updates main contrib non-free
EOF

# Update package lists (ignore expiry errors)
apt-get update -o Acquire::Check-Valid-Until=false

# Install Python 3
apt-get install -y python3


----------
> docker group 
The docker group is a key part of Docker’s permission system on Linux. It allows non-root users to interact with Docker without requiring sudo

--------------
> Purpose of the docker Group
Docker’s daemon (dockerd) runs as the root user for privileged operations (e.g., managing containers, networks, volumes).

The /var/run/docker.sock socket file (used by the Docker CLI to communicate with the daemon) is owned by root and the docker group:


srw-rw---- 1 root docker 0 Feb 28 09:08 /var/run/docker.sock
Users in the docker group inherit group-level permissions (rw-) to the socket, allowing them to run Docker commands without sudo.

----------------------------------
Users in the docker group inherit group-level permissions (rw-) to the socket, allowing them to run Docker commands without sudo.

---------------------------
sudo usermod -aG docker $USER  # Replace $USER with the target username




-----------------
> docker-compose
docker-compose up – Start services.
docker-compose down – Stop and remove services.
docker-compose build – Rebuild images.
docker-compose restart – Restart services.
docker-compose ps – List containers' status.
docker-compose exec – Execute commands inside containers.
docker-compose logs – Show container logs.
docker-compose pull – Pull images from a registry.
docker-compose up -d – Run in detached mode.