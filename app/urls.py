from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', views.CompanyDetail.as_view(), name='company-detail'),
    path('companies/<int:company_id>/comments/',
         views.CommentListByCompany.as_view(), name='company-comment-list'),
    path('comments/', views.CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path('companies/<int:company_id>/fetch_tweets/', views.fetch_tweets, name='fetch-tweets'),
]
