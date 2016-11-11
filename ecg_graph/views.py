from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, StreamingHttpResponse
from django.utils import timezone
from django.contrib.auth.models import User

from bokeh.plotting import figure
from bokeh.embed import components
import numpy as np
import json

from .models import ECGdata

# Create your views here.


def list(request):
    if request.user.is_authenticated():
        ecg_data_list = ECGdata.objects.filter(owner=request.user)
        user_list = []
        time_stamp_list = []
        data_list = []
        data_lengths = []
        id_list = []
        for ecg_data in ecg_data_list:
            id_list.append(ecg_data.id)
            data_dict = json.loads(ecg_data.data_json.replace("'", "\""))
            user_list.append(data_dict['user'])
            time_stamp_list.append(data_dict['timestamp'])
            data_list.append(data_dict['data'])
            data_lengths.append(len(data_dict['data']))

        zip_list = zip(id_list, time_stamp_list, user_list, data_lengths)
        context = {
            'zip_list': zip_list,
        }
        return render(request, 'ecg_graph/list.html', context)
    return redirect('/login')


def graph(request, data_id):
    if request.user.is_authenticated():
        # Do something for authenticated users.
        data = get_object_or_404(ECGdata, pk=data_id)
        data_dict = json.loads(data.data_json.replace("'", "\""))

        data_list = data_dict['data']
        print(data_list)
        data_x = np.arange(len(data_list))

        plot = figure(title=data_dict['timestamp'],
                      x_axis_label='time')
        plot.line(data_x, data_list)
        script, div = components(plot)

        context = {'script': script,
                   'div': div}

        return render(request, 'ecg_graph/graph.html', context)
    else:
        # redirect to ecg_graph/list
        return redirect('/ecg_graph/list')


def submit(request):
    if request.method == 'POST':
            received_json = json.loads(request.POST['data_json'])
            try:
                u = User.objects.get(username=received_json['user'])
            except:
                return HttpResponse('Unauthorized', status=401)
            item = ECGdata(data_json=received_json, created_date=timezone.now(), owner=u)
            item.save()
            return StreamingHttpResponse('data received...')

    context = {}

    return render(request, 'ecg_graph/submit.html', context)

