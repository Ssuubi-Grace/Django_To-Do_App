from django.urls import path, re_path #added re_path during swagger installation
#from .views import home
from . import views
from .views import task_list, add_task
#configuring swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    #path('',home),
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list'), # Listing all tasks
    path('tasks/add/', views.add_task, name='add_task'),  # Creating a task
    path('tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),  # Updating a task
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),  # Deleting a task
]

#swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Task API",
        default_version="v1",
        description="API documentation for the To-Do List App",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="hopeliz835@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]