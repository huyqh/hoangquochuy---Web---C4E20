from mongoengine import*
class Customer(Document):
    name = StringField()
    gender = IntField()
    job = StringField()
    email = EmailField()
    job = StringField()
    company = StringField()
    phone_number = StringField()
    status = BooleanField()
    