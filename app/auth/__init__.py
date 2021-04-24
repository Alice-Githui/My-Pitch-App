from flask import Blueprint  
# from . import forms,views

auth=Blueprint('auth',__name__)
from .import views,forms