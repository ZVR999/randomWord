# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string 



def index(request):
    return render(request, 'random_word/index.html')

def random(request):
    if not 'counter' in request.session:
        request.session['counter'] = 1
    request.session['counter'] += 1
    print request.session['counter']

    request.session['suby'] = request.POST['suby']
    
    if request.session['suby'] == 'random':    
        random = {
            'word': get_random_string(length=14)
        }
    else:
        random = {
            'word': ''
        }
    print request.session['suby']
    return render(request, 'random_word/index.html', random)

def reset(request):
    if 'counter' in request.session:
        request.session['counter'] = 0
    if 'suby' in request.session:
        request.session['suby'] = ''
    return redirect('/')