from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import *
from mysite.polls.models import *
import simplejson

import os

from datetime import datetime
from django.utils import timezone

import simplejson

class ViewHome(TemplateView):
    template_name = 'polls/home.html'
    
class ViewLogin(TemplateView):
    template_name = 'polls/login.html'
    
class ViewOneall(TemplateView):
    template_name = 'polls/oneall.html'
    def get_context_data(self, **kwargs):
        context = super(ViewOneall, self).get_context_data(**kwargs)

        context["useroneall"] = vars(self.request.user.identity)

        return context
    
    
class ViewIndex(ListView):
    template_name = 'polls/index.html'
    queryset = Poll.objects.order_by('-pub_date')
    context_object_name = 'polls'
    
    def get_context_data(self, **kwargs):
        context = super(ViewIndex, self).get_context_data(**kwargs)
        obj = Poll.objects.all()

        try:
            search =  self.request.REQUEST["search"]
        except KeyError:
            action = True
        else:
            action = False
            obj = obj.filter(question__icontains = search)
            
        p = Paginator(obj, 5)
        
        try:
            pagecurrent = self.request.REQUEST["page"]
        except KeyError:
            pagecurrent = 1
            

        context["pollspaginator"] = p.page(pagecurrent)
        context["page"] = pagecurrent
        context["paginator"] = p

        return context

class ViewForm(TemplateView):
    template_name = 'polls/form.html'

class ViewDetail(DetailView):
    template_name = 'polls/detail.html'
    model = Poll
    context_object_name = 'poll'
 
    def get_context_data(self, **kwargs):
        context = super(ViewDetail, self).get_context_data(**kwargs)
        try:
            before = Poll.objects.get(id__exact = int(self.kwargs["pk"]) - 1)
        except Poll.DoesNotExist:
            before = False
            
        try:
            after = Poll.objects.get(id__exact = int(self.kwargs["pk"]) + 1)
        except Poll.DoesNotExist:
            after = False
            
        context["before"] =  before
        context["after"] =  after
        
        return context


class ViewResults(DetailView):
    template_name = 'polls/results.html'
    model = Poll
    context_object_name = 'poll'

class ViewContact(TemplateView):
    template_name = 'polls/contact.html'
    
class ViewSobreApp(TemplateView):
    template_name = 'polls/sobreapp.html'
    
def submit(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    type_poll = request.GET['type_poll']

    if type_poll == 'radio':
        try:
            selected_choice = p.choice_set.get(pk=request.GET['choice'])
        except (KeyError, Choice.DoesNotExist):
            #no ha seleccionado una opcioon
            response = HttpResponse(simplejson.dumps({"operacion": False, "key2": "You didn't select a choice."}))  
            response["Access-Control-Allow-Origin"] = "*"  
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"  
            response["Access-Control-Max-Age"] = "1000"  
            response["Access-Control-Allow-Headers"] = "*"
            return response
        else:
            try:
                anterior = Vote.objects.filter(choice=selected_choice)[0].number_votes
            except IndexError:
                anterior = 0
            if(p.requiredAuthentication == "si"):
                try:
                    user_token = request.GET['user_token']
                except IndexError:
                    response = HttpResponse(simplejson.dumps({"operacion": False, "resultado": "error en la solicitud"}))
                else:
                    if request.user.is_authenticated and request.user.identity.identity_token == user_token:
                        if p.number_votes == "si":
                            #consultar si existen registros donde hayan votado en esa misma encuesta.
                            try:
                                k = Vote.objects.filter(user_token=user_token, choice__poll = p)[0]
                            except IndexError:
                                allreadyvote = False
                            else:
                                allreadyvote = True
                                
                            if not allreadyvote:
                                vote = Vote.objects.create(choice=selected_choice, number_votes=anterior + 1, user_token=user_token)
                                response = HttpResponse(simplejson.dumps({"operacion": True, "key2": "value"}))
                            else:
                                response = HttpResponse(simplejson.dumps({"operacion": False, "key2": "Usted ya voto en esta encuesta."}))
                            
                        else:
                            vote = Vote.objects.create(choice=selected_choice, number_votes=anterior + 1, user_token=user_token)
                            response = HttpResponse(simplejson.dumps({"operacion": True, "key2": "value"}))
                    else:
                        response = HttpResponse(simplejson.dumps({"operacion": False, "key2": "tiene que loguearse primero."}))
            else:
                vote = Vote.objects.create(choice=selected_choice, number_votes=anterior + 1)
                response = HttpResponse(simplejson.dumps({"operacion": True, "key2": "value"}))  
            response["Access-Control-Allow-Origin"] = "*"  
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"  
            response["Access-Control-Max-Age"] = "1000"  
            response["Access-Control-Allow-Headers"] = "*"
            return response
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
        type = request.POST['type_poll']
    except KeyError:
        response = simplejson.dumps({"response": "faul", "cod_error": "type_poll"})
        return HttpResponse(response, "text/json")
    try:
        question = request.POST['question']
    except KeyError:
        response = simplejson.dumps({"response": "faul", "cod_error": "question"})
        return HttpResponse(response, "text/json")
    try:
        options = request.POST['options']
    except KeyError:
        response = simplejson.dumps({"response": "faul", "cod_error": "options"})
        return HttpResponse(response, "text/json")

    #secumdarias
    #colores
    try:
        fondo = request.POST['fondo']
    except KeyError:
        fondo = "#FFF"
    try:
        borde = request.POST['borde']
    except KeyError:
        borde = "#dcdcdc"
    try:
        subfondo = request.POST['subfondo']
    except KeyError:
        subfondo = "#FFF"
    try:
        letra = request.POST['font']
    except KeyError:
        letra = "#000"
    try:
        letra_subblock = request.POST['font_subblock']
    except KeyError:
        letra_subblock= "#000"
    #font
    try:
        font_style = request.POST['font_style']
    except KeyError:
        font_style = "arial"
    #
    try:
        borde_visible = request.POST['borde_visible']
    except KeyError:
        borde_visible = "si"
    try:
        mostrar_resultados = request.POST['mostrar_resultados']
    except KeyError:
        mostrar_resultados = "si"
    try:
        width = request.POST['width']
    except KeyError:
        width = "300px"
    try:
        height = request.POST['height']
    except KeyError:
        height = "300px"
    try:
        border_width = request.POST['border_width']
    except KeyError:
        border_width = "300px"
    try:
        border_radius = request.POST['border_radius']
    except KeyError:
        border_radius = "10%"
    try:
        padding = request.POST['padding']
    except KeyError:
        padding = "10px"
    try:
        width_subblock = request.POST['width_subblock']
    except KeyError:
        width_subblock = "80%"
    try:
        height_subblock = request.POST['height_subblock']
    except KeyError:
        height_subblock = "50%"
    try:
        width_blocktitle = request.POST['width_blocktitle']
    except KeyError:
        width_blocktitle = "80%"
    try:
        height_blocktitle = request.POST['height_blocktitle']
    except KeyError:
        height_blocktitle = "30%"
    try:
        gradient1= request.POST['gradient1']
    except KeyError:
        gradient1 = "#d6e1e8"
    try:
        gradient2 = request.POST['gradient2']
    except KeyError:
        gradient2= "#b6b7b9"
    try:
        font_size_title = request.POST['font_size_title']
    except KeyError:
        font_size_title= "14"
    try:
        font_size_block = request.POST['font_size_block']
    except KeyError:
        font_size_block = "14"
    try:
        padding_std_options = request.POST['block_std_options']
    except KeyError:
        padding_std_options  = "7"
    try:
        etiquetas = request.POST['etiquetas']
    except KeyError:
        etiquetas = ""
    try:
        landscape = request.POST['landscape']
    except KeyError:
        landscape = "h"
    try:
        request.POST['filter_dateclose']
    except KeyError:
        fecha = None
    else:
        if request.POST['filter_dateclose'] == "yes":
            fecha = datetime.strptime(request.POST['dateclose'], "%m/%d/%Y %H:%M")
        else:
            fecha = None
    try:
        auth = request.POST['requiredAuthentication']
    except KeyError:
        auth= "si"
    
    if request.user.is_authenticated():
        obj = Poll.objects.create(tipo = type, question=question,user=request.user, pub_date=datetime.now(), width=width, height=height, border_visible=borde_visible, border_width=border_width, border_color=borde, background=fondo, border_radius=border_radius, sub_background=subfondo, font_family=font_style, font_color=letra, color_title=letra_subblock, padding=padding, width_subblock=width_subblock, height_subblock=height_subblock, width_blocktitle=width_blocktitle, height_blocktitle=height_blocktitle, gradient1=gradient1, gradient2=gradient2, show_results=mostrar_resultados, size_title=font_size_title, size_block=font_size_block, padding_std_options=padding_std_options, etiquetas=etiquetas, landscape=landscape, fechaCierre=fecha, requiredAuthentication=auth)
    else:
        obj = Poll.objects.create(tipo = type, question=question, pub_date=datetime.now(), width=width, height=height, border_visible=borde_visible, border_width=border_width, border_color=borde, background=fondo, border_radius=border_radius, sub_background=subfondo, font_family=font_style, font_color=letra, color_title=letra_subblock, padding=padding, width_subblock=width_subblock, height_subblock=height_subblock, width_blocktitle=width_blocktitle, height_blocktitle=height_blocktitle, gradient1=gradient1, gradient2=gradient2, show_results=mostrar_resultados, size_title=font_size_title, size_block=font_size_block, padding_std_options=padding_std_options, etiquetas=etiquetas, landscape=landscape, fechaCierre=fecha, requiredAuthentication=auth)
    
    opciones = options.split("\n")
    for i in opciones:
        Choice.objects.create(poll=obj, votes=0, name=i)
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
    c22 = etiquetas
    c23 = landscape
    c24 = border_visible
    c25 = close (si tiene fechs de cierre o no)
    c26 = fecha (fecha para el cierre)
    c27 = requiere authentificacion
    """
    obj = Poll.objects.get(pk=pk)
    choices = obj.get_choices()
    html = ""
    htmlR = ""
    SETTINGS_HOME = os.path.abspath(os.path.dirname(__file__))
    APP_HOME = os.path.split(SETTINGS_HOME)[0]
    path_file = os.path.join(APP_HOME, "polls", "gen_js", "template_js.txt")
    
    if obj.fechaCierre:
        current = timezone.now()
        if current > obj.fechaCierre:
            close = 'si'
            fecha = obj.fechaCierre.strftime("%m/%d/%Y %H:%M")
        else:
            close = 'no'
            fecha = obj.fechaCierre.strftime("%m/%d/%Y %H:%M")
    else:
        close = 'no'
        fecha = "Encuesta abierta"
        
    if obj.tipo == 'radio':
        path_file2 = os.path.join(APP_HOME, "polls", "gen_js", "radio_js.txt")
        path_file3 = os.path.join(APP_HOME, "polls", "gen_js", "radio_js_results.txt")
    else:
        path_file2 = os.path.join(APP_HOME, "polls", "gen_js", "checkbox_js.txt")
        path_file3 = os.path.join(APP_HOME, "polls", "gen_js", "radio_js_results.txt")
    f = open(path_file, "rb")
    fd = f.read()
    f.close()
    
    if close == "no":
        radio = open(path_file2, "rb")
        radio = radio.read()
        radio = str(radio)
    else:
       radio = "encuesta cerrada"
    
    radio2 = open(path_file3, "rb")
    radio2 = radio2.read()
    radio2 = str(radio2)
    total_votos = obj.votes_ultimate()
    
    size_landscape = (97 / choices.count());
    
    for i in choices:
        votos = i.count_votes()
        try:
            porcentaje = ( votos * 100) / total_votos
        except ZeroDivisionError:
            porcentaje = 0
        htmlR += radio2.format(c1=str(i.id), c2=i.name.encode("UTF-8").replace("\r", "").replace('"', "&quot;"), c3=str(votos), c4=str(obj.landscape) ,c5=str(size_landscape), c6=str(porcentaje))
        if close == "no":
            html += radio.format(c1=str(i.id), c2=i.name.encode("UTF-8").replace("\r", "").replace('"', "&quot;"), c3=str(votos), c4=str(obj.landscape) ,c5=str(size_landscape))
        else:
            html = "html += 'Encuesta cerrada &nbsp;&nbsp;&nbsp;&nbsp; <a onclick=" + '"toogle_subblocks()" style="color:white;background:#000;cursor:pointer"' + "> Ver Resultados </a>';"
    send = fd.format(corchete_c="}",corchete_o="{", nombre=obj.question, choices=html, choices_results=htmlR,c1=obj.background, c2=obj.border_radius, c3=str(str(obj.border_width) + " solid " + str(obj.border_color)), c4=obj.width, c5=obj.height, c6=obj.sub_background, c7=obj.font_family, c8=obj.font_color, c9=obj.padding, c10=obj.width_subblock, c11=obj.height_subblock, c12=obj.width_blocktitle, c13=obj.height_blocktitle, c14=obj.color_title, c15=obj.gradient1, c16=obj.gradient2, c17=obj.id, c18=obj.show_results, c19=obj.size_title, c20=obj.size_block, c21=obj.padding_std_options, c22=obj.etiquetas, c23=obj.landscape, c24=obj.border_visible, c25 = close, c26=fecha, c27=obj.requiredAuthentication)

    return HttpResponse(send, "text/javascript")
    
def submit_Contact(request):
    """sube la informacion que dejan en la parte de contacto"""
    name = request.REQUEST["name_crispander"]
    mail = request.REQUEST["mail_crispander"]
    text = request.REQUEST["text_crispander"]
    
    value = Contact.objects.create(name=name, mail=mail,text=text)
    
    return HttpResponse("gracias", "text/plain")
    
