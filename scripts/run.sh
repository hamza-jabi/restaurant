#!/bin/bash

set -e

mkdir data

if [ ! -f "data/restaurants.db" ]
then
    echo "Database not found. Initializing..."
    python3 init_db.py
fi

python3 app.py