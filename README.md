# ICD DISEASE CLASSIFICATION MANAGEMENT API

An api for managing a datastore of ICD disease classifications. The API is built using python, django and the django rest framework (DRF)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. Python 3 - (This can be downloaded and installed using a package installer like brew on mac (brew install python) or directly from the python webiste at https://www.python.org/downloads/)
2. Docker - (Instructions on how to install can be found here https://docs.docker.com/install/)

### Get Up and running

Once the prerequisites are met, The following steps can be used to get the application up and running. All commands are run from the root directory of the project

1. Build the docker image

```
docker build .
```

2. Build additional docker configuration in docker compose file

```
docker-compose build
```

3. Run database migrations

```
docker-compose run app sh -c "python manage.py makemigrations"
```

```
docker-compose run app sh -c "python manage.py migrate"
```

4. Load initial database into postgres database from diagnosis_codes.csv in the app directory

```
docker-compose run app sh -c "python manage.py load_initial_data_to_db"
```

5. Run the application using

```
docker-compose up
```

The API root can be accessed locally from http://127.0.0.1:8000/api/disease-classification

HTTP Operations can be run on http://127.0.0.1:8000/api/disease-classification/diagnosis

## Running the tests

This application includes test for Retrieving with pagination constraints, Deleting, Updating and Adding a Resource (ICD diagnosis code).

The tests can be run using

```
docker-compose run app sh -c "python manage.py test && flake8"
```

## Built With

- [django](https://www.djangoproject.com/) - The web framework used

## Authors

- **Tsatsu Adogla-Bessa Jnr**
