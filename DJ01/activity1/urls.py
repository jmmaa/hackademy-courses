from django.urls import path


from . import views

urlpatterns = [
    path("profile/", views.profile_view),
    path("register/", views.register_view),
    path("home/", views.home_view),
]
