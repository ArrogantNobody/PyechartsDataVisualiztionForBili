"""MM802_mini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from DJEchs import login_controller,rose_pie,viewing_bar,operations_radar,all_performance_lines,word_cloud
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_controller.login_map),
    path('login/', login_controller.ccid_verify),
    path('dashboard/', login_controller.login_success),
    path('rose_pie/', rose_pie.index),
    path('embed_rose_pie/', TemplateView.as_view(template_name='rose_pie.html'), name='embed_rose_pie'),
    path('ht_rose_pie/', rose_pie.RosePieView.as_view()),
    path('viewing_bar/',viewing_bar.index),
    path('embed_viewing_bar/', TemplateView.as_view(template_name='viewing_bar.html'), name='embed_viewing_bar'),
    path('ht_viewing_bar/', viewing_bar.ViewingBarView.as_view()),
    path('radar/', operations_radar.index),
    path('embed_radar/', TemplateView.as_view(template_name='op_radar.html'), name='embed_radar'),
    path('ht_radar/', operations_radar.RadarView.as_view()),
    path('lines/',all_performance_lines.index),
    path('embed_lines/',TemplateView.as_view(template_name='all_performance_lines.html'), name='embed_lines'),
    path('ht_lines/', all_performance_lines.ThreeLinesView.as_view()),
    path('cloud/', word_cloud.index),
    path('embed_cloud/', TemplateView.as_view(template_name='tag_cloud.html'), name='embed_cloud'),
    #path('ht_cloud/', word_cloud.CloudView.as_view())

]
