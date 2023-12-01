from PersistenceLayer.DataController import DataController
from BusinessLayer.users.User import User


controller: DataController = DataController()

# user: User = User("Adolin", "qazxsw")
# user.addProject("proj1", "desc1", ["Java"], ["Hibernate"])


# controller.createUser(user)

user: User = controller.readUser("Adolin")
user.logIn("qazxsw")

user.changeUsername("Rinarin", "qazxsw")
user.changePassword("qazxsw", "qwedsa")
user.addProject("proj2", "desc2", ["Python"], ["Flask", "MongoDB"])
user.addProject("proj3", "desc3", ["C"], [])
user.deleteProject("proj1")

controller.updateUser("Adolin", user)



