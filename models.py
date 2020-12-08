# https://git.generalassemb.ly/prudential-0921/flask-intro-get-post
# import * means import everything from peewee
from peewee import *
import datetime

# Connect to a Postgres database.
DATABASE = PostgresqlDatabase('flask_muse_app', host='localhost', port=5432)

#schema
class Song(Model):
    title = CharField()
    artist = CharField()
    album = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Song], safe=True)
    print("TABLES Created")
    DATABASE.close()