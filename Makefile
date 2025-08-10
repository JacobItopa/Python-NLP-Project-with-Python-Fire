install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval Untitled90.ipynb

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

deploy:
	# Add deployment commands here, e.g., to a server or cloud service

container lint:
	# Lint the Dockerfile or container configuration

refactor:
	# Refactor the codebase, e.g., by applying design patterns or improving structure

all: install lint test format deploy container
