SHELL := /bin/bash

publish_pypi: clean
	python3 setup.py sdist bdist_wheel
	source .envrc-dev && twine upload -u $$PYPI_USERNAME -p $$PYPI_PASSWORD dist/*
	make clean

dev_install: dev_uninstall
	python3 setup.py install --user

dev_uninstall:
	pip3 uninstall multipass-compose -y

setup_test_env:
	python3 -m venv venv

test: setup_test_env
	source venv/bin/activate && make dev_install
	source venv/bin/activate && cd tests && make test

clean:
	@rm -rf build dist *egg-info */__pycache__ tmp