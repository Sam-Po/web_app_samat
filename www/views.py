from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Record


def redirect(request):
    return HttpResponseRedirect(reverse('main'))


def main(request):
    contacts = Record.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request, 'www/index.html', context)


def new_contact(request):
    if request.method == "GET":
        return render(request, 'www/create.html')
    elif request.method == "POST":
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            phone = request.POST['phone']
            email = request.POST['email']
            contact = Record(first_name = first_name, last_name = last_name, phone = phone, email = email)
            contact.save()
            return HttpResponseRedirect(reverse('main'))
        except Exception as e:
            return HttpResponse(status=500)


def show_contact(request, contact_id):
    contact = Record.objects.get(id=contact_id)
    context = {
        'contact': contact,
    }
    return render(request, 'www/update.html', context)


def update_contact(request):
    contact_id = request.POST['contact_id']
    new_first_name = request.POST['first_name']
    new_last_name = request.POST['last_name']
    new_phone = request.POST['phone']
    new_email = request.POST['email']
    contact = Record.objects.get(id = contact_id)
    contact.first_name = new_first_name
    contact.last_name = new_last_name
    contact.phone = new_phone
    contact.email = new_email
    contact.save()
    return HttpResponseRedirect(reverse('main'))


def delete_contact(request):
    contact_id = request.POST['contact_id']
    contact = Record.objects.get(id=contact_id)
    contact.delete()
    return HttpResponseRedirect(reverse('main'))


