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

Find the Process ID (PID) Using the Port

sudo lsof -i :PORT


------
# Comment fonctionne le groupe Docker ?
# Le fichier socket Docker (/var/run/docker.sock) est la clé de communication entre les clients Docker et le démon Docker. Par défaut, ce fichier appartient à l'utilisateur root et au groupe docker. Cela signifie que si tu fais partie de ce groupe, tu peux accéder à Docker sans avoir besoin de privilèges d'administrateur.



----
