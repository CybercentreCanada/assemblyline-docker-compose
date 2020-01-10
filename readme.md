



### Setup

1. Install docker and docker-compose on a linux system.
2. Clone this repo `git clone git@bitbucket.org:cse-assemblyline/assemblyline_docker_compose.git` 
3. Copy in an existing or generate a self signed certificate into the `config` directory in the cloned repository.
   `openssl req -nodes -x509 -newkey rsa:4096 -keyout ./config/nginx.key -out ./config/nginx.crt -days 365`
4. Set passwords and paths in `.env` and `./config/bootstrap.py`.
6. Launch the system `docker-compose up -d`

#### Caveats

- Docker isn't supported in swarm mode