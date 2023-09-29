from django.shortcuts import render,redirect
from todo_app.models import todo_data
# Create your views here.

def homePage(req):
    # fetching data from database 
    data = todo_data.objects.all()
    if req.method == "POST":
       item = req.POST.get('item')
       # uploading data in database from user input 
       upload_data = todo_data(text=item)
       upload_data.save()
    return render(req,"homepage/home.html",{"data":data})

def delete(req,id):
    # Deleting specific item by id 
    id = todo_data.objects.get(id=id)
    id.delete()
    return redirect("/")
