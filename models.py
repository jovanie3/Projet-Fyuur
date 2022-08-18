from sqlalchemy import Column, String, Integer, Boolean, DateTime, ARRAY, ForeignKey
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# TODO: connect to a local postgresql database
def db_setup(app):
    db.app = app
    db.init_app(app)
    return db

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    description = db.Column(db.String(500))
    seeking_talent = db.Column(Boolean, default=False)
    website = db.Column(String(120))
    genres = db.Column(ARRAY(String))
    shows = db.relationship('Show', backref='Venue', lazy='True')

    def __init__(self, id, name, genres, address, city, state, phone, website, facebook_link, image_link,
                 seeking_talent=False, description=""):
        self.id = id
        self.name = name
        self.genres = genres
        self.city = city
        self.state = state
        self.address = address
        self.phone = phone
        self.image_link = image_link
        self.facebook_link = facebook_link
        self.website = website
        self.description = description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
  
    def short(self):
        return{
            'id':self.id,
            'name':self.name,
        }
    
    def long(self):
        print(self)
        return{
            'id' :self.id,
            'name' :self.name,
            'city' : self.city,
            'state' :self.state,
        }
    
    def detail(self):
        return{
            'id' :self.id,
            'name' :self.name,
            'genres' : self.genres,
            'address' :self.address,
            'city' :self.city,
            'phone' :self.phone,
            'website' :self.website,
            'facebook_link':self.facebook_link,
            'seeking_talent' :self.seeking_talent,
            'description' :self.description,
            'image-link' :self.image_link
        }

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artists'
    

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(120))
    website = db.Column(db.String(120))
    shows = db.relationship('Show', backref='Artist', lazy=True)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

    def __init__(self, id, name, genres, city, state, phone, image_link, website, facebook_link,
                 seeking_venue=False, seeking_description=""):
        self.id = id
        self.name = name
        self.genres = genres
        self.city = city
        self.state = state
        self.phone = phone
        self.website = website
        self.facebook_link = facebook_link
        self.seeking_description = seeking_description
        self.image_link = image_link
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def short(self):
        return{
            'id': self.id,
            'name':self.name,
        }
    
    def details(self):
        return{
            'id': self.id,
            'name': self.name,
            'genres': self.genres,
            'city': self.city,
            'state':self.state,
            'phone': self.phone,
            'website': self.website,
            'facebook_link': self.facebook_link,
            'seeking_venue': self.seeking_venue,
            'seeking_description': self.seeking_description,
            'image_link': self.image_link,

        }

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.



class Show(db.Model):

    __tablename__ = 'shows'
    id = db.Column(Integer,primary_key=True, autoincrement=True)
    venues_id = db.Column(Integer, db.ForeignKey("venues.id"), nullable=False)
    artists_id = db.Column(Integer, db.ForeignKey("artists.id"), nullable=False)
    start_time = db.Column(String(), nullable=False)


    def __init__(self, venues_id,artists_id,start_time):
        self.venues_id = venues_id
        self.artists_id = artists_id
        self.start_time = start_time

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def detail(self):
        return{
            'venues_id' :self.venues_id,
            'venues_name' :self.Venue.name,
            'artists_id' :self.artists_id,
            'artists_name' :self.Artist.name,
            'artists_image_link' :self.Artist.image_link,
            'start_time' :self.start_time
        }

    def artists_details(self):
        return{
            'artists_id' :self.artists_id,
            'artists_name' :self.Artist.name,
            'artists_image_link' :self.Artist.image_link,
            'start_time' :self.start_time

        }
 
    
    def venues_details(self):
        return{
            'venues_id' :self.venues_id,
            'venues_name' :self.Venue.name,
            'venues_image_link' :self.Venue.image_link,
            'start_time' :self.start_time
            
        }

        
  


 




