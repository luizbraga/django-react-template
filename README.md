## Base Django React Project

This is a simple Django React application based on my experience as a developer.
Suggestions and feedbacks are welcome!

The main idea is to use Django Rest Framework (DRF) as a backend supply for the React.

### Running

Assuming you have installed Python 3.6.5, Node 10.x, run the following commands:

* Python:
`$ pip install -r requirements/local.txt`
`$ python manage.py runserver 0.0.0.0:8000`

* Node:
`$ npm install`
`$ npm run dev`
`$ npm run start`

Also, it is possible to change the database URI in `docker/environ`.

### Running with DOCKER

In development environment this project will work using containers.
* Install [Docker](https://www.docker.com/products/overview) and [Docker Compose](https://docs.docker.com/compose/install/).
* `$ docker-compose build`
* `$ docker-compose up`
