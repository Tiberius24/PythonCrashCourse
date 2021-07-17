import turtle
import string


def print_number(t, height, k):  # Print the value of number used to create the bar
    x = t.xcor()
    y = t.ycor()+2
    t.penup()
    t.goto(x,y)
    t.write(str(k.upper() + ":" + str(height)), align="center", font=("Arial", 10))
    x = t.xcor()
    y = t.ycor() - 2
    t.goto(x, y)
    t.pendown()


def draw_bar(t, height, k):
    t.begin_fill()
    t.lt(90)
    t.fd(height)    # height of the bar graph
    t.rt(90)
    t.fd(20)        # Width of the bar graph
    print_number(t, height, k)
    t.fd(20)
    t.rt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()
    t.fd(5)         # Setup the turtle to start the next bar


def create_new_list(nd):
    new_list = list(nd.keys())
    new_list.sort()
    return new_list


def count_letters_matrix(p,d):  # loop through each character in the phase give and iterate the number of times it
    new_d = {}                  # occurs in the phrase
    for m in p:
        if m in d.keys():
            d[m] = d[m] + 1
        else:
            continue
    for (k, v) in d.items():    # loop through the old dictionary to create a new one where the number of times the
        if v > 0:               # character shows up in the phrase is greater than 1
            new_d[k] = v
        else:
            continue
    return new_d                # return the new dictionary


def count_dictionary():  # build the dictionary for each character in the alphabet
    count_dictionary_func = {}
    for i in string.ascii_lowercase:
        count_dictionary_func[i] = 0
    return count_dictionary_func


def main():

    quote = '''Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in
    Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war,
    testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great
    battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who
    here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
    But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground.
    The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract.
    The world will little note, nor long remember what we say here, but it can never forget what they did here.
    It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus 
    far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from 
    these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion --
    that we here highly resolve that these dead shall not have died in vain -- that this nation, under God,
    shall have a new birth of freedom -- and that government  of the people, by the people, for the people,
    shall not perish from the earth.

    Abraham Lincoln
    November 19, 1863'''

    quote = quote.lower()
    ct_dictionary = count_dictionary()
    new_ct_dictonary = count_letters_matrix(quote, ct_dictionary)
    new_cl_sorted = create_new_list(new_ct_dictonary)

    xs = list(new_ct_dictonary.values())

    wn = turtle.Screen()
    wn.bgcolor("light green")
    max_height = max(xs)
    num_bars = len(xs)
    border = 10
    wn.setworldcoordinates(0-border, 0-border, 45*num_bars+border, max_height+border)   # determine the display
    niko = turtle.Turtle()                                                              # window size
    niko.color("deep sky blue")
    niko.pencolor("navy")
    niko.fillcolor("red")
    niko.pensize(3)
    niko.speed(10)

    for k in new_cl_sorted:         # Loop through the sorted list of keys to determine the value for the key in the
        v = new_ct_dictonary[k]     # dictioinary, then use the key and value to draw the bar chart
        draw_bar(niko, v, k)
    wn.exitonclick()


if __name__ == '__main__':
    main()