"""Settings package initialization."""

import os
from dotenv import load_dotenv

load_dotenv()


# Ensure development settings are not used in testing and production:
if os.getenv('ENVIRONMENT') == 'PRODUCTION':
    from .production import *
elif os.getenv('ENVIRONMENT') == 'TRAVIS':
    from .testing import *
else:
    from .local import *
