from django.shortcuts import render, HttpResponse
import requests
import json
# Create your views here.

# GET https://www.googleapis.com/youtube/v3/channels

# return use by name: forUsername

def index(request);
    youtube = requests.get('GET https://www.googleapis.com/youtube/v3/channels/')
    
   
# return `videoCategories` resources, 

# The categoryId parameter specifies a YouTube guide category, 
# thereby requesting YouTube channels associated with that category.


# search