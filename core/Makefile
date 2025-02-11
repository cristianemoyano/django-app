# shell container
shell:
	docker compose exec web bash

# variables
TAG ?= latest
IMAGE ?= clifford666/django-app

# build and push docker image
publish:
	docker build -t $(IMAGE):$(TAG) .
	docker push $(IMAGE):$(TAG)

deploy:
	docker stack deploy -c docker-compose-prod.yml django_app

db-logs:
	docker service logs django_app_db

web-logs:
	docker service logs django_app_web
	
nginx-logs:
	docker service logs django_app_nginx

# update or add environment variable in a running service
update-env:
	docker service update --env-add $(ENV_VAR) django_app_web

# check the status of the Docker Swarm
swarm-status:
	docker node ls

deploy-portainer:
	docker stack deploy -c docker-compose-portainer.yml portainer
