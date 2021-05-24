from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tester", views.tester, name="tester"),
    path("wiki/<str:pageName>", views.wikiPage, name="wikiPage")
]
