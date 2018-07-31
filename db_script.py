# create_engine: database engine
# column: represents a table column
# Integer: integer datatype
# String: string datatype
# Datetime: datetime datatype
# Text: text datatype
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
# Constructs a base class for declarative class definitions
from sqlalchemy.ext.declarative import declarative_base
# The ORM’s “handle” to the database
from sqlalchemy.orm import sessionmaker
from datetime import datetime


# Connect to the database and create an engine for the\
# SLQAlchemy app
db_eng = create_engine('sqlite:///tweets_db.db', echo=True)

# Classes mapped using the Declarative system are defined in\
# terms of a base class which maintains a catalog of classes\
# and tables relative to that base - this is known as the\
# declarative base class.
Base = declarative_base()

# Bind the Session objects to the created engine
Session = sessionmaker(bind=db_eng)

# Create a new session
session = Session()


class Tweets(Base):
    """
    A class to create the tweets table in the database.

    ...

    Attributes
    ----------
    id : sqlalchemy.orm.attributes.InstrumentedAttribute
        The id column of the tweets table.
    tweet_text : sqlalchemy.orm.attributes.InstrumentedAttribute
        The tweet_text column of the tweets table.
    source : sqlalchemy.orm.attributes.InstrumentedAttribute
        The source column of the of tweets table.
    date_posted : sqlalchemy.orm.attributes.InstrumentedAttribute
        The date_posted column of the tweets table.

    Methods
    -------
    repr()
        Creates the string output for when a table row is printed.
    """
    
    # Set the table name
    __tablename__ = 'tweets'

    # Create an "id" column of the Integer type, which is\
    # the primary key for the table. Because it is called "id"\
    # and is the primary key, it will also be auto incrementing
    id = Column(Integer, primary_key=True)
    # Create a "tweet_text" column of the String type. Each\
    # field takes only 240 characters, must be unique and can't\
    # be null
    tweet_text = Column(String(240), unique=True, nullable=False)
    # Create a column called "source" of the String type. The fields\
    # can't be null
    source = Column(String(50), nullable=False)
    # Create a column called "date_posted" of the DateTime type. The\
    # fields can't be null
    date_posted = Column(DateTime, nullable=False)

    def __repr__(self):
        '''
        When printing a row of this table, it will look like:
        tweet_source, tweet_date_posted: tweet_text
        '''
        return f"{self.source}, '{self.date_posted}': {self.tweet_text}"


def update_db(session, text, text_source, date):
    '''
    Create a tweets table row using the passed arguments 
    to this function. Only commit the changes if the tweet
    is not a duplicate.

    
    Parameters
    ----------
    session : sqlalchemy.orm.session.Session
        A database session.
    text : str
        The URL for the image to download.
    text_source : str
        The name to use for the saved image.
    date : datetime.datetime
        The date and time of the tweet being created.

    Returns
    -------
    None
    '''

    # Check if the tweet already exists in the database
    # If the tweet already exists than do nothing
    if session.query(Tweets).filter_by(tweet_text=text).first():
        return False

    # If it doesn't exist save it in the database
    else:
        # Create three tweets and add them to the "staging area"
        tweet = Tweets(tweet_text=text, source=text_source, date_posted=date)
        session.add(tweet)

        # Commit the changes to the dabatase
        session.commit()
        return True
    

    # session.query(Tweets).filter_by(tweet_text='text').first()


if __name__ == "__main__":

    # Create three tweets and add them to the "staging area"
    tweet = Tweets(tweet_text='Tweet1', source='Source1', date_posted=datetime.now())
    session.add(tweet)
    tweet = Tweets(tweet_text='Tweet2', source='Source1', date_posted=datetime.now())
    session.add(tweet)
    tweet = Tweets(tweet_text='Tweet3', source='Source2', date_posted=datetime.now())
    session.add(tweet)

    # Commit the changes to the dabatase
    session.commit()

'''
Useful commands:

    Base.metadata.create_all(db_eng) -> create all tables
    Base.metadata.drop_all(db_eng) -> delete all tables
    session.query(<table_name>) -> SELECT * FROM <table_name>
    session.query(<table_name>).filter_by(<column>=<value>)->
SELECT * FROM <table_name> WHERE <column> = <value>
    list(session.query(<table_name>)) -> Make a list of all
tweets a table has
    session.query(<table_name>).first() -> Get just the first
tweet of a result-set
'''