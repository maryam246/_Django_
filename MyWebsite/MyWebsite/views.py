from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import myForm
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from contactenquiry.models import contactEnquiry
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


#simple function for url
def homePage(request):                           # - before column name mean descending without - mean ascending
    """
    subject='Testinge Mail'
    from_email='khanammaryam036@gmail.com'
    msg = '<p>Wellcome to my <b>Website.</p>'
    to='intizarkhan05586501@gmail.com'
    msg=EmailMultiAlternatives(subject,from_email,msg,[to])  # pass the parameter  note here list[] is use in which we pass the multiple email id varable, to send mail
    msg.content_subtype='html'
    msg.send()

    send_mail(
        'testinmail',
        'Here is the message.',
        'khanammaryam036@gmail.com',
        ['intizarkhan05586501@gmail.com'], # where email goes mean TO
        fail_silently=False,
    )
    """
    newsData= News.objects.all()
    servicesData= Service.objects.all().order_by('-service_title')[:3]
   # for i in servicesData:
     #   print(i.service_icon)
   # print(services)
    data = {
           'newsData' :newsData,
           'serviceData':servicesData
       }
    """data = {
        "title": "Home new page",
        'bdata': "Welcome to MyWebsite | Presented by Maryam Khan",
        'clist': ['PHP','Java','Django'],
        'numbers':[10,20,30,40,50],
        'students_details':[
            {'name':'Alina','phone':3323553220},
            {'name':'Horiya','phone':1542353220},
        ],
    }"""
    # request parameter in mandatory
    return render(request,"index.html",data)

def newsDetails(request,slug):
    newsDetails=News.objects.get(news_slug=slug)
    data={
        'newsDetails':newsDetails
    }
    return render(request,'newsdetails.html',data)

def features(request):
    return render(request,'features.html')

def submitform(request):
    try:
        if request.method =="POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalAns = n1 + n2

            data = {
                'n1': n1,
                'n2': n2,
                'output': finalAns,
            }

            return HttpResponse(finalAns)
    except:
        pass

def services(request):
    # __icontains
    ServiceData = Service.objects.all()   # it carry all the data
    paginator = Paginator(ServiceData,1) # in this line we apply limit
    page_no= request.GET.get('page')  # here, we get the number
    ServiceDataFinal= paginator.get_page(page_no) # here, show which page datato show

    totalpage= ServiceDataFinal.paginator.num_pages # it gives the totla number of pages according to the set limit
    """if request.method=="GET":
        st= request.GET.get("servicename")
        if st!=None:
            ServiceData = Service.objects.filter(service_title__icontains=st)
    data = {
        "servicesData" :ServiceData
    }"""
    data={
        "lastpage":totalpage,
        "servicesData":ServiceDataFinal,
        'totalPagelist': [n+1 for n in range(totalpage)]
    }
    return render(request,'services.html',data)

"""def services(request):
    ServiceData = Service.objects.all()
    if request.method=="GET":
        st= request.GET.get("servicename")
        if st!=None:
            ServiceData = Service.objects.filter(service_title=st)
    data = {
        "servicesData" :ServiceData
    }
    if request.method=="GET":
        output = request.GET.get('output')
    return render(request,'services.html', {'output':output},data)"""

def contact(request):
    return render(request,'contact.html')

def saveEnquiry(request):
    n=''
    if request.method=="POST":
        name= request.POST.get('name')   # here, we get /recive the data
        email= request.POST.get('email')
        phone = request.POST.get('phone')
        websitelink = request.POST.get('websitename')
        message = request.POST.get('message')
        en= contactEnquiry(name=name,email=email,phone=phone,websitelink=websitelink,message=message)
        en.save()
        n='Data Inserted.'
    return render(request, 'contact.html',{'n':n})
def userform(request):
    finalAns = 0
    fn = myForm()
    data = {'form': fn}
    try:
        if request.method =="POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalAns = n1 + n2

            data = {
                'form': fn,
                'output': finalAns,
            }
            url= "/services/?output={}".format(finalAns)

            return redirect(url)
        #n1= int(request.GET['num1'])
        #n2 = int(request.GET['num2'])

    except:
        pass
    return render(request,'userform.html',data)

def calculator(request):
    c =""
    try:
        if request.method=="POST":
            n1 = float(request.POST.get('num1'))
            n2 = float(request.POST.get('num2'))
            Operator = request.POST.get('Operator')

            if Operator =="+":
                c = n1+n2;
            elif Operator =="-":
                c = n1-n2
            elif Operator =="*":
                c = n1*n2
            elif Operator =="/":
                c = n1/n2

        data={
            'n1':n1,
            'n2':n2,
            'c':c,
        }
    except:
        c = "Invalid operation"

    print(c)
    return render(request,'calculator.html', data)


def evenodd(request):
    c =''
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request, 'evenodd.html', {'error': True})

        n = int(request.POST.get('num1'))
        if n % 2==0:
            c = "Even number"
        else:
            c ="Odd number"
    return render(request,'evenodd.html',{'c':c})

def markssheet(request):
    if request.method=="POST":
        s1 = int(request.POST.get('Subject1'))
        s2 = int(request.POST.get('Subject2'))
        s3 = int(request.POST.get('Subject3'))
        s4 = int(request.POST.get('Subject4'))
        s5 = int(request.POST.get('Subject5'))
        t = s1+s2+s3+s4+s5
        p= t*100/500;

        if p>=60:
            r= 'First Division'
        elif p>=48:
            r= 'Second Division'
        elif p>=35:
            r= 'Third Division',
        else:
            r= 'Fail'

        data={
            'total':t,
            'percentage':p,
            'division':r
        }
        return render(request, "markssheet.html", data)

    return render(request,"markssheet.html")