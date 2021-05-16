import site
import threading
import sys, os

pkgdir = os.path.join(os.path.dirname(__file__), 'lib')

site.addsitedir(pkgdir)
os.environ['PYTHONPATH'] = pkgdir + os.pathsep + os.environ.get('PYTHONPATH', '')

from app import app as dashapp
import app as cryptoapp
application = dashapp.server

cryptoapp.handleArgs(sys.argv[1:])
wdThread = threading.Thread(target=cryptoapp.watchdog)
wdThread.daemon = False
wdThread.start()