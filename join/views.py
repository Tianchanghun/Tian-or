from django.shortcuts import render

# Create your views here.
from . models import member_info
from board.models import board
from banner.models import Mainbanner, subbanner
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import login