from django.urls import path
from .views import FileViewSet, index

file_list = FileViewSet.as_view({
    'get': 'list_files',
})

file_upload = FileViewSet.as_view({
    'post': 'upload',
})

file_detail = FileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'delete',
})

urlpatterns = [
    path('', index),
    path('files/', file_list),
    path('files/upload/', file_upload),
    path('files/<int:pk>/', file_detail),
]