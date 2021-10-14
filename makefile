SHELL := /bin/bash

create_image:
	docker build -t weevenetwork/filter . -f image/Dockerfile
.phony: create_image

run_image:
	docker run -p 5000:80 --rm --env-file=./config.env weevenetwork/filter:latest
.phony: run_image

lint:
	pylint main.py app/
.phony: lint

install_local:
	pip3 install -r image/requirements.txt
.phony: install_local

run_local:
	 python image/src/main.py
.phony: run_local
