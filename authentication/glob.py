from django.conf import settings
def init_global():
  global auth
  auth = False
  global debug
  debug = settings.DEBUG