from django.urls import path
from test_app import views


urlpatterns = [
    path('JeQuestion/', views.JeQuestionAPIView.as_view(), name="je-question"),
    path('JeTest/', views.JeTestAPIView.as_view(), name="je-test"),
    path('JeTestDetails/', views.JeTestDetailsAPIView.as_view(), name="je-test-details"),

    path('je-question-details/<int:pk>/', views.JeQuestionDetail.as_view()),
    path('je-question-list/', views.JeQuestionList.as_view()),
    path('je-test-details-detail/<int:pk>/', views.JeTestDetailsDetail.as_view()),
    path('je-test-details-list/', views.JeTestDetailsList.as_view()),
    path('je-test-detail/<int:pk>/', views.JeTestDetail.as_view()),
    path('je-test-detail-list/', views.JeTestList.as_view()),
]
