from irekua_dev_settings.settings import *
from irekua_database.settings import *
from selia_admin.settings import *
from selia_visualizer.settings import *
from selia_annotator.settings import *


INSTALLED_APPS = (
    SELIA_ADMIN_APPS +
    SELIA_VISUALIZERS_APPS +
    SELIA_ANNOTATOR_APPS +
    IREKUA_DATABASE_APPS +
    IREKUA_BASE_APPS
)
