
import math

handlers = {}
class LambdaMachine:
    global handlers 

    def insert(self,key,fn):
        handlers[key] = fn

    def retrieve(self,key):
        return handlers[key]

pythagora = lambda x,y: int(math.sqrt(x**2 + y**2))
addition = lambda x,y: x + y
multiplication = lambda x,y: x * y

lambdaMachine = LambdaMachine()
lambdaMachine.insert("pythagora",pythagora)
print(lambdaMachine.retrieve("pythagora")(3,4)) #--> 5

lambdaMachine.insert("addition", addition)
print(lambdaMachine.retrieve("addition")(2,5)) #--> 7

lambdaMachine.insert("multiplication", multiplication)
print(lambdaMachine.retrieve("multiplication")(4,10)) # --> 40
