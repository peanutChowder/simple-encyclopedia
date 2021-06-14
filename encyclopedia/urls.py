from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:pageName>", views.wikiPage, name="wiki-page"),
    path("search", views.search, name="search-page"),
    path("new-entry", views.newEntry, name="new-entry"),
    path("all-pages", views.allPages, name="all-pages"),

    path("tester", views.tester, name="tester")
]
