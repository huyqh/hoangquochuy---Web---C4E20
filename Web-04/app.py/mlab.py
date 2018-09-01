import mongoengine

# mongodb://cms:<adminc4e20@ds233228.mlab.com:33228/cms

host = "ds233228.mlab.com"
port = 33228
db_name = "cms"
user_name = "admin"
password = "adminc4e20"


def connect():
    mongoengine.connect(db_name, 
                        host=host, 
                        port=port, 
                        username=user_name, 
                        password=password
                    )

