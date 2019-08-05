from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index')]
urlpatterns += [path('update_clarification', views.receive, name="receive")]
urlpatterns += [path('delete', views.delete,name='delete')]
urlpatterns += [path('update_time', views.time_response, name="time_response")]
urlpatterns += [path('start', views.start, name="start")]
