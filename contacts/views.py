from django.shortcuts import  redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import Contact

def contact(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']


        #Check if user has made any inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request,'You have alraedy made an inquiry for this listing')
                return redirect('/listings/'+ listing_id)



        contact = Contact(listing = listing, listing_id = listing_id, name = name, email = email, message = message, phone = phone,
        user_id = user_id)

        contact.save()

        #Send Email
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry'+ listing +'. Sign into the admin panel for more info',
            'vashishthadeepak2@gmailcom',
            [realtor_email, 'vashishthadeepak1@gmail.com'],
            fail_silently= False
        )

        messages.success(request, 'Your inquiries has been submitted we will get back to you soon')
        return redirect('/listings/'+ listing_id)

