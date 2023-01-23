from django.urls import include, path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),

        path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view()),
path('api-auth/', include('rest_framework.urls')),
path('', views.api_root),
path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),


# JWT AUTH

path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
     path('api/login/<phone>',views.getPhoneNumberRegistered.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)