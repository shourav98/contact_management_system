from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})


def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/edit_contact.html', {'form': form, 'contact': contact})



def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})


def contact_list(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(first_name__icontains=query) | Contact.objects.filter(email__icontains=query)
    else:
        contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})
