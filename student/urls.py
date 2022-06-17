from django.urls import path

from .views import (GradeCreateView, GradeDeleteView, GradeDetailView,
                    GradeListView, GradeUpdateView, StudentSmsSendMajorView,InstallmentCreateView,
                    MajorCreateView, MajorDeleteView, MajorUpdateView,
                    StudentCreateView, StudentDeleteView, StudentDetailView,
                    StudentInstallmentListView, StudentInstallmentUpdateView,
                    StudentListView, StudentSelectView, StudentUpdateView, StudentProfileView, UploadStudentProfileView,StudentSmsSendView,StudentSmsSendOnlyView)

app_name = "Student"

urlpatterns = [
    path("list/", StudentListView.as_view(), name="list"),
    path("detail/<int:id>/", StudentDetailView.as_view(), name="detail"),
    path("delete/<int:id>/", StudentDeleteView.as_view(), name="delete"),
    path("update/<int:id>", StudentUpdateView.as_view(), name="update"),
    path("create/", StudentCreateView.as_view(), name="create"),
    path("grade_list/", GradeListView.as_view(), name="grade_list"),
    path("grade_create/", GradeCreateView.as_view(), name="grade_create"),
    path("grade_delete/<int:grade_id>/", GradeDeleteView.as_view(), name="grade_delete"),
    path("grade_update/<int:id>/", GradeUpdateView.as_view(), name="grade_update"),
    path("grade_detail/<int:id>/", GradeDetailView.as_view(), name="grade_detail"),
    path("select/", StudentSelectView.as_view(), name="select"),
    # path("major_create/", MajorCreateView.as_view(), name="major_create"),
    path('major/update/<int:major_id>/', MajorUpdateView.as_view(), name="major_update"),
    path('major/delete/<int:major_id>/', MajorDeleteView.as_view(), name="major_delete"),
    path('installment_create_view/<int:student_id>/', InstallmentCreateView.as_view(), name='installmentcreateview'),
    path('student_installment_view/<int:student_id>/', StudentInstallmentListView.as_view(),
         name='student_installment_list'),
    path('student_installment_update/<int:installment_id>/', StudentInstallmentUpdateView.as_view(),
         name='student_insallmet_update'),
    path('profile/', StudentProfileView.as_view(), name='profile'),
    path('uploade/<int:id>/', UploadStudentProfileView.as_view(), name='upload_profile'),
    path('sms/',StudentSmsSendView.as_view(),name='sms'),
  path('sms1/',StudentSmsSendOnlyView.as_view(),name='sms1'),
  path('sms2/',StudentSmsSendMajorView.as_view(),name='sms2')
  
]
