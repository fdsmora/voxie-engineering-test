#!/bin/bash
. venv/bin/activate
export FLASK_APP=project
export FLASK_ENV=development
flask init-db
flask run -h localhost -p 8000 
