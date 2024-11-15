# FastAPI Media Uploader Service

A microservice for handling media file uploads (photos, videos, audio) using FastAPI and S3 storage.

## Run Locally

### Run with Docker Compose

> :warning: **Linux Users**: You may need to use the `sudo` command with `docker-compose` if your user is not in the `docker` group.

> :warning: **Windows Users**: Ensure your `git config core.autocrlf` is set to `false` before starting, as builds/runs might fail if this setting is enabled.

```shell script
	make run
```

or

```shell script
	cp .env.example .env
	cp ./deploy/compose/local/docker-compose.yml docker-compose.yml
	docker-compose up -d
```

### Useful Tips

- use http://localhost to access web UI
- use http://rabbitmq.localhost to access rabbitmq dashboard (see credentials in .env or .env.example)
- use `make logs` to see logs
