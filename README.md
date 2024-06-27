# Propiedades test

To build and deploy your application for the first time, run the following in your shell:

```bash
docker-compose build
```
## Run Docker
```bash
docker-compose up
```
make migrations:

```bash
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```

Create super user:
```bash
docker-compose run web python manage.py createsuperuser
```

rebuild:
```bash
docker-compose up -d --build
```

```

## Run unit test
```bash
docker-compose run web pytest
```