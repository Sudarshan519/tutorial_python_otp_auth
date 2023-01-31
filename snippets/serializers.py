from rest_framework import serializers
from snippets.models import Attendance, Employer, Invitation, Snippet, LANGUAGE_CHOICES, STYLE_CHOICES,Employee,Company,Approver
from django.contrib.auth.models import User 
from rest_framework.validators import UniqueForDateValidator
from rest_framework.validators import UniqueTogetherValidator
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         owner = serializers.ReadOnlyField(source='owner.username')
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
        
#         instance.save()
#         return instance


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    # owner_detail=serializers.ReadOnlyField(source='owner_detail')
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner','owner_detail',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets','email','date_joined','is_staff'
        ]

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # company_name=serializers.CharField()
    # owner=serializers.SlugRelatedField(read_only=True,slug_field='username')
    class Meta:
        model=Company
        fields=['company_name','employer','login_time','logout_time','break_start','break_end','employees']
    def create(self, validated_data):
        return super().create(validated_data)
  

# class CompanySerializer(serializers.HyperlinkedModelSerializer):
#     company_name=serializers.CharField()
#     # employee=serializers.ReadOnlyField(source='employee',many=True)
#     # owner=serializers.SlugRelatedField(read_only=True,slug_field='username')
#     class Meta:
#         model=Company
#         fields=['url','code','company_name','owner','login_time','logout_time','break_start','break_end','hours'
#         ]
#     def create(self, validated_data):
#         return super().create(validated_data)
  
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    username= serializers.ReadOnlyField(source='user.username')
    company=CompanySerializer('company')
    class Meta:
        model=Employee
        fields=['url','id','first_name','middle_name','last_name','username','company']

class EmployerSerializer(serializers.HyperlinkedModelSerializer):
    # username=serializers.ReadOnlyField(source='user.username')
    # company=serializers.ReadOnlyField(source='company.company_name')

    class Meta:
        model=Employer
        fields=['user','first_name', #'company_details',
        'employer_details',
        ]

 
    # def create(self, validated_data):
    #     return super().create(validated_data)
# class UserSerializer(serializers.HyperlinkedRelatedField):
#     class Meta:
#         model:User
#         fields=['username']

# class CustomUserSerializer(serializers.RelatedField):
#     # users=UserSerializer(users)
#     def to_representation(self, value):
#         return UserSerializer(value)
class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    # user_detail=  serializers.ReadOnlyField(source='dict')#.__dict__
    # user_detail= UserSerializer(source='user',)#serializers.PrimaryKeyRelatedField(read_only=True) #
    class Meta:
        model=Attendance
        fields=['id',#,'user_name',
        'username',
        'date', 'login_time','logout_time','start_break','end_break',
        # 'created_at'
        #'user_detail'
        ]
        # extra_kwargs = {'user_detail': {'required': False}}
        # validators=[UniqueTogetherValidator(
        #     queryset=Attendance.objects.all(),
        #     fields=('date','username'))]
# class InvitationSerializer(serializers.Serializer):
#     accepted=serializers.BooleanField()
#     created_at=serializers.DateTimeField()

#     updated_at=serializers.DateTimeField()
#     username=serializers.CharField()
#     company=CompanySerializer('company')

#     def create(self, validated_data):
#         return super().create(validated_data)

class InvitationSerializer(serializers.HyperlinkedModelSerializer):
    # company=CompanySerializer('company')
    class Meta:
        model=Invitation
        fields=['accepted','created_at','id','company','company_name',
        ]

    # def to_representation(self, instance):
    #     return super().to_representation(instance)
    # company=serializers.ReadOnlyField(source='company')
    # company = serializers.SlugRelatedField(
    #     # many=True,
    #     read_only=True,
    #     slug_field='company_name'
    #  )


  # class Meta:
    #     fields=['accepted','created_at','updated_at']
# class InvitationSerializer(serializers.HyperlinkedModelSerializer):
#     invitations=serializers.HyperlinkedModelSerializer(many=True)
#     class Meta:
#         model = Invitation
#         fields=['company_name','user','created_at']
    # company=serializers.RelatedField(many=False,related_name='company_name') 
    # user=serializers.OneToOneField('auth.User' )
    # accepted=serializers.BooleanField(default=False)
    # created_at = serializers.DateTimeField(default=datetime.now, blank=True)
    # updated_at = serializers.DateTimeField(auto_now=True)

# class CompanySerializer(serializers.Serializer):
#     company=serializers.RelatedField(many=False,read_only=True,related_name='company_name')
#     class Meta:
#         model=Company
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']


# class EmployeeSerializer(serializers.ModelSerializer):
#     username=serializers.CharField(blank=True,max_length=255)
#     first_name=serializers.CharField(max_length=30, )
#     middle_name=serializers.CharField(max_length=64,default='',blank=True)
#     last_name=serializers.CharField(max_length=64,blank=True)
    # user = serializers.ForeignKey('auth.User', related_name='employee', on_delete=models.CASCADE,blank=True,null=True)
    # company=serializers.ForeignKey(Company,on_delete=models.CASCADE, null=True,blank=True)
    # phone=models.ForeignKey(phoneModel,on_delete=models.CASCADE,unique=True)