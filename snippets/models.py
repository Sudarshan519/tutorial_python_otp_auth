 
from datetime import datetime
from django.db import models
from django.forms import model_to_dict
from django.urls import reverse
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

from rest_framework import serializers
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

from django.contrib.auth.models import User

# class User(AbstractUser):
#       EMPLOYEE = 1
#       EMPLOYER = 2
#       OWNER =3
      
#       ROLE_CHOICES = (
#           (EMPLOYEE, 'EMPLOYEE'),
#           (EMPLOYER, 'EMPLOYER'),
#           (OWNER, 'OWNER'),
#       )
#       role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
#       # You can create Role model separately and add ManyToMany if user has more than one role
      

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
    class Meta:
        ordering = ['created']
    def __str__(self) -> str:
        return self.code

    def owner_detail(self):
        return model_to_dict(self.owner,fields=['username','first_name','last_name','email','date_joined','is_active'#,'last_login'
        ,'user_permissions','groups'])

# this model Stores the data of the Phones Verified
class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)   # For HOTP Verification
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.Mobile)

class Employer(models.Model):
    username=models.CharField(blank=True,max_length=255)
    first_name=models.CharField(max_length=30,blank=True)
    # middle_name=models.CharField(max_length=30,blank=True)
    last_name=models.CharField(max_length=64,blank=True)
    user = models.ForeignKey('auth.User', related_name='employer', on_delete=models.CASCADE)
    # company=models.ForeignKey(Company,on_delete=models.CASCADE)
    phone=models.ForeignKey(phoneModel,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.phone)
    
    def user_name(self):
        return self.user.username

    def company_details(self):
        return model_to_dict(self.company)
    
        
    def employer_details(self):
        return model_to_dict(self.user,fields=['id','username','email','is_staff','date_joined','user_permissions'])

class Approver(models.Model):
    user=models.ForeignKey('auth.User',related_name='approver',on_delete=models.CASCADE)
    # company=models.ForeignKey(Company,on_delete=models.CASCADE)

    # owner= models.OneToOneField('auth.User', related_name='owner', on_delete=models.CASCADE)
    # def __str__(self) -> str:
    #     return  self.company.company_name
    # def owner_name(self):
    #     print(self.owner)
    #     return self.owner

class Company(models.Model):
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    company_name=models.CharField(max_length=30,null=False) 
    login_time= models.TimeField(default="9:00:00",blank=True)
    logout_time=models.TimeField(default="18:00:00",blank=True)
    break_start=models.TimeField(default="13:00:00",blank=True)
    break_end=models.TimeField(default="13:45:00",blank=True)
    employer=models.ManyToManyField(Employer, null=True,blank=True)
    approvers=models.ManyToManyField(Approver, null=True,blank=True)
    # def approvers(self):
    #     return Approver.objects.get(id=self.id)

    def __str__(self) -> str:
        return self.company_name
    
    def hours(self):
        return (self.login_time-self.logout_time)-(self.break_end-self.break_start)

    def employees(self):
        dict=[]
        employees=self.employee_set.all()
        print(employees)
        for emp in employees:
            dict.append(model_to_dict(emp))
        return dict
# class Company(models.Model):
#     created_at = models.DateTimeField(default=datetime.now, )
#     updated_at = models.DateTimeField(auto_now=True)
#     company_name=models.CharField(max_length=30,null=False,blank=False) 
#     login_time= models.TimeField(default="9:00:00",null=False,blank=False)
#     logout_time=models.TimeField(default="18:00:00",blank=False,null=False)
#     break_start=models.TimeField(default="13:00:00",blank=False,null=False)
#     break_end=models.TimeField(default="13:45:00",blank=False,null=False)
#     employer=models.ForeignKey(Employer, on_delete=models.CASCADE,null=False,blank=True)
#     def approvers(self):
#         return Approver.objects.get(id=self.id)
#     def code(self):
#         return self.company_name[0:2].upper()+str(self.id).zfill(3)
#     def __str__(self) -> str:
#         return self.company_name
    
#     def hours(self):
#         try:
#             return ((self.logout_time.hour-self.login_time.hour))-((self.break_end.minute-self.break_start.minute))/60
#         except:
#             return '0'
#             # raise serializers.ValidationError('* Required')
#     def employee(self):
#         return self.employee_set.all()
#     def owner(self):
#         username=self.employer.user.username
#         employees=self.employee_set.all()#.count()
#         # print(employees)
#         employees_dict=[]
#         for employee in employees:
#             empdict= model_to_dict(employee)
#             employees_dict.append(empdict)
        
#         dict= model_to_dict(self.employer)
#         dict['employee']=employees_dict
#         #employees_dict
#         dict['user']=model_to_dict(self.employer.user,fields=['id','email','date_joined','username'])
#         dict['phone']=username
#         return dict




 
 

class Owner(models.Model):
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    user=models.ForeignKey('auth.User', related_name='owner_user', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return  self.company_name

    def user_name(self)->str:
        return self.user_name


class Employee(models.Model):
    username=models.CharField(blank=True,max_length=255)
    first_name=models.CharField(max_length=30,blank=True)
    middle_name=models.CharField(max_length=64,default='',blank=True)
    last_name=models.CharField(max_length=64,blank=True)
    user = models.ForeignKey('auth.User', related_name='employee', on_delete=models.CASCADE,blank=True,null=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE, null=True,blank=True)
    phone=models.OneToOneField(phoneModel,on_delete=models.CASCADE,unique=True,null=True)
    def __str__(self):
        return str(self.user)
    def company_details(self):
        return model_to_dict(self.company)


class Invitation(models.Model):
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE,unique=False)
    # employer=models.ForeignKey(Employer,null=True,blank=True,on_delete=models.SET_NULL)
    accepted=models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def company_name(self):
        return self.company.company_name
    # def company(self):
    #     return model_to_dict(self.company,fields=['id','company_name','login_time'])
    # def company_url(self):
    #     redirect_url = reverse('my_function', args=(backend,))
    #     parameters = urlencode(form.cleaned_data)
    #     return redirect(f'{redirect_url}?{parameters}')
    #     # return self.company_url
    def username(self):
        return self.user

    # def __str__(self):
    #     return self.company.company_name +' has invited '+ self.user.username

class Attendance(models.Model):
    login_time=models.TimeField( blank=False,null=True)
    logout_time=models.TimeField(blank=True,null=True)
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    start_break=models.TimeField(blank=True,null=True)
    end_break=models.TimeField(blank=True,null=True)
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    # updated_at = models.DateTimeField(auto_now=True)
    def username(self):
        return self.user.username
    def __str__(self) -> str:
        return self.user.username+" " + str(self.date)
    def dict(self):
        return model_to_dict(self.user,fields=['username','first_name','last_name','email','date_joined','is_active'#,'last_login'
        ,'user_permissions','groups'])

    def checkIfValid(self):

        raise serializers.ValidationError('* Required')
    
 

class Leave(models.Model):
    date=models.DateField(blank=False)
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    reason=models.CharField(max_length=255)
    type=models.CharField(max_length=60)
    

class ApiReport(models.Model):
    label=models.CharField(max_length=255)
    platform=models.CharField(max_length=255)
    error_message=models.CharField(max_length=255)
    function_name=models.CharField(max_length=255)
    log=models.CharField(max_length=255)
    user_id=models.CharField(max_length=255)


class Banner(models.Model):
    title=models.CharField(max_length=255)
    logo=models.CharField(max_length=255)
    redirect_url=models.CharField(max_length=255)
    bannerable_type=models.CharField(max_length=255)
    bannerable_id=models.CharField(max_length=255)


class Exchange(models.Model):
    id=models.IntegerField(primary_key=True)
    flag=models.CharField(max_length=255)
    unit=models.CharField(max_length=255)
    code=models.CharField(max_length=255)
    rate=models.CharField(max_length=255)
    created_at=models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)    
    # updated_by=models.ForeignKey('auth.User', related_name='owner_user', on_delete=models.CASCADE)


