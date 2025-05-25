import django_filters 
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation=django_filters.CharFilter(field_name="designation",lookup_expr="iexact")
    name=django_filters.CharFilter(field_name="name",lookup_expr='icontains')
    # id=django_filters.RangeFilter(field_name="id")
    id_min=django_filters.CharFilter(method='filter_by_id_range',label='From Emp ID')
    id_max=django_filters.CharFilter(method='filter_by_id_range',label='From Emp ID')
    class Meta:
        model=Employee
        fields=['designation','name',"id","id_min","id_max"]

    def filter_by_id_range(self,queryset,name,value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset    
