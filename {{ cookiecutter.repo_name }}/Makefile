.PHONY: clean data lint requirements freeze create_environment

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_INTERPRETER = {{ cookiecutter.python_interpreter }}
DEPENDENCY_MANAGER = {{ cookiecutter.dependency_manager }}

SUBDIR_ROOTS := src notebooks
DIRS := . $(shell find $(SUBDIR_ROOTS) -type d)
GARBAGE_PATTERNS := *.pyc *~ *-checkpoint.ipynb
GARBAGE := $(foreach DIR,$(DIRS),$(addprefix $(DIR)/,$(GARBAGE_PATTERNS)))

ifeq ($(DEPENDENCY_MANAGER), pipenv)
    RUN_PRE = pipenv run
    INSTALL_DEPENDENCIES = pipenv install
    PYTHON_INTERPRETER := $(RUN_PRE) $(PYTHON_INTERPRETER)
else
    INSTALL_DEPENDENCIES = $(DEPENDENCY_MANAGER) install -r requirements.txt
endif

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
requirements: test_environment
	$(INSTALL_DEPENDENCIES)

## Gets the data and stores it locally
data-get:
	$(PYTHON_INTERPRETER) scripts/get_data.py

## Processes the raw data and stores the processed result
data-process:
	$(PYTHON_INTERPRETER) scripts/process_data.py

## Deletes any processed data files/features data files
data-clean:
	@rm -rf data/processed/*
	@rm -rf data/features/*

## Delete all compiled Python files or temp files
clean:
	@rm -rf $(GARBAGE)

## Lint using flake8
lint:
	flake8 --exclude=env/,lib/,bin/,docs/conf.py .

## Set up python interpreter environment
create_environment:
ifeq($(DEPENDENCY_MANAGER), pipenv)
    @echo ">>> Installing pipenv if not already installed"
	@pip install -q pipenv
	@echo ">>> Creating new virtualenv with pipenv"
	@pipenv install
else
    @echo ">>> Installing virtualenv if not already installed"
    @pip install -q virtualenv
    @echo ">>> Creating new virtual environment for project"
    @virtualenv env/
endif

## Freeze dependencies
freeze:
ifeq($(DEPENDENCY_MANAGER), pipenv)
    $(RUN_PRE) pip freeze --local > requirements.txt
else
    $(DEPENDENCY_MANAGER) freeze --local > requirements.txt
endif

## Test python environment is setup correctly
test_environment:
	$(PYTHON_INTERPRETER) test_environment.py

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################



#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := show-help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: show-help
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
