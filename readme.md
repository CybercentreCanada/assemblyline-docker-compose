## Assemblyline 4 - Docker compose documentation

**NOTE:** Appliances are built on top of Docker but for the moment they do not support Docker in swarm mode.


## Setup

For full documentation on how to setup an Assemblyline appliance see the documentation page.
https://cybercentrecanada.github.io/assemblyline4_docs/

#### Quickstart

##### 1. Install docker and docker-compose on a linux system
```NOTE:``` If using the Docker Compose plugin, replace `docker-compose` commands with `docker compose`.

##### 2. Clone this repository
```bash
git clone https://github.com/CybercentreCanada/assemblyline-docker-compose.git
mkdir ~/deployments
cp -R ~/git/assemblyline-docker-compose ~/deployments/assemblyline
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

- `minimal`: This setup includes the bare-minimum components for everything to be able to run. There will be no metrics collected and you will have to tail the log from the docker container logs.
- `full`: This setup includes every single components and all metrics and logging capabilities. Metrics and logs will be gathered inside the same Elasticsearch instance as the processing data and you will have access kibana to view all of those.
- `archive`: This deploys the Archiver component of Assemblyline but this requires `datastore.archive.enabled: true` in your [configuration](./config/config.yml) otherwise the container will terminate.

**Note**: The `minimal` and `full` profiles are mutually exclusive and are not to be used together.

You can specify which profiles to use on the commandline using the `--profile` flag or set `COMPOSE_PROFILES` in your `.env` file (default: `COMPOSE_PROFILES=minimal`)

The following instructions assume `.env` contains `COMPOSE_PROFILES`, otherwise the `--profile` flag can be used to override what's set in `.env`:
 1. Pull the containers, depending on which profile you'd like to deploy:
    ```bash
    sudo docker-compose pull --ignore-buildable
    sudo docker-compose build
    sudo docker-compose -f bootstrap-compose.yaml pull
    ```

 2. Launch the core system, relative to the profile of choice.
    ```bash
    sudo docker-compose up -d
    ```
 3. Perform first time only setup and service initialization.
    ```bash
    sudo docker-compose -f bootstrap-compose.yaml up
    ```
