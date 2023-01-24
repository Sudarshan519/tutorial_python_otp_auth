 
from datetime import datetime
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
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
    company_name=models.CharField(max_length=30)
    owner= models.OneToOneField('auth.User', related_name='owner', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return  self.company_name

class Owner(models.Model):
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    user=models.ForeignKey('auth.User', related_name='owner_user', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return  self.company_name


class Employee(models.Model):
    username=models.CharField(blank=True,max_length=255)
    first_name=models.CharField(max_length=30,blank=True)
    middle_name=models.CharField(max_length=64,default='',blank=True)
    last_name=models.CharField(max_length=64,blank=True)
    user = models.ForeignKey('auth.User', related_name='employee', on_delete=models.CASCADE,blank=True,null=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE, null=True,blank=True)
    phone=models.ForeignKey(phoneModel,on_delete=models.CASCADE,unique=True,null=True)
    def __str__(self):
        return str(self.user)


class Employer(models.Model):
    username=models.CharField(blank=True,max_length=255)
    first_name=models.CharField(max_length=30,blank=True)
    last_name=models.CharField(max_length=64,blank=True)
    user = models.ForeignKey('auth.User', related_name='employer', on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    phone=models.ForeignKey(phoneModel,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.phone)


class Invitation(models.Model):
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    user=models.OneToOneField('auth.User', on_delete=models.CASCADE)
    accepted=models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company.company_name +' has invited '+ self.user.username

 