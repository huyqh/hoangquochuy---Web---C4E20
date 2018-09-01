from models.user import User
import mlab

mlab.connect()



user = User(    
    name = input("Họ và tên đầy đủ:"),
    email = input("Email:"),
    username = input("Username:"),
    password = input("Password:")
)
user.save()
 