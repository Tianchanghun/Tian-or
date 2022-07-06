from board.models import board
from banner.models import Mainbanner, subbanner
from django.shortcuts import render, redirect, get_object_or_404


def defult():
    mainbanner = Mainbanner.objects.order_by('-created_date')[:1]
    Subbanner = subbanner.objects.filter(subbanner_part='info').order_by('-created_date')[:1]
    Notice = board.objects.filter(board_use=True, board_part='notice').order_by('-created_date')[:3]
    news = board.objects.filter(board_use=True, board_part='news').order_by('-created_date')[:3]
    context = {'mainbanner': mainbanner, 'Subbanner': Subbanner, 'Notice': Notice, 'News': news}

    return (context)
