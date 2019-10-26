from django.urls import path
from general_app import views

urlpatterns = [
    path('JeCategory/', views.JeCategoryAPIView.as_view(), name="je-category"),
    path('JeSubCategory/', views.JeSubCategoryAPIView.as_view(), name="Je-subcategory"),
    path('JeJobType/', views.JeJobTypeAPIView.as_view(), name="je-job-type"),
    path('JeDurationUnitType/', views.JeDurationUnitTypeAPIView.as_view(), name="je-duration-unit"),
    path('JeRateUnitType,/', views.JeRateUnitTypeAPIView.as_view(), name="je-rate-unit-type"),
    path('JeSkill/', views.JeSkillAPIView.as_view(), name="jke-skill"),
    path('JeSkillType/', views.JeSkillTypeAPIView.as_view(), name="je-skill-type"),
    path('JeWorkStatus/', views.JeWorkStatusAPIView.as_view(), name="je-skill-type"),
    path('je-category/<int:pk>/', views.JeCategoryDetail.as_view()),
    path('je-category-list/', views.JeCategoryList.as_view()),
    path('je-subcategory/<int:pk>/', views.JeSubCategoryDetail.as_view()),
    path('je-subcategory-list/', views.JeSubCategoryList.as_view()),
    path('je-job-type/<int:pk>/', views.JeJobTypeDetail.as_view()),
    path('je-job-type-list/', views.JeJobTypeList.as_view()),
    path('je-rate-unit-type/<int:pk>/', views.JeRateUnitTypeDetail.as_view()),
    path('je-rate-unit-type-list/', views.JeRateUnitTypeList.as_view()),
    path('je-duration-unit-type/<int:pk>/', views.JeDurationUnitTypeDetail.as_view()),
    path('je-duration-unit-type-list/', views.JeRateUnitTypeList.as_view()),
    path('je-skill/<int:pk>/', views.JeSkillTypeDetail.as_view()),
    path('je-skill-list/', views.JeSkillTypeList.as_view()),

]
