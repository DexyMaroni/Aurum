from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo_app.urls')),  # Include the URLs from the todo_app
    
]
