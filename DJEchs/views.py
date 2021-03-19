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