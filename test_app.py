import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movies, Actors


class CastingAgencyTestCase(unittest.TestCase):
    # Class represents the  Casting Agency Test Case.

    def setUp(self):
        # Define test variables & initialise the app.

        self.ASSISTANT_TOKEN ='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5MZEpKX3dPMXdUNUMxN1FQb1RaOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tb3dlYnNpdGUudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxNTczM2YyY2FjMzdmMDA2ODQ0MjEzMyIsImF1ZCI6IkNhc3RpbmdBZ2VuY3kiLCJpYXQiOjE2MzMzMTAwMDcsImV4cCI6MTYzMzM5NjQwNywiYXpwIjoiQXl5UFRFMFhzb3F3Sld5eWpiWXh5eVR5SlYwMjBjZHYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.KLwV96RfKqRM_h7-NThmwPewjF3uuWPrKEBS14cVkvIE0Lg7kJJfE83AOC9p6okaL0Fh7SWneGtxBOHWK48WGj4RRRGyCja6ii9iod0MZ5XfM5Ff-nFATvSZTkfXoqaQyUCedFCklj0OP0bxcATEldWpjrx4p8UCfqrlktcyGiGdj_9mXbt8_6zDfxqpRgy3IxDxN1dbG-36nT2vxyGkuAdviHq4A9XXJePOqOMuH9C3sdP0vyFXDSRYLaLegAxDlAeGteo-oFQjWMYCwMezZrmqxl7axQ2fb5dGFXlHSVPlYIV9B05jTbhjfxjiexLiJ8dwsTfaompigAc1Zqck5g'
        self.DIRECTOR_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5MZEpKX3dPMXdUNUMxN1FQb1RaOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tb3dlYnNpdGUudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxNTczNDRjY2FjMzdmMDA2ODQ0MjE1OCIsImF1ZCI6IkNhc3RpbmdBZ2VuY3kiLCJpYXQiOjE2MzMzMDk3NTEsImV4cCI6MTYzMzM5NjE1MSwiYXpwIjoiQXl5UFRFMFhzb3F3Sld5eWpiWXh5eVR5SlYwMjBjZHYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.xUOVO3JEpsYl-UO8yRm6Kn4WSAppp-UyJwbR_a7jfWbM1e-_GN8N7o98B_0ci7VPk4NRc5RTM7XShiXO7dqgrMWUK6HnJNmaL5s1rBkGYe5-gFg86eMrwgUalzV7YV-ZS_CARADr-L6lQVX7yVBLk40WUT-Ow6mhCkLCQsb6yC5QXf6G9BQH0t3PJVHxzTJInB0FhRmvDu-xNrbeLYGLRt2WCFtJx_algT7zkerMa1XcmRV11M7OCdlLOzhTmG3mP6zDM1dSiF0Q2j6pv_g9of38LirrdjnN2I0FY9GAAtfiEoc8gLJgSATlWqr42Ge9fx3yP3HBbukPfY-2sPQfPw'
        self.PRODUCER_TOKEN ='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5MZEpKX3dPMXdUNUMxN1FQb1RaOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tb3dlYnNpdGUudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxNTczNGE5MWUzOGQ5MDA2ODU5OTA5NyIsImF1ZCI6IkNhc3RpbmdBZ2VuY3kiLCJpYXQiOjE2MzMxODAyNTMsImV4cCI6MTYzMzI2NjY1MywiYXpwIjoiQXl5UFRFMFhzb3F3Sld5eWpiWXh5eVR5SlYwMjBjZHYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOm1vdmllcyIsInBvc3Q6bW92aWVzIl19.uKuH9x88lI9PcYPFQvFmCc-EtjL2inG_vr2Pml2uL7DpOiH9a9BQ5XCPOccy7l57snT9iQQIzqWwXQnQlfXlFcwmE6DWQFn5Je5krraE0kjmF6WFVimQyq25FCC8yhAA7m90Ce4LiZvn4R-nDmPYvQHnZLw0jX61lH7-SlCdLQsTO0sRY5QdhcOShQNK9FXHvhw9hkwm3fY4yRY2lnzharN8TY8pNrqo0yKzgbY1Y6N_Iplh2nmLlzOpEQ2Wvbh_vIMs1d1CaONogY1k7FrHBo1x3VSLxptDhJPVyBcc997NTkRSNA7iidqM5lB-yTQPIk5TbOyb-0B02FaaEHBtDw'

        self.token_assistant = {'Content-Type': 'application/json',
                                'Authorization': 'Bearer {}'.format(self.ASSISTANT_TOKEN)}
        self.token_director = {'Content-Type': 'application/json',
                               'Authorization': 'Bearer {}'.format(self.DIRECTOR_TOKEN)}
        self.token_producer = {'Content-Type': 'application/json',
                               'Authorization': 'Bearer {}'.format(self.PRODUCER_TOKEN)}
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            'postgres', 'adeoluwa', 'localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)

        # Binds the app to the current context.
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # Create all tables.
            self.db.create_all()

    def tearDown(self):
        # Executed after each test.
        pass

    # Movie endpoints.
    # Test created for retrieve_movies.
    def test_retrieve_movies(self):
        movie = Movies(title='Ghost', release_date='08-12-1995')
        movie.insert()
        res = self.client().get('/movies', headers=self.token_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # Test created for retrieve_movies failure.
    def test_retrieve_movies_fail(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    # Test created for post_movie.
    def test_add_movie(self):
        res = self.client().post('/movies', headers=self.token_producer,
                                 json={'title': 'Sex Education', 'release_date': '01-11-2019'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    # Test created for post_movie failure.
    def test_add_movie_failure(self):
        res = self.client().post('/movies', headers=self.token_assistant,
                                 json={'title': 'Sex Education', 'release_date': '01-11-2019'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    # Test created for edit_movie
    def test_update_movie(self):
        movie = Movies(title='Hoax', release_date='27-12-77')
        movie.insert()
        movie_id = movie.id
        res = self.client().patch('/movies/'+str(movie_id) + '', headers=self.token_director,
                                  json={'title': 'New Add Movie', 'release_date': '27-12-1977'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    # Test created for edit_movie failure.
    def test_update_movie_failure(self):
        movie = Movies(title='New Movieee',
                       release_date='20-05-1980')
        movie.insert()
        movie_id = movie.id
        res = self.client().patch('/movies/'+str(movie_id) + '', headers=self.token_assistant,
                                  json={'title': 'Spirit', 'release_date': '02-06-1983'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    # Test created for delete_movie.
    def test_delete_movie(self):
        movie = Movies(title='Akira', release_date='25-01-1988')
        movie.insert()
        movie_id = movie.id
        res = self.client().delete('/movies/'+str(movie_id) +
                                   '', headers=self.token_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    # Test for delete_movie failure.
    def test_delete_movie_failure(self):
        res = self.client().delete('/movies/3534', headers=self.token_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # Actor Endpoints
    # Test created for retrieve_actors.
    def test_retrieve_actors(self):
        actor = Actors(name='Arnold', age=57, gender='Male')
        actor.insert()
        res = self.client().get('/actors', headers=self.token_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # Test created for retrieve_actors failure.
    def test_retrieve_actors_fail(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    # Test created for post_actor.
    def test_add_actor(self):
        res = self.client().post('/actors', headers=self.token_producer,
                                 json={'name': 'Femi Bello', 'age': 31, 'gender': 'Male'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    # Test created for post_actor failure.
    def test_add_actor_failure(self):
        res = self.client().post('/actors', headers=self.token_assistant,json={'name': 'Omobolaji', 'age': 61, 'gender': 'Male'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        #self.assertTrue(data['actor'])


    # Test created for edit_actor
    def test_update_actor(self):
        actor = Actors(name='Scarlett Johansson', age=31, gender='Male')
        actor.insert()
        actor_id = actor.id
        res = self.client().patch('/actors/'+str(actor_id) + '', headers=self.token_director,
                                  json={'name': 'Femi Bello', 'age': 36, 'gender': 'Female'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    # Test created for edit_actor failure.
    def test_update_actor_failure(self):
        actor = Actors(name='Harrison Ford', age=79, gender='male')
        actor.insert()
        actor_id = actor.id
        res = self.client().patch('/actors/'+str(actor_id) + '', headers=self.token_assistant,
                                  json={'name': 'Harry Ford', 'age': 79, 'gender': 'Female'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    # Test created for delete_actor.
    def test_delete_actor(self):
        actor = Actors(name='Sholaowale Toyin', age=67, gender='Female')
        actor.insert()
        actor_id = actor.id
        res = self.client().delete('/actors/'+str(actor_id) +
                                   '', headers=self.token_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    # Test for delete_actor failure.
    def test_delete_actor_failure(self):
        res = self.client().delete('/actors/1034', headers=self.token_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


if __name__ == "__main__":
    unittest.main()
