from django.http import HttpResponse
from main.admin_forms import TestingDynamicForm
from django.shortcuts import render
import json

def test(request):
    """if(request.method == "POST"):
        path = request.POST.get("path",[])
        form = ProductAdminForm(path=path)

    else:     
        form = ProductAdminForm(path=[])
    return render(request,'dynamic_form.html',{'form':form})"""
    path_str = request.POST.get('path', '')
    path = list(map(int, path_str.split(','))) if path_str else []

    if request.method == 'POST':
        selected_id = request.POST.get('field')
        if selected_id:
            path.append(int(selected_id))

    form = TestingDynamicForm(path=path)
    return render(request, 'dynamic_form.html', {'form': form})