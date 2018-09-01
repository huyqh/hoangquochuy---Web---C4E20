from mongoengine import*

class Video(Document):
    title = StringField()
    views = IntField()
    thumbnail = StringField()
    youtube_id = StringField()
    link = StringField()