import mlab
from models.service import Service


mlab.connect()

all_service = Service.objects()


first_service = all_service[0]

print(first_service["name"])
# delete
# id_to_find = "5b781d8b5d600b1580e11460"
# # hera = Service.objects(id=id_to_find) # [Service obj]
# # hera = Service.objects.get(id = id_to_find) # Service obj
# service = Service.objects.with_id(id_to_find) # Service obj

# if service is not None:
#     service.delete() 
#     print("deleted")
# else:
#     print("not found")
# update
# id_to_find = "5b781f2e5d600b09d4cdd32e"
# service = Service.objects.with_id(id_to_find)
# if service is not None:
#     print(service.to_mongo())
#     service.update(set__yob=2000,set__name="Linh Kute")
#     service.reload()
#     print(service.yob)
# else:
#     print("not found")
