"""collegeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from clgeapp import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'role', views.RoleViewSet)
router.register(r'department', views.DepartmentViewSet)
router.register(r'year', views.YearViewSet)
router.register(r'section', views.SectionViewSet)
router.register(r'semester', views.SemesterViewSet)
router.register(r'batch', views.BatchViewSet)
router.register(r'regulation', views.RegulationViewSet)
router.register(r'subject', views.SubjectViewSet)
router.register(r'staff', views.StaffViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'staffuser', views.StaffUserViewSet, 'staffuser')
router.register(r'studentuser', views.StudentUserViewSet)
router.register(r'mark', views.MarkViewSet)
router.register(r'rank', views.RankViewSet, 'rank')

urlpatterns = [
    path('', views.api_root),
    path('college/', views.CollegeList.as_view()),
    path('college/<int:pk>/', views.CollegeDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

