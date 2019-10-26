from django.urls import path
from buyer_app import views

urlpatterns = [
    path('JeBuyer/', views.JeBuyerAPIView.as_view(), name="Je-buyer"),
    path('ScUser/', views.ScUserAPIView.as_view(), name="sc-user"),

    path('je-buyer-detail/<int:pk>/', views.JeBuyerDetail.as_view()),
    path('je-buyer-list/', views.JeBuyerList.as_view()),
    path('sc-user-detail/<int:pk>/', views.ScUserDetail.as_view()),
    path('sc-user-list/', views.ScUserList.as_view()),

]
