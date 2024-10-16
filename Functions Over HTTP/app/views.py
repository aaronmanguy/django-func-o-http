from django.http.response import HttpResponse


def hey_you(request, name):
    return HttpResponse(f"Hey, {name}!")

def how_old(request,end, birthyear):
    result = (end - birthyear)
    return HttpResponse(result)

def order_total(request, burgers, fries, drinks):
    b_total = burgers * 4.5
    f_total = fries * 1.5
    d_total = drinks * 1
    total = (b_total + f_total + d_total)
    return HttpResponse(total)