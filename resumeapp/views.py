from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact_me, About, Education, Professional, Service, Friend, Links


# Create your views here.


def index(request):
    contact = Contact_me.objects.all()
    about = About.objects.all()
    education = Education.objects.all()
    pro = Professional.objects.all()
    service = Service.objects.all()
    friend = Friend.objects.all()
    links = Links.objects.first()

    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    ctx = {
        'form': form,
        'contact': contact,
        'about': about,
        'education': education,
        'pro': pro,
        'service': service,
        'friend': friend,
        'links': links,
    }
    return render(request, 'index.html', ctx)


def service_detail(request, pk):
    service_pk = Service.objects.get(id=pk)
    service = Service.objects.all()
    ctx = {
        'detail': service_pk,
        'service': service
    }
    return render(request, 'service-details.html', ctx)
