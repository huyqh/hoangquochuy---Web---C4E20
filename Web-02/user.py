from models.user import User
import mlab

mlab.connect()



new_user = User(    
    fullname = input("Họ và tên đầy đủ:"),
    email = input("Email:"),
    username = input("Username:"),
    password = input("Password:")
)
new_user.save()
 