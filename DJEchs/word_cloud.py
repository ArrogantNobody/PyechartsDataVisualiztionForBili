from django.shortcuts import render
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie, Bar,Radar,Line,WordCloud
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

# def get_date():
#     df=pd.read_csv(r'C:\Users\Gingi\PycharmProjects\MM802_mini\DJEchs\bilibili.csv')
#     # print(df.info())
#     #波浪线~表示不选取该部分
#     df_without_all=df[~df['rank_tab'].isin(['全站'])]
#     return df_without_all
#
# def build_tags_value(df):
# 	#获取tag_name标签下的数据
# 	#利用join为列表解嵌套，获得字符串
# 	#通过逗号对字符串进行拆分，获得无嵌套列表
# 	tag_list=','.join(df['tag_name']).split(',')
# 	#构造Series并调用.value_counts()
# 	tags_count=pd.Series(tag_list).value_counts()
# 	return tags_count
#
# df_without_all=get_date()
# tags_count=build_tags_value(df_without_all)
# #print(tags_count)
#
# def wordcloud_base() :
#     c=(
#         WordCloud()
#         .add(
#             '',
#             [list(z) for z in zip(tags_count.index,tags_count)],
#             word_size_range=[5,100],
#             shape='pentagon',
#         )
#         .set_global_opts(title_opts=opts.TitleOpts(title='Hot Tags'))
#         .dump_options_with_quotes()
#     )
#     return c
#
# class CloudView(APIView):
#     def get(self, request, *args, **kwargs):
#         return JsonResponse(json.loads(wordcloud_base()))

def index(request):
    return render(request, 'tag_cloud.html')