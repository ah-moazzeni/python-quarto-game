import sys
import time
from socketio import *
import pygame
import hashlib
import webbrowser
if sys.version_info < (3, 6):
    import sha3
#########pygame##########
pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("quato")
color = (12, 12, 12)
frame_per_second = 60
scale_img = (88.2, 88.2)
base_font = pygame.font.Font(None, 32)
bbase_font = pygame.font.Font(None, 42)
big_font = pygame.font.Font(None, 56)
small_font = pygame.font.Font(None, 29)
no_font = pygame.font.Font(None, 48)
yes = v_small_font = pygame.font.Font(None, 19)
v_big_font = pygame.font.Font(None, 70)


###########vars##############
def rraankk():
    global rank_txt1, rank_txt2, rank_txt3, rank_txt4, rank_txt5, rank_txt6, rank_txt7, rank_txt8, rank_txt9, rank_txt10, rank_txt11
    global rank_txt1s, rank_txt2s, rank_txt3s, rank_txt4s, rank_txt5s, rank_txt6s, rank_txt7s, rank_txt8s, rank_txt9s, rank_txt10s, rank_txt11s
    global rank_txt1d, rank_txt2d, rank_txt3d, rank_txt4d, rank_txt5d, rank_txt6d, rank_txt7d, rank_txt8d, rank_txt9d, rank_txt10d, rank_txt11d
    rank_txt1 = '1.'
    rank_txt2 = '2.'
    rank_txt3 = '3.'
    rank_txt4 = '4.'
    rank_txt5 = '5.'
    rank_txt6 = '6.'
    rank_txt7 = '7.'
    rank_txt8 = '8.'
    rank_txt9 = '9.'
    rank_txt10 = '10.'
    rank_txt11 = ''
    rank_txt1s = ''
    rank_txt2s = ''
    rank_txt3s = ''
    rank_txt4s = ''
    rank_txt5s = ''
    rank_txt6s = ''
    rank_txt7s = ''
    rank_txt8s = ''
    rank_txt9s = ''
    rank_txt10s = ''
    rank_txt11s = ''
    rank_txt1d = ''
    rank_txt2d = ''
    rank_txt3d = ''
    rank_txt4d = ''
    rank_txt5d = ''
    rank_txt6d = ''
    rank_txt7d = ''
    rank_txt8d = ''
    rank_txt9d = ''
    rank_txt10d = ''
    rank_txt11d = ''


rank_val = False
last = False
first_show = True
status1 = [False]
status2 = [False]
user_text = ''
pass_text = ''
new_player = False
temp_notif = ""
final_val = False
won = False
menu_val = True
wait_val = False
connect_val = False
count=0
tied=False
##########socket#############
client = Client()


def place_filler_help():
    if last:
        tempـimg.image = pygame.transform.scale(black, scale_img)
    else:
        tempـimg.image = pygame.transform.scale(wait, scale_img)


def user_check_check(s):
    global first_show
    global temp_notif
    if s == True:
        first_show = False
        refresh2()
    else:
        temp_notif = s
        start_btn.clicked = False


def rank_fill(s, q):
    global rank_txt1, rank_txt2, rank_txt3, rank_txt4, rank_txt5, rank_txt6, rank_txt7, rank_txt8, rank_txt9, rank_txt10, rank_txt11
    global rank_txt1s, rank_txt2s, rank_txt3s, rank_txt4s, rank_txt5s, rank_txt6s, rank_txt7s, rank_txt8s, rank_txt9s, rank_txt10s, rank_txt11s
    global rank_txt1d, rank_txt2d, rank_txt3d, rank_txt4d, rank_txt5d, rank_txt6d, rank_txt7d, rank_txt8d, rank_txt9d, rank_txt10d, rank_txt11d
    for i in s:
        if rank_txt1 == '1.':
            rank_txt1 += i[0]
            rank_txt1s = i[1]
            rank_txt1d = i[2]
        elif rank_txt2 == '2.':
            rank_txt2 += i[0]
            rank_txt2s = i[1]
            rank_txt2d = i[2]
        elif rank_txt3 == '3.':
            rank_txt3 += i[0]
            rank_txt3s = i[1]
            rank_txt3d = i[2]
        elif rank_txt4 == '4.':
            rank_txt4 += i[0]
            rank_txt4s = i[1]
            rank_txt4d = i[2]
        elif rank_txt5 == '5.':
            rank_txt5 += i[0]
            rank_txt5s = i[1]
            rank_txt5d = i[2]
        elif rank_txt6 == '6.':
            rank_txt6 += i[0]
            rank_txt6s = i[1]
            rank_txt6d = i[2]
        elif rank_txt7 == '7.':
            rank_txt7 += i[0]
            rank_txt7s = i[1]
            rank_txt7d = i[2]
        elif rank_txt8 == '8.':
            rank_txt8 += i[0]
            rank_txt8s = i[1]
            rank_txt8d = i[2]
        elif rank_txt9 == '9.':
            rank_txt9 += i[0]
            rank_txt9s = i[1]
            rank_txt9d = i[2]
        elif rank_txt10 == '10.':
            rank_txt10 += i[0]
            rank_txt10s = i[1]
            rank_txt10d = i[2]
        elif rank_txt11 == '' and q != None:
            rank_txt11 = str(q) + "." + s[q - 1][0]
            rank_txt11s = s[q - 1][1]
            rank_txt11d = s[q - 1][2]

@client.event
def connect():
    print("I'm connected!")


@client.event
def connect_error(data):
    print("The connection failed!")


@client.event
def disconnect():
    print("I'm disconnected!")

@client.event
def place_filler(data):
    print(data)
    if data == [1, 1]:
        base1_button1.image = tempـimg.image
        base1_button1.clicked = True
    elif data == [2, 1]:
        base1_button2.image = tempـimg.image
        base1_button2.clicked = True
    elif data == [3, 1]:
        base1_button3.image = tempـimg.image
        base1_button3.clicked = True
    elif data == [4, 1]:
        base1_button4.image = tempـimg.image
        base1_button4.clicked = True
    elif data == [1, 2]:
        base1_button5.image = tempـimg.image
        base1_button5.clicked = True
    elif data == [2, 2]:
        base1_button6.image = tempـimg.image
        base1_button6.clicked = True
    elif data == [3, 2]:
        base1_button7.image = tempـimg.image
        base1_button7.clicked = True
    elif data == [4, 2]:
        base1_button8.image = tempـimg.image
        base1_button8.clicked = True
    elif data == [1, 3]:
        base1_button9.image = tempـimg.image
        base1_button9.clicked = True
    elif data == [2, 3]:
        base1_button10.image = tempـimg.image
        base1_button10.clicked = True
    elif data == [3, 3]:
        base1_button11.image = tempـimg.image
        base1_button11.clicked = True
    elif data == [4, 3]:
        base1_button12.image = tempـimg.image
        base1_button12.clicked = True
    elif data == [1, 4]:
        base1_button13.image = tempـimg.image
        base1_button13.clicked = True
    elif data == [2, 4]:
        base1_button14.image = tempـimg.image
        base1_button14.clicked = True
    elif data == [3, 4]:
        base1_button15.image = tempـimg.image
        base1_button15.clicked = True
    elif data == [4, 4]:
        base1_button16.image = tempـimg.image
        base1_button16.clicked = True
    place_filler_help()


opp = ""


@client.event
def opp_finder(data1):
    global opp
    opp = data1
    print(opp, "connected as my opponent")


@client.event
def piece_chooser():
    tempـimg.image = pygame.transform.scale(black, (1, 1))
    status2[0] = True
    if count == 16:
        client.emit("s_tie",data=opp)

@client.event
def tie():
    global tied
    global final_val
    global last, wait_val
    status1[0] = False
    status2[0] = False
    last = True
    tied = True
    time.sleep(.5)
    final_val = True
    wait_val = False
    refresh2()



@client.event
def place_chooser(data):
    if data == "a":
        tempـimg.image = pygame.transform.scale(a_img, scale_img)
        game_button1.image = pygame.transform.scale(black, (1, 1))
    elif data == "b":
        tempـimg.image = pygame.transform.scale(b_img, scale_img)
        game_button2.image = pygame.transform.scale(black, (1, 1))
    elif data == "c":
        tempـimg.image = pygame.transform.scale(c_img, scale_img)
        game_button3.image = pygame.transform.scale(black, (1, 1))
    elif data == "d":
        tempـimg.image = pygame.transform.scale(d_img, scale_img)
        game_button4.image = pygame.transform.scale(black, (1, 1))
    elif data == "e":
        tempـimg.image = pygame.transform.scale(e_img, scale_img)
        game_button5.image = pygame.transform.scale(black, (1, 1))
    elif data == "f":
        tempـimg.image = pygame.transform.scale(f_img, scale_img)
        game_button6.image = pygame.transform.scale(black, (1, 1))
    elif data == "g":
        tempـimg.image = pygame.transform.scale(g_img, scale_img)
        game_button7.image = pygame.transform.scale(black, (1, 1))
    elif data == "i":
        tempـimg.image = pygame.transform.scale(i_img, scale_img)
        game_button8.image = pygame.transform.scale(black, (1, 1))
    elif data == "j":
        tempـimg.image = pygame.transform.scale(j_img, scale_img)
        l_game_button1.image = pygame.transform.scale(black, (1, 1))
    elif data == "k":
        tempـimg.image = pygame.transform.scale(k_img, scale_img)
        l_game_button2.image = pygame.transform.scale(black, (1, 1))
    elif data == "l":
        tempـimg.image = pygame.transform.scale(l_img, scale_img)
        l_game_button3.image = pygame.transform.scale(black, (1, 1))
    elif data == "m":
        tempـimg.image = pygame.transform.scale(m_img, scale_img)
        l_game_button4.image = pygame.transform.scale(black, (1, 1))
    elif data == "n":
        tempـimg.image = pygame.transform.scale(n_img, scale_img)
        l_game_button5.image = pygame.transform.scale(black, (1, 1))
    elif data == "o":
        tempـimg.image = pygame.transform.scale(o_img, scale_img)
        l_game_button6.image = pygame.transform.scale(black, (1, 1))
    elif data == "p":
        tempـimg.image = pygame.transform.scale(p_img, scale_img)
        l_game_button7.image = pygame.transform.scale(black, (1, 1))
    elif data == "q":
        tempـimg.image = pygame.transform.scale(q_img, scale_img)
        l_game_button8.image = pygame.transform.scale(black, (1, 1))
    status1[0] = True


@client.event
def first():
    global menu_val
    menu_val = False
    print("your fist")


@client.event
def second():
    global menu_val
    menu_val = False

    tempـimg.image = pygame.transform.scale(wait, (90, 90))
    print("your second")


@client.event
def final(data):
    global won
    global final_val
    global last, wait_val
    status1[0] = False
    status2[0] = False
    last = True
    time.sleep(.5)
    final_val = True
    wait_val = False
    if data == True:
        won = True
    else:
        won = False
    refresh2()
    print("done")


client.connect("http://127.0.0.1:5000")

#############images###################
ranking = pygame.image.load("image/rank.PNG").convert_alpha()
base1_img = pygame.image.load("image/base1.PNG").convert_alpha()
a_img = pygame.image.load("image/a.PNG").convert_alpha()
b_img = pygame.image.load("image/b.PNG").convert_alpha()
c_img = pygame.image.load("image/c.PNG").convert_alpha()
d_img = pygame.image.load("image/d.PNG").convert_alpha()
e_img = pygame.image.load("image/e.PNG").convert_alpha()
f_img = pygame.image.load("image/f.PNG").convert_alpha()
g_img = pygame.image.load("image/g.PNG").convert_alpha()
i_img = pygame.image.load("image/i.PNG").convert_alpha()
j_img = pygame.image.load("image/j.PNG").convert_alpha()
k_img = pygame.image.load("image/k.PNG").convert_alpha()
l_img = pygame.image.load("image/l.PNG").convert_alpha()
m_img = pygame.image.load("image/m.PNG").convert_alpha()
n_img = pygame.image.load("image/n.PNG").convert_alpha()
o_img = pygame.image.load("image/o.PNG").convert_alpha()
p_img = pygame.image.load("image/p.PNG").convert_alpha()
q_img = pygame.image.load("image/q.PNG").convert_alpha()
black = pygame.image.load("image/black.PNG").convert_alpha()
wait = pygame.image.load("image/wait.PNG").convert_alpha()
game_start = pygame.image.load("image/GO_TO_GAME.PNG").convert_alpha()
checkbox = pygame.image.load("image/checkbox.PNG").convert_alpha()
checked = pygame.image.load("image/checked.PNG").convert_alpha()
play = pygame.image.load("image/play.PNG").convert_alpha()
back = pygame.image.load("image/back.PNG").convert_alpha()
how = pygame.image.load("image/how.PNG").convert_alpha()
exit_ = pygame.image.load("image/exit.PNG").convert_alpha()
quit_ = pygame.image.load("image/quit.PNG").convert_alpha()


#######################
class button():
    def __init__(self, x, y, image, scale, a, b, atr, clicked=False):

        self.atr = atr
        self.a = a
        self.b = b
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = clicked

    def draw(self):
        global wait_val, rank_val
        global new_player,run
        global temp_notif, connect_val,count
        if self.atr == "2":
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    if len(password_asli) <= 7:
                        temp_notif = "your password must be at least 8 character"
                    elif user_text != '':
                        self.clicked = True
                        hashed_pass = hashlib.new("sha3_512", password_asli.encode())

                        if new_player:
                            client.emit("user_check",
                                        data={"user": user_text, "password": hashed_pass.hexdigest(), "val": True},
                                        callback=user_check_check)
                        else:
                            client.emit("user_check",
                                        data={"user": user_text, "password": hashed_pass.hexdigest(), "val": False},
                                        callback=user_check_check)
                    refresh2()
        elif self.atr == '3':
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    if self.b == 100:
                        self.image = pygame.transform.scale(checked, (15, 15))
                        checked_btn.image = pygame.transform.scale(checkbox, (15, 15))
                        self.clicked = True
                        checked_btn.clicked = False
                        new_player = True
                    elif self.b == 200:
                        self.image = pygame.transform.scale(checked, (15, 15))
                        checkbox_btn.image = pygame.transform.scale(checkbox, (15, 15))
                        self.clicked = True
                        checkbox_btn.clicked = False
                        new_player = False
        elif self.atr == '6':
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    wait_val = True
                    self.clicked = True
                    refresh()
                    if connect_val == False:
                        client.emit("game_start", data=user_text)
                    else:
                        client.emit("regame", data={"o": opp})
                    connect_val = True



        elif self.atr == "8":
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    webbrowser.open(
                        'https://www.aparat.com/v/odFOV/%D9%85%D8%B9%D8%B1%D9%81%DB%8C_%D8%A8%D8%A7%D8%B2%DB%8C_Quarto')

        elif self.atr == "4":
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    client.emit("rank", data=user_text, callback=rank_fill)
                    rraankk()
                    rank_val = True
        elif self.atr == "5":
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    rank_val = False


        elif self.atr == "7":
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    run=False

        elif self.atr == "0":
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and status1 == [True]:
                    self.clicked = True
                    client.emit("get_send_place", data={"place": (self.a, self.b), "opp": opp})
                    client.emit("place_adapt", data={"pls": (self.a, self.b), "opp": opp})
                    self.image = tempـimg.image
                    tempـimg.image = pygame.transform.scale(black, (1, 1))
                    status1[0] = False
                    count+=2
                    print(count)
        elif self.atr == "quit":
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                    self.clicked=True
                    client.emit("semi",data={"opp": opp})

        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and status2 == [True]:
                    client.emit("get_send_piece", data={"piece": self.atr, "opp": opp})
                    print(str({"piece": self.atr, "opp": opp}) + "sended")
                    self.clicked = True
                    tempـimg.image = pygame.transform.scale(self.image, scale_img)
                    self.image = pygame.transform.scale(black, (1, 1))
                    status2[0] = False


############buttons################
def refresh():
    global base1_button1, base1_button2, base1_button3, base1_button4, base1_button5, base1_button9, base1_button13, base1_button8, base1_button6
    global base1_button10, base1_button11, base1_button12, base1_button7, base1_button14, base1_button15, base1_button16, game_button1, game_button2
    global game_button3, game_button4, game_button5, game_button6, game_button7, game_button8, l_game_button1, l_game_button2, l_game_button3, l_game_button4
    global l_game_button5, l_game_button6, l_game_button7, l_game_button8, tempـimg,quit_btn,last,count,tied,won
    base1_button1 = button(290, 130, base1_img, 0.6, 1, 1, "0")
    base1_button2 = button(390, 130, base1_img, 0.6, 2, 1, "0")
    base1_button3 = button(490, 130, base1_img, 0.6, 3, 1, "0")
    base1_button4 = button(590, 130, base1_img, 0.6, 4, 1, "0")
    base1_button5 = button(290, 230, base1_img, 0.6, 1, 2, "0")
    base1_button9 = button(290, 330, base1_img, 0.6, 1, 3, "0")
    base1_button13 = button(290, 430, base1_img, 0.6, 1, 4, "0")
    base1_button8 = button(590, 230, base1_img, 0.6, 4, 2, "0")
    base1_button6 = button(390, 230, base1_img, 0.6, 2, 2, "0")
    base1_button10 = button(390, 330, base1_img, 0.6, 2, 3, "0")
    base1_button11 = button(490, 330, base1_img, 0.6, 3, 3, "0")
    base1_button12 = button(590, 330, base1_img, 0.6, 4, 3, "0")
    base1_button7 = button(490, 230, base1_img, 0.6, 3, 2, "0")
    base1_button14 = button(390, 430, base1_img, 0.6, 2, 4, "0")
    base1_button15 = button(490, 430, base1_img, 0.6, 3, 4, "0")
    base1_button16 = button(590, 430, base1_img, 0.6, 4, 4, "0")
    game_button1 = button(290, 560, a_img, 0.49, 0, 0, "a")
    game_button2 = button(20, 60, b_img, 0.49, 0, 0, "b")
    game_button3 = button(20, 160, c_img, 0.49, 0, 0, "c")
    game_button4 = button(20, 260, d_img, 0.49, 0, 0, "d")
    game_button5 = button(20, 360, e_img, 0.49, 0, 0, "e")
    game_button6 = button(20, 460, f_img, 0.49, 0, 0, "f")
    game_button7 = button(20, 560, g_img, 0.49, 0, 0, "g")
    game_button8 = button(390, 560, i_img, 0.49, 0, 0, "i")
    l_game_button1 = button(490, 560, j_img, 0.49, 0, 0, "j")
    l_game_button2 = button(890, 60, k_img, 0.49, 0, 0, "k")
    l_game_button3 = button(890, 160, l_img, 0.49, 0, 0, "l")
    l_game_button4 = button(890, 260, m_img, 0.49, 0, 0, "m")
    l_game_button5 = button(890, 360, n_img, 0.49, 0, 0, "n")
    l_game_button6 = button(890, 460, o_img, 0.49, 0, 0, "o")
    l_game_button7 = button(890, 560, p_img, 0.49, 0, 0, "p")
    l_game_button8 = button(590, 560, q_img, 0.49, 0, 0, "q")
    tempـimg = button(430, 18, black, 1, 0, 0, "12")
    quit_btn = button(733, 583, quit_, 1, 0, 0, "quit")
    last=False
    count=0
    tied=False
    won=False


def refresh2():
    global ranking_btn, exit_btn, how_btn, play_btn, back_btn
    ranking_btn = button(335, 280, ranking, 1, 0, 0, "4")
    exit_btn = button(335, 430, exit_, 1, 0, 0, "7")
    how_btn = button(335, 355, how, 1, 0, 0, "8")
    play_btn = button(335, 205, play, 1, 0, 0, "6")
    back_btn = button(654, 610, back, 1, 0, 0, "5")


start_btn = button(600, 540, game_start, 1, 0, 0, "2")
checkbox_btn = button(347.9, 528, checkbox, .366, 0, 100, "3")
checked_btn = button(347.9, 549, checked, .366, 0, 200, "3")

########

back_ground = pygame.Rect(0, 175, 1000, 350)
main_rect = pygame.Rect(245, 100, 500, 500)
main_rect_ = pygame.Rect(313, 180, 350, 334)
inp_rect = pygame.Rect(300, 300, 240, 32)
pass_rect = pygame.Rect(300, 430, 240, 32)
color_rect = pygame.Color('lightskyblue3')
color_rect_passive = pygame.Color('gray15')


####
def draw_():
    global menu_val, final_val
    screen.fill(color)
    base1_button1.draw()
    base1_button2.draw()
    base1_button3.draw()
    base1_button4.draw()
    base1_button5.draw()
    base1_button6.draw()
    base1_button7.draw()
    base1_button8.draw()
    base1_button9.draw()
    base1_button10.draw()
    base1_button11.draw()
    base1_button12.draw()
    base1_button13.draw()
    base1_button14.draw()
    base1_button15.draw()
    base1_button16.draw()
    game_button1.draw()
    game_button2.draw()
    game_button3.draw()
    game_button4.draw()
    game_button5.draw()
    game_button6.draw()
    game_button7.draw()
    game_button8.draw()
    l_game_button1.draw()
    l_game_button2.draw()
    l_game_button3.draw()
    l_game_button4.draw()
    l_game_button5.draw()
    l_game_button6.draw()
    l_game_button7.draw()
    l_game_button8.draw()
    tempـimg.draw()
    quit_btn.draw()
    pygame.display.update()


######3
def res():
    screen.fill(color)
    winner = v_big_font.render("you won the match", True, (255, 255, 255))
    loser = v_big_font.render("you lost the match", True, (255, 255, 255))
    tiedd= v_big_font.render("           tied       ", True, (255, 255, 255))
    pygame.draw.rect(screen, (20, 20, 20), back_ground)
    if won:
        screen.blit(winner, (273, 315))
    elif tied:
        screen.blit(tiedd, (280, 315))
    else:
        screen.blit(loser, (280, 315))
    pygame.display.update()


############
def menu():
    screen.fill(color)
    pygame.draw.rect(screen, color_rect, main_rect_, 2)
    ranking_btn.draw()
    play_btn.draw()
    how_btn.draw()
    exit_btn.draw()
    if wait_val:
        please = base_font.render("please wait till your opponent connect ...", True, (255, 255, 255))
        screen.blit(please, (290, 550))

    quarto = v_big_font.render("QUARTO", True, (255, 255, 255))
    screen.blit(quarto, (380, 90))

    pygame.display.update()


kk = pygame.Rect(245, 101, 500, 54)


############
def rank():
    screen.fill(color)
    pygame.draw.rect(screen, color_rect, main_rect, 2)
    back_btn.draw()
    ranking = big_font.render("RANKING", True, (255, 255, 255))
    p = bbase_font.render("player", True, (255, 255, 255))
    w = bbase_font.render("win", True, (255, 255, 255))
    l = bbase_font.render("lose", True, (255, 255, 255))
    r1 = bbase_font.render(rank_txt1, True, (255, 255, 255))
    r2 = bbase_font.render(rank_txt2, True, (255, 255, 255))
    r3 = bbase_font.render(rank_txt3, True, (255, 255, 255))
    r4 = bbase_font.render(rank_txt4, True, (255, 255, 255))
    r5 = bbase_font.render(rank_txt5, True, (255, 255, 255))
    r6 = bbase_font.render(rank_txt6, True, (255, 255, 255))
    r7 = bbase_font.render(rank_txt7, True, (255, 255, 255))
    r8 = bbase_font.render(rank_txt8, True, (255, 255, 255))
    r9 = bbase_font.render(rank_txt9, True, (255, 255, 255))
    r10 = bbase_font.render(rank_txt10, True, (255, 255, 255))
    r11 = bbase_font.render(rank_txt11, True, (255, 255, 255))
    r1d = bbase_font.render(rank_txt1d, True, (255, 255, 255))
    r2d = bbase_font.render(rank_txt2d, True, (255, 255, 255))
    r3d = bbase_font.render(rank_txt3d, True, (255, 255, 255))
    r4d = bbase_font.render(rank_txt4d, True, (255, 255, 255))
    r5d = bbase_font.render(rank_txt5d, True, (255, 255, 255))
    r6d = bbase_font.render(rank_txt6d, True, (255, 255, 255))
    r7d = bbase_font.render(rank_txt7d, True, (255, 255, 255))
    r8d = bbase_font.render(rank_txt8d, True, (255, 255, 255))
    r9d = bbase_font.render(rank_txt9d, True, (255, 255, 255))
    r10d = bbase_font.render(rank_txt10d, True, (255, 255, 255))
    r11d = bbase_font.render(rank_txt11d, True, (255, 255, 255))
    r1s = bbase_font.render(rank_txt1s, True, (255, 255, 255))
    r2s = bbase_font.render(rank_txt2s, True, (255, 255, 255))
    r3s = bbase_font.render(rank_txt3s, True, (255, 255, 255))
    r4s = bbase_font.render(rank_txt4s, True, (255, 255, 255))
    r5s = bbase_font.render(rank_txt5s, True, (255, 255, 255))
    r6s = bbase_font.render(rank_txt6s, True, (255, 255, 255))
    r7s = bbase_font.render(rank_txt7s, True, (255, 255, 255))
    r8s = bbase_font.render(rank_txt8s, True, (255, 255, 255))
    r9s = bbase_font.render(rank_txt9s, True, (255, 255, 255))
    r10s = bbase_font.render(rank_txt10s, True, (255, 255, 255))
    r11s = bbase_font.render(rank_txt11s, True, (255, 255, 255))
    screen.blit(r1, (275, 165))
    screen.blit(r2, (275, 200))
    screen.blit(r3, (275, 235))
    screen.blit(r4, (275, 270))
    screen.blit(r5, (275, 305))
    screen.blit(r6, (275, 340))
    screen.blit(r7, (275, 375))
    screen.blit(r8, (275, 410))
    screen.blit(r9, (275, 445))
    screen.blit(r10, (275, 480))
    screen.blit(r11, (275, 515))
    screen.blit(r1s, (485, 165))
    screen.blit(r2s, (485, 200))
    screen.blit(r3s, (485, 235))
    screen.blit(r4s, (485, 270))
    screen.blit(r5s, (485, 305))
    screen.blit(r6s, (485, 340))
    screen.blit(r7s, (485, 375))
    screen.blit(r8s, (485, 410))
    screen.blit(r9s, (485, 445))
    screen.blit(r10s, (485, 480))
    screen.blit(r11s, (485, 515))
    screen.blit(r1d, (683, 165))
    screen.blit(r2d, (683, 200))
    screen.blit(r3d, (683, 235))
    screen.blit(r4d, (683, 270))
    screen.blit(r5d, (683, 305))
    screen.blit(r6d, (683, 340))
    screen.blit(r7d, (683, 375))
    screen.blit(r8d, (683, 410))
    screen.blit(r9d, (683, 445))
    screen.blit(r10d, (683, 480))
    screen.blit(r11d, (683, 515))
    screen.blit(p, (275, 113))
    screen.blit(l, (465, 113))
    screen.blit(w, (665, 113))
    screen.blit(ranking, (395, 50))
    pygame.draw.rect(screen, color_rect, kk, 2)
    pygame.display.update()


##############################
def show():
    screen.fill(color)
    checkbox_btn.draw()
    checked_btn.draw()
    start_btn.draw()
    pygame.draw.rect(screen, color_rect, main_rect, 2)
    if user_active:
        pygame.draw.rect(screen, color_rect, inp_rect, 2)
    else:
        pygame.draw.rect(screen, color_rect_passive, inp_rect, 2)
    if pass_active:
        pygame.draw.rect(screen, color_rect, pass_rect, 2)
    else:
        pygame.draw.rect(screen, color_rect_passive, pass_rect, 2)
    letsgo = big_font.render("let's go", True, (255, 255, 255))
    notification = no_font.render(temp_notif, True, (255, 255, 255))
    new = small_font.render("new player ?", True, (255, 255, 255))
    yes = v_small_font.render("Yes", True, (255, 255, 255))
    no = v_small_font.render("No", True, (255, 255, 255))
    username = base_font.render("USER_NAME:", True, (255, 255, 255))
    password = base_font.render("PASSWORD:", True, (255, 255, 255))

    user_surface = base_font.render(user_text, True, (255, 255, 255))
    pass_surface = base_font.render(pass_text, True, (255, 255, 255))
    screen.blit(new, (300, 500))
    screen.blit(letsgo, (300, 150))
    screen.blit(username, (300, 270))
    screen.blit(password, (300, 400))
    screen.blit(yes, (300, 528))
    screen.blit(no, (301, 549))
    screen.blit(notification, (150, 40))

    screen.blit(user_surface, (inp_rect.x + 5, inp_rect.y + 5))
    screen.blit(pass_surface, (pass_rect.x + 5, pass_rect.y + 11))
    inp_rect.w = max(200, user_surface.get_width() + 10)
    pass_rect.w = max(200, pass_surface.get_width() + 10)

    pygame.display.update()


#####################################


user_active = False
pass_active = False
password_asli = ''

run = True
######################################
def main():
    global run
    global user_active
    global user_text
    global pass_active
    global pass_text
    global password_asli, final_val, menu_val
    clock = pygame.time.Clock()

    while run:
        clock.tick(frame_per_second)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pass_rect.collidepoint(event.pos):
                    pass_active = True
                    user_active = False

                else:
                    pass_active = False

                if inp_rect.collidepoint(event.pos):
                    user_active = True
                    pass_active = False
                else:
                    user_active = False

            if event.type == pygame.KEYDOWN:
                if pass_active:

                    if event.key == pygame.K_BACKSPACE:
                        pass_text = pass_text[:-1]
                        password_asli = password_asli[:-1]
                    else:
                        pass_text += "*"
                        password_asli += event.unicode
                if user_active:

                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
        if first_show:
            show()
        elif rank_val:
            rank()
        elif final_val:
            res()
            time.sleep(3)
            menu_val = True
            final_val = False
        elif menu_val:
            menu()
        else:
            draw_()

    pygame.quit()
    client.disconnect()


if __name__ == "__main__":
    main()
