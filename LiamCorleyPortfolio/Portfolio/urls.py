from django.urls import path

from . import views

urlpatterns = [
	#ex: /Portfolio/
    path('', views.IndexView.as_view(), name='index'),
    #es: /Portfolio/5
    path('<int:pk>/', views.ShowDetailView.as_view(), name='show-detail')
]