from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
import random

from myadmin.models import Consumer


def index(request, pIndex=1):  # pIndex代表是分页处理的第几页
    umod = Consumer.objects
    consumer_list = umod.all()
    pIndex = int(pIndex)
    pages = Paginator(consumer_list, 10)  # 十条数据进行分页

    # 防止页数越界
    maxpage = pages.num_pages  # 获取最大页数
    if pIndex > maxpage:
        pIndex = maxpage
    if pIndex < 1:
        pIndex = 1
    list2 = pages.page(pIndex)  # 当前页数据
    plist = pages.page_range  # 页码数列表

    # 数据都给出了,这个地方可以进行封装了
    print('a')
    print(consumer_list)
    return HttpResponse("list of consumers")
