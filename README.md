# jobPlatformPortal
A platform listing jobs from various company career pages


## Requirements
- Python3
- Pipenv
- Postgres with a database named `job_portal`


## How to get started

For local development, run the following:

```
pipenv install
pipenv shell

python manage.py migrate
python manage.py runserver
# Loads the site at http://127.0.0.1:8000
```

We can also add a sample job offer by running the following command:
```
python manage.py populate_db
```
