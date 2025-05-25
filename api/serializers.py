from rest_framework import serializers
from week.models import Students
from employee.models import Employee
from blogs.models import Blog,Comment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields="__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"  

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"                
    
class BlogSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True,read_only=True)
    class Meta:
        model=Blog
        fields="__all__"        
    
    
    