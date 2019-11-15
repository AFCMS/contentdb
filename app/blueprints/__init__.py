import os, importlib

def create_blueprints(app):
	dir = os.path.dirname(os.path.realpath(__file__))
	modules = next(os.walk(dir))[1]	
	
	for modname in modules:		
		if all(c.islower() for c in modname):
			module = importlib.import_module("." + modname, __name__)		
			app.register_blueprint(module.bp)
