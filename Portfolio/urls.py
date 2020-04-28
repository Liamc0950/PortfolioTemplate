#LIAM CORLEY \\ 2020
#App urls

from django.urls import path

from . import views



urlpatterns = [
	#root -> IndexView
    path('', views.IndexView.as_view(), name='index'),
    #Show pk -> ShowDetailView
    path('<int:pk>/', views.ShowDetailView.as_view(), name='show-detail')
]