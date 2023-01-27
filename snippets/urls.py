# from django.urls import include, path
# from snippets import views
# from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


# from rest_framework_simplejwt.views import TokenVerifyView
# from snippets.views import SnippetViewSet, UserViewSet, api_root
# from rest_framework import renderers


# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })




# urlpatterns = [
#     # path('snippets/', views.snippet_list),
#     # path('snippets/<int:pk>/', views.snippet_detail),

#     #     path('snippets/', views.SnippetList.as_view(),name="snippets"),
#     # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
#     # path('users/', views.UserList.as_view(),name="users"),
# # path('users/<int:pk>/', views.UserDetail.as_view()),
# # path('api-auth/', include('rest_framework.urls')),
# # path('', views.api_root),
# # path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),


# # JWT AUTH

# path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#      path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
#      path('api/login/<phone>',views.getPhoneNumberRegistered.as_view()),
#       path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

from django.views.generic import TemplateView


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='Pastebin API')
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet,basename="snippet")
router.register(r'users', views.UserViewSet,basename="user")
router.register(r'api/invitation',views.InvitationV,basename='invitation')
router.register(r'api/employee',views.EmployeeV,basename='employee')
router.register(r'api/employer',views.EmployerV,basename='employer')
router.register(r'api/attendance',views.Attendance,basename='attendance')
router.register(r'api/company',views.CompanyV,basename='company')
# router.register('api/employee/',views.CreateEmployee.as_view())


# The API URLs are now determined automatically by the router.
urlpatterns = [
   path('', include(router.urls)),
    # path('api/swagger-ui', schema_view),
    #     path('swagger-ui/', TemplateView.as_view(
    #     template_name='swagger-ui.html',
    #     extra_context={'schema_url':"127.0.0.1:8000"}
    # ), name='swagger-ui'),
    path('api/login/<phone>',views.getPhoneNumberRegistered.as_view()),
    path('api/employee/',views.CreateEmployee.as_view()),
    # path('api/invitations/',views.InvitationList.as_view(),name='invitations_list')


]