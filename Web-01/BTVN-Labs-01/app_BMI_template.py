from flask import Flask, render_template
app = Flask(__name__)


@app.route("/BMI_template/<int:weight>/<int:high>")
def BMI_template(weight, high):
    BMI = (weight * 10000) / (high * high)
    return render_template("BMI.html", BMI = BMI)

if __name__ == "__main__":
  app.run(port=8000, debug=True)




