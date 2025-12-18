#!/bin/sh

set -e
scriptDir=$(cd "$(dirname "$0")" && pwd)
cd "$scriptDir/../backend"

if [ ! -f "data/restaurants.db" ]
then
    echo "Database not found. Initializing..."
    if [ ! -d "data" ]
    then
        mkdir data
    fi
    python3 init_db.py
fi

python3 app.py