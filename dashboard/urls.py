from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.forecastDash , name='index'),
    path('', views.ForecastDashboardView.as_view(), name='index'),
    # path('new/', views.line_chart , name='new')
    #  path('', views.ForecastView.as_view(), name='dashboard')
    # path('', TemplateView.as_view(template_name='home.html'))

]

# def forecastDash(request):
# demands= Forecast_Master.objects.filter( forecast_type= "TLD_Forecast" , ID= "INDUP000000", date= '2021-12-31' )
# # for d in demands:
# #     print("data", demands)
# print("data", demands[0])
# b="block"
# bNo= 1
# all_demands= []
# blocks=list(range(1,97))
# print("blocks", blocks)
# while bNo <= 96 :
#     blockno=b + str(bNo)
#     # print("blockno", blockno)
#     blockData=getattr(demands[0], blockno)
#     all_demands.append(blockData)
#     bNo +=1


# # all_demands= [demands[0].block1 , demands[0].block2,demands[0].block3,demands[0].block4	,demands[0].block5,
# demands[0].block6, demands[0].block7	, demands[0].block8, demands[0].block9, demands[0].block10	 demands[
# 0].block11	 demands[0].block12	 demands[0].block13	 demands[0].block14	 demands[0].block15	 demands[0].block16
#  demands[0].block17	 demands[0].block18	 demands[0].block19	 demands[0].block20	 demands[0].block21	 demands[
# 0].block22	 demands[0].block23	 demands[0].block24	 demands[0].block25	 demands[0].block26	 demands[0].block27
#  demands[0].block28	 demands[0].block29	 demands[0].block30	 demands[0].block31	 demands[0].block32	 demands[
# 0].block33	 demands[0].block34	 demands[0].block35	 demands[0].block36	 demands[0].block37	 demands[0].block38
#  demands[0].block39	 demands[0].block40	 demands[0].block41	 demands[0].block42	 demands[0].block43	 demands[
# 0].block44	 demands[0].block45	 demands[0].block46	 demands[0].block47	 demands[0].block48	 demands[0].block49
#  demands[0].block50	 demands[0].block51	 demands[0].block52	 demands[0].block53	 demands[0].block54	 demands[
# 0].block55	 demands[0].block56	 demands[0].block57	 demands[0].block58	 demands[0].block59	 demands[0].block60
#  demands[0].block61	 demands[0].block62	 demands[0].block63	 demands[0].block64	 demands[0].block65	 demands[
# 0].block66	 demands[0].block67	 demands[0].block68	 demands[0].block69	 demands[0].block70	 demands[0].block71
#  demands[0].block72	 demands[0].block73	 demands[0].block74	 demands[0].block75	 demands[0].block76	 demands[
# 0].block77	 demands[0].block78	 demands[0].block79	 demands[0].block80	 demands[0].block81	 demands[0].block82
#  demands[0].block83	 demands[0].block84	 demands[0].block85	 demands[0].block86	 demands[0].block87	 demands[
# 0].block88	 demands[0].block89	 demands[0].block90	 demands[0].block91	 demands[0].block92	 demands[0].block93
#  demands[0].block94	 demands[0].block95	 demands[0].block96
# print("blocks", blocks)
# print("all_demands",all_demands)
# # for d in demands:
# #     print("data",d)


# context={
#     'all_demands': all_demands,
#     'blocks': blocks

# }


# return render(request, 'dashboard/forecastDash.html', context)
