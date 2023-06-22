from mcstatus import JavaServer
from datetime import datetime
from flask import Flask

server_address = "" #include port
gif_url = "https://media.tenor.com/O0TyL2rC55AAAAAC/minecraft.gif"
create_year = 1924
create_month = 6
create_day = 22
app = Flask(__name__)


def players():
    return JavaServer.lookup(server_address).query().players.names


def players_formatted_into_html():
    bwomp = ""
    for pl in players():
        bwomp += '<div class="inner-div">'
        bwomp += '<img src="https://mc-heads.net/avatar/' + pl + '" width="24" height="24">'
        bwomp += '<p class="player-name">' + pl + '</p>'
        bwomp += '</div>'
    return '<div class="centered-div">' + bwomp + '</div>'


def gif():
    return gif_url


def time_from():
    today = datetime.now()
    date_created = datetime(create_year, create_month, create_day)
    months = (today.year - date_created.year) * 12 + (today.month - date_created.month)
    return months


def index_file():
    return ("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Server Name Here</title>
    <link href='https://fonts.googleapis.com/css?family=Comfortaa' rel='stylesheet'>
    <style>
        body {
            font-family: 'Comfortaa';
            background-image: url("imageurl.gif");
            background-color: #cccccc;
            background-repeat: no-repeat;
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }

        .centered-div {
            background-color: #3e3f40;
            border-radius: 10px;
            padding: 10px;
            width: 850px;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 10px;
        }

        .inner-div {
            font-size: 24px;
            color: white;
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }

        .player-name {
            margin-left: 6px; 
        }

        .div-space {
            height: 10px;
        }
    </style>
</head>
<body>
    <h1 style="font-size: 60px; color: white;">Server Name Here</h1>
    <br>
    <div class="centered-div">
       <p style="font-size: 24px; color: white;">hi hi hi so uhh yeah this server was made on 6/22/1924 which was uhh like beandi months ago uhh so yeah uhhhhhhhh join lorem ipsum or whatnot filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text filler text</p> 
    </div>
    <br>
    <h1 style="font-size: 60px; color: white;">Online Players</h1>
    <div class="centered-div">
       ghhiuihfdhikgfdkfdjhggggggggggggghghhrhrhthrrytyhtrytythryhtryt
    </div>
</body>
</html>
""".replace("imageurl.gif", gif()).replace("beandi", str(time_from()))).replace(
        "ghhiuihfdhikgfdkfdjhggggggggggggghghhrhrhthrrytyhtrytythryhtryt", players_formatted_into_html())


@app.route("/")
def hello():
    return index_file()


if  __name__ == '__main__':
    app.run(host="127.0.0.1", port=8912)
