from django.contrib.auth.models import Group
from django.forms import model_to_dict

employee, created = Group.objects.get_or_create(name='Employee')

employee.permissions.set([73,72,74])

# employee.permissions.add(1)
# employee.permissions.add( )
# employee.permissions.remove( )
# employee.permissions.clear()


def is_employee(user):
 
    return user.groups.filter(name='Employee').exists()
from django.contrib.auth.decorators import user_passes_test

def is_employer(user):
     return user.groups.filter(name='Employer').exists()

def is_owner(user):
     return user.groups.filter(name='Owner').exists()

@user_passes_test(is_employee)
def my_view(request):
    pass
 