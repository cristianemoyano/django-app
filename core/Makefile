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

