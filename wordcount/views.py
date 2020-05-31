
from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

def home(request):
	return render(request,'home.html')
def about(request):
	return render(request,'about.html')	
def count(request):
	fulltext= request.GET['fulltext']
	s=fulltext.split(" ") 
	counter=Counter(s)
	mostcommon=counter.most_common()
	return render(request,'count.html',{'fulltext':fulltext,'count':len(s),'mostcommon':mostcommon})
	
# templates used for html writings!

	
 
