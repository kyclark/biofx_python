TAG = kyclark/biofx_python:0.1.0
TAG38 = kyclark/biofx_python_3.8:0.1.0
DOCKER = sudo docker

img:
	$(DOCKER) build --tag=$(TAG) .

3.8:
	$(DOCKER) build --tag=$(TAG38) -f ./Dockerfile.3.8 .

3.10:
	$(DOCKER) build --tag=$(TAG) -f Dockerfile.3.10

shell:
	$(DOCKER) run -it $(TAG) bash

shell38:
	$(DOCKER) run -it $(TAG38) bash

push: 
	$(DOCKER) push $(TAG)
