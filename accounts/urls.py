from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name='user-login'),
    path('profile/', views.profile, name='user-profile'),
    path('profile/update/', views.profile_update,
         name='user-profile-update'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
    name='user-logout'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)