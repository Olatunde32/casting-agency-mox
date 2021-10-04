# Casting Agency

## Introduction

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. Executive Producer within the company is saddled with the responsibility to create a system to simplify and streamline processes within the company.

This is a capstone project for Udacity's Full-Stack Developer Nanodegree I undertook to use the concepts and the skills I learnt during the duration of my Nanodegree's program.

## Getting Started

### Base URL

You can run the app locally or in Heroku:

- Locally: http://127.0.0.1:5000/
- Heroku: https://casting-agency-app-mox.herokuapp.com/

### Installing Dependencies

Python 3.9
Follow instructions to install the latest version of python here (https://docs.python.org/3/)

PIP Dependencies
Install dependencies by running:
`pip install -r requirements.txt`

This will install all of the required packages within the requirements.txt file.

_All needed variables are saved in setup.sh_ and .env

### Run the server locally:

Create a local database using postgresql, run the following:

```
Update the postgresql connection strings in the models appropriately
```

Then run the app using this command:
`set FLASK_APP=app.py`
`set FLASK_ENV=development`
`flask run`

### Authentication:

I used Auth0 tokens for the authentication. There are three roles for the casting agency:

**Casting Assistant**

- Can view actors and movies

**Casting Director**

- Can view actors and movies

- Add or delete an actor from the database

- Modify actors or movies

**Executive Producer**

- Can view actors and movies

- Add or delete an actor from the database

- Modify actors or movies

- Add or delete a movie from the database

## Test

You can test the app by running the test_app.py or using Postman collection.

## Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error": 404,
    "message": "Resource Not Found"
}
```

### Error Types and Messages

The Casting Agency app will return the below error types when requests fail:

- 404: Resource Not Found
- 422: Not Processable
- 405: Method Not Allowed
- 400: Bad Request
- 500: Internal Server Error

## Resource Endpoint Library

### GET '/movies'

- General
  - Fetches a dictionary of movies
  - Request Arguments: None
  - Returns: An object that contains movies array, and a success boolean value.
- Sample: `curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:5000/movies`

```
{
  "movies": [
    {
      "id": 1,
      "release_date": "25-01-1988",
      "title": "Akira"
    },
    {
      "id": 2,
      "release_date": "08-12-1995",
      "title": "Ghost"
    },
    {
      "id": 3,
      "release_date": "27-12-1977",
      "title": "Ajagbandi"
    },

  ],
  "success": true
}
```

### GET '/actors'

- General
  - Fetches a dictionary of actors
  - Request Arguments: None
  - Returns: An object that contains actors array, and a success boolean value.
- Sample: `curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:5000/actors`

```
{
  "actors": [
    [
      {
        "age": 67,
        "gender": "Female",
        "id": 1,
        "name": "Sholaowale Toyin"
      },
      {
        "age": 57,
        "gender": "Male",
        "id": 2,
        "name": "Arnold"
      },
      {
        "age": 36,
        "gender": "Female",
        "id": 3,
        "name": "Femi Bello"
      }
    ]
  ],
  "success": true
}
```

### POST '/movies'

- General
  - Creates a new movie
  - Request Arguments: None
  - Returns: An object that contains a success boolean value and the created movie.
- Sample: `curl http://127.0.0.1:5000/movies -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d "{\"title\":\"Akira\",\"release-date\":\"25-01-1988\"}"`

```
{
  "movie": {
    "id": 1,
    "release_date": "25-01-1988",
    "title": "Akira"
  },
  "success": true
}
```

### POST '/actors'

- General
  - Creates a new actor
  - Request Arguments: None
  - Returns: An object that contains a success boolean value and the created actor.
- Sample: `curl http://127.0.0.1:5000/actors -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d "{\"name\":\"Sholaowale Toyin\",\"age\":\"67\",\"gender\":\"Female\"}"`

```
{
  "actor": {
    "age": 67,
    "gender": "Female",
    "id": 1,
    "name": "Sholaowale Toyin"
  },
  "success": true
}
```

### PATCH '/movies/1'

- General
  - Updates the specified movie
  - Request Arguments: None
  - Returns: An object that contains a success boolean value and the updated movie.
- Sample: `curl http://127.0.0.1:5000/movies/1 -X PATCH -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d "{\"title\":\"New add Movie\"}"`

```
{
  "movie": {
    "id": 5,
    "release_date": "04/10/2021",
    "title": "New add Movie"
  },
  "success": true
}
```

### PATCH '/actors/1'

- General
  - Updates the specified actor
  - Request Arguments: None
  - Returns: An object that contains a success boolean value and the updated actor.
- Sample: `curl http://127.0.0.1:5000/actors/1 -X PATCH -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d "{\"name\":\"Any New Name\"}"`

```
{
  "actor": {
    "age": 67,
    "gender": "Male",
    "id": 5,
    "name": "Any New Name"
  },
  "success": true
}
```

### DELETE '/movies/2'

- Genreal
  - Removes the specified movie
  - Request Arguments: The movie's ID
  - Returns: An object than contains a success boolean value and the ID of the deleted movie.
- Sample: `curl -X DELETE -H "Authorization: Bearer $TOKEN" http://127.0.0.1:5000/movies/3`

```
{
  "deleted": 3,
  "success": true
}
```

### DELETE '/actors/3'

- Genreal
  - Removes the specified actor
  - Request Arguments: The actor's ID
  - Returns: An object than contains a success boolean value and the ID of the deleted actor.
- Sample: `curl -X DELETE -H "Authorization: Bearer $TOKEN" http://127.0.0.1:5000/actors/3`

```
{
  "deleted": 3,
  "success": true
}
```
