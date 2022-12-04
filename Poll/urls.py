from django.urls import path 
from .views import PostList, PartyResultList, PostList2

urlpatterns = [ 
    path('', PostList.as_view(), name = 'post-list'),
    path('create/', PartyResultList.as_view(), name = 'create-list'),    
    path('Total/', PostList2, name = 'post-list'),

]