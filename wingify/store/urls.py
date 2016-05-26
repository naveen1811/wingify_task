from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add_product/$', views.add_product),
    url(r'^get_product/$', views.get_product),
    url(r'^edit_product/(?P<id>\d+)$', views.edit_product),
    url(r'^delete_product/$',views.delete_product)
]