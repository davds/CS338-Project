from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path("profile/<username>/", views.profile, name="profile"),
    path("profile/<username>/edit", views.profile_edit, name="editprofile"),
    path("profile/", views.myprofile, name="myprofile"),
    path("update/<username>/", views.profile_update, name="updateprofile"),
    path("search/", views.search, name="search"),
    path("search/<username>/", views.searchByUsername, name="searchByUsername"),
]