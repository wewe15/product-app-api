# products-web-app

## Project SetUp

- Install Python 3.8
- Install [docker](https://www.docker.com/products/docker-desktop).
- Install [docker-compose](https://docs.docker.com/compose/).
- Clone the project using git.
- Go to project files.
- Run `docker-compose up -d --build` to run the db container `-d` run into detached mode.
- Apply the migrations `docker-compose exec web python manage.py migrate`.
- Visit the project on this URL: [localhost:8000/api/product](http://localhost:8000/api/product)
- You should see the project running without any problems.
