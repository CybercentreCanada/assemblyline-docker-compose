## Assemblyline 4 - Docker compose documentation

There are two types of comfiguration possible:
    
- Minimal appliance
- Full Appliance

```NOTE:``` Appliances are built on top of docker but for the moment they do not support Docker in swarm mode.

### Minimal Appliance

This setup includes the bare-minimum components for everything to be able to run. There will be no metrics collected and you will have to tail the log from the docker container logs.

#### Setup 

##### 1. Install docker and docker-compose on a linux system
##### 2. Clone this repository

    git clone git@bitbucket.org:cse-assemblyline/assemblyline_docker_compose.git

##### 3. Copy in an existing or generate a self signed certificate into the `./minimal_appliance/config` directory in the cloned repository
    
    openssl req -nodes -x509 -newkey rsa:4096 -keyout ./minimal_appliance/config/nginx.key -out ./minimal_appliance/config/nginx.crt -days 365

##### 4. Set passwords and paths in `./minimal_appliance/.env` and `./minimal_appliance/config/bootstrap.py`
##### 5. Launch the system
    
    (cd ./minimal_appliance/ && docker-compose up -d)


### Full Appliance

This setup includes every single components and all metrics and logging capabilities. Metrics and logs will be gathered inside the same Elasticsearch instance as the processing data and you will have access kibana to view all of those.

#### Setup 

##### 1. Install docker and docker-compose on a linux system
##### 2. Clone this repository

    git clone git@bitbucket.org:cse-assemblyline/assemblyline_docker_compose.git

##### 3. Copy in an existing or generate a self signed certificate into the `./full_appliance/config` directory in the cloned repository

   openssl req -nodes -x509 -newkey rsa:4096 -keyout ./full_appliance/config/nginx.key -out ./full_appliance/config/nginx.crt -days 365

##### 4. Set passwords and paths in `./full_appliance/.env` and `./full_appliance/config/bootstrap.py`
##### 5. Launch the system
    
    (cd ./full_appliance/ && docker-compose up -d)

