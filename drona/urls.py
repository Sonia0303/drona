from django.conf.urls import url, include
from django.contrib import admin
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/', views.SignUpView.as_view(), name="signup"),
    url(r'^$', views.HomeView.as_view(), name='home'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
