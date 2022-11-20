# Video Resizer

This is a simple Django project to resize videos to a specific size. It uses ffmpeg to do the resizing.

## Requirements

- ffmpeg
- poetry
- docker and docker-compose (optional)

## Development

There are two ways to run this project. You can either use poetry to run it or you can use docker.

### 1. Using Poetry

### Installation

First of all you need to set the environment variables. You can do this by duplicating the `.env.example` file and renaming it to `.env`. Then you can set the variables in the `.env` file.

```bash
cp .env.example .env
nano .env
```

Then you need to install the dependencies.

```bash
poetry install
```

### Running

And finally you can run the project.

```bash
poetry run python manage.py migrate
poetry run python manage.py runserver
```

Now the project should be up and running on [http://localhost:8000](http://localhost:8000).


You can create a super user to access [Django admin panel]:(http://localhost:8000/admin)

```bash
poetry run python manage.py createsuperuser
```

Now in another terminal, let's run celery:
```bash
poetry run python -m celery -A video_resizer worker
```


### 2. Docker

### Installation

For this method you also need to see the appropriate environment variables in the `.env.docker.example` and `.env.db.example` files and set them in the `.env.docker` and `.env.db` files.

Although you should be good to go with the default values.

```bash
cp .env.docker.example .env.docker
cp .env.db.example .env.db

nano .env.docker
nano .env.db
```

### Running

And now let's run the project using `docker-compose`.

```bash
docker-compose up -d
```

Let's do the migrations too:
```bash
docker-compose exec app poetry run python manage.py migrate
```

Also if you need to create a superuser:
```bash
docker-compose exec app poetry run python manage.py createsuperuser
```


## Testing

You can find the test cases in `video/tests.py`.

In order to run the tests in local development:
```bash
poetry run python manage.py test
```

and in docker environment:
```bash
docker-compose exec app poetry run python manage.py test
```