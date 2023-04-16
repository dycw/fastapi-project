# FastAPI project

Example [FastAPI](https://fastapi.tiangolo.com/) project

## Set up

### Heroku

1. Create app:

   ```bash
   heroku create
   heroku container:login
   export APP=infinite-shore-17009
   ```

1. Test:

   ```bash
   # just heroku-create
   heroku addons:create heroku-postgresql:mini --app "$APP"

   # just heroku-build
   docker build -f project/Dockerfile.prod -t "registry.heroku.com/$APP/web" ./src

   # just heroku-run
   docker run --name app -e PORT=8765 -e APP_ENVIRONMENT=production -p 5003:8765 "registry.heroku.com/$APP/web":latest
   ```

1. Remove:

   ```bash
   # just prod-rm
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

1. Add secret `HEROKU_AUTH_TOKEN` from below, update `HEROKU_APP_NAME` in
   GitHub Actions:

   ```bash
   heroku auth:token
   ```
