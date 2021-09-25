from .form import DataForm
from django.shortcuts import render
import os
import requests

def search(gender_val, species_val):  
   url = 'https://rickandmortyapi.com/api/character'
   params =  {"gender": gender_val,  "species": species_val}
   print(gender_val)
   if gender_val==None or species_val==None:
      r = requests.get(url, headers={'Authorization':'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
   else:
      r = requests.get(url, params=params, headers={'Authorization':'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
   
   data = r.json()
   data_list = []
   for i in range(len(data['results'])):
      data_list.append(data['results'][i])
   return data_list

def getdata(request):
    search_result = {}
    
    form = DataForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
       gender = form.cleaned_data['gender']
       species = form.cleaned_data['species']
       search_result = search(gender, species)
   
    else:
       search_result = search(None, None)

   

    return render(request, 'ricky_morty.html', {'form': form, 'data': search_result})