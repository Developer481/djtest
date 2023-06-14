from django.urls import path
from pdfapp import views

app_name = 'pdfapp'


urlpatterns = [
   #path('api/scrape/', views.scrape_api,name='scrape_api'),
   path('', views.members,name='scrape_api'),
  
]   