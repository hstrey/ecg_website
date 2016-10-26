from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from bokeh.plotting import figure
from bokeh.embed import components

import requests

# Create your views here.

def index(request):
	# api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/appl.json'
	# session = requests.Session()
	# session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
	# raw_data = session.get(api_url)

	plot = figure()
	plot.circle([1.2],[3,4])
	script, div = components(plot)

	template = loader.get_template('ecg_graph/index.html')
	context = {'script': script,
			 'div': div}

	return HttpResponse(template.render(context, request))
