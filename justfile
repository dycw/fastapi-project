alias t := test

set dotenv-load := true
set export := true
set positional-arguments := true

#### local ####################################################################

black:
  docker compose exec web python -m black --check .

db-migrate:
  docker compose exec web aerich migrate

db-upgrade:
  docker compose exec web aerich upgrade

down:
  docker compose down

lint:
  docker compose exec web python -m black . --check && python -m ruff .

logs-web:
  docker compose logs web

psql:
  docker compose exec web-db psql -U postgres

@ruff *args='.':
  docker compose exec web python -m ruff "$@"

@test *args='.':
  docker compose exec web python -m pytest "$@"

@test-cov *args='.':
  docker compose exec web python -m pytest "$@" --cov="."

up:
  docker compose up -d --build

#### production ###############################################################

prod-build:
  docker build -f src/Dockerfile.prod -t web ./src

prod-rm:
  docker rm app -f

#### heroku ###################################################################

APP := "infinite-shore-17009"

heroku-build:
  docker build -f src/Dockerfile.prod -t "registry.heroku.com/$APP/web" ./src

heroku-create:
  heroku addons:create heroku-postgresql:mini --app "$APP"

heroku-run:
  docker run --name app -e PORT=8765 -e DATABASE_URL=sqlite://sqlite.db \
    -p 5003:8765 registry.heroku.com/$APP/web:latest

heroku-push:
  docker push "registry.heroku.com/$APP/web:latest"

heroku-release:
  heroku container:release web --app "$APP"

heroku-migrate:
  heroku run aerich upgrade --app "$APP"

#### github ###################################################################

github-build:
  docker build -f src/Dockerfile.prod \
    -t ghcr.io/dycw/tutorial-test-driven-development-with-fastapi-and-docker/summarizer:latest \
    ./src

github-push:
  docker push ghcr.io/dycw/tutorial-test-driven-development-with-fastapi-and-docker/summarizer:latest
