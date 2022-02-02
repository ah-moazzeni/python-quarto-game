from socketio import *
from gevent import pywsgi
from logic_server import *

server = Server(async_mode='gevent')
temp8 = {}


@server.event
def connect(sid, environ, auth):
    print(sid, "connected")


@server.event
def game_start(sid, data):
    global temp8
    temp8.update({str(sid): data})
    print(temp8)
    stat = user_match(sid)
    if stat[0]:
        clear_()
        player1 = stat[1]
        player2 = stat[2]
        server.emit("opp_finder", player1, room=player2)
        server.emit("opp_finder", player2, room=player1)
        server.emit("piece_chooser", room=player1)
        server.emit("first", room=player1)
        server.emit("second", room=player2)


t = True


@server.event
def regame(sid, data):
    global t, w
    if t:
        t = False
    else:
        clear_()
        server.emit("second", room=data["o"])
        server.emit("first", room=sid)
        server.emit("piece_chooser", room=sid)
        t = True


@server.event
def user_check(sid, data):
    return u_name(data)

@server.event
def disconnect(sid):
    print('disconnect ', sid)


@server.event
def get_send_piece(sid, data):
    server.emit("place_chooser", data["piece"], room=data["opp"])
    matcher(data["piece"], "piece")


@server.event
def get_send_place(sid, data):
    vall, kindd = matcher(data["place"], "place")
    if vall == True:
        print(kindd)
        print(vall)
        server.emit("final", data=False, room=data["opp"])
        server.emit("final", data=True, room=sid)
        result({"username": temp8[str(sid)], "value": True})
        result({"username": temp8[str(data["opp"])], "value": False})
        print("_done_")
    else:
        server.emit("piece_chooser", room=sid)
count=0
@server.event
def s_tie(sid , data):
    global count
    count+=1
    if count%2==0:
        server.emit("tie",room=data)
        server.emit("tie", room=sid)
@server.event
def semi(sid, data):
    server.emit("final", data=True, room=data["opp"])
    server.emit("final", data=False, room=sid)
    result({"username": temp8[str(sid)], "value": False})
    result({"username": temp8[str(data["opp"])], "value": True})
    print("done_semi")


@server.event
def place_adapt(sid, data):
    server.emit("place_filler", data["pls"], room=data["opp"])
    print(data)


@server.event
def rank(sid, data):
    return rank_finder(data)


app = WSGIApp(server)
pywsgi.WSGIServer(("127.0.0.1", 5000), app).serve_forever()
