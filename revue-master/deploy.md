# Deploying to a DigitalOcean droplet

1. Create droplet
2. Install docker in the droplet
3. Clone the entire project into the droplet
4. Add in `config.py`
5. `docker-compose up -d`
6. Initialize `mongodb`
    ```
    > docker exec -it mongodb bash
    > mongo -u flaskuser -p
    > use revue
    > db.createUser({user: 'flaskuser', pwd: 'passwd123', roles: [{role: 'readWrite', db: 'revue'}]})
    ```
7. build or serve the frontend to point to DigitalOcean. Configure it using a `.env.[mode]` file.

## Updating
When updating the containers, you need to make sure to clear the `appdata` volume so that it is rebuilt. We want to make sure not to delete the `mongodb` volume, though, since that has data. Since python is not compiled, you don't actually have to rebuild the entire docker container everytime you update your python code **unless** you have updated your `requirements.txt`.
- List all volumes: `docker volume ls`
- remove a specific volume: `docker volume rm [volume-name]`
- [Backing up a volume](https://docs.docker.com/storage/volumes/#backup-a-container)
- [Removing docker images, containers, volumes, networks](https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/)
