from django.urls import path
from job_app import views

urlpatterns = [
    path('JeJob/', views.JeJobAPIView.as_view(), name="je-job"),
    path('JeJobSkill/', views.JeJobSkillAPIView.as_view(), name="je-job-skill"),
    path('JeJobAttachment/', views.JeJobAttachmentAPIView.as_view(), name="je-job-attachment"),

    path('je-job/<int:pk>/', views.JeJobDetail.as_view()),
    path('je-job-list/', views.JeJobList.as_view()),
    path('je-job-skill/<int:pk>/', views.JeJobSkillDetail.as_view()),
    path('je-job-skill-list/', views.JeJobSkillList.as_view()),
    path('je-job-attachment/<int:pk>/', views.JeJobAttachmentDetail.as_view()),
    path('je-job-attachment-list/', views.JeJobAttachmentList.as_view()),
]
