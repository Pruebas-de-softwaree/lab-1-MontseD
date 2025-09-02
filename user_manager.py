import time
class UserManager:
    def __init__(self):
        self.users = []  

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":
    user_manager= UserManager()

    #for i in range(500):
        #user_manager.add_user(i,f"yo soy el num:{i}")

    #RF1
    #for i in range(500):
        #user_found = user_manager.find_user(i)
        #print(user_found)

    #RF2
    #for i in range(500):
        #user_found = user_manager.find_user(i)
        #print(user_found)

    #RF3
    #for i in range(500):
        #user_found = user_manager.find_user(i)
        #print(user_found)
    #for i in range(500):
        #user_manager.delete_user(i)
        #user_found = user_manager.find_user(i)
        #print(user_found)
        #print(f"Borrando usuario {i}")

    #RF5
    #for i in range(500):
        #user_manager.add_user(i,f"Yo soy el numero:{i}")  
    #average=user_manager.average_user_id()
    #print(average)

    #RNF1
    #for i in range(1000):
        #user_manager.add_user(i,f"Yo soy el numero:{i}")

    #print("Usuarios creados:", len(user_manager.users))

    #RNF2
    #user_manager = UserManager()
    #for i in range(1000):
        #user_manager.add_user(i, f"Usuario {i}")
    #inicio = time.time()
        #user_found = user_manager.find_user(999)
    #fin = time.time()
    #tiempo = fin - inicio
    #print(f"Tiempo de búsqueda: {tiempo:.5f} segundos")
    #print("Usuario encontrado:", user_found)

    #RNF3
    user_manager = UserManager()
    user_manager.add_user(1, "Usuario 1")
    user_manager.add_user(1, "Usuario 2")
    user_manager.add_user(2, "Usuario 3")
    print("Usuarios antes de borrar duplicados:")
    for u in user_manager.users:
        print(u)
    user_manager.delete_user(1)
    print("Usuarios después de borrar duplicados:")
    for u in user_manager.users:
        print(u)





    print("end")