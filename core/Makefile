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

# restart services
restart:
	docker service update --force django_app_web
	docker service update --force django_app_db
	docker service update --force django_app_nginx

db-logs:
	docker service logs django_app_db -f

web-logs:
	docker service logs django_app_web -f
	
nginx-logs:
	docker service logs django_app_nginx -f

# update or add environment variable in a running service
update-env:
	docker service update --env-add $(ENV_VAR) django_app_web

# check the status of the Docker Swarm
swarm-status:
	docker node ls

deploy-portainer:
	docker stack deploy -c docker-compose-portainer.yml portainer

portainer-logs:
	docker service logs portainer_portainer

portainer:
	open http://localhost:9000
