from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.utils import timezone

from bokeh.plotting import figure
from bokeh.embed import components
import numpy as np
import json

from .models import ECGdata

# Create your views here.


def index(request):

    plot = figure(title='ECG Plot',
                  x_axis_label='time')
    plot.circle([1, 2], [3, 4])
    script, div = components(plot)

    template = loader.get_template('ecg_graph/index.html')
    context = {'script': script,
               'div': div}

    return HttpResponse(template.render(context, request))


def list(request):

    ecg_data_list = ECGdata.objects.order_by('-created_date')
    context = {
        'ecg_data_list': ecg_data_list,
    }
    return render(request, 'ecg_graph/list.html', context)


def graph(request, data_id):

    data = get_object_or_404(ECGdata, pk=data_id)
    data_dict = json.loads(data.data_json.replace("'", "\""))

    data_list = data_dict['data']
    data_x = np.arange(len(data_list))

    plot = figure(title=data_dict['timestamp'],
                  x_axis_label='time')
    plot.line(data_x, data_list)
    script, div = components(plot)

    context = {'script': script,
               'div': div}

    return render(request, 'ecg_graph/index.html', context)


@csrf_exempt
def submit(request):

    if request.method == 'POST':
        received_json = json.loads(request.body.decode("utf-8"))
        item = ECGdata(data_json=received_json, created_date=timezone.now())
        item.save()
        return StreamingHttpResponse('data received...')

    plot = figure()
    plot.circle([1, 2], [3, 4])
    script, div = components(plot)

    template = loader.get_template('ecg_graph/index.html')
    context = {'script': script,
               'div': div}

    return HttpResponse(template.render(context, request))
