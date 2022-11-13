from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    prin=request.POST.get('text','default')
    rmp=request.POST.get('removepunc','off')
    pun='|\/><,.)'''' (.?|}{:[]#$@;"''][|)(&^%$#@'''
    an=""
    if rmp=='on':

     for char in prin:
        if char not in pun:
            an=an+char

     prin=an;
    cont = {
        'purpose': 'Remove Punctuation',
        'analyzed_text': prin
    }
    return render(request,'analyze.html',cont)


