from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#Establish appropriate relationships within the models whereever needed.
# Define Album Model below with id, album_name, artist_id(Foreign key)
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(100), index=True)
    album = db.relationship(
        'Album',
        backref='artist',
        lazy=True,
        uselist=True
    )

    def __init__(self, artist_name):
        self.artist_name = artist_name

    def __repr__(self):
        return "<Artist '{}'>".format(self.artist_name)
# Define Artist model below with fields id, artist_name
class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    album_name = db.Column(db.String(100), index=True)
    artist_id = db.Column(db.Integer(), db.ForeignKey('artist.id'), nullable=False)

    track = db.relationship(
        'Track',
        backref='album',
        lazy=True,
        uselist=True
    )

    def __init__(self, album_name,artist_id):
        self.album_name = album_name
        self.artist_id=artist_id
    def __repr__(self):
        return "<Album '{}'>".format(self.album_name)

# Define Track Model below with fields id, track_name, track_time, album_id(Foreign key)
class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_name = db.Column(db.String(100), index=True)
    track_time = db.Column(db.Integer, index=True)
    album_id = db.Column(db.Integer(), db.ForeignKey('album.id'), nullable=False)
    def __init__(self, track_name,track_time,album_id):
        self.track_name = track_name
        self.track_name = track_name
        self.album_id = album_id
    def __repr__(self):
        return "<Track '{}'>".format(self.track_name)