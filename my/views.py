from django.shortcuts import render
from .models import contact
import requests
import json
# Create your views here.
#from django.http import HttpResponse

def menu(request):
	if request.method == 'POST':
		firstname=request.POST.get('fname')
		lastname=request.POST.get('lname')
		
		r=requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
		jason_data = json.loads(r.text)
		joke = jason_data.get('value').get('joke')
		context = {'joker':joke}
		return render(request, 'my/menu.html',context)

		#mot = requests.get('http://quotes.rest/qod.json')
		#jason_d=json.loads(mot.text)
		#motivation = jason_d.get('contents').get('quote')
		#print(motivation)
		#return render(request,'my/menu.html')
	else:
		firstname='Vinoth'
		lastname='K'

		r=requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
		jason_data = json.loads(r.text)
		joke = jason_data.get('value').get('joke')
		context = {'joker':joke}
		return render(request, 'my/menu.html',context)
		
def Portfolio(request):
	return render(request,'my/portfolio.html')

def Contact(request):
		if request.method == 'POST':
			mail_m = request.POST.get('email')
			subject_m = request.POST.get('subject')
			message_m = request.POST.get('message')

			con=contact(email = mail_m,subject=subject_m,message=message_m)
			con.save()

			return render(request,'my/thankyou.html')
		else:
			return render(request,'my/contact.html')
		
	