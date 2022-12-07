from django.urls import path

from gameplay.game.views import home_page, edit_game, details_game, delete_game, game_create, \
    details_profile, create_profile, delete_profile, edit_profile, dashboard

urlpatterns = (
    path('', home_page, name='home page'),

    path('dashboard/', dashboard, name='show dashboard'),

    path('game/create/', game_create, name='create game'),
    path('game/edit/<int:pk>', edit_game, name='edit game'),
    path('game/details/<int:pk>', details_game, name='details game'),
    path('game/delete/<int:pk>', delete_game, name='delete game'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)

