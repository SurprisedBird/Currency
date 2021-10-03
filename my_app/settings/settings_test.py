from settings.settings import *

DEBUG = False
# Когда селери находит эту настройку, то все таски будут выполняться как функции, игнорируя брокер.
CELERY_TASK_ALWAYS_EAGER = True
