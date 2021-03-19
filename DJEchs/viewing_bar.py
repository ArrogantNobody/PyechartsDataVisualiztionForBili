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

def top100_viewing_bar():
    genres_rank_df = df_without_all.sort_values(by='score',ascending=False)[:100]
    genre_mean = genres_rank_df.groupby('rank_tab').mean().astype('int')
    genre_mean['genre'] = genre_mean.index
    c = (
        Bar()
            .add_xaxis(genre_mean['genre'].tolist())
            .add_yaxis('average view', genre_mean['view'].tolist(), category_gap=60)
            .set_series_opts(itemstyle_opts={
            'normal': {
                # 调用js语句，制作渐变颜色
                'color': JsCode("""new echarts.graphic.LinearGradient(0,0,0,1,[{
                            offset:0,
                            color:'rgba(0,244,255,1)'
                        },{
                            offset:1,
                            color:'rgba(0,77,167,1)'
                        }],false)"""),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": 'rgb(0,160,221)'
            }})
            .set_global_opts(title_opts=opts.TitleOpts(title='Comprehensive score Top100 average viewing volume '))
            .dump_options_with_quotes()
    )
    return c

class ViewingBarView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(top100_viewing_bar()))

def index(request):
    return render(request, 'viewing_bar.html')