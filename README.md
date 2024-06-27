# Propiedades test

Create a new file with name .env in the root project and copy the content .env.template

To build and deploy your application for the first time, run the following in your shell:

```bash
docker-compose up --build
```
## Run Docker
```bash
docker-compose up
```

You can use  

make migrations:

```bash
docker-compose run --rm web python manage.py makemigrations
docker-compose run --rm web python manage.py migrate
```

rebuild:
```bash
docker-compose up -d --build
```

```

## Run unit test
```bash
docker-compose run --rm web pytest
```