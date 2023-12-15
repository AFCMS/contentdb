#!/bin/sh

# Create a database migration, and copy it back to the host.

set -e
. "${BASH_SOURCE%/*}/common.sh"

docker exec "$(container app)" sh -c "FLASK_CONFIG=../config.cfg FLASK_APP=app/__init__.py flask db downgrade"
