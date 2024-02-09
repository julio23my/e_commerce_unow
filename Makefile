-include .env
export
.PHONY: docs test help
.DEFAULT_GOAL := help

SHELL := /bin/bash

create-env:
	@echo "Creating .env file"
	@cp .env.example .env
	python -m venv env
	@echo -e "\r\nYou can activate the environment with:\r\n\r\n$$ source env/bin/activate\r\n"

lint: ## Run linter
	@echo "Running linter"
	@flake8

pretty: ## Run code formatter
	@echo "Running code formatter"
	@black .