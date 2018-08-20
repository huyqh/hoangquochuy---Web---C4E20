from flask import Flask, render_template
import mlab
from mongoengine import*
from models.service import Service
from models.customer import Customer
app = Flask(__name__)

mlab.connect()
# design pattern (MVC, MVP,...)
# design database

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/search/<g>")
def search(g):

    all_service = Service.objects(gender=g, yob__gte=18, height__gte=165, address__icontains="Hà Nội")
    return render_template("search.html", all_service = all_service)


@app.route("/customer")
def customer():
    all_customer = Customer.objects()
    return render_template("customer.html", all_customer = all_customer)




if __name__ == "__main__":
  app.run(debug=True)
 