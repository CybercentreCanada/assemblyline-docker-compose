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
```NOTE:``` If using the Docker Compose plugin, replace `docker-compose` commands with `docker compose`.

##### 2. Clone this repository
```bash
git clone https://github.com/CybercentreCanada/assemblyline-docker-compose.git
mkdir ~/deployments
cp -R ~/git/assemblyline-docker-compose/minimal_appliance ~/deployments/assemblyline
cd ~/deployments/assemblyline
```
##### 3. Set domain, passwords, and paths in `./.env` and `./config/bootstrap.py`

##### 4. Copy in an existing or generate a self-signed certificate into the `./config` directory in the cloned repository
```bash
source .env
openssl req -nodes -x509 -newkey rsa:4096 -keyout ./config/nginx.key -out ./config/nginx.crt -days 365 -subj "/C=CA/ST=Ontario/L=Ottawa/O=CCCS/CN=$DOMAIN"
```

##### 5. Launch the system

###### Docker Compose Profiles

These following profiles can be combined (unless otherwise specified) depending on your deployment requirements:

- `minimal`: Deploy the Assemblyline with the bare necessities to get the system up and going
- `full`: Deploy Assemblyline with additional components for gathering metrics & logging and the deployment of Kibana
- `archive`: This deploys the Archiver component of Assemblyline but this requires `datastore.archive.enabled: true` in your [configuration](./config/config.yml) otherwise the container will terminate.

**Note**: The `minimal` and `full` profiles are mutually exclusive and are not to be used together.

Pull the containers, depending on which profile you'd like to deploy:
```bash
sudo docker-compose --profile [minimal | full] pull --ignore-buildable
sudo docker-compose --profile [minimal | full] build
sudo docker-compose -f bootstrap-compose.yaml pull
```
Launch the core system, relative to the profile of choice.
```bash
sudo docker-compose --profile [minimal | full] up -d
```
Perform first time only setup and service initialization.
```bash
sudo docker-compose -f bootstrap-compose.yaml up
 ```
