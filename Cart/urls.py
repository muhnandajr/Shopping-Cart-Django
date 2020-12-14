from django.conf.urls import url 
from Cart import views 
 
urlpatterns = [ 
    url(r'^api/cart$', views.cart_list),
    url(r'^api/cart/(?P<pk>[0-9]+)$', views.cart_detail),
]