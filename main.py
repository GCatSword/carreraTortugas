import turtle
import random

class Circuit():
    runners = []
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height):
               
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__starLine = -width / 2 + 20
        self.__finishLine = width / 2 - 20
        
        self.__createRunners()
        
    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__starLine, self.__posStartY[i])
            self.runners.append(new_turtle)
    
    def race(self):
        winner = False
        while not winner:
            for turtle in self.runners:
                advance = random.randint(1, 6)
                turtle.fd(advance)
                
                if turtle.position()[0] >= self.__finishLine:
                    winner = True
                    print("The winner is {} turtle".format(turtle.color()[0]))
                    
        
    
     
if __name__ == '__main__':
    circuit = Circuit(640, 480)
    circuit.race()











