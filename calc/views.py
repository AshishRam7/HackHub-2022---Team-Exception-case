from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import smtplib
from email.message import EmailMessage



# Create your views here.


def home(request):

    return render(request, 'home.html', {'name': 'Ashish'})


def add(request):

    soil = str(request.POST['soil'])
    month = str(request.POST['month'])
    ph = float(request.POST['ph'])
    temp = float(request.POST['temp'])
    rainfall = float(request.POST['rainfall'])

    soils_for_each_crop = {

        # soil suitable for paddy:
        'paddy': [
            'sand loamy',
            'silty loam',
            'clay loamy',
            'silty'
        ],

        # soil suitable for wheat:
        'wheat': [
            'loamy',
            'clay loamy'
        ],
        # soil suitable for cotton:
        'cotton': [
            'alluvial',
            'clayey',
            'red loamy'],

        # soil suitable for maize:
        'maize': [
            'alluvial',
            'clay loamy',
            'red loamy',
            'clay loamy',
            'sand loamy'],

        # soil suitable for jowar:
        'jowar': [
            'sand loamy'
        ],
    }

    crops = {
        'paddy': 0,
        'wheat': 0,
        'cotton': 0,
        'maize': 0,
        'jowar': 0,
    }

    paddy = 0
    wheat = 0
    cotton = 0
    maize = 0
    jowar = 0

    # paddy_ph = [6, 7]
    # paddy_ph = [6, 7]
    # paddy_ph = [6, 7]
    # paddy_ph = [6, 7]
    # paddy_ph = [6, 7]

    for i in soils_for_each_crop:
        if soil in soils_for_each_crop[i]:
            crops[i] += 1
        else:
            crops[i] -= 5

    # print(crops)

    # print(crops)

    month_for_each_crop = {

        # sowing month suitable for paddy:
        'paddy': [
            'kharif'
        ],

        # month suitable for wheat:
        'wheat': [
            'rabi'
        ],

        # month suitable for cotton:
        'cotton': [
            'kharif'
        ],

        # month suitable for maize:
        'maize': [
            'kharif',
            'rabi'
        ],

        # month suitable for jowar:
        'jowar': [
            'kharif',
            'rabi'
        ],
    }

    for i in month_for_each_crop:
        if month in month_for_each_crop[i]:
            crops[i] += 1
        else:
            crops[i] -= 5

    '''
    if ph>=5 and ph<=9.5:
    paddy+= 1
    if ph>=6 and ph<=7:
        wheat+=1
        maize+=1
        cotton+=1
        jowar+=1
    elif ph<6 and ph>=5.5:
        maize+=1
    elif ph>7 and ph<=7.5:
        jowar+=1
        maize+=1
    elif ph>7.5 and ph<=8:
        cotton+=1
    '''

    # checking for ph level of soil

    if ph >= 6 and ph <= 7:
        wheat += 1
        maize += 1
        cotton += 1
        paddy += 1
        jowar += 1

    elif ph <= 5.5 and ph < 6:
        maize += 1
        paddy += 1

    elif ph >= 5 and ph < 5.5:
        paddy += 1

    elif ph > 7 and ph <= 7.5:
        paddy += 1
        jowar += 1
        maize += 1
        cotton += 1

    elif ph > 7.5 and ph <= 8:
        paddy += 1
        cotton += 1

    elif ph > 8 and ph <= 9.5:
        paddy += 1

    # paddy final

    # wheat final

    '''for i in crops:
    crops[i]+=paddy
    '''

    # print(crops)

    # jowar(kharif)- 6 to 7.5
    # jowar(rabi)- 6 to 7.5
    # paddy - 5 to 9.5
    # maize(kharif)- 5.5 to 7.5
    # maize(rabi)-5.5 to 7.5
    # cotton - 6 to 8
    # wheat -6 to 7

    # temperature checking:

    if temp >= 25 and temp <= 30:
        cotton += 1
        paddy += 1
        jowar += 1
        maize += 1

    elif temp >= 21 and temp < 25:
        wheat += 1
        cotton += 1
        paddy += 1

    elif temp > 30 and temp <= 32:
        cotton += 1
        jowar += 1

    elif temp >= 25 and temp <= 30:
        cotton += 1
        paddy += 1
        jowar += 1
        maize += 1

    elif temp >= 21 and temp < 25:
        wheat += 1
        cotton += 1
        paddy += 1

    elif temp > 30 and temp <= 32:
        cotton += 1
        jowar += 1

    # jowar(kharif)-25°C - 32°C
    # paddy - 16-30° C
    # maize-25°C - 30°C
    # cotton - 15-35°C
    # wheat -21-26°C

    # checking rainfall:
    if rainfall >= 20 and rainfall <= 40:
        jowar += 1
        wheat += 1

    elif rainfall > 20 and rainfall <= 75:
        wheat += 1

    elif rainfall > 50 and rainfall <= 100:
        cotton += 1
        maize += 1

    elif rainfall > 100:
        paddy += 1

    elif rainfall >= 21 and rainfall < 25:
        wheat += 1
        cotton += 1
        paddy += 1

    elif rainfall > 30 and rainfall <= 32:
        cotton += 1
        jowar += 1

    #print(paddy,wheat,cotton, maize, jowar)

    # jowar(kharif)- 20 cm - 40cm
    # paddy - 100 cm - 200 cm
    # maize(kharif) - 50 cm - 100 cm
    # cotton - 55 cm - 100 cm
    # wheat - 20 - 75cm
    # paddy final
    crops['paddy'] += paddy
    crops['wheat'] += wheat
    crops['jowar'] += jowar
    crops['maize'] += maize
    crops['cotton'] += cotton

    # print(crops)

    # max=0
    # for i in crops:
    #   if crops[i]>max:
    #       max+=crops[i]

    # print(max)
    # wheat final

    res = max(crops, key=crops.get)
    
    email = request.user.email
    first_name=request.user.first_name
    print(email)
    '''
    with open("../templates/result.html") as f:
        content = f.read()'''

    if res == 'wheat':
        email_alert("Hey", res, email)

    elif res == 'maize':
        email_alert("Hey", res, email)

    elif res == 'paddy':
        email_alert("Hey", res, email)

    elif res == 'cotton':
        email_alert("Hey", res, email)

    elif res == 'jowar':
        email_alert("Hey", res, email)

    return render(request, 'result.html', {'res': res})


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = 'agroxtech22@gmail.com'
    password = "".join(list(map(chr, list(map(int, '104.109.101.114.104.97.115.111.111.109.100.114.103.117.114.107'.split("."))))))
    msg['from'] = user

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


def labs(request):
    return render(request, 'pricing.html')