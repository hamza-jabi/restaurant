#!/bin/bash

cd "$(git rev-parse --show-toplevel)"
git add .
msg="${1:-"Update $(date '+%Y-%m-%d %H:%M:%S')"}"
git commit -m "$msg"
git push origin main