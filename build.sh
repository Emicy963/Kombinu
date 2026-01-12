#!/usr/bin/env bash
# script de build para o render
set -o errexit

pip install -r requirements.txt

# roda as migrações do django e coleta ficheiros estáticos
python manage.py collectstatic --no-input
python manage.py migrate
