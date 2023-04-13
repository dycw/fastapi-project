# FastAPI project

Example [FastAPI](https://fastapi.tiangolo.com/) project

## Set up

### Heroku

1. Create app:

   ```bash
   heroku create
   heroku container:login
   export APP=sheltered-falls-06080
   ```

1. Test:

   ```bash
   heroku addons:create heroku-postgresql:mini --app "$APP"

   # just heroku-build
   docker build -f project/Dockerfile.prod -t "registry.heroku.com/$APP/web" ./src

   # just heroku-run
   docker run --name fastapi-project -e PORT=8765 -e DATABASE_URL=sqlite://sqlite.db -p 5003:8765 "registry.heroku.com/$APP/web":latest
   ```

1. Remove:

   ```bash
   # just docker-rm
   docker rm app -f
   ```

1. Push, release and migrate:

   ```bash
   # just heroku-push
   docker push "registry.heroku.com/$APP/web:latest"

   # just heroku-release
   heroku container:release web --app "$APP"

   # just heroku-migrate
   heroku run aerich upgrade --app "$APP"
   ```

1. Personal access token (`workflow`, `write:packages` and `delete:packages`), build, tag:

   ```bash
   export TOKEN=
   export USER=dycw
   export REPO=fastapi-project

   # just github-build
   docker build -f src/Dockerfile.prod -t "ghcr.io/$USER/$REPO/summarizer:latest" ./src

   docker login ghcr.io -u "$USER" -p "$TOKEN"

   # just github-push
   docker push "ghcr.io/$USER/$REPO/summarizer:latest"
   ```

1. Add secret `HEROKU_AUTH_TOKEN`:

   ```bash
   heroku auth:token
   ```
