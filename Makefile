SHELL  = /bin/bash
PYTHON = /usr/bin/python3

-include .env
export

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("	%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@echo "Usage: make <command>"
	@echo "Options:"
	@$(PYTHON) -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

build:  ## Build api
	docker-compose down --volumes
	docker-compose build

bash:  ## Run api bin/bash
	@docker-compose run --rm runner

seeder:  ## Seed database
	@docker-compose run --rm runner python seeds/seed_*.py

tests: -B  ## Run api tests
	@docker-compose run --rm runner pytest --cov-report=term-missing --cov-report=html --cov=.

code-convention:  ## Run code convention
	@docker-compose run --rm runner flake8 main.py app tests
	@echo == Code convention is ok

run:  ## Run api
	@docker-compose up cart_api

run-debug:  ## Run api in debugger mode
	@docker-compose run --rm --service-ports cart_api flask run

encrypt-secrets:  ## Encrypt secret vars
	@sops -e -i --encrypted-regex "^(data|stringData)$$" \
		--age $$(cat ~/.sops/age/key.txt | grep -oP "public key: \K(.*)") $(file)

decrypt-secrets:  ## Decrypt secret vars
	@export SOPS_AGE_KEY_FILE=~/.sops/age/key.txt && \
	    sops -d -i $(file)

encrypt-gpg-secrets:  ## Encrypt secret vars gpg
	@sops -e -i --encrypted-regex "^(data|stringData)$$" \
		-p "$$(gpg --list-secret-keys $$(kubectl config get-contexts -o name) | sed -n 2p | xargs)" $(file)

decrypt-gpg-secrets:  ## Decrypt secret vars gpg
	@sops -d -i $(file)

create-tag:  ##
	@git tag $(tag) && \
	  git push origin $(tag)

delete-tag:  ##
	@git tag -d $(tag) && \
	  git push origin :refs/tags/$(tag)

monitoring: -B  ## Run prometheus
	@docker-compose up -d prometheus \
	  grafana

install: build seeder tests code-convention  ## Install api

%:
	@:
