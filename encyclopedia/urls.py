from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:pageName>", views.wikiPage, name="wiki-page"),
    path("wiki/<str:pageName>/edit", views.editEntry, name="edit-entry"),
    path("search", views.search, name="search-page"),
    path("new-entry", views.newEntry, name="new-entry"),
    path("random-page", views.randomPage, name="random-page"),
    path("all-pages", views.allPages, name="all-pages"),

    path("tester", views.tester, name="tester")
]
