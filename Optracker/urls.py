from django.conf.urls import url
from Optracker import views

urlpatterns = [
    url(r'^$',views.userform,name="userform"),
    url(r'^dash/new/f78ba4a3b33292549c3c8d5ebea144da$',views.dashboard,name='dashboard'),
    url(r'^export/csv/',views.export_users_csv,name="export_users_csv"),
    url(r'^dash/(?P<id>\d+)/edit/$',views.edit_post,name='edit'),
    url(r'^mainform/f78ba4a3b33292549c3c8d5ebea144da$',views.opform,name="opform"),
    url(r'^thankyou/$',views.thankyou,name="thankyou")

    #url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
]
