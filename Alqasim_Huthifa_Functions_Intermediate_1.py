import random
def randInt(min=0, max=100):
    num = random.random()
    return num*(max-min) +(min)
print(randInt(min=1 , max=-1))



