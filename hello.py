from flask import Flask, render_template, session, redirect, url_for
from flask_session.__init__ import Session
from tempfile import mkdtemp
from minimax import *
 
app = Flask(__name__)
 
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
 
@app.route("/")
def index():
 
    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
        session["winner"] = None

    return render_template("game.html", game=session["board"], turn=session["turn"], winner = session["winner"])
 
@app.route("/reset")
def reset(): 
    session.clear()
    return redirect(url_for("index"))

@app.route("/cpu")
def cpu(): 
    row = minimax(session["board"], session["turn"])[1]["row"]
    col = minimax(session["board"], session["turn"])[1]["col"]
    return redirect(f"/play/{row}/{col}")


@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["turn"]
    if session["turn"] == "X":
        session["turn"] = "O"
    else:
        session["turn"]  = "X"
    
    for x in range(0,3):
        if session["board"][x] == ["X", "X", "X"] or session["board"][x] == ["O", "O", "O"] or session["board"][0][x] == session["board"][1][x] == session["board"][2][x] != None: 
            session["winner"] = 1 
    if session["board"][0][0] == session["board"][1][1] == session["board"][2][2]!= None or session["board"][0][2] == session["board"][1][1] == session["board"][2][0] != None:
        session["winner"] = 1
        
    return redirect(url_for("index"))