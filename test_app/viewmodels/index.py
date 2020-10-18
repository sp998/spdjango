#This import is common for every viewmodel eg:render, models etc
from .common_imports import  * 

#any other imports which are specifc to this particular view
from django.http import HttpResponse

#Create model
#You can remove this if you don't need any model
#Do make migrations after adding this
class TestModel(models.Model):
    name=models.CharField(max_length=300)



#if you don't define get_path function 
#you will get this view with url <name of this file>
#if you don't define this function at all 
#it will try to render the default template with name "default.html"
#if you don't have any "default.html" then you'll get an error

def get_view():
    def index_view(request):
        names=TestModel.objects.all()
        context={"names":names}
        return HttpResponse("<h1>Index Page</h1>")
    return index_view

#Url Pattern
#you can remove this you don't want to specify the url 
#The url will be <name of this file>
def get_path():
    return path("index",get_view(),name="index")

#Register model  to Admin Site
#You can remove this if you don't want to register your model to admin page
def model_register():
    return TestModel