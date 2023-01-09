ALPHA ?= true
HOST ?= localhost
PORT ?= 5000
SYSTEM_PYTHON ?= python3
FLASK_APP ?= app.py

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip3
REQUIREMENTS = geometric-service/requirements.txt
FLASK = $(VENV)/bin/flask
GUNICORN = $(VENV)/bin/gunicorn

######################################################
# Deploy
######################################################

debug: $(VENV)/bin/activate
	@ ALPHA=$(ALPHA) FLASK_APP=geometric-service/app.py $(FLASK) run --host=$(HOST) --port=$(PORT)
.PHONY: debug

release: $(VENV)/bin/activate
	@ ALPHA=$(ALPHA) $(GUNICORN) --pythonpath geometric-service --bind $(HOST):$(PORT) wsgi:app
.PHONY: release

######################################################
# Test
######################################################

test: $(VENV)/bin/activate
	@ pytest
.PHONY: test

######################################################
# Help Targets
######################################################

$(VENV)/bin/activate: $(REQUIREMENTS)
	$(SYSTEM_PYTHON) -m venv $(VENV)
	$(PIP) install -r $(REQUIREMENTS)

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
.PHONY: clean