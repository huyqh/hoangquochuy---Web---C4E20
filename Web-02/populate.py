from models.service import Service
import mlab
from faker import*
from random import*
mlab.connect()

fake = Faker()


description_female = ["ngoan hiền", "xinh gái", "đảm đang", "hiếu thảo", "ham vui", "thích quảng giao", "trầm tính", "ít nói", "năng động"]
description_male = ["thích bóng đá", "ga lăng", "điềm đạm", "hiếu thắng","bồng bột", "chín chắn", "ngoan ngoãn"]



measurements = [randint(85,95), randint(55,65), randint(85,95)]



image_female = [ "001.jpg", "002.jpg", "003.jpg", "004.jpg", "005.jpg", "006.jpg"]
image_male = [ "007.jpg", "008.jpg", "009.jpg", "010.jpg", "011.jpg"]




for i in range(20):
    print("loading service:", (i+1))
    gender = randint(0,1)
    
    if gender == 0:
        new_service = Service(
            name = fake.name(),
            yob = randint(1998,2001),
            height = randint(165,175),
            address = fake.address(),
            phone = fake.phone_number(),
            status = choice([True,False]),
            description = sample(description_female, 3),
            measurements = measurements,
            image = "../static/image/female/"+ choice(image_female) 
            )
       

    else:
        new_service = Service(
            name = fake.name(),
            yob = randint(1998,2001),
            height = randint(165,175),
            address = fake.address(),
            phone = fake.phone_number(),
            status = choice([True,False]),
            description = sample(description_male, 3),
            measurements = measurements,
            image = "../static/image/male/" + choice(image_male)
            )
    new_service.save()

    