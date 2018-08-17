from flask import Flask, render_template
app = Flask(__name__)


@app.route("/user/<username>/")
def username(username):
    users = {
        "huy" : {
            "name" : "huy",
            "age"  : 20,
            "author_sex" : "male",
            "hobbit" : "gym"
        } 
        ,
        "vinh" : {
            "name" : "vinh",
            "age"  : 21,
            "author_sex" : "male",
            "hobbit" : "watching movie"   
        }
        ,
        "minh phuong" : {
            "name" : "minh phuong",
            "age"  : 21,
            "author_sex" : "female",
            "hobbit" : "go to trip"
        }
    }
    if username in users:
        return render_template("username.html", username = users[username])
    else:
        return "User not found"
    

if __name__ == "__main__":
  app.run(debug=True)
 