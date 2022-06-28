from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create, name="create"),
    path('create/item/', views.create_item, name="create_item"),
    path('create/champion/', views.create_champion, name='create_champion'),
    path('list/', views.list, name='list'),
    path('list/champion/', views.list_champions, name='list_champions'),
    path('list/champion/<slug:slug>/', views.champion_detail, name='champion_detail'),
    path('list/item/', views.list_items, name="list_items"),
    path('list/item/<slug:slug>/', views.item_detail, name='item_detail'),
    # path('crispy/', views.crispy_view, name='crispy'),

]
