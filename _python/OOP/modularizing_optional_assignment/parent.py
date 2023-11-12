local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

if __name__ == "__main__": #means execute the following lines only in this file so
    print(square(5))        #if this file imported to other .py file as module (child in this case)
    user = User("Anna")     #those lines will be executed cuz __name__ in child will be "parent"
    print(user.name)
    print(user.say_hello())


