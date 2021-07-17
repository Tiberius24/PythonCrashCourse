import turtle

def moveTurtle(k, m):
    k.lt(90)
    k.fd(m)
    k.rt(90)
    k.fd(5)
    x = k.xcor()
    y = k.ycor()+2
    if m > 100:
        k.pu()
        k.goto(x,y)
        k.write(m, align="center", font=("Arial", 10))
        y = k.ycor() - 2
        k.goto(x,y)
        k.pd()
    k.fd(5)
    k.rt(90)
    k.fd(m)
    k.lt(90)
    k.fd(5)

def seq3np1(n,k):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0
    while n != 1:
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
        count = count +1
    moveTurtle(k,count)
    return count

def main():

    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.reset()
    wn.setworldcoordinates(0, 0, 750, 200)

    koda = turtle.Turtle()
    koda.color("saddle brown")
    koda.speed(20)
    maxSoFar = 0

    for start in range(1,50):
        result = seq3np1(start, koda)
        if maxSoFar < result:
            maxSoFar = result

        if start == 49:
            print(maxSoFar)


    wn.exitonclick()

if __name__ == '__main__':
    main()