from tkinter import *
import random, twl2, socket, pickle

server = "xxx.xxx.x.xxx" 
port = 5555
addr = (server, port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(addr)
print(f'CLIENT CONNECTED TO: {addr}')

root = Tk()
root.config(bg="green")
root.geometry("1440x780")
root.title('PLAYER 2 (CLIENT)')

blank_frame = Frame(root,height=30, width=100, bg="blue").grid(row=0, column=0, padx=0, pady=0)
blank_button = Button(root).grid(row=1, column=0, pady=80)

bg_image = PhotoImage(file="images/bgimage.gif")
bg_image = bg_image.zoom(2)
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

emptycard = PhotoImage(file="images/empty.gif")
emptycard = emptycard.zoom(3)
emptycard= emptycard.subsample(4)

back = PhotoImage(file="images/back.gif")
back = back.zoom(3)
back = back.subsample(4)

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

class Cards:
    def __init__(self, letter, pointvalue, frontimage):
        self.letter = letter
        self.pointvalue = pointvalue
        self.backimage = PhotoImage(file="images/back.gif")
        self.frontimage = frontimage
        self.title = self.letter + " " + str(self.pointvalue)

    def __repr__(self):
        return self.title

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

CARDS_DICT = {}
CARDS_DICT['A'] = A_CARDS
CARDS_DICT['B'] = B_CARDS
CARDS_DICT['C'] = C_CARDS
CARDS_DICT['D'] = D_CARDS
CARDS_DICT['E'] = E_CARDS
CARDS_DICT['F'] = F_CARDS
CARDS_DICT['G'] = G_CARDS
CARDS_DICT['H'] = H_CARDS
CARDS_DICT['I'] = I_CARDS
CARDS_DICT['J'] = J_CARDS
CARDS_DICT['K'] = K_CARDS
CARDS_DICT['L'] = L_CARDS
CARDS_DICT['M'] = M_CARDS
CARDS_DICT['N'] = N_CARDS
CARDS_DICT['O'] = O_CARDS
CARDS_DICT['P'] = P_CARDS
CARDS_DICT['Q'] = Q_CARDS
CARDS_DICT['R'] = R_CARDS
CARDS_DICT['S'] = S_CARDS
CARDS_DICT['T'] = T_CARDS
CARDS_DICT['U'] = U_CARDS
CARDS_DICT['V'] = V_CARDS
CARDS_DICT['W'] = W_CARDS
CARDS_DICT['X'] = X_CARDS
CARDS_DICT['Y'] = Y_CARDS
CARDS_DICT['Z'] = Z_CARDS
CARDS_DICT['ER'] = ER_CARDS
CARDS_DICT['CL'] = CL_CARDS
CARDS_DICT['IN'] = IN_CARDS
CARDS_DICT['TH'] = TH_CARDS
CARDS_DICT['QU'] = QU_CARDS

random.shuffle(ALL_CARDS)

for card in ALL_CARDS:
    card.frontimage = card.frontimage.zoom(3)
    card.frontimage = card.frontimage.subsample(4)

deck = ALL_CARDS.copy()

data = pickle.loads(client_socket.recv(2084*6))     # 1ST RECV # DRAW CARD FROM SERVER #
print(f'RECEIVED FROM SERVER: {data}')

new_draw_card = CARDS_DICT[data]

deck.insert(10, new_draw_card[0])

print(f'FIRST DECK: {deck}')

your_cards = {}
your_cards_info = {}
temp_cards = []
turn = True
face_down_card = False
words = []
total_points = 0
label_offset = 0
word_offset = 0
all_words = []
letters = []
last_turn = False
clicked_cards = []
round_score = 0
longest_word = ''

def submit():
    global clicked_cards
    global total_points
    global word_offset
    global label_offset
    global letters
    global words
    global turn
    global temp_cards
    global your_cards_info
    global score_label
    global word_label
    global word_title
    global game_state
    global all_words
    global round_score
    global longest_word
    global NO_OUT_LABEL

    if not face_down_card:
        your_cards[11].grid_forget()

    reset.configure(command=do_nothing)

    try:
        word_label.destroy()
        score_label.destroy()
        word_title.destroy()
    except:
        print('LABELS NOT CREATED YET')
        pass

    points = 0
    for card in your_cards_info.values():
        letters.append(card.letter)
        points += card.pointvalue

    print(f'Letters: {letters}')

    spelled_word = ''.join(letters)

    print(f'SPELLED WORD:: {spelled_word, type(spelled_word)}')

    if len(spelled_word) > len(longest_word):
        longest_word = spelled_word
        print(f'LONGEST WORD: {longest_word}')

    words.append(spelled_word)

    print(f'WORDS: {words}')

    letters = []

    print(f'letters after [] {letters}')

    all_words.append(words)

    print(f'SUBMIT PRESSED - WORDS: {all_words}')

    if twl2.check(words[0].lower()):  ## CHECKS SPELLING AGAINST SCRABBLE DICTIONARY ##
        print('WORD IS CORRECT')
    else:
        points = 0 - points
        print(f'NOT SPELLED RIGHT - MINUSING POINTS: {points}')

    round_score += points
    print(f'ROUND SCORE: {round_score}')

    word_title = Label(root, text='YOUR WORDS', bg='green')
    word_title.place(x=1100, y=(270))
    word_label = Label(root, text=f'{words[word_offset]}', bg='green')
    word_label.place(x=1100, y=(300 + label_offset))
    word_offset += 1
    label_offset += 30

    for key in your_cards_info.keys():
        temp_cards.append(deck[key])
        print(f'CARD ADDED TO temp_cards: {deck[key]}')
        clicked_cards.append(key)

    print(f'CLICKED CARDS LIST: {clicked_cards}')

    print(f'your_cards_info: {your_cards_info}')
    print(f'your_cards_info.keys: {your_cards_info.keys()}')

    for key in sorted(your_cards_info.keys(), reverse=True):
        your_cards[key].destroy()

    print(f'temp cards list: {temp_cards}')

    if len(temp_cards) == cards_per_hand:
        print('ALL CARDS IN HAND USED - YOUR ROUND IS OVER')
        turn = False
        label_offset = 0
        game_state = 'ROUND OVER'

        your_numbers = list(your_cards_info.keys())
        print(f'YOUR NUMBERS: {your_numbers}')
        if not face_down_card:
            numbers = [10]
        else:
            numbers = [11]
        for num in range(cards_per_hand):
            numbers.append(num)
        print(f'numbers: {numbers}')
        discarded_card = [x for x in numbers if x not in clicked_cards]
        print('DISCARDED CARD AFTER SUBMIT:')
        print(discarded_card)
        card_str = deck[discarded_card[0]].letter  #### HERE ###

        if round_score <= 0:
            round_score = 0
        else:
            total_points += round_score

        print(f'TOTAL POINTS: {total_points}')

        score_label = Label(root, text=f'YOU SCORED {round_score} POINTS - TOTAL: {total_points}', bg='green')
        score_label.place(x=1100, y=240)

        data_to_send = [card_str, all_words, round_score]
        print(f'SENDING (DURING SUBMIT): {data_to_send}')  ### data = list of score etc

        client_socket.sendall(pickle.dumps(data_to_send))

        round_score = 0
        your_cards_info = {}
        words = []
        word_offset = 0
        all_words = []
        temp_cards = []
        clicked_cards = []
        reset.configure(command=lambda: reset_hand())

        try:
            NO_OUT_LABEL.destroy()
            print('LABEL TO DESTROY')

        except:
            print('NO LABEL TO DESTROY')

    elif len(temp_cards) < cards_per_hand:
        print('LAST TURN = TRUE')
        print('NOT ALL CARDS HAVE BEEN USED - TURN CONTINUES')
        word_offset = 0
        words = []
        your_cards_info = {}
        print(f'ROUND SCORE: {round_score}')
        """else:
            print('LAST TURN = FLASE')
            print('YOU MUST USE ALL CARDS IN YOUR HAND TO GO OUT FIRST')
            round_score = 0
            your_cards_info = {}
            words = []
            word_offset = 0
            all_words = []
            temp_cards = []
            clicked_cards = []
            word_title.destroy()
            word_label.destroy()
            NO_OUT_LABEL = Label(root, text='YOU MUST USE ALL CARDS IN YOUR HAND TO GO OUT FIRST', bg='green')
            NO_OUT_LABEL.place(x=800, y=(270))
            reset_hand()"""

    elif len(temp_cards) > cards_per_hand:
        print(f'YOU USED ONE TOO MANY CARDS!  THIS IS A {str(cards_per_hand)} CARD HAND')
        words = []
        word_offset = 0
        your_cards_info = {}
        round_score -= points
        reset_hand() #MOVE THIS ELIF TO TOP - SUBMIT DOES NOTHING IF TOO MANY CARDS

def reset_hand():                   ### CAN NOT RESET AFTER SUBMIT PRESSED atm
    global temp_cards
    global word_label
    global score_label
    global offset
    global your_cards
    global your_cards_info
    global word_title
    global longest_word

    longest_word = ''

    if temp_cards:
        print(f'temp_cards True: {temp_cards}')
        for temp in temp_cards:
            deck.insert(0, temp)
    print(f'RESET PRESSED - DECK: {deck}')
    print(f'RESET PRESSED - DRAW CARD: {deck[10]}')

    offset = 0
    your_cards_info = {}

    for kw in your_cards:
        your_cards[kw].destroy()

    your_cards[0] = Button(root, image=deck[0].frontimage, command=lambda: clicked_card_in_hand(0))
    your_cards[1] = Button(root, image=deck[1].frontimage, command=lambda: clicked_card_in_hand(1))
    your_cards[2] = Button(root, image=deck[2].frontimage, command=lambda: clicked_card_in_hand(2))
    your_cards[3] = Button(root, image=deck[3].frontimage, command=lambda: clicked_card_in_hand(3))
    your_cards[4] = Button(root, image=deck[4].frontimage, command=lambda: clicked_card_in_hand(4))
    your_cards[5] = Button(root, image=deck[5].frontimage, command=lambda: clicked_card_in_hand(5))
    your_cards[6] = Button(root, image=deck[6].frontimage, command=lambda: clicked_card_in_hand(6))
    your_cards[7] = Button(root, image=deck[7].frontimage, command=lambda: clicked_card_in_hand(7))
    your_cards[8] = Button(root, image=deck[8].frontimage, command=lambda: clicked_card_in_hand(8))
    your_cards[9] = Button(root, image=deck[9].frontimage, command=lambda: clicked_card_in_hand(9))

    if face_down_card:       ## if you clked the faec down deck card revealing what it is...
        your_cards[10] = Button(root, image=back, command=lambda: do_nothing())
        your_cards[10].grid(row=2, column=2, padx=0, pady=25)
        your_cards[11] = Button(root, image=deck[11].frontimage, command=lambda: draw_from_deck()) ##THIS IS FACE DOWN DECK
        your_cards[11].grid(row=3, column=cards_per_hand, padx=0, pady=0)

    else:
        your_cards[10] = Button(root, image=deck[10].frontimage, command=lambda: draw_from_draw_pile())
        your_cards[10].grid(row=2, column=2, padx=0, pady=25)
        your_cards[11] = Button(root, image=back, command=lambda: clicked_deck())
        your_cards[11].grid(row=2, column=3, padx=0, pady=0)

    for kw in your_cards:
        if kw < cards_per_hand:
            your_cards[kw].grid(row=3, column=kw, padx=0, pady=0)

    temp_cards = []

offset = 0

def draw_from_draw_pile():
    global offset
    print('DREW A CARD FROM DRAW PILE')
    your_cards_info[10] = deck[10]
    your_cards[10].grid_configure(row=1, column=offset)
    your_cards[10].configure(command=do_nothing())
    print(f'your_cards_info: {your_cards_info}')
    offset += 1

def draw_from_deck():
    global offset
    your_cards_info[11] = deck[11]
    your_cards[11].grid_configure(row=1, column=offset)
    print(f'your_cards_info: {your_cards_info}')
    print(f'deck: {deck}')
    offset += 1

def clicked_deck():
    global face_down_card
    print('CLICKED DECK (FACE DOWN CARD)')
    face_down_card = True
    your_cards[11].configure(image=deck[11].frontimage)
    your_cards[11].configure(command=lambda:draw_from_deck())
    your_cards[11].grid(row=3, column=cards_per_hand, padx=0, pady=0)
    your_cards[10].configure(image=back)
    your_cards[10].configure(command=lambda: do_nothing())

def do_nothing():
    pass

def clicked_card_in_hand(index):
    global offset
    your_cards[index].grid_configure(row=1, column=offset)
    your_cards[index].configure(command=do_nothing)
    print(f'CLICKED CARD: {index}')
    your_cards_info[index] = deck[index]
    print(f'your_cards_info: {your_cards_info}')
    offset += 1
    print(f'deck: {deck}')

def discard_card():
    global turn
    print('DISCARD PRESSED')
    print(your_cards_info)
    if len(your_cards_info) == 1:
        turn = False
        if not face_down_card:
            print('deck card was not previously clicked')
            if list(your_cards_info.keys())[0] != 10:
                del deck[list(your_cards_info.keys())[0]]
                print('you want to pick up the draw card')
                deck.insert(0, deck.pop(9))
            elif list(your_cards_info.keys())[0] == 10:
                del deck[10]
        elif face_down_card:
            print('deck card was clicked')
            if list(your_cards_info.keys())[0] != 11:
                del deck[list(your_cards_info.keys())[0]]
                print('you want to pick up the deck card')
                deck.insert(0, deck.pop(10))
            elif list(your_cards_info.keys())[0] == 11:
                del deck[11]

        print(f'DISCARDING {your_cards_info}')
        print(f'DECK AFTER DISCARD: {deck}')

        for key in sorted(your_cards_info.keys(), reverse=True):
            your_cards[key].destroy()

        discarded_card = list(your_cards_info.values())[0]
        data_to_send = discarded_card.letter
        client_socket.sendall(pickle.dumps(data_to_send))  # 1ST SEND # DISCARD CARD TO BECOME SERVER DRAW CARD #

    else:
        print('YOU CAN ONLY DISCARD 1 CARD PER HAND')       #ADD something to pop up for user

cards_per_hand = 3

reset = Button(root, text="    RESET   ", padx=0, pady=50, highlightbackground='green', fg='white', command=lambda: reset_hand())
reset.grid(row=2, column=1, padx=25, pady=25)
submit = Button(root, text="SUBMIT WORD", padx=0, pady=50, command=submit, highlightbackground='green', fg='white')
submit.grid(row=2, column=6, padx=0, pady=25)
end_turn_button = Button(root, text="     DISCARD     ", padx=0, pady=50, highlightbackground='green', fg='white', command=lambda: discard_card())
end_turn_button.grid(row=2, column=7, padx=0, pady=25)
your_cards[10] = Button(root, image=deck[10].frontimage, command=lambda: draw_from_draw_pile())  # DATA RECVD = Here
your_cards[10].grid(row=2, column=2, padx=0, pady=25)
your_cards[11] = Button(root, image=back, command=lambda:clicked_deck())    ##  MAKE NEW FUNCTION: MOVES CARD TO YOUR HAND AREA ON FIRST CLICK
your_cards[11].grid(row=2, column=3, padx=0, pady=0)

your_cards[0] = Button(root, image=deck[0].frontimage, command=lambda: clicked_card_in_hand(0))
your_cards[1] = Button(root, image=deck[1].frontimage, command=lambda: clicked_card_in_hand(1))
your_cards[2] = Button(root, image=deck[2].frontimage, command=lambda: clicked_card_in_hand(2))
your_cards[3] = Button(root, image=deck[3].frontimage, command=lambda: clicked_card_in_hand(3))
your_cards[4] = Button(root, image=deck[4].frontimage, command=lambda: clicked_card_in_hand(4))
your_cards[5] = Button(root, image=deck[5].frontimage, command=lambda: clicked_card_in_hand(5))
your_cards[6] = Button(root, image=deck[6].frontimage, command=lambda: clicked_card_in_hand(6))
your_cards[7] = Button(root, image=deck[7].frontimage, command=lambda: clicked_card_in_hand(7))
your_cards[8] = Button(root, image=deck[8].frontimage, command=lambda: clicked_card_in_hand(8))
your_cards[9] = Button(root, image=deck[9].frontimage, command=lambda: clicked_card_in_hand(9))

for kw in your_cards:
    if kw < cards_per_hand:
        your_cards[kw].grid(row=3, column=kw, padx=0, pady=0)

print(f'FIRST DECK: {deck}')

game_state = 'PLAYING'

ppp = 0

game = True

while game:     # GAME LOOP #

    if game_state == 'PLAYING':

        round_label = Label(root, text=f'ROUND: {cards_per_hand - 2} (cards per hand): {cards_per_hand} ', bg='green')
        round_label.place(x=1, y=(1))

        if turn:         # WHILE ITS YOUR TURN #
            if ppp == 0:
                reset_hand()
            ppp += 1
            root.update()
            root.update_idletasks()

        else:
            face_down_card = False
            print('GAME STATE = PLAYING  -  TURN = FALSE')
            data = pickle.loads(client_socket.recv(2084 * 6))  # 1ST RECV # DISCARD CARD FROM CLIENT # BECOMES DRAW CARD
            print(f'RECEIVED: {data} FROM SERVER')

            if type(data) == list:
                last_turn = True
                end_turn_button.grid_forget() ### DELETE DISCARD BUTTON ###
                print(f'LIST CONTENTS: {data[0], data[1], data[2]}')
                new_draw_card = CARDS_DICT[data[0]]
                deck.insert(10, new_draw_card[0])
                del deck[11]

                their_words = data[1]
                their_longest_word_list = []

                for item in their_words:
                    their_longest_word_list.append(item[0])

                biggest = 1

                for w in their_longest_word_list:
                    if len(w) > biggest:
                        biggest = len(w)
                        their_longest_word = w

                print(f'their longest word: {their_longest_word}')

                if len(their_longest_word) > len(longest_word):
                    print('OPPONENT GETS 10 POINTS')
                    bonus_message = 'OPPONENT GETS 10 POINTS'
                elif len(their_longest_word) < len(longest_word):
                    print('YOU GET 10 POINTS')
                    bonus_message = 'YOU GET 10 POINTS'
                else:
                    print('NO ONE GETS 10 POINTS')
                    bonus_message = 'NO ONE GETS 10 POINTS'

                reset_hand()

                WORDS_LABEL = Label(root, text=f'THEY SPELLED: {data[1][0]}', bg='green')
                WORDS_LABEL.place(x=1100, y=(110))
                POINTS_LABEL = Label(root, text=f'THEIR POINTS: {data[2]}', bg='green')
                POINTS_LABEL.place(x=1100, y=(140))
                BONUS_LABEL = Label(root, text=f'BONUS: {bonus_message}', bg='green')
                BONUS_LABEL.place(x=730, y=(140))

                root.update()
                root.update_idletasks()
                turn = True

            elif type(data) == str:
                new_draw_card = CARDS_DICT[data]
                deck.insert(10, new_draw_card[0])
                del deck[11]
                temp_cards = {}
                reset_hand()
                root.update()
                root.update_idletasks()
                turn = True


    elif game_state == 'ROUND OVER':
        print('GAME STATE = ROUND OVER')
        face_down_card = False
        deck = ALL_CARDS.copy()     # NEW DECK
        random.shuffle(deck)
        print(f'\n\nNEW DECK?: {deck}')
        print(f'DRAW CARD: {deck[10]}\n\n')
        ppp = 0

        if not last_turn:
            print('CAN RECEIVE ONE LAST TIME')

            data = pickle.loads(client_socket.recv(2084 * 6))
            print(f'RECEIVED: {data} FROM SERVER')

            their_words = data[1]
            their_longest_word_list = []

            for item in their_words:
                their_longest_word_list.append(item[0])

            biggest = 1

            for w in their_longest_word_list:
                if len(w) > biggest:
                    biggest = len(w)
                    their_longest_word = w

            print(f'their longest word: {their_longest_word}')

            if len(their_longest_word) > len(longest_word):
                print('OPPONENT GETS 10 POINTS')
                bonus_message = 'OPPONENT GETS 10 POINTS'
            elif len(their_longest_word) < len(longest_word):
                print('YOU GET 10 POINTS')
                bonus_message = 'YOU GET 10 POINTS'
            else:
                print('NO ONE GETS 10 POINTS')
                bonus_message = 'NO ONE GETS 10 POINTS'

            WORDS_LABEL = Label(root, text=f'THEY SPELLED: {data[1][0]}', bg='green')
            WORDS_LABEL.place(x=1100, y=(110))
            POINTS_LABEL = Label(root, text=f'THEIR POINTS: {data[2]}', bg='green')
            POINTS_LABEL.place(x=1100, y=(140))
            BONUS_LABEL = Label(root, text=f'BONUS: {bonus_message}', bg='green')
            BONUS_LABEL.place(x=730, y=(140))

            end_turn_button.grid(row=2, column=7, padx=0, pady=25)
            reset_hand()
            root.update()
            root.update_idletasks()

            game_state = 'PLAYING'

            cards_per_hand += 1
            print(f'CARDS PER HAND: {cards_per_hand}')

            if cards_per_hand >= 11:
                print('GAME IS OVER')
                game_state = 'GAME OVER'

            if cards_per_hand % 2 == 1:  # IF NEW ROUND IS ODD
                turn = True
            else:
                print('PASS - EVEN ROUND')
                turn = False
        else:
            cards_per_hand += 1
            print('LAST TURN = TRUE')
            game_state = 'PLAYING'
            last_turn = False
            end_turn_button.grid(row=2, column=7, padx=0, pady=25)

            #DISPLAY LONGEST WORD / POINTS ANEW

            root.update()
            root.update_idletasks()

            if cards_per_hand >= 11:
                print('GAME IS OVER')
                game_state = 'GAME OVER'

            if cards_per_hand % 2 == 1:  # IF NEW ROUND IS ODD
                turn = True
                reset_hand()
                root.update()
                root.update_idletasks()
            else:
                print('PASS - EVEN ROUND')
                turn = False
                reset_hand()
                root.update()
                root.update_idletasks()

    elif game_state == 'GAME OVER':
        print('GAME STATE = GAME OVER')
        game = False

# FINAL SCREEN

for widget in root.winfo_children():
    widget.destroy()

# gather total points to display [and other info to display at end screen]

print(f'TOTAL POINTS: {total_points}')

last_label = Label(root, text=f'TOTAL SCORE: {total_points}', bg='green')
last_label.place(x=600, y=400)

root.mainloop()



# FIX SCORING

# ONLY SCORE BONUS IF WORD IS CORRECT

# WHEN YOU CLICKED CARD FROM YOUR HAND YOU SHOULD BE ABLE TO
# CLICK AGAIN AND HAVE IT RESET TO ORGINIAL POSITION IN HAND
