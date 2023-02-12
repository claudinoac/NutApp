ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)
MAKEFLAGS += --silent
$(eval TEST_TYPE := $(shell [[ -z "$(ARGS)" ]] && echo "null" || echo "$(ARGS)"))
RUN = docker-compose run --rm -w /code api
EXEC = docker-compose exec -w /code api

# HELP COMMANDS
.PHONY: help
help: ## show this help
	@echo 'usage: make [target] [option]'
	@echo ''
	@echo 'Available targets:'
	@egrep '^(.+)\:\ .*##\ (.+)' ${MAKEFILE_LIST} | sed 's/:.*##/#/' | column -t -c 2 -s '#'

.PHONY: init
init:  ### Install dependencies and start application
	@ docker-compose up -d --build
	@ make migrations
	@ make migrate

.PHONY: run $(ARGS)
run:  ### Run apps
	@ docker-compose up -d

.PHONY: migrations $(ARGS)
migrations: run  ### Generate pending migrations
	@ $(EXEC) python manage.py makemigrations $(ARGS)

.PHONY: migrate
migrate: run  ### Apply pending migrations
	@ $(EXEC) python manage.py migrate

.PHONY: superuser
superuser: run  ### Create a superuser
	@ $(EXEC) python3.8 manage.py createsuperuser

.PHONY: shell
shell: run
	@ $(EXEC) python3.8 manage.py shell_plus
