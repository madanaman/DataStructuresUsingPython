import turtle
import random

def tree(branchLen,t):
    # To generate random angle
    angle=random.randint(15,45)
    print(angle)
    if branchLen>5:
        #t.width(branchLen)
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen-15,t)
        t.left(angle*2)
        tree(branchLen-15,t)
        # t.width(branchLen-10)
        t.right(angle)
        # To ensure that leaf node stays green and rest of the tree stays brown
        if branchLen!=15:
            t.color('brown')
        else:
            t.color('green')
        t.backward(branchLen)
def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    # t.up()
    # t.backward(100)
    # t.down()
    t.color("brown")
    tree(75,t)
    myWin.exitonclick()

main()
