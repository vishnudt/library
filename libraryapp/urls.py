from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    
    path('book/create/', views.CreateBook.as_view()),
    path('book/list/', views.ListBook.as_view()),
    path('book/list/<int:pk>/', views.SingleBook.as_view()),
    path('book/update/<int:pk>/', views.UpdateBook.as_view()),
    path('book/delete/<int:pk>/', views.DeleteBook.as_view()),

    path('token-auth/', auth_views.obtain_auth_token),
    path('student/create/', views.CreateStudent.as_view()),
    path('student/list/', views.ListStudent.as_view()),
    path('student/list/<int:pk>/', views.SingleStudent.as_view()),
    path('student/update/<int:pk>/', views.UpdateStudent.as_view()),
    path('student/delete/<int:pk>/', views.DeleteStudent.as_view()),


    path('cart/create/', views.CartCreate.as_view()),
    path('cart/list/', views.CartList.as_view()),

]
