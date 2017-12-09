"""smuofertas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
admin.site.site_header = 'NOKIA SMU'
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
from smuofertas.schema import schema
from django.contrib.auth import views as auth_views

class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name='logout'),
    # url(r'^graphql', csrf_exempt(PrivateGraphQLView.as_view(graphiql=True, schema=schema)), name='graphql'),
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
