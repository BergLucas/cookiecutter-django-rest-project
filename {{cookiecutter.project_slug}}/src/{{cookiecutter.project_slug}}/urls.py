"""{{ cookiecutter.project_slug }} URL Configuration.

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.ADMIN_PAGE:
    urlpatterns += [path("admin/", admin.site.urls)]

if settings.API_PAGE:
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

    urlpatterns += [
        path(
            "api/schema/file/", SpectacularAPIView.as_view(), name="api__schema__file"
        ),
        path(
            "api/schema/",
            SpectacularSwaggerView.as_view(url_name="api__schema__file"),
            name="api__schema",
        ),
    ]
