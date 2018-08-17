
from flask import Flask
app = Flask(__name__)
@app.route("/BMI/<int:weight>/<int:high>/")
def BMI(weight, high):
    BMI = (weight * 10000) / (high * high)
    if BMI < 16 : 
        print =  "Severely underweight"
    elif BMI < 18.5: 
        print = "Underweight"
    elif BMI < 25: 
        print = "Normal"
    elif BMI < 30: 
        print = "Overweight"
    else :
        print = "Obese"
    return "Your BMI : {} and {}".format(BMI,print)

if __name__ == "__main__":
  app.run(debug=True)
 