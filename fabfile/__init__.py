import glob, os, re

pre_globals = dict([(key, value) for key, value in globals().items()])

for fabfile in [py for py in glob.glob('fabfile/*.py') if not py.endswith('__init__.py')]:
    module_name = os.path.splitext(os.path.split(fabfile)[1])[0]
    module = __import__(module_name, globals(), locals(), ['*'], -1)
    for key in pre_globals.keys():
        setattr(module, key, pre_globals[key])
    for key in dir(module):
        if not re.match('^__.+__$', key):
            globals()[key] = getattr(module, key)
