TAG39 = kyclark/biofx_python_3.9:0.1.0
TAG38 = kyclark/biofx_python_3.8:0.1.0
TAG310 = kyclark/biofx_python_3.10:0.1.0
DOCKER = sudo docker

39:
	$(DOCKER) build --tag=$(TAG39) -f Dockerfile.3.9 .

38:
	$(DOCKER) build --tag=$(TAG38) -f Dockerfile.3.8 .

310:
	$(DOCKER) build --tag=$(TAG310) -f Dockerfile.3.10

test: test38 test39 test310

test38:
	$(DOCKER) run $(TAG38) /app/biofx_python/bin/uber_test.sh

test39:
	$(DOCKER) run $(TAG39) /app/biofx_python/bin/uber_test.sh

test310:
	$(DOCKER) run $(TAG310) /app/biofx_python/bin/uber_test.sh

shell38:
	$(DOCKER) run -it $(TAG38) bash

shell39:
	$(DOCKER) run -it $(TAG39) bash

shell310:
	$(DOCKER) run -it $(TAG310) bash

push38: 
	$(DOCKER) push $(TAG38)

push39: 
	$(DOCKER) push $(TAG39)

push310: 
	$(DOCKER) push $(TAG310)
