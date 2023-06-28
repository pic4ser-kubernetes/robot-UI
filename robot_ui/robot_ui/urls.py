from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from .schema import schema
from .admin import my_admin_site


urlpatterns = [
    path('', my_admin_site.urls),
    # path('', include('data.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)), name='graphql'),
]
