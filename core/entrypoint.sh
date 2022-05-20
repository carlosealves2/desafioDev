#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $HOST $PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

cd core/
python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic --no-input

exec "$@"