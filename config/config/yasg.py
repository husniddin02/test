# config/yasg.py
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
        
    openapi.Info(
        title="Sport Platform",
        default_version='v1',
        description="Sport Health Platform",
        license=openapi.License(name="MIT License"),
    ),

    public=True,
    permission_classes=(permissions.AllowAny,),
    
)

urlpatterns = [
    # ... другие URL-паттерны
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавляем параметры для каждого эндпоинта

schema_view = get_schema_view(
   openapi.Info(
      title="Sport Platform",
      default_version='v1',
      description="Sport Health Platform",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # другие URL-паттерны
   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавление параметров для каждого эндпоинта

schema_view = get_schema_view(
   openapi.Info(
      title="Sport Platform",
      default_version='v1',
      description="Sport Health Platform",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # другие URL-паттерны
   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавление параметров для каждого эндпоинта

schema_view = get_schema_view(
   openapi.Info(
      title="Sport Platform",
      default_version='v1',
      description="Sport Health Platform",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # другие URL-паттерны
   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавление параметров для каждого эндпоинта

schema_view = get_schema_view(
   openapi.Info(
      title="Sport Platform",
      default_version='v1',
      description="Sport Health Platform",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # другие URL-паттерны
   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавление параметров для каждого эндпоинта

schema_view = get_schema_view(
   openapi.Info(
      title="Sport Platform",
      default_version='v1',
      description="Sport Health Platform",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # другие URL-паттерны
   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавление параметров для каждого эндпоинта

schema_view = get_schema_view(
   openapi.Info(
      title="Sport Platform",
      default_version='v1',
      description="Sport Health Platform",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # другие URL-паттерны
   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавление параметров для каждого эндпоинта

schema_view = get_schema_view(
   openapi.Info(
      title="Sport Platform",
      default_version='v1',
      description="Sport Health Platform",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавление параметров для каждого эндпоинта

schema_view = get_schema_view(
   openapi.Info(
      title="Sport Platform",
      default_version='v1',
      description="Sport Health Platform",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавление параметров для каждого эндпоинта

schema_view = get_schema_view(
   openapi.Info(
      title="Sport Platform",
      default_version='v1',
      description="Sport Health Platform",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # другие URL-паттерны
   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавление параметров для каждого эндпоинта

schema_view = get_schema_view(
   openapi.Info(
      title="Sport Platform",
      default_version='v1',
      description="Sport Health Platform",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # другие URL-паттерны
   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавление параметров для каждого эндпоинта

schema_view = get_schema_view(
   openapi.Info(
      title="Sport Platform",
      default_version='v1',
      description="Sport Health Platform",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # другие URL-паттерны
   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавление параметров для каждого эндпоинта

schema_view = get_schema_view(
   openapi.Info(
      title="Sport Platform",
      default_version='v1',
      description="Sport Health Platform",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # другие URL-паттерны
   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
