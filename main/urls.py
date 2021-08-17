from django.urls import path

from .views import index, create, update, delete, log, region_create, region_update, region_index, region_delete
urlpatterns = [
    path('', index, name='main_index'),
    path('log/', log, name='main_log'),
    path('create/', create, name='main_create'),
    path('update/<int:id>/', update, name='main_update'),
    path('delete/<int:id>/', delete, name='main_delete'),
    path('region/create/<int:id>/', region_create, name="main_region_create"),
    path('region/update/<int:id>/', region_update, name="main_region_update"),
    path('region/index/<int:id>/', region_index, name="main_region_index"),
    path('region/delete/<int:id>-<int:cid>/', region_delete, name="main_region_delete")
]