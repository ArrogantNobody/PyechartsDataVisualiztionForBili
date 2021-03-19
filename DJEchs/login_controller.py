from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ccid_verify(request):
    if request.method == "POST":
        username = request.POST['username']
        if username == 'zihao17':
            return redirect('/dashboard/')
        else:
            return render(request, 'Signin Template for Bootstrap.html', {'script':"alert",'wrong':'账号错误'})


def login_map(request):
    return render(request, 'Signin Template for Bootstrap.html')

def login_success(request):
    return render(request, 'data_dashboard.html')