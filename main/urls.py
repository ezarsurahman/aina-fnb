from django.urls import path
from main.views import show_main, create_food_entry, show_xml, show_json ,show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_food, delete_food, add_food_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-food-entry', create_food_entry, name='create_food_entry'),
    path('xml/', show_xml , name='show_xml'),
    path('json/', show_json , name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('edit-food/<uuid:id>', edit_food, name="edit_food" ),
    path('delete-food/<uuid:id>', delete_food, name="delete_food"),
    path('create-ajax', add_food_entry_ajax, name="add_food_entry_ajax")
]