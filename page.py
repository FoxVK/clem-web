__author__ = 'fox'

import players
from socket import gethostname
import soundcards

def index():
    head = ''
    body = ''

    head += "<title>" + gethostname() + "</title>"

    body += "<h1>Sound Cards:</h1>\n"

    for card in soundcards.Card.get():
        inc_values = [10, 5, 1]
        dec_values = inc_values[:]
        inc_values.reverse()
        body += "\t\t<b>{0}:</b>" .format(str(card))

        for v in dec_values:
            body += "<a href=/card/{0}/dec/{1}><button>-{1}%</button></a>  ".format(int(card), v)

        body += str(int(card.volume))+"%"

        for v in inc_values:
            body += "<a href=/card/{0}/inc/{1}><button>+{1}%</button></a>  ".format(int(card), v)

    body += "<h1>Players:</h1>\n"

    for plr in players.Player.get():
        body += "<h3>" + str(plr) + "</h3>\n"
        ppath = "/player/" + str(plr) + "/"
        body += ''' <a href={0}play><button>Play</button></a>
                    <a href={0}pause><button>Pause</button></a>
                    <a href={0}stop><button>Stop</button></a>
                    <a href={0}prev><button>Prev</button></a>
                    <a href={0}next><button>Next</button></a>
                    <hr>
                '''.format(ppath)

        tracks = []
        current = plr.current_track
        for t in plr.tracks:
            b, be = "", ""
            if t == current:
                b, be = "<b>", "</b>"

            b += "<a href={0}track/{1}>".format(ppath, int(t))
            be = "</a>" + be

            tracks.append("<tr> <td>{2}{0}{3}</td><td>{2}{1}{3}</td> </tr>".format(str(t), t.strlen(), b, be))

        body += "\n<table border=1>\n\t{0}\n\t</table>\n".format("\n\t".join(tracks))

    return "<html>\n <head>\n" + head + "</head>\n<body>\n" + body + "</body>\n</html>\n"