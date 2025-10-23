import importlib, sys
sys.path.append(r"c:\Users\thanh\OneDrive\Desktop\catalog")
try:
    importlib.import_module('catalog_app.views')
    print('views.py imported successfully')
except Exception as e:
    print('IMPORT ERROR:', e)
