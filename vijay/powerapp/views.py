from django.shortcuts import render 
def power(request): 
    context={} 
    context['power'] = "0" 
    context['r'] = "0" 
    context['i'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        r = request.POST.get('Resistance','0')
        i = request.POST.get('Intensity','0')
        print('request=',request) 
        print('Resistance=',r) 
        print('Intensity=',i) 
        power = int(r) *int(i) *int(i) 
        context['power'] = power
        context['r'] = r
        context['i'] = i
        print('power=',power) 
    return render(request,'powerapp/math.html',context)

