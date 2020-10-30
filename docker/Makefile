TAG = kyclark/biofx_python:0.1.0

img:
	docker build --tag=$(TAG) .

3.10:
	docker build --tag=$(TAG) -f Dockerfile.3.10

shell:
	docker run -it $(TAG) bash

push: 
	docker push $(TAG)
