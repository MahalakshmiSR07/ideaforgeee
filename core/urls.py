from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.home, name='home'),
    path('dashboard/add-project/', views.add_project, name='add_project'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('quiz/', views.quiz, name='quiz'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/<int:pk>/save/', views.save_project, name='save_project'),
    path('project/<int:pk>/remove/', views.remove_saved_project, name='remove_saved_project'),
    path('saved-projects/', views.saved_projects, name='saved_projects'),
    path('search/', views.search, name='search'),
    
    # OTP Password Reset URLs
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('password-reset/verify/', views.password_reset_verify, name='password_reset_verify'),
    path('password-reset/confirm/', views.password_reset_confirm_custom, name='password_reset_confirm_custom'),
]
