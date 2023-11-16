from ServiceLayer.Response import Response
from ServiceLayer.Service import Service


service: Service = Service()

response: Response[bool] = service.register("John Thina", "1234")

print(response.getValue())
