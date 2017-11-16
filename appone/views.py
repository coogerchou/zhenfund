# -*- coding: ascii -*-
from django.views.generic import TemplateView

from django.shortcuts import render, redirect

from .forms import ContactForm, SignUpForm, TransferForm

from .code import Code

from .models import Transfer


# Create your views here.


def post(request):

	template_title = 'forms.html'

	form = TransferForm(request.POST or None)

	result = 'Upload your raw txt and you will get what you want'
		
	if form.is_valid():

		instance = form.save(commit=False)
			
		if instance.original_txt == None:
			instance.original_txt == 'Please enter the whole txt'
		if instance.email == None:
			instance.email== 'Please use @zhenfund.com'
		instance.save()
			

		print(instance.email)
		print(instance.timestamp)
		#print(ascii(Code(instance.original_txt)))


		result = Code(instance.original_txt)
		form = TransferForm
		#return redirect('home:home')



	args = {'form':form,'result':result}
	return render(request, template_title, args)



'''
class HomeView(TemplateView):
	template_title = 'forms.html'

	def get(self, request):
		form = TransferForm
		posts = Transfer.objects.all()

		args = {'form':form, 'posts':posts}
		print(posts)
		return render(request, template_title, args)



	def post(self, request):
		form = TransferForm(request.POST or None)
		
		if form.is_valid():
			instance = form.save(commit=False)
			
			if instance.original_txt == None:
				instance.original_txt == 'Please enter the whole txt'
			instance.save()
			

			print(instance.email)
			print(instance.timestamp)
			#print(ascii(Code(instance.original_txt)))


			result = Code(instance.original_txt)
			form = TransferForm
			return redirect('home:home')

		args = {'form':form,'result':result}
		return render(request, self.template_title,args)



def home(request):
	title = 'Welcome'
	if request.user.is_authenticated():
		title = 'My Title %s' %(request.user)



	#add a form
	#if request.method == 'POST':
	#	print request.POST
	#add a form
	#request.POST means the user has to send something
	#or None means None is OK
	form = TransferForm(request.POST or None)
	posts = Transfer.objects.all()



	if form.is_valid():
		#save(commit=False) means the timestamp and other information is not saved
		instance = form.save(commit=False)
		if instance.original_txt == None:
			instance.original_txt == 'Please enter the whole txt'
		instance.save()
		print(instance.email)
		print(instance.timestamp)
		#print(ascii(Code(instance.original_txt)))
		result = Code(instance.original_txt)


	context = {
		'template_title' : title,
		'form' : form,
		

	}

	return render(request,"forms.html",context)


def contact(request):

	form = ContactForm(request.POST or None)
	#because this is not a model.form so we can not save

	if form.is_valid():

		for key in form.cleaned_data:
			
			print(form.cleaned_data.get(key))
		#email = form.cleaned_data.get('email')
		#message = form.cleaned_data.get('message')
		#full_name = form.cleaned_data.get('full_name')
		#print(email,message,full_name)

	context = {
		'form':form,

	}

	return render(request,'forms.html',context)
'''
