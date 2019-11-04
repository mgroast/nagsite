from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http.response import JsonResponse
import random

# /api/title
def title(request):
    #名詞 小説、私、あれ、インターネット
    #noun = ['タピオカ', '宮本', '麻雀', 'ぴかてう']
    #動名詞
    #vnoun = ['転生', '計画', '拒否']
    #動詞 する、いる、ある、思う
    #形容詞 ない、面白い、よい、早い
    #副詞 ちょっと、まだ、少し
    #助詞 て、に、を、は
    #助動詞	だ、です、ます、ある
    #接続詞	また、しかし、ただ、それから
    #接頭詞	御、お、ご
    #連体詞	この、そんな、大きな
    #感動詞	ええ、なるほど、さあ、うん
    #フィラー	ええと、まあ、あー
    #記号	。 、 「 」 … ！ ？
    #title = f"{random.choice(vnoun)}したら{random.choice(noun)}だった件"
    result = { "title": title }
    return JsonResponse(result)

# タイトル生成
def create_title():
    return "title"