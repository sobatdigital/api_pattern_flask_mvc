import os
from dotenv import load_dotenv

load_dotenv()

# OR, the same with increased verbosity:
load_dotenv(verbose=True)

basedir = os.path.dirname(os.path.abspath(__file__))
configfile = os.path.join(basedir, '../..', '.env')
dotenv = load_dotenv(dotenv_path=configfile)
