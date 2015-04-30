#!/usr/bin/python3
from _codecs import raw_unicode_escape_decode

import players

__author__ = 'fox@vsetin.org'

from bottle import route, run
import page


@route('/')
def index():
    return page.index()


@route('/player/<player>/play')
def play(player):
    for p in players.Player.get():
        print(p, "==", player)
        if p == player:
            p.play()
            break
    return page.index()

run(host='localhost', port=8080, debug=True)






