#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn

python manage.py collectstatic --noinput
python manage.py migrate