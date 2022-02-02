
lst_row1 = []
lst_row2 = []
lst_row3 = []
lst_row4 = []
lst_col1 = []
lst_col2 = []
lst_col3 = []
lst_col4 = []
lst_diag1 = []
lst_diag2 = []


def clear_():
    """
    it will clear all data  in places
    """
    lst_diag1.clear()
    lst_diag2.clear()
    lst_row1.clear()
    lst_row2.clear()
    lst_row3.clear()
    lst_row4.clear()
    lst_col1.clear()
    lst_col2.clear()
    lst_col3.clear()
    lst_col4.clear()


def result(data):
    """

    :param data: the name of winner or loser and the state of winnig or losing
    it will write it in data_base
    """
    text = []
    with open("scour.txt", "r+") as s:
        for line in s:
            t = []
            l = line.split()
            if l[0] != "game":
                t.append(l[0])
                t.append(l[1])
                t.append(l[2])
                text.append(t)
    with open("scour.txt", "w") as s:
        s.write("")
    with open("scour.txt", "a") as s:
        s.write("game \t lost \t win")
        check = True
        for line in text:
            if line[0] == data["username"]:

                check = False
                if data["value"]:
                    sc = int(line[2]) + 1
                    s.write("\n" + str(data["username"]) + "\t" + str(line[1]) + "\t" + str(sc))
                else:
                    sc = int(line[1]) + 1
                    s.write("\n" + str(data["username"]) + "\t" + str(sc) + "\t" + str(line[2]))
            else:

                s.write("\n" + str(line[0]) + "\t" + str(line[1]) + "\t" + str(line[2]))
        if check:

            if data["value"]:
                s.write("\n" + str(data["username"]) + "\t" + "0" + "\t" + "1")
            else:
                s.write("\n" + str(data["username"]) + "\t" + "1" + "\t" + "0")


def u_name(data):
    """

    it will check password errors

    """
    with open('password.txt', 'r+') as pass_file:
        temp = []
        if data["val"]:
            for line in pass_file:
                temp.append(line)
                l = line.split()
                if l[0] == data["user"]:
                    return "                 your username is used           "
            pass_file.write("\n" + str(data["user"] + "\t" + str(data["password"])))
            return True
        if not data["val"]:
            for line in pass_file:
                l = line.split()
                if l[0] == data["user"]:
                    if l[1] == data["password"]:
                        return True
                    else:
                        return "             your password in not correct       "
            return "                    username not found            "


def rank_finder(data):

    """
    :param data:username
    :return: scour board
    """
    with open("scour.txt", "r") as scs:
        s = []
        rank = []
        for line in scs:
            t = []
            l = line.split()
            if l[0] != "game":
                t.append(l[0])
                t.append(l[1])
                t.append(l[2])
                t.append(int(l[2]) - int(l[1]))
                s.append(int(l[2]) - int(l[1]))
                rank.append(t)

    txt = []
    flag = False
    print(t)
    s = list(set(s))
    for _ in range(len(s)):
        x = max(s)
        print(x)
        print(rank)
        for i in rank:
            if i[3] == x:
                aa=[]
                aa.append(str(i[0]))
                aa.append(str(i[1]))
                aa.append(str(i[2]))
                txt.append(aa)
                if i[0]==data:
                    flag = True
                    rotbe=txt.index(aa)+1
        s.remove(x)
    if flag and rotbe>10:
        return txt ,rotbe
    return txt , None


def identify(lst):
    """
    it identify pieces
    """
    res = []
    for mot in lst:
        if mot == "a":
            res.append(a)
        elif mot == "b":
            res.append(b)
        elif mot == "c":
            res.append(c)
        elif mot == "d":
            res.append(d)
        elif mot == "e":
            res.append(e)
        elif mot == "f":
            res.append(f)
        elif mot == "g":
            res.append(g)
        elif mot == "i":
            res.append(i)
        elif mot == "j":
            res.append(j)
        elif mot == "k":
            res.append(k)
        elif mot == "l":
            res.append(l)
        elif mot == "m":
            res.append(m)
        elif mot == "n":
            res.append(n)
        elif mot == "o":
            res.append(o)
        elif mot == "p":
            res.append(p)
        elif mot == "q":
            res.append(q)
    return winner_checker(*res)


def matcher(data, condition):
    """

    :param data: piece or place
    :param condition: piece or place
    it will connect piece and place
    """
    temp_ = []
    global piece
    if condition == "piece":
        piece = data
    elif condition == "place":
        if data[0] == 1:
            lst_col1.append(piece)
            temp_.append(lst_col1)
            if data[1] == 1:
                lst_diag1.append(piece)
                temp_.append(lst_diag1)
            elif data[1] == 4:
                lst_diag2.append(piece)
                temp_.append(lst_diag2)
        elif data[0] == 2:
            lst_col2.append(piece)
            temp_.append(lst_col2)
            if data[1] == 2:
                lst_diag1.append(piece)
                temp_.append(lst_diag1)
            elif data[1] == 3:
                lst_diag2.append(piece)
                temp_.append(lst_diag2)
        elif data[0] == 3:
            lst_col3.append(piece)
            temp_.append(lst_col3)
            if data[1] == 3:
                lst_diag1.append(piece)
                temp_.append(lst_diag1)
            elif data[1] == 2:
                lst_diag2.append(piece)
                temp_.append(lst_diag2)
        elif data[0] == 4:
            lst_col4.append(piece)
            temp_.append(lst_col4)
            if data[1] == 4:
                lst_diag1.append(piece)
                temp_.append(lst_diag1)
            elif data[1] == 1:
                lst_diag2.append(piece)
                temp_.append(lst_diag2)
        if data[1] == 1:
            lst_row1.append(piece)
            temp_.append(lst_row1)
        elif data[1] == 2:
            lst_row2.append(piece)
            temp_.append(lst_row2)
        elif data[1] == 3:
            lst_row3.append(piece)
            temp_.append(lst_row3)
        elif data[1] == 4:
            lst_row4.append(piece)
            temp_.append(lst_row4)
        piece = ""
        for i in temp_:
            if len(i) == 4:
                print(i, "is going to be checked")

                val, kind = identify(i)
                print(val,i)
                if val:
                    return True, kind
        return False, None


def winner_checker(piece1, piece2, piece3, piece4):
    '''
    this function runs to check the pieces parameter to be the same
    '''
    if all( [piece1.color == i.color for i in [piece2,piece3,piece4]]):
        print("color")
        return True, "color"

    elif all([piece1.background_color == i.background_color for i in [piece2, piece3, piece4]]):
        print("back")
        return True, "back"

    elif all([piece1.letter == i.letter for i in [piece2, piece3, piece4]]):
        print("letter")
        return True, "letter"

    elif all([piece1.shape == i.shape for i in [piece2, piece3, piece4]]):
        print("shape")
        return True, "shape"
    return False, None


##########

if __name__ == "--main__":
    winner_checker()
user = ""


def user_match(data):
    """

    it matches users
    """
    global user
    if user == "":
        user = data
        return (False,)
    else:
        temp = user
        user = ""
        return (True, temp, data)


class game_pieces:
    def __init__(self, color, background_color, letter, shape):
        self.color = color
        self.background_color = background_color
        self.letter = letter
        self.shape = shape

###############pieces#########################
a = game_pieces("white", "black", "A", "square")
b = game_pieces("black", "white", "A", "square")
c = game_pieces("white", "black", "A", "circle")
d = game_pieces("black", "white", "A", "circle")
e = game_pieces("black", "black", "A", "square")
f = game_pieces("white", "white", "A", "square")
g = game_pieces("black", "black", "A", "circle")
i = game_pieces("white", "white", "A", "circle")
j = game_pieces("white", "black", "B", "square")
k = game_pieces("black", "white", "B", "square")
l = game_pieces("white", "black", "B", "circle")
m = game_pieces("black", "white", "B", "circle")
n = game_pieces("black", "black", "B", "square")
o = game_pieces("white", "white", "B", "square")
p = game_pieces("black", "black", "B", "circle")
q = game_pieces("white", "white", "B", "circle")
