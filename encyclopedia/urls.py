from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:pageName>", views.wikiPage, name="wikiPage"),

    path("tester", views.tester, name="tester"),
    path("search", views.search, name="search-page")

]
