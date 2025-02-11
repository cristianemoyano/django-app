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

deploy-logs:
	docker service logs django_app_web
