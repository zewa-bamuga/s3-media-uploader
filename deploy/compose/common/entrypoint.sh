#!/bin/bash

set -o errexit
set -o pipefail

# Let the DB start
python -m a8t_tools.db.wait_for_db

alembic upgrade head

exec "$@"