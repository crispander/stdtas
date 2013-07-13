from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import *
from mysite.polls.models import *

import os

from datetime import datetime

import simplejson

class ViewHome(TemplateView):
    template_name = 'polls/home.html'
    
class ViewIndex(ListView):
    template_name = 'polls/index.html'
    queryset = Poll.objects.order_by('-pub_date')
    context_object_name = 'polls'

class ViewForm(TemplateView):
    template_name = 'polls/form.html'

class ViewDetail(DetailView):
    template_name = 'polls/detail.html'
    model = Poll
    context_object_name = 'poll'


class ViewResults(DetailView):
    template_name = 'polls/results.html'
    model = Poll
    context_object_name = 'poll'


def submit(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    type_poll = request.GET['type_poll']

    if type_poll == 'radio':
        try:
            selected_choice = p.choice_set.get(pk=request.GET['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the poll voting form.
            return render_to_response('polls/detail.html', {
                'poll': p,
                'error_message': "You didn't select a choice.",
            }, context_instance=RequestContext(request))
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect('/polls/{0}/results/'.format(p.id))
    elif type_poll == 'checkbox':
        for i in request.GET:
            if not i == 'type_poll':
                try:
                    selected_choice = p.choice_set.get(pk=str(i))
                except (KeyError, Choice.DoesNotExist):
                    pass
                else:
                    selected_choice.votes += 1
                    selected_choice.save()
        return HttpResponseRedirect('/polls/{0}/results/'.format(p.id))

def create_poll(request):
    """creacion de una encuesta"""
    #main
    try:
        type = request.GET['type_poll']
    except KeyError:
        response = simplejson.dumps({"response": "faul", "cod_error": "type_poll"})
        return HttpResponse(response, "text/json")
    try:
        question = request.GET['question']
    except KeyError:
        response = simplejson.dumps({"response": "faul", "cod_error": "question"})
        return HttpResponse(response, "text/json")
    try:
        options = request.GET['options']
    except KeyError:
        response = simplejson.dumps({"response": "faul", "cod_error": "options"})
        return HttpResponse(response, "text/json")

    #secumdarias
    #colores
    try:
        fondo = request.GET['fondo']
    except KeyError:
        fondo = "#FFF"
    try:
        borde = request.GET['borde']
    except KeyError:
        borde = "#dcdcdc"
    try:
        subfondo = request.GET['subfondo']
    except KeyError:
        subfondo = "#FFF"
    try:
        letra = request.GET['font']
    except KeyError:
        letra = "#000"
    try:
        letra_subblock = request.GET['font_subblock']
    except KeyError:
        letra_subblock= "#000"
    #font
    try:
        font_style = request.GET['font_style']
    except KeyError:
        font_style = "arial"
    #
    try:
        borde_visible = request.GET['borde_visible']
    except KeyError:
        borde_visible = "si"
    try:
        mostrar_resultados = request.GET['mostrar_resultados']
    except KeyError:
        mostrar_resultados = "si"
    try:
        width = request.GET['width']
    except KeyError:
        width = "300px"
    try:
        height = request.GET['height']
    except KeyError:
        height = "300px"
    try:
        border_width = request.GET['border_width']
    except KeyError:
        border_width = "300px"
    try:
        border_radius = request.GET['border_radius']
    except KeyError:
        border_radius = "10%"
    try:
        padding = request.GET['padding']
    except KeyError:
        padding = "10px"
    try:
        width_subblock = request.GET['width_subblock']
    except KeyError:
        width_subblock = "80%"
    try:
        height_subblock = request.GET['height_subblock']
    except KeyError:
        height_subblock = "50%"
    try:
        width_blocktitle = request.GET['width_blocktitle']
    except KeyError:
        width_blocktitle = "80%"
    try:
        height_blocktitle = request.GET['height_blocktitle']
    except KeyError:
        height_blocktitle = "30%"
    try:
        gradient1= request.GET['gradient1']
    except KeyError:
        gradient1 = "#d6e1e8"
    try:
        gradient2 = request.GET['gradient2']
    except KeyError:
        gradient2= "#b6b7b9"
    try:
        font_size_title = request.GET['font_size_title']
    except KeyError:
        font_size_title= "14"
    try:
        font_size_block = request.GET['font_size_block']
    except KeyError:
        font_size_block = "14"
    try:
        padding_std_options = request.GET['block_std_options']
    except KeyError:
        padding_std_options  = "7"
	
    if request.user.is_authenticated():
        obj = Poll.objects.create(tipo = type, question=question,user=request.user, pub_date=datetime.now(), width=width, height=height, border_visible=borde_visible, border_width=border_width, border_color=borde, background=fondo, border_radius=border_radius, sub_background=subfondo, font_family=font_style, font_color=letra, color_title=letra_subblock, padding=padding, width_subblock=width_subblock, height_subblock=height_subblock, width_blocktitle=width_blocktitle, height_blocktitle=height_blocktitle, gradient1=gradient1, gradient2=gradient2, show_results=mostrar_resultados, size_title=font_size_title, size_block=font_size_block, padding_std_options=padding_std_options)
    else:
        obj = Poll.objects.create(tipo = type, question=question, pub_date=datetime.now(), width=width, height=height, border_visible=borde_visible, border_width=border_width, border_color=borde, background=fondo, border_radius=border_radius, sub_background=subfondo, font_family=font_style, font_color=letra, color_title=letra_subblock, padding=padding, width_subblock=width_subblock, height_subblock=height_subblock, width_blocktitle=width_blocktitle, height_blocktitle=height_blocktitle, gradient1=gradient1, gradient2=gradient2, show_results=mostrar_resultados, size_title=font_size_title, size_block=font_size_block, padding_std_options=padding_std_options)
    
    opciones = options.split("\n")
    for i in opciones:
        Choice.objects.create(poll=obj, votes=0, choice=i)
    response = simplejson.dumps({"response": "creado", "id": obj.pk})
    return HttpResponse(response, "text/json")

def render_poll(request, pk):
    """enviar en formato javascript la encuesta
    
    c1 = background-color main
    c2 = border radius
    c3 = border
    c4 = width
    c5 = height
    c6 = background subblock
    c7 = font-style
    c8 = font-color
    c9 = padding
    c10 = width_subblock
    c11 = height_subblock
    c12 = width_blocktitle
    c13 = height_blocktitle
    c14 = color title
    c15 = gradient1
    c16 = gradient2
    c17 = id poll
    c18 = mostrar resultados
    c19 = font_size_title
	c20 = font_size_block
	c21 = padding_std_options
    """
    obj = Poll.objects.get(pk=pk)
    choices = obj.get_choices()
    html = ""
    SETTINGS_HOME = os.path.abspath(os.path.dirname(__file__))
    APP_HOME = os.path.split(SETTINGS_HOME)[0]
    path_file = os.path.join(APP_HOME, "polls", "gen_js", "template_js.txt")
    if obj.tipo == 'radio':
        path_file2 = os.path.join(APP_HOME, "polls", "gen_js", "radio_js.txt")
    else:
        path_file2 = os.path.join(APP_HOME, "polls", "gen_js", "checkbox_js.txt")
    f = open(path_file, "rb")
    fd = f.read()
    f.close()
    
    radio = open(path_file2, "rb")
    radio = radio.read()

    for i in choices:
        html += radio.format(c1=str(i.id), c2=str(i.choice).encode('string_escape'), c3=str(i.votes))
    send = fd.format(corchete_c="}",corchete_o="{", nombre=obj.question, choices=html, c1=obj.background, c2=obj.border_radius, c3=str(str(obj.border_width) + " solid " + str(obj.border_color)), c4=obj.width, c5=obj.height, c6=obj.sub_background, c7=obj.font_family, c8=obj.font_color, c9=obj.padding, c10=obj.width_subblock, c11=obj.height_subblock, c12=obj.width_blocktitle, c13=obj.height_blocktitle, c14=obj.color_title, c15=obj.gradient1, c16=obj.gradient2, c17=obj.id, c18=obj.show_results, c19=obj.size_title, c20=obj.size_block, c21=obj.padding_std_options)

    return HttpResponse(send, "text/javascript")
