from tkinter import *
import random
import enchant
d = enchant.Dict("en_US")
root = Tk()
run = True

root.config(bg="green")

emptycard = PhotoImage(file="images/empty.gif")

back = PhotoImage(file="images/back.gif")
a_front = PhotoImage(file="images/A.gif")
b_front = PhotoImage(file="images/B.gif")
c_front = PhotoImage(file="images/C.gif")
d_front = PhotoImage(file="images/D.gif")
f_front = PhotoImage(file="images/F.gif")
g_front = PhotoImage(file="images/G.gif")
h_front = PhotoImage(file="images/H.gif")
j_front = PhotoImage(file="images/J.gif")
k_front = PhotoImage(file="images/K.gif")
l_front = PhotoImage(file="images/L.gif")
m_front = PhotoImage(file="images/M.gif")
n_front = PhotoImage(file="images/N.gif")
o_front = PhotoImage(file="images/O.gif")
p_front = PhotoImage(file="images/P.gif")
q_front = PhotoImage(file="images/Q.gif")
r_front = PhotoImage(file="images/R.gif")
s_front = PhotoImage(file="images/S.gif")
t_front = PhotoImage(file="images/T.gif")
u_front = PhotoImage(file="images/U.gif")
v_front = PhotoImage(file="images/V.gif")
w_front = PhotoImage(file="images/W.gif")
x_front = PhotoImage(file="images/X.gif")
y_front = PhotoImage(file="images/Y.gif")
z_front = PhotoImage(file="images/Z.gif")
cl_front = PhotoImage(file="images/CL.gif")
th_front = PhotoImage(file="images/TH.gif")
er_front = PhotoImage(file="images/ER.gif")
qu_front = PhotoImage(file="images/QU.gif")
in_front = PhotoImage(file="images/IN.gif")
i_front = PhotoImage(file="images/I.gif")
e_front = PhotoImage(file="images/eee.gif")

wordtocheck = []

cardsused = []

discard = []

class Cards:
    def __init__(self, letter, pointvalue, frontimage):
        self.letter = letter
        self.pointvalue = pointvalue
        self.backimage = PhotoImage(file="images/back.gif")
        self.frontimage = frontimage

A_CARDS = [Cards("A", 2, a_front) for x in range(10)]
B_CARDS = [Cards("B", 8, b_front) for x in range(2)]
C_CARDS = [Cards("C", 8, c_front) for x in range(2)]
D_CARDS = [Cards("D", 5, d_front) for x in range(4)]
E_CARDS = [Cards("E", 2, e_front) for x in range(12)]
F_CARDS = [Cards("F", 6, f_front) for x in range(2)]
G_CARDS = [Cards("G", 6, g_front) for x in range(4)]
H_CARDS = [Cards("H", 7, h_front) for x in range(2)]
I_CARDS = [Cards("I", 2, i_front) for x in range(8)]
J_CARDS = [Cards("J", 13, j_front) for x in range(2)]
K_CARDS = [Cards("K", 8, k_front) for x in range(2)]
L_CARDS = [Cards("L", 3, l_front) for x in range(4)]
M_CARDS = [Cards("M", 5, m_front) for x in range(2)]
N_CARDS = [Cards("N", 5, n_front) for x in range(6)]
O_CARDS = [Cards("O", 2, o_front) for x in range(8)]
P_CARDS = [Cards("P", 6, p_front) for x in range(2)]
Q_CARDS = [Cards("Q", 15, q_front) for x in range(2)]
R_CARDS = [Cards("R", 5, r_front) for x in range(6)]
S_CARDS = [Cards("S", 3, s_front) for x in range(4)]
T_CARDS = [Cards("T", 3, t_front) for x in range(6)]
U_CARDS = [Cards("U", 4, u_front) for x in range(6)]
V_CARDS = [Cards("V", 11, v_front) for x in range(2)]
W_CARDS = [Cards("W", 10, w_front) for x in range(2)]
X_CARDS = [Cards("X", 12, x_front) for x in range(2)]
Y_CARDS = [Cards("Y", 4, y_front) for x in range(4)]
Z_CARDS = [Cards("Z", 14, z_front) for x in range(2)]
ER_CARDS = [Cards("ER", 7, er_front) for x in range(2)]
CL_CARDS = [Cards("CL", 10, cl_front) for x in range(2)]
IN_CARDS = [Cards("IN", 7, in_front) for x in range(2)]
TH_CARDS = [Cards("TH", 9, th_front) for x in range(2)]
QU_CARDS = [Cards("QU", 9, qu_front) for x in range(2)]

ALL_CARDS = QU_CARDS + TH_CARDS + IN_CARDS + CL_CARDS + ER_CARDS + Z_CARDS + Y_CARDS + X_CARDS + W_CARDS + V_CARDS +\
            U_CARDS + T_CARDS + S_CARDS + R_CARDS + Q_CARDS + P_CARDS + O_CARDS + N_CARDS + M_CARDS + L_CARDS +\
            K_CARDS + J_CARDS + I_CARDS + H_CARDS + G_CARDS + F_CARDS + E_CARDS + D_CARDS + C_CARDS + B_CARDS + A_CARDS

random.shuffle(ALL_CARDS)

deck = ALL_CARDS[:48]

area = Frame(root, bg="green")
area.pack()

button1 = Button(area, image=deck[0].frontimage, command=lambda: Clicked1(1)).grid(row=0, column=0, padx=5, pady=30)
button2 = Button(area, image=deck[1].frontimage, command=lambda: Clicked1(2)).grid(row=0, column=1, padx=5, pady=30)
button3 = Button(area, image=deck[2].frontimage, command=lambda: Clicked1(3)).grid(row=0, column=2, padx=5, pady=30)
button4 = Button(area, image=deck[3].frontimage, command=lambda: Clicked1(4)).grid(row=0, column=3, padx=5, pady=30)
button5 = Button(area, image=deck[4].frontimage, command=lambda: Clicked1(5)).grid(row=0, column=4, padx=5, pady=30)
button6 = Button(area, image=deck[5].frontimage, command=lambda: Clicked1(6)).grid(row=0, column=5, padx=5, pady=30)
button7 = Button(area, image=deck[6].frontimage, command=lambda: Clicked1(7)).grid(row=0, column=6, padx=5, pady=30)
button8 = Button(area, image=deck[7].frontimage, command=lambda: Clicked1(8)).grid(row=0, column=7, padx=5, pady=30)

slot = Frame(root, height=300, width=1000, bg="green")
slot.pack()

def Checkcard():
    if len(wordtocheck) <=1:
        print("too short")

    elif (d.check("".join(wordtocheck))) == False:
        print("".join(wordtocheck))
        print('not a word')

    elif (d.check("".join(wordtocheck))) == True:
        global button1
        global button2
        global button3
        global button4
        global button5
        global button6
        global button7
        global button8
        global bn
        global slot
        global deck
        global bn3
        print("".join(wordtocheck))
        print('good word')
        slot.destroy()
        slot = Frame(root, height=300, widt=1000, bg="green")
        slot.pack()
        wordtocheck.clear()


        for t in sorted(discard, reverse=True):
            del deck[t]

        print(len(deck))
        discard.clear()



        if len(deck) >= 10:
            button1 = Button(area, image=deck[0].frontimage, command=lambda: Clicked1(1)).grid(row=0, column=0, padx=5, pady=30)
            button2 = Button(area, image=deck[1].frontimage, command=lambda: Clicked1(2)).grid(row=0, column=1, padx=5, pady=30)
            button3 = Button(area, image=deck[2].frontimage, command=lambda: Clicked1(3)).grid(row=0, column=2, padx=5, pady=30)
            button4 = Button(area, image=deck[3].frontimage, command=lambda: Clicked1(4)).grid(row=0, column=3, padx=5, pady=30)
            button5 = Button(area, image=deck[4].frontimage, command=lambda: Clicked1(5)).grid(row=0, column=4, padx=5, pady=30)
            button6 = Button(area, image=deck[5].frontimage, command=lambda: Clicked1(6)).grid(row=0, column=5, padx=5, pady=30)
            button7 = Button(area, image=deck[6].frontimage, command=lambda: Clicked1(7)).grid(row=0, column=6, padx=5, pady=30)
            button8 = Button(area, image=deck[7].frontimage, command=lambda: Clicked1(8)).grid(row=0, column=7, padx=5, pady=30)

        elif len(deck) == 9:
            print("8 cards left")
            button1 = Button(area, image=deck[0].frontimage, command=lambda: Lastclick(1)).grid(row=0, column=0, padx=5,pady=30)
            button2 = Button(area, image=deck[1].frontimage, command=lambda: Lastclick(2)).grid(row=0, column=1, padx=5,pady=30)
            button3 = Button(area, image=deck[2].frontimage, command=lambda: Lastclick(3)).grid(row=0, column=2, padx=5,pady=30)
            button4 = Button(area, image=deck[3].frontimage, command=lambda: Lastclick(4)).grid(row=0, column=3, padx=5,pady=30)
            button5 = Button(area, image=deck[4].frontimage, command=lambda: Lastclick(5)).grid(row=0, column=4, padx=5,pady=30)
            button6 = Button(area, image=deck[5].frontimage, command=lambda: Lastclick(6)).grid(row=0, column=5, padx=5,pady=30)
            button7 = Button(area, image=deck[6].frontimage, command=lambda: Lastclick(7)).grid(row=0, column=6, padx=5,pady=30)
            button8 = Button(area, image=deck[7].frontimage, command=lambda: Lastclick(8)).grid(row=0, column=7, padx=5,pady=30)
        elif len(deck) == 8:
            print("8 cards left")
            button1 = Button(area, image=deck[0].frontimage, command=lambda: Lastclick(1)).grid(row=0, column=0, padx=5,pady=30)
            button2 = Button(area, image=deck[1].frontimage, command=lambda: Lastclick(2)).grid(row=0, column=1, padx=5,pady=30)
            button3 = Button(area, image=deck[2].frontimage, command=lambda: Lastclick(3)).grid(row=0, column=2, padx=5,pady=30)
            button4 = Button(area, image=deck[3].frontimage, command=lambda: Lastclick(4)).grid(row=0, column=3, padx=5,pady=30)
            button5 = Button(area, image=deck[4].frontimage, command=lambda: Lastclick(5)).grid(row=0, column=4, padx=5,pady=30)
            button6 = Button(area, image=deck[5].frontimage, command=lambda: Lastclick(6)).grid(row=0, column=5, padx=5,pady=30)
            button7 = Button(area, image=deck[6].frontimage, command=lambda: Lastclick(7)).grid(row=0, column=6, padx=5,pady=30)
            button8 = Button(area, image=deck[7].frontimage, command=lambda: Lastclick(8)).grid(row=0, column=7, padx=5,pady=30)
        elif len(deck) == 7:
            button1 = Button(area, image=deck[0].frontimage, command=lambda: Lastclick(1)).grid(row=0, column=0, padx=5,pady=30)
            button2 = Button(area, image=deck[1].frontimage, command=lambda: Lastclick(2)).grid(row=0, column=1, padx=5,pady=30)
            button3 = Button(area, image=deck[2].frontimage, command=lambda: Lastclick(3)).grid(row=0, column=2, padx=5,pady=30)
            button4 = Button(area, image=deck[3].frontimage, command=lambda: Lastclick(4)).grid(row=0, column=3, padx=5,pady=30)
            button5 = Button(area, image=deck[4].frontimage, command=lambda: Lastclick(5)).grid(row=0, column=4, padx=5,pady=30)
            button6 = Button(area, image=deck[5].frontimage, command=lambda: Lastclick(6)).grid(row=0, column=5, padx=5,pady=30)
            button7 = Button(area, image=deck[6].frontimage, command=lambda: Lastclick(7)).grid(row=0, column=6, padx=5,pady=30)
        elif len(deck) == 6:
            button1 = Button(area, image=deck[0].frontimage, command=lambda: Lastclick(1)).grid(row=0, column=0, padx=5,pady=30)
            button2 = Button(area, image=deck[1].frontimage, command=lambda: Lastclick(2)).grid(row=0, column=1, padx=5,pady=30)
            button3 = Button(area, image=deck[2].frontimage, command=lambda: Lastclick(3)).grid(row=0, column=2, padx=5,pady=30)
            button4 = Button(area, image=deck[3].frontimage, command=lambda: Lastclick(4)).grid(row=0, column=3, padx=5,pady=30)
            button5 = Button(area, image=deck[4].frontimage, command=lambda: Lastclick(5)).grid(row=0, column=4, padx=5,pady=30)
            button6 = Button(area, image=deck[5].frontimage, command=lambda: Lastclick(6)).grid(row=0, column=5, padx=5,pady=30)
        elif len(deck) == 5:
            button1 = Button(area, image=deck[0].frontimage, command=lambda: Lastclick(1)).grid(row=0, column=0, padx=5,pady=30)
            button2 = Button(area, image=deck[1].frontimage, command=lambda: Lastclick(2)).grid(row=0, column=1, padx=5,pady=30)
            button3 = Button(area, image=deck[2].frontimage, command=lambda: Lastclick(3)).grid(row=0, column=2, padx=5,pady=30)
            button4 = Button(area, image=deck[3].frontimage, command=lambda: Lastclick(4)).grid(row=0, column=3, padx=5,pady=30)
            button5 = Button(area, image=deck[4].frontimage, command=lambda: Lastclick(5)).grid(row=0, column=4, padx=5,pady=30)
        elif len(deck) == 4:
            button1 = Button(area, image=deck[0].frontimage, command=lambda: Lastclick(1)).grid(row=0, column=0, padx=5,pady=30)
            button2 = Button(area, image=deck[1].frontimage, command=lambda: Lastclick(2)).grid(row=0, column=1, padx=5,pady=30)
            button3 = Button(area, image=deck[2].frontimage, command=lambda: Lastclick(3)).grid(row=0, column=2, padx=5,pady=30)
            button4 = Button(area, image=deck[3].frontimage, command=lambda: Lastclick(4)).grid(row=0, column=3, padx=5,pady=30)
        elif len(deck) == 3:
            button1 = Button(area, image=deck[0].frontimage, command=lambda: Lastclick(1)).grid(row=0, column=0, padx=5,pady=30)
            button2 = Button(area, image=deck[1].frontimage, command=lambda: Lastclick(2)).grid(row=0, column=1, padx=5,pady=30)
            button3 = Button(area, image=deck[2].frontimage, command=lambda: Lastclick(3)).grid(row=0, column=2, padx=5,pady=30)
        elif len(deck) == 2:
            button1 = Button(area, image=deck[0].frontimage, command=lambda: Lastclick(1)).grid(row=0, column=0, padx=5,pady=30)
            button2 = Button(area, image=deck[1].frontimage, command=lambda: Lastclick(2)).grid(row=0, column=1, padx=5,pady=30)
        elif len(deck) == 1:
            button1 = Button(area, image=deck[0].frontimage, command=lambda: Lastclick(1)).grid(row=0, column=0, padx=5,pady=30)
        else:
            print("something else happened")


submit = Button(root, text="SUBMIT WORD", padx=25, pady=25, command=Checkcard).pack()

def Lastclick(bn3):
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global nocard
    global bn
    bn = bn3
    if bn3 == 1:
        nocard = Button(area, image=back).grid(row=0, column=0, padx=5, pady=30)
        button1 = Button(slot, image=deck[0].frontimage, command=lambda: Lastclick(1)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        discard.append(0)
        counter = 1
        cardsused.append(counter)

    elif bn3 == 2:
        nocard = Button(area, image=back).grid(row=0, column=1, padx=5, pady=30)
        button2 = Button(slot, image=deck[1].frontimage, command=lambda: Lastclick(2)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(1)
        counter = 1
        cardsused.append(counter)

    elif bn3 == 3:
        nocard = Button(area, image=back).grid(row=0, column=2, padx=5, pady=30)
        button3 = Button(slot, image=deck[2].frontimage, command=lambda: Lastclick(3)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(2)
        counter = 1
        cardsused.append(counter)

    elif bn3 == 4:
        nocard = Button(area, image=back).grid(row=0, column=3, padx=5, pady=30)
        button4 = Button(slot, image=deck[3].frontimage, command=lambda: Lastclick(4)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(3)
        counter = 1
        cardsused.append(counter)


    elif bn3 == 5:
        nocard = Button(area, image=back).grid(row=0, column=4, padx=5, pady=30)
        button5 = Button(slot, image=deck[4].frontimage, command=lambda: Lastclick(5)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(4)
        counter = 1
        cardsused.append(counter)


    elif bn3 == 6:
        nocard = Button(area, image=back).grid(row=0, column=5, padx=5, pady=30)
        button6 = Button(slot, image=deck[5].frontimage, command=lambda: Lastclick(6)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(5)
        counter = 1
        cardsused.append(counter)


    elif bn3 == 7:
        nocard = Button(area, image=back).grid(row=0, column=6, padx=5, pady=30)
        button7 = Button(slot, image=deck[6].frontimage, command=lambda: Lastclick(7)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(6)
        counter = 1
        cardsused.append(counter)


    elif bn3 == 8:
        nocard = Button(area, image=back).grid(row=0, column=7, padx=5, pady=30)
        button8 = Button(slot, image=deck[7].frontimage, command=lambda: Lastclick(8)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(7)
        counter = 1
        cardsused.append(counter)


def Clicked1(bn):
    # Move Cards to Slots in order from left to right
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global letter1
    global wordtocheck
    global back
    global nocard
    global counter
    #print(f"\n\n\n\nbutton {bn} was pressed")

    if bn == 1:
        nocard = Button(area, image=back).grid(row=0, column=0, padx=5, pady=30)
        button1 = Button(slot, image=deck[0].frontimage, command=lambda: Unclicked(1)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn -1].letter)
        #print(wordtocheck)
        discard.append(0)
        counter = 1
        cardsused.append(counter)

    elif bn == 2:
        nocard = Button(area, image=back).grid(row=0, column=1, padx=5, pady=30)
        button2 = Button(slot, image=deck[1].frontimage, command=lambda: Unclicked(2)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(1)
        counter = 1
        cardsused.append(counter)

    elif bn == 3:
        nocard = Button(area, image=back).grid(row=0, column=2, padx=5, pady=30)
        button3 = Button(slot, image=deck[2].frontimage, command=lambda: Unclicked(3)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(2)
        counter = 1
        cardsused.append(counter)

    elif bn == 4:
        nocard = Button(area, image=back).grid(row=0, column=3, padx=5, pady=30)
        button4 = Button(slot, image=deck[3].frontimage, command=lambda: Unclicked(4)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(3)
        counter = 1
        cardsused.append(counter)


    elif bn == 5:
        nocard = Button(area, image=back).grid(row=0, column=4, padx=5, pady=30)
        button5 = Button(slot, image=deck[4].frontimage, command=lambda: Unclicked(5)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(4)
        counter = 1
        cardsused.append(counter)


    elif bn == 6:
        nocard = Button(area, image=back).grid(row=0, column=5, padx=5, pady=30)
        button6 = Button(slot, image=deck[5].frontimage, command=lambda: Unclicked(6)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(5)
        counter = 1
        cardsused.append(counter)


    elif bn == 7:
        nocard = Button(area, image=back).grid(row=0, column=6, padx=5, pady=30)
        button7 = Button(slot, image=deck[6].frontimage, command=lambda: Unclicked(7)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(6)
        counter = 1
        cardsused.append(counter)


    elif bn == 8:
        nocard = Button(area, image=back).grid(row=0, column=7, padx=5, pady=30)
        button8 = Button(slot, image=deck[7].frontimage, command=lambda: Unclicked(8)).pack(side=LEFT)
        letter1 = deck[bn - 1].letter
        wordtocheck.append(letter1)
        #print(deck[bn - 1].letter)
        #print(wordtocheck)
        discard.append(7)
        counter = 1
        cardsused.append(counter)

def Unclicked(bn2):
    # Move Cards back to correct button
    global button1
    global slot1
    global letter2
    global wordtocheck
    global nocard
    global slot
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    if bn2 == 1:
        button1 = Button(area,image=deck[0].frontimage,command=lambda: Clicked1(1)).grid(row=0,column=0,padx=5,pady=30)
        button2 = Button(area,image=deck[1].frontimage,command=lambda: Clicked1(2)).grid(row=0,column=1,padx=5,pady=30)
        button3 = Button(area,image=deck[2].frontimage,command=lambda: Clicked1(3)).grid(row=0,column=2,padx=5,pady=30)
        button4 = Button(area, image=deck[3].frontimage, command=lambda: Clicked1(4)).grid(row=0, column=3, padx=5, pady=30)
        button5 = Button(area, image=deck[4].frontimage, command=lambda: Clicked1(5)).grid(row=0, column=4, padx=5, pady=30)
        button6 = Button(area, image=deck[5].frontimage, command=lambda: Clicked1(6)).grid(row=0, column=5, padx=5, pady=30)
        button7 = Button(area, image=deck[6].frontimage, command=lambda: Clicked1(7)).grid(row=0, column=6, padx=5, pady=30)
        button8 = Button(area, image=deck[7].frontimage, command=lambda: Clicked1(8)).grid(row=0, column=7, padx=5, pady=30)

        slot.destroy()
        slot = Frame(root, height=300, widt=1000, bg="green")
        slot.pack()
        wordtocheck.clear()
        discard.clear()

    elif bn2 == 2:
        button1 = Button(area,image=deck[0].frontimage,command=lambda: Clicked1(1)).grid(row=0,column=0,padx=5,pady=30)
        button2 = Button(area,image=deck[1].frontimage,command=lambda: Clicked1(2)).grid(row=0,column=1,padx=5,pady=30)
        button3 = Button(area,image=deck[2].frontimage,command=lambda: Clicked1(3)).grid(row=0,column=2,padx=5,pady=30)
        button4 = Button(area, image=deck[3].frontimage, command=lambda: Clicked1(4)).grid(row=0, column=3, padx=5, pady=30)
        button5 = Button(area, image=deck[4].frontimage, command=lambda: Clicked1(5)).grid(row=0, column=4, padx=5, pady=30)
        button6 = Button(area, image=deck[5].frontimage, command=lambda: Clicked1(6)).grid(row=0, column=5, padx=5, pady=30)
        button7 = Button(area, image=deck[6].frontimage, command=lambda: Clicked1(7)).grid(row=0, column=6, padx=5, pady=30)
        button8 = Button(area, image=deck[7].frontimage, command=lambda: Clicked1(8)).grid(row=0, column=7, padx=5, pady=30)

        slot.destroy()
        slot = Frame(root, height=300, widt=1000, bg="green")
        slot.pack()
        wordtocheck.clear()
        discard.clear()

    elif bn2 == 3:
        button1 = Button(area,image=deck[0].frontimage,command=lambda: Clicked1(1)).grid(row=0,column=0,padx=5,pady=30)
        button2 = Button(area,image=deck[1].frontimage,command=lambda: Clicked1(2)).grid(row=0,column=1,padx=5,pady=30)
        button3 = Button(area,image=deck[2].frontimage,command=lambda: Clicked1(3)).grid(row=0,column=2,padx=5,pady=30)
        button4 = Button(area, image=deck[3].frontimage, command=lambda: Clicked1(4)).grid(row=0, column=3, padx=5, pady=30)
        button5 = Button(area, image=deck[4].frontimage, command=lambda: Clicked1(5)).grid(row=0, column=4, padx=5, pady=30)
        button6 = Button(area, image=deck[5].frontimage, command=lambda: Clicked1(6)).grid(row=0, column=5, padx=5, pady=30)
        button7 = Button(area, image=deck[6].frontimage, command=lambda: Clicked1(7)).grid(row=0, column=6, padx=5, pady=30)
        button8 = Button(area, image=deck[7].frontimage, command=lambda: Clicked1(8)).grid(row=0, column=7, padx=5, pady=30)

        slot.destroy()
        slot = Frame(root, height=300, widt=1000, bg="green")
        slot.pack()
        wordtocheck.clear()
        discard.clear()

    elif bn2 == 4:
        button1 = Button(area,image=deck[0].frontimage,command=lambda: Clicked1(1)).grid(row=0,column=0,padx=5,pady=30)
        button2 = Button(area,image=deck[1].frontimage,command=lambda: Clicked1(2)).grid(row=0,column=1,padx=5,pady=30)
        button3 = Button(area,image=deck[2].frontimage,command=lambda: Clicked1(3)).grid(row=0,column=2,padx=5,pady=30)
        button4 = Button(area, image=deck[3].frontimage, command=lambda: Clicked1(4)).grid(row=0, column=3, padx=5, pady=30)
        button5 = Button(area, image=deck[4].frontimage, command=lambda: Clicked1(5)).grid(row=0, column=4, padx=5, pady=30)
        button6 = Button(area, image=deck[5].frontimage, command=lambda: Clicked1(6)).grid(row=0, column=5, padx=5, pady=30)
        button7 = Button(area, image=deck[6].frontimage, command=lambda: Clicked1(7)).grid(row=0, column=6, padx=5, pady=30)
        button8 = Button(area, image=deck[7].frontimage, command=lambda: Clicked1(8)).grid(row=0, column=7, padx=5, pady=30)

        slot.destroy()
        slot = Frame(root, height=300, widt=1000, bg="green")
        slot.pack()
        wordtocheck.clear()
        discard.clear()

    elif bn2 == 5:
        button1 = Button(area,image=deck[0].frontimage,command=lambda: Clicked1(1)).grid(row=0,column=0,padx=5,pady=30)
        button2 = Button(area,image=deck[1].frontimage,command=lambda: Clicked1(2)).grid(row=0,column=1,padx=5,pady=30)
        button3 = Button(area,image=deck[2].frontimage,command=lambda: Clicked1(3)).grid(row=0,column=2,padx=5,pady=30)
        button4 = Button(area, image=deck[3].frontimage, command=lambda: Clicked1(4)).grid(row=0, column=3, padx=5, pady=30)
        button5 = Button(area, image=deck[4].frontimage, command=lambda: Clicked1(5)).grid(row=0, column=4, padx=5, pady=30)
        button6 = Button(area, image=deck[5].frontimage, command=lambda: Clicked1(6)).grid(row=0, column=5, padx=5, pady=30)
        button7 = Button(area, image=deck[6].frontimage, command=lambda: Clicked1(7)).grid(row=0, column=6, padx=5, pady=30)
        button8 = Button(area, image=deck[7].frontimage, command=lambda: Clicked1(8)).grid(row=0, column=7, padx=5, pady=30)

        slot.destroy()
        slot = Frame(root, height=300, widt=1000, bg="green")
        slot.pack()
        wordtocheck.clear()
        discard.clear()

    elif bn2 == 6:
        button1 = Button(area,image=deck[0].frontimage,command=lambda: Clicked1(1)).grid(row=0,column=0,padx=5,pady=30)
        button2 = Button(area,image=deck[1].frontimage,command=lambda: Clicked1(2)).grid(row=0,column=1,padx=5,pady=30)
        button3 = Button(area,image=deck[2].frontimage,command=lambda: Clicked1(3)).grid(row=0,column=2,padx=5,pady=30)
        button4 = Button(area, image=deck[3].frontimage, command=lambda: Clicked1(4)).grid(row=0, column=3, padx=5, pady=30)
        button5 = Button(area, image=deck[4].frontimage, command=lambda: Clicked1(5)).grid(row=0, column=4, padx=5, pady=30)
        button6 = Button(area, image=deck[5].frontimage, command=lambda: Clicked1(6)).grid(row=0, column=5, padx=5, pady=30)
        button7 = Button(area, image=deck[6].frontimage, command=lambda: Clicked1(7)).grid(row=0, column=6, padx=5, pady=30)
        button8 = Button(area, image=deck[7].frontimage, command=lambda: Clicked1(8)).grid(row=0, column=7, padx=5, pady=30)

        slot.destroy()
        slot = Frame(root, height=300, widt=1000, bg="green")
        slot.pack()
        wordtocheck.clear()
        discard.clear()

    elif bn2 == 7:
        button1 = Button(area,image=deck[0].frontimage,command=lambda: Clicked1(1)).grid(row=0,column=0,padx=5,pady=30)
        button2 = Button(area,image=deck[1].frontimage,command=lambda: Clicked1(2)).grid(row=0,column=1,padx=5,pady=30)
        button3 = Button(area,image=deck[2].frontimage,command=lambda: Clicked1(3)).grid(row=0,column=2,padx=5,pady=30)
        button4 = Button(area, image=deck[3].frontimage, command=lambda: Clicked1(4)).grid(row=0, column=3, padx=5, pady=30)
        button5 = Button(area, image=deck[4].frontimage, command=lambda: Clicked1(5)).grid(row=0, column=4, padx=5, pady=30)
        button6 = Button(area, image=deck[5].frontimage, command=lambda: Clicked1(6)).grid(row=0, column=5, padx=5, pady=30)
        button7 = Button(area, image=deck[6].frontimage, command=lambda: Clicked1(7)).grid(row=0, column=6, padx=5, pady=30)
        button8 = Button(area, image=deck[7].frontimage, command=lambda: Clicked1(8)).grid(row=0, column=7, padx=5, pady=30)

        slot.destroy()
        slot = Frame(root, height=300, widt=1000, bg="green")
        slot.pack()
        wordtocheck.clear()
        discard.clear()

    elif bn2 == 8:
        button1 = Button(area,image=deck[0].frontimage,command=lambda: Clicked1(1)).grid(row=0,column=0,padx=5,pady=30)
        button2 = Button(area,image=deck[1].frontimage,command=lambda: Clicked1(2)).grid(row=0,column=1,padx=5,pady=30)
        button3 = Button(area,image=deck[2].frontimage,command=lambda: Clicked1(3)).grid(row=0,column=2,padx=5,pady=30)
        button4 = Button(area, image=deck[3].frontimage, command=lambda: Clicked1(4)).grid(row=0, column=3, padx=5, pady=30)
        button5 = Button(area, image=deck[4].frontimage, command=lambda: Clicked1(5)).grid(row=0, column=4, padx=5, pady=30)
        button6 = Button(area, image=deck[5].frontimage, command=lambda: Clicked1(6)).grid(row=0, column=5, padx=5, pady=30)
        button7 = Button(area, image=deck[6].frontimage, command=lambda: Clicked1(7)).grid(row=0, column=6, padx=5, pady=30)
        button8 = Button(area, image=deck[7].frontimage, command=lambda: Clicked1(8)).grid(row=0, column=7, padx=5, pady=30)

        slot.destroy()
        slot = Frame(root, height=300, widt=1000, bg="green")
        slot.pack()
        wordtocheck.clear()
        discard.clear()

#print(len(deck))

class Game:
    def __init__(self):
        while run:
            print("running")




mainloop()
