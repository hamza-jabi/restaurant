#!/bin/bash

set -e

mkdir -p data

if [ ! -f "data/restaurants.db" ]
then
    echo "Database not found. Initializing..."
    python init_db.py
fi

python app.py