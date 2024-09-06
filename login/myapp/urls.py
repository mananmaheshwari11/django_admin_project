from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from pathlib import Path
urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('view/<str:slug>',views.view,name='view'),
    path('update/<int:s_id>',views.update,name='update'),
    path('makeupdate/<int:s_id>',views.makeupdate,name='makeupdate'),
    path('delete/<int:s_id>',views.delete,name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)