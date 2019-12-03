



### Setup

1) Install docker and docker-compose on a linux system.
2) Clone this repo `git clone git@bitbucket.org:cse-assemblyline/alv4_appliance.git` 
3) Copy in an existing or generate a self signed certificate into the `config` directory in the cloned repository.
   `openssl req -x509 -newkey rsa:4096 -keyout ./config/nginx.key -out ./config/nginx.crt -days 365`
5) Launch the system `docker-compose up -d`

