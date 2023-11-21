from django.urls import path, include
from myadmin.views import index, Consumer

urlpatterns = [
    path('', index.index, name="myadmin_index"),

    # 后台员工信息管理
    path('consumer/<int:pIndex>', Consumer.index, name="myadmin_consumer_index"),  # 浏览信息
]
