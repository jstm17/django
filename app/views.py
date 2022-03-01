from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from .models import Question
from .forms import QuestionForm

# QUESTIONS LIST
def list(request):

	context = {"dataset" : Question.objects.all()}
		
	return render(request, "app/index.html", context)

# CREATE QUESTIONS
def create(request):
	context ={}

	form = QuestionForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context = {'form' : form}
	return render(request, "app/create.html", context)

# QUESTIONS DETAILS

def details(request, id):
    context = {"data" : Question.objects.get(id = id)}
         
    return render(request, "app/details.html", context)

# UPDATE QUESTIONS

def update(request, id):
    obj = get_object_or_404(Question, id = id)
 
    form = QuestionForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app/"+id)
 
    context = {"form" : form, "data" : Question.objects.get(id = id)}
 
    return render(request, "app/update.html", context)

# DELETE QUESTIONS

def delete(request, id):
    context = {"data" : Question.objects.get(id = id)}
    obj = get_object_or_404(Question, id = id)
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/app")
 
    return render(request, "app/delete.html", context)