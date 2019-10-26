from django.urls import path
from application_app import views
urlpatterns = [
    path('JeJobApplication/', views.JeJobApplicationAPIView.as_view(), name="je-job-application"),
    path('JeWorkStatus/', views.JeWorkStatusAPIView.as_view(), name="je-work-statusAPIView"),

    path('je-job-application-detail/<int:pk>/', views.JeJobApplicationDetail.as_view()),
    path('je-job-application-list/', views.JeJobApplicationList.as_view()),
    path('je-work-status-detail/<int:pk>/', views.JeWorkStatusDetail.as_view()),
    path('je-work-status-list/', views.JeJobWorkStatusList.as_view()),

]
