from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def insert_topic(request):
    tn=input("enter the topic_name:")
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse("topicobject inserted successfully")
def insert_webpage(request):
    t=input("enter the topic_name:")
    to=topic.objects.get_or_create(topic_name=t)[0]
    to.save()
    n=input("enter the name:")
    ur=input("enter the urlfield")
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=ur)[0]
    wo.save()
    return HttpResponse("webpage object is inserted successfully")
def insert_access(request):
    t=input("enter the topic name:")
    tobject=topic.objects.get_or_create(topic_name=t)[0]
    tobject.save()
    nam=input("enter the name:")
    ur=input("enter the url:")
    wobject=webpage.objects.get_or_create(topic_name=tobject,name=nam,url=ur)[0]
    wobject.save()
    a=input("enter the author name:")
    em=input("enter the email:")
    aobject=accessrecords.objects.get_or_create(name=wobject,author=a,email=em)[0]
    aobject.save()
    return HttpResponse("accessrecords object got inserted successfully")
def topic_insert(request):
    t=input("enter the topic name:")
    to=topic.objects.get_or_create(topic_name=t)[0]
    to.save()
    qsto=topic.objects.all()
    dict={"qsto":qsto}
    return render(request,"topic_insert.html",dict)
def webpage_insert(request):
    t=input("enter the topic_name:")
    to=topic.objects.get(topic_name=t)
    na=input("enter the name:")
    u=input("enter the url:")
    wo=webpage.objects.get_or_create(topic_name=to,name=na,url=u)[0]
    wo.save()
    qswo=webpage.objects.all()
    d={"qswo":qswo}
    return render(request,"webpage_insert.html",d)


def access_insert(request):
    tn=input("enter the topic_name")
    to=topic.objects.get(topic_name=tn)
    p=input("enter the pk")
    wo=webpage.objects.get(pk=p)
    a=input("enter the author:")
    em=input("enter the email:")
    ao=accessrecords.objects.get_or_create(name=wo,author=a,email=em)[0]
    ao.save()

    qsao=accessrecords.objects.all()
    d={"qsao":qsao}
    return render(request,"access_insert.html",d)

def display_webpage(request):
    qswo=webpage.objects.all()
    d={"qswo":qswo}
    return render(request,"webpage_insert.html",d)


def retrieving(request):
    qset=webpage.objects.all().order_by("topic_name")
    qset=webpage.objects.all().order_by("name")
    qset=topic.objects.all().order_by("topic_name")
    qset=accessrecords.objects.all().order_by("author")
    qset=accessrecords.objects.all().order_by("author")
    qset=webpage.objects.all().order_by("topic_name")
    qset=webpage.objects.all().order_by("name")
    qset=webpage.objects.all().order_by("-name")
    qset=webpage.objects.all().order_by(Length("name"))
    qset=accessrecords.objects.all().order_by(Length("author"))
    qset=webpage.objects.all().order_by(Length("name").desc())
    qset=topic.objects.all().order_by(Length("topic_name"))
    qset=topic.objects.all().order_by(Length("topic_name").desc())
    qset=webpage.objects.filter(name__startswith="p")
    qset=webpage.objects.filter(name__endswith="o")
    qset=accessrecords.objects.filter(author__startswith="a")
    qset=accessrecords.objects.all()
    qset=accessrecords.objects.all()
    qset=accessrecords.objects.filter(author__startswith="a")
    qset=accessrecords.objects.filter(author__contains="chand")
    qset=accessrecords.objects.filter(author__startswith="r")
    qset=topic.objects.filter(topic_name__in=("cricket","hockey"))
    qset=topic.objects.filter(topic_name__in=("chess","volleyball"))
    qset=accessrecords.objects.filter(date__year=2023)
    qset=accessrecords.objects.filter(date__day__gt=25)
    qset=accessrecords.objects.filter(date__day__lt=26)
    qset=accessrecords.objects.filter(date__day=25)
    qset=webpage.objects.filter(Q(topic_name="football") & Q(name__contains="r"))
    qset=webpage.objects.filter(Q(name__startswith="k") & Q(topic_name="c"))
    qset=webpage.objects.all()
    d={"qset":qset}
    return render(request,"retrieving.html",d)

def updating(request):
    webpage.objects.filter(name="kohli").update(url="https://kohli.com")
    webpage.objects.filter(name="bheem").update(url="https://chottabheem.com")
    webpage.objects.filter(name="hdksld").update(url="hiiiii.com")
    webpage.objects.filter(name="pvsindhu").update(topic_name="tennis")
    webpage.objects.filter(name="ronaldo").update(topic_name="chess")
    webpage.objects.update_or_create(name="dhoni",defaults={"url":"https.mahindrasdhoni.com"})




    qset=webpage.objects.all()
    d={"qset":qset}
    return render(request,"retrieving.html",d)

