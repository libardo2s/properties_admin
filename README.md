# Propiedades Admin

Create a new file with name .env in the root project and copy the content .env.template

To build and deploy your application for the first time, run the following in your shell:

To build and run the project run this command in the root path the project
```bash
docker-compose up --build

```
To run project aready build
```bash
docker-compose up
```

Migration run automatically to build project but you can run aditional migrations with this commands

```bash
docker-compose run --rm web python manage.py makemigrations
docker-compose run --rm web python manage.py migrate
```
To connect to the data base use pg_admin with the credentials in the .env file 