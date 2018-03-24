import turtle

def tree(branchLen,t):
    if branchLen>5:
        #t.width(branchLen)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        # t.width(branchLen-10)
        t.right(20)
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
