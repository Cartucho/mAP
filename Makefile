.ONESHELL:
SHELL := /bin/bash

#TAG=$(shell git describe  --all --long | cut -d "/" -f2)

define PROJECT_HELP_MSG
Usage:
	make help                           show this message
	make setup
	make build
endef
export PROJECT_HELP_MSG

help:
	@echo "$$PROJECT_HELP_MSG" | less

setup:
	pipenv install

build: clean
	python setup.py sdist bdist_wheel

clean:
	-rm -r dist
	-rm -r build
	-rm -r mAP.egg-info