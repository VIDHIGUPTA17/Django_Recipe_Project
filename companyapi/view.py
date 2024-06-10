from django.http import HttpResponse,JsonResponse

def homepage(request):
    print("home page requested")
    list=[
        'ankit',
        'ravi',
        'uttam'
    ]
    return JsonResponse(list,safe=False)