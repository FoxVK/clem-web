#!/usr/bin/python3
from _codecs import raw_unicode_escape_decode

import players
import soundcards

__author__ = 'fox@vsetin.org'

from bottle import route, run, redirect
import page


@route('/')
def index():
    return page.index()


@route('/player/<player>/play')
def play(player):
    for p in players.Player.get():
        if p == player:
            p.play()
            break
    redirect("/")
    #return page.index()


@route('/player/<player>/stop')
def play(player):
    for p in players.Player.get():
        if p == player:
            p.stop()
            break
    redirect("/")


@route('/card/<cid:int>/inc/<val>')
def sound_inc(cid, val):
    print(val)
    list(soundcards.Card.get())[int(cid)].volume.inc(val)
    redirect("/")


@route('/card/<cid:int>/dec/<val>')
def sound_inc(cid, val):
    list(soundcards.Card.get())[int(cid)].volume.dec(val)
    redirect("/")


@route('/card/<cid:int>/set/<val>')
def sound_inc(cid, val):
    list(soundcards.Card.get())[int(cid)].volume = val
    redirect("/")


@route('/player/<player>/pause')
def play(player):
    for p in players.Player.get():
        if p == player:
            p.pause()
            break
    redirect("/")


@route('/player/<player>/next')
def play(player):
    for p in players.Player.get():
        if p == player:
            p.next()
            break
    redirect("/")


@route('/player/<player>/prev')
def play(player):
    for p in players.Player.get():
        if p == player:
            p.prev()
            break
    redirect("/")


@route('/player/<player>/track/<t:int>')
def play(player, t):
    for p in players.Player.get():
        if p == player:
            p.current_track = t
            print(t)
            break
    redirect("/")

run(host='0.0.0.0', port=8080, debug=True)






