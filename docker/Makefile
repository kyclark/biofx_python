TAG390 = kyclark/biofx_python_3.9.0:0.1.0
TAG391 = kyclark/biofx_python_3.9.1:0.1.0
TAG38 = kyclark/biofx_python_3.8:0.1.0
TAG310 = kyclark/biofx_python_3.10:0.1.0
DOCKER = sudo docker

imgs: docker38 docker390 docker391 docker310

docker391:
	$(DOCKER) build --tag=$(TAG39) -f Dockerfile391 .

docker390:
	$(DOCKER) build --tag=$(TAG39) -f Dockerfile390 .

docker38:
	$(DOCKER) build --tag=$(TAG38) -f Dockerfile38 .

docker310:
	$(DOCKER) build --tag=$(TAG310) -f Dockerfile310

test: test38 test39 test310

test38:
	$(DOCKER) run $(TAG38) /app/biofx_python/bin/uber_test.sh

test390:
	$(DOCKER) run $(TAG390) /app/biofx_python/bin/uber_test.sh

test391:
	$(DOCKER) run $(TAG391) /app/biofx_python/bin/uber_test.sh

test310:
	$(DOCKER) run $(TAG310) /app/biofx_python/bin/uber_test.sh

shell38:
	$(DOCKER) run -it $(TAG38) bash

shell390:
	$(DOCKER) run -it $(TAG390) bash

shell391:
	$(DOCKER) run -it $(TAG391) bash

shell310:
	$(DOCKER) run -it $(TAG310) bash

push38: 
	$(DOCKER) push $(TAG38)

push390: 
	$(DOCKER) push $(TAG390)

push391: 
	$(DOCKER) push $(TAG391)

push310: 
	$(DOCKER) push $(TAG310)
