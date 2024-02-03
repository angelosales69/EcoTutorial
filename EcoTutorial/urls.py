from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="homeagri"),
    path('about/', views.about_page, name="aboutagri"),
    path('tutorial/', views.tutorial_page, name="tutorialagri"),
    path('contact/', views.contact_page, name="contactagri"),
    path('tutorialform/', views.tutorialform_page, name="tutorialformagri"),
    path('dashboard/', views.admindashboard_page, name="dashboardagri"),
    path('update_tutorial/<int:pk>/', views.updatetutorial, name="updatetutorial"),
    path('delete_tutorial/<int:pk>/', views.deletetutorial, name="deletetutorial"),

]
