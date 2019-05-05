from django.conf.urls import url
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$',views.store, name='index')
    ]