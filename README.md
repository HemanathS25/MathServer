# Ex.05 Design a Website for Server Side Processing
## Date:05/12/2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :

```
math.html

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<title>POWER CALCULATOR</title>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<style type="text/css">
body {
    background-image: linear-gradient(to right,#4ca1af,#c4e0e5)



     
}

.edge {
    width: 100%;
    text-align: center;

}
.box {
    display: inline-block;
    border: BLUE;
    width: 600px;
    min-height: 400px;
    font-size: 20px;
    background-color: gray;
    font-style: italic;
}
.formlet{
    margin-top: 20px;
    font-style: italic;
    font-weight: normal;
}
#formelt {
   margin-top: 20px;
   font-style: oblique;
    font-weight: bold;

}
h1 {
    color: orange;
    padding-top: 20px;
}
.i1{
    font-style: italic;
    font-weight: normal;
    margin-left: 60px;
    margin-top: 20px;
   
}
#i1{
    height: 30px;
    width:220px;
    text-align: center;
}
.r1{
    font-style: italic;
    font-weight: normal;
    margin-bottom: 20px;
    margin-top: 30px;
}
#r1{
    height: 30px;
    width:220px;
    text-align: center;
}
.c1{
    font-style: italic;
    font-weight: normal;
    
}
#c1{
    background: red;
    height: 30px;
    color: white;
    width: 100px;
    border: none;
}
.owner{
    color : purple
}
p{
    padding-top: 50px;
    font-size: x-large;
    color: azure;
}

</style>
</head>
<body>
    
    <center>
    <h2 class="owner"> <b>HEMANATH S (24009648)</b></h2>
</center>
<div class="edge">
    <div class="box">
        <h1>POWER CALCULATOR </h1>
        <form method="POST">
            {% csrf_token %}
            <div class="i1">
                Intensity: <input type="text" name="Intensity" placeholder="Enter Intensity" value="{{i}}" id="i1" > A<br/>
            </div>
            <div class="r1">
                Resistance: <input type="text" name="Resistance" placeholder="Enter resistance" value="{{r}}" id="r1"> Ω<br/>
            </div>
            <div class="c1">
                <input type="submit" value="Calculate" id="c1"><br/>
            </div>
            <div class="formelt">
                Power: <input type="text" name="power" value="{{power}}" id="formelt"> W<br/>
            </div>
        </form>
        
    </div>
</div>
<center>
<h4>Power is defined as the rate at which work is done upon an object. Power is a time-based quantity. <br>
    The unit for standard metric work is the Joule and the standard metric unit for time is the second, so the standard metric unit for power is a Joule / second, defined as a Watt and abbreviated W.

</h4>
<h2>P = I<sup>2</sup>/R</h2>
<h4>P : Power <br>
    I : Intensity <br>
    R : Resistance
</h4>
</center>
</body>
</html>

views.py

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

urls.py

from django.contrib import admin 
from django.urls import path 
from powerapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('power/',views.power,name="calculatepower"),
    path('',views.power,name="calculatepower")
]

```


## SERVER SIDE PROCESSING:
![alt text](<Screenshot (23).png>)



## HOMEPAGE:


![alt text](<Screenshot (24).png>)


## RESULT:
The program for performing server side processing is completed successfully.
