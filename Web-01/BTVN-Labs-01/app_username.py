from flask import Flask, render_template
app = Flask(__name__)


@app.route("/user/<username>/")
def username(username):
    usernames = {
        "huy" : {
            "name" : "huy",
            "age"  : 20,
            "auther_sex" : "male",
            "hobbit" : "gym"
        } 
        ,
        "vinh" : {
            "name" : "vinh",
            "age"  : 21,
            "auther_sex" : "male",
            "hobbit" : "watching movie"   
        }
        ,
        "minh phuong" : {
            "name" : "minh phuong",
            "age"  : 21,
            "auther_sex" : "female",
            "hobbit" : "go to trip"
        }
    }
    if username in users:
        return render_template("username.html", username = usernames[username])
    else:
        return "User not found"
    

if __name__ == "__main__":
  app.run(debug=True)
 