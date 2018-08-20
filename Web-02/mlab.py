import mongoengine

# mongodb://admin:adminc4e20@ds125932.mlab.com:25932/muadongkhonglanh

host = "ds125932.mlab.com"
port = 25932
db_name = "muadongkhonglanh"
user_name = "admin"
password = "adminc4e20"


def connect():
    mongoengine.connect(db_name, 
                        host=host, 
                        port=port, 
                        username=user_name, 
                        password=password
                    )

