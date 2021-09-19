from django.urls import path

from . import views

app_name = "courses"
urlpatterns = [
    path('', views.index, name="index"),
    path('<c_id>', views.course, name="course"),
    path('<c_id>/book', views.books, name="book"),
    path('<c_id>/cancel', views.cancel_enrollment,name="cancel"),

]