from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:pageName>", views.wikiPage, name="wiki-page"),
    path("search", views.search, name="search-page"),
    path("wiki/newEntry", views.newEntry, name="new-entry"),

    path("tester", views.tester, name="tester")
]
