from hashlib import new
from logging import PlaceHolder
import re
from django.core.exceptions import ValidationError
from django.http.response import HttpResponse
from django.shortcuts import render
from . import util

from markdown2 import Markdown
from django import forms

markdowner = Markdown()

class EntryForm(forms.Form):
    pageTitle = forms.CharField(label="Page Title", widget=forms.TextInput(attrs={"class": "entry-title"}))
    pageContent = forms.CharField(label="Page Content", widget=forms.Textarea(attrs={"class": "entry-content"}))

def index(request):
    return render(request, "encyclopedia/index.html", {})

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

def newEntry(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            newTitle = form.cleaned_data["pageTitle"]
            if newTitle.lower() in [title.lower() for title in util.list_entries()]:
                return render(request, "encyclopedia/new-entry.html", {
                    "entryForm": form,
                    "titleExists": True
                })
    return render(request, "encyclopedia/new-entry.html", {
        "entryForm": EntryForm(),
    })

def wikiPage(request, pageName):
    pageMarkdown = open(f"entries/{pageName}.md", "r")
    pageHtml = markdowner.convert(pageMarkdown.read())

    return render(request, "encyclopedia/wiki-page.html", {
        "content": pageHtml
    })

def allPages(request):
    return render(request, "encyclopedia/all-pages.html", {
        "entries": util.list_entries()
    })

def tester(request):
    return HttpResponse("hello")