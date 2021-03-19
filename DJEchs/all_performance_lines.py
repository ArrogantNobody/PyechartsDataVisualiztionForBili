from django.shortcuts import render
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie, Bar,Radar,Line
from pyecharts.commons.utils import JsCode
import json
from random import randrange
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)

JsonResponse = json_response
JsonError = json_error

def three_operations():
    df=pd.read_csv(r'C:\Users\Gingi\PycharmProjects\MM802_mini\DJEchs\top100_all_categories.csv')
    genre=df['genre'].tolist()
    view=df['view'].tolist()
    coin = df['coin'].tolist()
    favorite = df['favorite'].tolist()
    view=[i//10000 for i in view]
    coin=[i//10000 for i in coin]
    favorite=[i//10000 for i in favorite]
    return genre,view,coin,favorite

genre, view, coin, favorite = three_operations()
def three_lines_base():
    c=(
        Line()
        .add_xaxis(genre)
        .add_yaxis(
            'viewing',
            view,
            #设置标签指出最高值
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .add_yaxis(
        'coins',
         coin,
        # 设置标签指出最高值
        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
         )
            .add_yaxis(
            'favorite',
            favorite,
            # 设置标签指出最高值
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title='viewing amount grouped by categories'),
            #将分区名旋转45度来保证所有分区都能显示
            xaxis_opts=opts.AxisOpts(axislabel_opts={'rotate':45})
        )
        .dump_options_with_quotes()
    )
    return c

class ThreeLinesView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(three_lines_base()))

def index(request):
    return render(request, 'all_performance_lines.html')