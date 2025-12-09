from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    """Contact form view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message
            contact_message = form.save(commit=False)
            contact_message.ip_address = request.META.get('REMOTE_ADDR')
            contact_message.save()
            
            # Send email notification
            send_mail(
                f"New Contact Message: {contact_message.subject}",
                f"From: {contact_message.name} ({contact_message.email})\n\n{contact_message.message}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)

def contact_success(request):
    """Contact success page"""
    return render(request, 'contact/success.html')