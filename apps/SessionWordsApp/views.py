# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
# from time import gmtime, strftime
# from django.utils.timezone import localtime
from datetime import datetime


def index(request):
    if "logs" not in request.session:
        request.session["logs"] = []
    context = {
        "words" : request.session["logs"]
    }
    return render(request, "index.html", context)

def result(request):
    if request.method == "POST":
        time = (datetime.now().strftime("%I:%M %p"))
        word = request.POST["word"]
        color = request.POST["color"]
    if "bigfont" in request.POST:
        bigfont = request.POST["bigfont"]
    else:
        bigfont = False
    print word
    words = {
        "word" : word,
        "color" : color,
        "bigfont" : bigfont,
        "time" : time
    }
    request.session["logs"].append(words)

    request.session.modified = True
    
    print request.session["logs"]
    return redirect('/')


def clear(request):
    request.session.flush()
    return redirect('/')