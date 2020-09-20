from flask_testing import TestCase
#from flask import current_app
from myflaskproj import app
import os
#from myflaskproj.tests import BaseTestCase
from myflaskproj.models import db, Artist, Album, Track

class BaseTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['BASE_DIR'] = os.path.dirname(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myflaskproj_test.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return app
        
    @classmethod
    def setUp(cls):
            db.create_all()
            a1 = Artist(artist_name='Artist1')
            a2 = Artist(artist_name='Artist2')
            alb1 = Album(album_name='Album1', artist_id=1)
            #alb1.atrist = a1
            
            alb2 = Album(album_name='Album2', artist_id=2)
            #alb2.artist = a2
            t1 = Track(track_name='Track1', track_time=46, album_id=1)
            t2 = Track(track_name='Track2', track_time=61, album_id=1)
            t3 = Track(track_name='Track3', track_time=53, album_id=1)

            t4 = Track(track_name='Track4', track_time=72, album_id=2)
            t5 = Track(track_name='Track5', track_time=56, album_id=2)
            
            #t1.album = alb1
            #t2.album = alb1
            #t3.album = alb1
            #t4.album = alb2
            #t5.album = alb2
            db.session.add(t1)
            db.session.add(t2)
            db.session.add(t3)
            db.session.add(t4)
            db.session.add(t5)
            db.session.add(alb1)
            db.session.add(alb2)
            db.session.add(a1)
            db.session.add(a2)
            db.session.commit()
    
    @classmethod
    def tearDown(cls):
        db.drop_all()
        

class TestSample(BaseTestCase):
    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'<h1>Welcome to MyFlaskProj </h1>')
        
    
    def test_artist_count(self):
        c = Artist.query.all()
        self.assertEqual(2, len(c))

    def test_album_test(self):
        c = Album.query.all()
        self.assertEqual(2, len(c))

    def test_track_count(self):
        c = Track.query.all()
        self.assertEqual(5, len(c))

    def test_schema_artist(self):
        content = Artist.__table__.columns.keys()
        self.assertEqual(len(content), 2)
        self.assertEqual('id', content[0])
        self.assertEqual('artist_name', content[1])

    def test_schema_album(self):
        content = Album.__table__.columns.keys()
        self.assertEqual(len(content), 3)
        self.assertEqual('id', content[0])
        self.assertEqual('album_name', content[1])
        self.assertEqual('artist_id', content[2])

    def test_schema_track(self):
        content = Track.__table__.columns.keys()
        self.assertEqual(len(content), 4)
        self.assertEqual('id', content[0])
        self.assertEqual('track_name', content[1])
        self.assertEqual('track_time', content[2])
        self.assertEqual('album_id', content[3])
        
        
        
