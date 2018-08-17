from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/about_me")
def about_me():
    about_me = {
            "name" : "Hoàng Quốc Huy",
            "work": "student",
            "school": 'Bach Khoa University',
            "hobbit": "gym"
    }
    return render_template("about_me.html", about_me = about_me)

@app.route("/school")
def school():
    return redirect("http://techkids.vn")

if __name__ == "__main__":
  app.run(debug=True)