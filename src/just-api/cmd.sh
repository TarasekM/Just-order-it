#!/bin/bash
if [ "$FLASK_ENV" = 'development' ]; then
    echo "Running Development Server"
    exec python -m flask run --host=0.0.0.0 --port=$FLASK_RUN_PORT
elif [ "$FLASK_ENV" = 'testing' ]; then
    echo "Running Tests"
    exec python -m pytest
else
    echo "Running Production Server"
    exec uwsgi --http 0.0.0.0:$FLASK_RUN_PORT --wsgi-file ./wsgi.py \
    --callable app --master
fi