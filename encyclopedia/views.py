from django.http.response import HttpResponse
from django.shortcuts import render
from . import util

from markdown2 import Markdown

markdowner = Markdown()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wikiPage(request, pageName):
    pageMarkdown = open(f"entries/{pageName}.md", "r")
    pageHtml = markdowner.convert(pageMarkdown.read())

    return render(request, "encyclopedia/wikiPage.html", {
        "content": pageHtml
    })
