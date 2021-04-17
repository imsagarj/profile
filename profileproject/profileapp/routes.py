from django.urls import path
from .views import home, profile, edit_profile, delete_profile, ProfileClassView

urlpatterns = [
    path('', home, name="home"),
    # path('', ProfileClassView.as_view(), name="home"),
    path('/profile', profile, name="profile"),
    path('/edit_profile/<int:profile_id>', edit_profile, name="edit_profile"),
    path('/delete_profile/<int:profile_id>', delete_profile, name="delete_profile")
]
