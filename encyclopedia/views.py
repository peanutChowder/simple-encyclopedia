from logging import PlaceHolder
from django.http.response import HttpResponse
from django.shortcuts import render
from . import util

from markdown2 import Markdown
from django import forms

markdowner = Markdown()

class SearchForm(forms.Form):
    searchQuery = forms.CharField()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        matchingEntries = [entry for entry in util.list_entries() if searched.lower() in entry.lower()]
        
        return render(request, "encyclopedia/search.html", {
            'searched': searched,
            "matchingEntries": matchingEntries
        })
    else:
        return render(request, "encyclopedia/search.html", {})

def tester(request):
    return HttpResponse("hello")

def wikiPage(request, pageName):
    pageMarkdown = open(f"entries/{pageName}.md", "r")
    pageHtml = markdowner.convert(pageMarkdown.read())

    return render(request, "encyclopedia/wikiPage.html", {
        "content": pageHtml
    })
