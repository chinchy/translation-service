#!/bin/bash
set -e
if [ -z "$NO_MIGRATION" ]; then
    echo "Applying migrations"
    poetry run alembic upgrade head
    echo "Done"
fi

echo "Starting application"
exec "$@"
