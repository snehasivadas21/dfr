from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewset,basename='employee')

urlpatterns = [
    #function based view
    path('students/',views.studentsView), 
    path('students/<int:pk>/',views.studentsDetailView),
  
    #class based view,mixins,generics
    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>/',views.EmployeesDetail.as_view())

    #viewsets
    path('',include(router.urls)),

    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),
    path('blogs/<int:pk>/',views.BlogDetailView.as_view()),
    path('comments/<int:pk>/',views.CommentDetailView.as_view())
]