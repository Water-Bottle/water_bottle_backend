from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import JsonResponse


def login_view(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            data = {
                'status': True,
            }
            return JsonResponse(data)
    # anything else is a failure
    data = {
        'status': False,
    }
    return JsonResponse(data)

