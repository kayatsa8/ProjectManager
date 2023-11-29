from PersistenceLayer.DataController import DataController
from BusinessLayer.users.User import User

# user: User = User("Adolin", "qazxsw")
# user.addProject("proj1", "desc1", ["Java"], ["Hibernate"])

controller: DataController = DataController()

# controller.createUser(user)

adolin: User = controller.readUser("Adolin")

print(adolin.getProjects()["proj1"])

