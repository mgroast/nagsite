from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http.response import JsonResponse
import random
import sqlite3
from contextlib import closing

# 
dbname = 'db.sqlite3'

# /api/title
def title(request):
    title = create_title()
    result = { "title": title }
    return JsonResponse(result)

# タイトル生成
def create_title():
    title = ""
    with closing(sqlite3.connect(dbname)) as conn:
        cursor = conn.cursor()
        # 初期ID決定
        id = get_start_id(cursor)
        # 連鎖
        while id != 0 and len(title) < 100:
            # 単語追加
            title += get_word(cursor, id)
            # ID決定
            sum = get_chainsum(cursor, id)
            chains = get_chains(cursor, id)
            rnd = random.random()
            num = 0
            for record in chains:
                num += record[2]
                if num / sum >= rnd:
                    id = record[1]
                    break
    return title

# 初期文字取得
def get_start_id(cursor):
    sql = 'select id2 from api_titlechains where id1=0 order by RANDOM() limit 1'
    result = cursor.execute(sql)
    record = list(result)[0]
    return record[0]

# 文字取得
def get_word(cursor, id):
    sql = 'select word from api_titlewords where id=?'
    result = cursor.execute(sql, (id,))
    record = list(result)[0]
    return record[0]

# 連鎖合計取得
def get_chainsum(cursor, id):
    sql = 'select count(num) from api_titlechains where id1=?'
    result = cursor.execute(sql, (id,))
    record = list(result)[0]
    return record[0]

# 連鎖取得
def get_chains(cursor, id):
    sql = 'select id1,id2,num from api_titlechains where id1=?'
    result = cursor.execute(sql, (id,))
    return list(result)