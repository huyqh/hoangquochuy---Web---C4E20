from flask import *
import mlab
from mongoengine import*
from models.service import Service
from models.customer import Customer
from models.user import User
app = Flask(__name__)

mlab.connect()
app.secret_key = "very very secret key"
# design pattern (MVC, MVP,...)
# design database

@app.route("/")
def index():
    return render_template("index.html")







@app.route("/search/<g>")
def search(g):
    all_service = Service.objects(gender=g)
    # all_service = Service.objects(gender=g, yob__gte=18, height__gte=165, address__icontains="Hà Nội")
    return render_template("search.html", all_service = all_service)


# @app.route("/customer")
# def customer():
#     all_customer = Customer.objects()
#     return render_template("customer.html", all_customer = all_customer)





@app.route("/admin")
def admin():
    all_service = Service.objects()
    return render_template("admin.html", all_service = all_service)







# all_delete
@app.route("/delete/<service_id>")
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
    
        service_to_delete.delete()
        return redirect(url_for("admin"))
    else:
        return "Service not found"






@app.route("/all_delete")  
def all_delete():
    service_to_delete = Service.objects()
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for("admin"))
    else:
        return "service not found"







@app.route("/new-service", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("new-service.html")

    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone = form["phone"]
        new_service = Service(
            name = name,
            yob = yob,
            phone = phone
        )
        new_service.save()
        return redirect(url_for("admin"))
    

# setdefault input value
# radio button


@app.route("/detail/<service_id>")
def detail(service_id):
    service = Service.objects.with_id(service_id)
    session["service"] = str(service.id)
    if "loggedin" in session:
        if session["loggedin"] == True:
            if service is not None:
                return render_template("detail.html", service = service)
            else:
                return "Service is not found"
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))


@app.route("/update_service/<service_id>", methods = ["GET", "POST"])
def update_service(service_id):
    
    if request.method == "GET":
        return render_template("update_service.html", service = service)
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone = form["phone"]
        height = form["height"]
        address = form["address"]
        measurements = form["measurements"]
        # status = form["status"]
        descriptions = form["descriptions"]

        Service.objects.with_id(service_id).update(
            name = name,
            yob = yob,
            phone = phone,
            height = height,
            address = address,
            measurements = measurements,
            descriptions = descriptions,
            # status = status
        )
        return redirect( url_for("admin") )



@app.route("/sign-in", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        new_user = User.objects()
        return render_template("sign-in.html", new_user = new_user)
    elif request.method == "POST":
        form = request.form 
        fullname = form["fullname"]
        email = form["email"]
        username = form["username"]
        password = form["password"]

        new_user = User(
            fullname = fullname,
            email = email,
            username = username,
            password = password
        ) 

        new_user.save()
        return redirect(url_for("index"))

@app.route("/login/<service_id>", methods = ["GET","POST"])
def login(service_id):
    if request.method == "GET":
        return render_template("login.html")
    elif request.method =="POST":
        form = request.form
        username = form["username"]
        password = form["password"]

        found_user = User.objects(
            username = username,
            password = password
        )

        if found_user:
            session["loggedin"] = True
            new_user = User.objects.get(username = username)
            session["new_user"] = str(new_user.id)
            service_id = session["service"]
            return redirect( url_for("detail", service_id = service_id))
        else:
            return redirect(url_for("signin"))
  





@app.route("/logout")
def logout():
    session["loggedin"] = False
    session.clear()
    return redirect(url_for("index"))


    










if __name__ == "__main__":
  app.run(debug=True)
 