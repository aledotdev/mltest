
The purpose of this project is to show a brief example of an API to expose a Machine Learning model.






You need

- Docker
- Docker Compose
- Docker Machine

First create docker cloud!!!
Example with Digital Ocean
  - Set DO Access Token
    - `export DIGITALOCEAN_ACCESS_TOKEN=<DO_ACCESS_TOKEN>`
  - Create Docker Swarm nodes
    - `docker-machine create --driver digitalocean --digitalocean-private-networking do-manager`
    - `docker-machine create --driver digitalocean --digitalocean-private-networking do-worker-1`
    - `docker-machine create --driver digitalocean --digitalocean-private-networking do-worker-2`
  - Set `do-manager` node as Swarm manager:
    - `docker-machine ssh do-manager` # Connect to do-manager node
    - `export MANAGER_IP=$(docker-machine ssh do-manager ip route | grep 'eth1' | grep -oP "src \K([0-9\.]+)")` # get node private IP
    - `docker swarm init --advertise-addr $MANAGER_IP`
    - Copy the complete `docker swarm join` command to apply in workers nodes
    - Logout from do-manager node
  - Set Docker Swarm nodes
    - `docker-machine ssh do-worker-1` # Connect to do-manager node
    - Paste the complete `docker swarm join`
    - Logout from do-worker-1 node
    - `docker-machine ssh do-worker-2` # Connect to do-manager node
    - Paste the complete `docker swarm join`
    - Logout from do-worker-2 node

  - Set `do-manager` as current Docker machine
    - `eval $(docker-machine env do-manager)`
    - `docker node ls` # List nodes on docker swarm

  - Login to docker
    - `export DOCKER_REPO_USER=<DOCKER_USER>` # Set repo docker username
    - `docker login --username=$DOCKER_REPO_USER`

  - Build and push API image to repo
    - `docker build -t $DOCKER_REPO_USER/api . -f deploy/api.dockerfile`
    - `docker push $DOCKER_REPO_USER/api

  - docker stack deploy --compose-file=docker-compose.yml prod
  - `docker service ls` # List services started, prod_api and prod_haproxy

  - Scale api containers
   - `docker service scale prod_api`
