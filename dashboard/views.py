from cgi import test
import json
import random
from operator import attrgetter
# from chartjs.views.lines import BaseLineChartView
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Forecast_Master
# from django.db.models import F


# import pandas as pd
BLOCK_CONSTANTS = [
    'block1', 'block2', 'block3', 'block4', 'block5', 'block6', 'block7', 'block8', 'block9', 'block10', 'block11',
    'block12', 'block13', 'block14', 'block15', 'block16', 'block17', 'block18', 'block19', 'block20', 'block21',
    'block22', 'block23', 'block24', 'block25', 'block26', 'block27', 'block28', 'block29', 'block30', 'block31',
    'block32', 'block33', 'block34', 'block35', 'block36', 'block37', 'block38', 'block39', 'block40', 'block41',
    'block42', 'block43', 'block44', 'block45', 'block46', 'block47', 'block48', 'block49', 'block50', 'block51',
    'block52', 'block53', 'block54', 'block55', 'block56', 'block57', 'block58', 'block59', 'block60', 'block61',
    'block62', 'block63', 'block64', 'block65', 'block66', 'block67', 'block68', 'block69', 'block70', 'block71',
    'block72', 'block73', 'block74', 'block75', 'block76', 'block77', 'block78', 'block79', 'block80', 'block81',
    'block82', 'block83', 'block84', 'block85', 'block86', 'block87', 'block88', 'block89', 'block90', 'block91',
    'block92', 'block93', 'block94', 'block95', 'block96'
]

BLOCKS_TABLE = ['block1', 'block2', 'block3', 'block4', 'block5']

class ForecastDashboardView(TemplateView):
    template_name = 'index.html'
    model = Forecast_Master

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = self.request.GET.get('refdate', None)
        States= self.request.GET.get('states', None)
        forecast_types = self.request.GET.getlist('ftype')
        # editedblock1 = self.request.GET.get('block1')
        # editedblock2 = self.request.GET.get('block2')
        # editedblock3 = self.request.GET.get('block3')
        # editedblock4 = self.request.GET.get('block4')
        # editedblock5 = self.request.GET.get('block5')
      
        # print("self.request.GET",self.request.GET)
        # print("forecast_types", forecast_types)
        # print("states", type(States) )
       
        
        state_choices = [
            'INDBH000000', 'INDMPCZ0000', 'INDMPEZ0000', 'INDMPMP0000', 'INDMPWZ0000', 'INDUP000000'
        ]

        states = {'Uttar Pradesh': 'INDUP000000', 'Madhya Pradesh': 'INDMPMP0000',
              'Madhya Pradesh East Zone': 'INDMPEZ0000', 'Madhya Pradesh West Zone': 'INDMPWZ0000',
              'Madhya Pradesh Central Zone': 'INDMPCZ0000', 'Bihar': 'INDBH000000'}     

        forecast_type_choices = list(Forecast_Master.objects.all().values_list("forecast_type",flat=True).distinct())

        
        
        date_choices = Forecast_Master.objects.all().exclude(
            date__isnull=True
        ).values_list('date', flat=True).order_by('-date').distinct()
        datasets = []
        datasets_table = []
        border_colors = [
            'indianred', 'salmon', 'darksalmon', 'crimson', 'red', 'darkred', 'pink', 'hotpink', 'deeppink',
            'palevioletred', 'coral', 'tomato', 'orangered', 'darkorange', 'orange', 'gold', 'palegoldenrod',
            'darkkhaki', 'thistle', 'plum', 'violet', 'orchid', 'fuchsia', 'magenta', 'rebeccapurple', 'blueviolet',
            'darkviolet', 'darkorchid', 'darkmagenta', 'purple', 'indigo', 'slateblue', 'darkslateblue', 'greenyellow',
            'lawngreen', 'limegreen', 'springgreen', 'seagreen', 'forestgreen', 'green', 'darkgreen', 'yellowgreen',
            'olivedrab', 'darkolivegreen', 'darkseagreen', 'darkcyan', 'teal', 'cyan', 'aquamarine', 'turquoise',
            'darkturquoise', 'cadetblue', 'steelblue', 'powderblue', 'skyblue', 'deepskyblue', 'dodgerblue',
            'cornflowerblue', 'royalblue', 'blue', 'darkblue', 'navy', 'midnightblue', 'burlywood', 'tan', 'rosybrown',
            'sandybrown', 'goldenrod', 'darkgoldenrod', 'peru', 'chocolate', 'saddlebrown', 'sienna', 'brown', 'maroon',
            'aliceblue', 'darkgray', 'darkslategray', 'black'
        ]
        # print("states now",States)
        # print("datenow",date)
        # test = self.model.objects.filter(forecast_type='TLD_Forecast',date=date,ID=States)
        # print("test OBJECT===>",test )
        for forecast in forecast_types:
            fc = self.model.objects.filter(
                forecast_type__iexact=forecast, date=date,loc_ID =States
            ).first()  
            
            print("FC OBJECT===>", fc)
            block_values = attrgetter(*BLOCK_CONSTANTS)(fc)
            block_values_table = attrgetter(*BLOCKS_TABLE)(fc)
            color = random.choice(border_colors)
           
            datasets.append({
                'label': fc.forecast_type,
                'borderColor': color,
                'borderWidth': 2,
                'data': block_values
            })
            datasets_table.append(block_values_table)

         
        # print("datasets",datasets) 
        # print("datasets_table",datasets_table)
        # demand_instance=''
        
        # for forecast in forecast_types: 
        #     demand_instance = Forecast_Master.objects.filter(forecast_type=forecast,date=date,loc_ID =States)
            # demand_instance.block1=editedblock1
            # demand_instance.block2=editedblock2
            # demand_instance.block3=editedblock3
            # demand_instance.block4=editedblock4
            # demand_instance.block5=editedblock5
            # demand_instance.save()
            
        
        # for d in demand_instance: 
        # #  demand_instance.block1 = editedblock1
        #  print(d.block1) 
       
        # print("demand_instance",demand_instance)
        # for demand in demand_instance:
        #     print(demand.block1)
        
        context['datasets'] = json.dumps(datasets)
        context['labels'] = json.dumps([i for i in range(1, 97)])
        context['fcast_types'] = forecast_type_choices
        context['date_choices'] = date_choices
        context['states'] = states
        context['f_type_selected'] = forecast_types
        # context['demand_instance'] = demand_instance
        return context





