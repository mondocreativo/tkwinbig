from django.urls import path
from . import views

urlpatterns = [

    # 获取省份数据
    path('areas', views.ProvinceView.as_view()),

    # 获取市--区县数据
    path('areas/<int:area_id>', views.CityDistrictView.as_view()),
]