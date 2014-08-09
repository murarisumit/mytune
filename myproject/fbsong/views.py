# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
import createJson

def index(request):
	#data=createJson.get_feed_from_page2()
	data=createJson.checkk()
	return render_to_response('fbsong/index.html',{'data':data})
