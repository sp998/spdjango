
from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")]


import types
def imports():
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            yield val

def get_modules():
	modules=[]
	pkgname=dirname(__file__).split("/").pop()
	for module in list(imports()):
		if ( pkgname in module.__name__):
			modules.append(module)
	return  modules
