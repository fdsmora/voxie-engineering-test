#!/bin/bash
. venv/bin/activate
export FLASK_APP=project
flask init-db
flask run -h '0.0.0.0' -p 5000
