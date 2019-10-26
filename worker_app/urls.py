from django.urls import path
from worker_app import views
urlpatterns = [
	path('JeWorker/', views.JeWorkerAPIView.as_view(), name="je-worker"),
    path('JeWorkerPortfolio/', views.JeWorkerPortfolioAPIView.as_view(), name="Je-worker-portfolio"),
	path('JeJobType/', views.JeWorkerSkillAPIView.as_view(), name="je-worker-skill"),
	path('JeWorkerCertification/', views.JeWorkerCertificationAPIView.as_view(), name="je-worker-certification"),
    path('JeCertification/', views.JeCertificationAPIView.as_view(), name="je-certification"),

	path('je-worker/<int:pk>/', views.JeWorkerDetail.as_view()),
	path('je-subcategory-list/', views.JeWorkerList.as_view()),
	path('je-job-type/<int:pk>/', views.JeWorkerSkillDetail.as_view()),
	path('je-job-type-list/', views.JeWorkerSkillList.as_view()),
	path('je-rate-unit-type/<int:pk>/', views.JeWorkerPortfolioDetail.as_view()),
	path('je-rate-unit-type-list/', views.JeWorkerPortfolioList.as_view()),
	path('je-duration-unit-type/<int:pk>/', views.JeWorkerCertificationDetail.as_view()),
	path('je-duration-unit-type-list/', views.JeWorkerCertificationList.as_view()),
	path('je-skill/<int:pk>/', views.JeCertificationDetail.as_view()),
	path('je-skill-list/', views.JeCertificationList.as_view()),

]

