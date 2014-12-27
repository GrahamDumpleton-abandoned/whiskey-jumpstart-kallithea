import os

import mod_wsgi.openshift

OPENSHIFT_DATA_DIR = os.environ['OPENSHIFT_DATA_DIR']
KALLITHEA_HOMEDIR = os.path.join(OPENSHIFT_DATA_DIR, 'kallithea-runtime')
KALLITHEA_INIFILE = os.path.join(KALLITHEA_HOMEDIR, 'production.ini')

mod_wsgi.openshift.start("--application-type", "paste", KALLITHEA_INIFILE)
