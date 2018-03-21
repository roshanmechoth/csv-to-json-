from django.conf.urls import  url,include
import views


urlpatterns =[
    
    url(r'^create-sccode/(\d+)/$', views.create_sccode, name='create_sccode'),
    # url(r'^view/pdf/$', views.clients, name='print_clients'),
    

]

