 
from datetime import datetime
from django.db import models
from django.forms import model_to_dict
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from rest_framework import serializers
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


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


class Company(models.Model):
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    company_name=models.CharField(max_length=30,null=False) 
    login_time= models.TimeField(default="9:00:00",blank=True)
    logout_time=models.TimeField(default="18:00:00",blank=True)
    break_start=models.TimeField(default="13:00:00",blank=True)
    break_end=models.TimeField(default="13:45:00",blank=True)

    def approvers(self):
        return Approver.objects.get(id=self.id)

    def __str__(self) -> str:
        return self.company_name
    
    def hours(self):
        return (self.login_time-self.logout_time)-(self.break_end-self.break_start)


class Approver(models.Model):
    user=models.ForeignKey('auth.User',related_name='approver',on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)



    owner= models.OneToOneField('auth.User', related_name='owner', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return  self.company.company_name
    def owner_name(self):
        print(self.owner)
        return self.owner
 
 

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

class Employer(models.Model):
    username=models.CharField(blank=True,max_length=255)
    first_name=models.CharField(max_length=30,blank=True)
    # middle_name=models.CharField(max_length=30,blank=True)
    last_name=models.CharField(max_length=64,blank=True)
    user = models.ForeignKey('auth.User', related_name='employer', on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    phone=models.ForeignKey(phoneModel,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.phone)
    
    def user_name(self):
        return self.user.username

    def company_details(self):
        return model_to_dict(self.company)

    def employer_details(self):
        return model_to_dict(self.user,fields=['id','username','email','is_staff','date_joined','groups','user_permissions'])

class Invitation(models.Model):
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    user=models.OneToOneField('auth.User', on_delete=models.CASCADE)
    accepted=models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    def company_name(self):
        return self.company.company_name
    def username(self):
        return self.user

    def __str__(self):
        return self.company.company_name +' has invited '+ self.user.username

class Attendance(models.Model):
    login_time=models.TimeField(blank=False,null=True)
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
    

