from django.contrib import admin
# Register your models here.
import test_app.viewmodels as viewmodels
from test_app.viewmodels import *


for module in viewmodels.get_modules():
    if(hasattr(module,'model_register')):
        admin.site.register(module.model_register())