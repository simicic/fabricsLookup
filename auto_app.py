from flask.helpers import get_debug_flag

from lookup.app import create_app
from lookup.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
