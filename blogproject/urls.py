from django.contrib import admin
from django.urls import path
from django.conf import settings
import accounts.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),

    path('blog/<int:pk>', blog.views.detail, name='detail'),
    path('blog/new/', blog.views.new, name='new'),
    path('blog/newblog/', blog.views.create, name = "newblog"),
    path('blog/update/<int:pk>', blog.views.update, name="update"),
    path('blog/delete/<int:pk>', blog.views.delete, name='delete'),
    path('blog/add_comment/<int:pk>', blog.views.add_comment, name='add_comment'),

    path('accounts/signup/', accounts.views.signup, name='signup'),
    path('accounts/login/', accounts.views.login, name='login'), 
    path('accounts/accounts/logout/', accounts.views.logout, name='logout'),
]
