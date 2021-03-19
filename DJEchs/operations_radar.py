from django.shortcuts import render
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie, Bar,Radar
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

df = pd.read_csv(r'C:\Users\Gingi\PycharmProjects\MM802_mini\DJEchs\bilibili.csv')#(1300, 14)
df_without_all = df[~df['rank_tab'].isin(['全站'])]#(1200, 14)
def top_100_performance(df):
    genres_rank_df = df.sort_values(by='score',ascending=False)[:100]
    genre_mean = genres_rank_df.groupby('rank_tab').mean().astype('int')
    genre_mean['genre'] = genre_mean.index
    return genre_mean

top_100 = top_100_performance(df_without_all)
def radar_base():
    c=(
        Radar()
        .add_schema(
            schema=[
                opts.RadarIndicatorItem(name='动画',max_=650000),
                opts.RadarIndicatorItem(name='娱乐',max_=650000),
                opts.RadarIndicatorItem(name='影视',max_=650000),
                opts.RadarIndicatorItem(name='时尚',max_=650000),
                opts.RadarIndicatorItem(name='游戏',max_=650000),
                opts.RadarIndicatorItem(name='生活',max_=650000),
                opts.RadarIndicatorItem(name='科技',max_=650000),
                opts.RadarIndicatorItem(name='音乐',max_=650000),
                opts.RadarIndicatorItem(name='鬼畜',max_=650000),
            ]
        )
        #添加指标，设置线条颜色
        .add('投币',[top_100['coin'].tolist()],color='#49010F')
        .add('点赞',[top_100['like'].tolist()],color='#C16200')
        .add('收藏',[top_100['favorite'].tolist()],color='#881600')
        .set_series_opts(
        	#不显示指标数值
            label_opts=opts.LabelOpts(is_show=False),
            # 设置线条格式，宽度为3，样式为虚线
            linestyle_opts=opts.LineStyleOpts(width=3,type_='dotted'),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title='Operations on top100'))
        .dump_options_with_quotes()
    )
    return c
class RadarView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(radar_base()))

def index(request):
    return render(request, 'op_radar.html')