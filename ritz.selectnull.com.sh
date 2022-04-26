#!/bin/bash

NAME=ritz.selectnull.com
USER=ritz
HOME=/home/$USER

WSGI_FILE=$HOME/projects/$NAME/project/wsgi.py
VENV=$HOME/.venvs/$NAME

echo "$(date) - Starting project $NAME as $(whoami)"

sudo -u $USER touch "$HOME/projects/run/.reload-$NAME"

# Activate the virtual environment
source $VENV/bin/activate

exec uwsgi \
    --master \
    --pythonpath=$HOME/projects/$NAME \
    --pidfile=$HOME/projects/run/$NAME.pid \
    --socket=/$HOME/projects/run/$NAME.sock \
    --chdir=$HOME \
    --wsgi-file=$WSGI_FILE \
    --chmod-socket=666 \
    --processes=8 \
    --threads=4 \
    --enable-threads \
    --harakiri=600 \
    --harakiri-verbose \
    --vacuum \
    --log-x-forwarded-for \
    --idle=300 \
    --max-requests=5000 \
    --buffer-size=32768 \
    --logger=file:$HOME/logs/$NAME-uwsgi.log \
    --logdate \
    --post-buffering=1 \
    --uid=$USER \
    --gid=$USER \
    --stats=$HOME/projects/run/$NAME-stats.sock \
    --touch-reload=$HOME/projects/run/.reload-$NAME
