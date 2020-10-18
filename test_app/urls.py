from .import views
from django.urls import path
from django.views.generic import TemplateView
from os.path import dirname
import test_app.viewmodels as viewmodels
from test_app.viewmodels import  *


urlpatterns=[

]
for module in viewmodels.get_modules():
        module_name=module.__name__.split(".").pop()
        if(hasattr(module,'get_path')):
            urlpatterns.append(module.get_path())
        else:
            if(hasattr(module,'get_view')):
                urlpatterns.append(path(module_name,module.get_view(),name=module_name))
            else:
                app_name=dirname(__file__).split("/").pop()
                urlpatterns.append(path(module_name,TemplateView.as_view(template_name=app_name+"/default.html"),name=module_name))
                


