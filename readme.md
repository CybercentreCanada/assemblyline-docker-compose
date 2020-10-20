## Assemblyline 4 - Docker compose documentation

There are two types of configuration possible:
    
- Minimal appliance
- Full Appliance

```NOTE:``` Appliances are built on top of docker but for the moment they do not support Docker in swarm mode.

### Minimal Appliance

This setup includes the bare-minimum components for everything to be able to run. There will be no metrics collected and you will have to tail the log from the docker container logs.

### Full Appliance

This setup includes every single components and all metrics and logging capabilities. Metrics and logs will be gathered inside the same Elasticsearch instance as the processing data and you will have access kibana to view all of those.

## Setup

For full documentation on how to setup an assemblyline appliance see the documentation page. 
https://cybercentrecanada.github.io/assemblyline4_docs/

#### Quickstart

##### 1. Install docker and docker-compose on a linux system
##### 2. Clone this repository

    git clone git@bitbucket.org:cse-assemblyline/assemblyline_docker_compose.git

##### 3 Choose deployment type

Choose one of the minimal or full deployments. The rest of the commands 
and paths given will be relative to the directory specific to the deployment
type you are doing. 

##### 3. Copy in an existing or generate a self signed certificate into the `./config` directory in the cloned repository
    
    openssl req -nodes -x509 -newkey rsa:4096 -keyout ./config/nginx.key -out ./config/nginx.crt -days 365 -subj "/C=CA/ST=Ontario/L=Ottawa/O=CCCS/CN=assemblyline.local"
    
##### 4. Set passwords and paths in `./.env` and `./config/bootstrap.py`
##### 5. Launch the system
    
Pull the containers and launch the core system.
    
    sudo docker-compose pull
    sudo docker-compose up -d

Pull the containers and perform first time only setup and install.

    sudo docker-compose -f bootstrap-compose.yaml pull 
    sudo docker-compose -f bootstrap-compose.yaml up -d 
 