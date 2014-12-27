=============================
Whiskey Jumpstart - Kallithea
=============================

This is a Whiskey jumpstart example for Kallithea.

To get it running follow the steps outlined below for each deployment type.

Docker
------

The Docker instructions assume you have already installed Docker and
Fig (https://pypi.python.org/pypi/fig).

Note that the Docker build will take longer the first time due to the
need to pull down any required images. If you have previously used the
``mod_wsgi-docker`` image, ensure that you pull down the latest version
of the ``grahamdumpleton/mod-wsgi-docker:python-2.7-onbuild`` image.

1. Clone this git repository.
2. Run ``fig build``.
3. Run ``fig up``.
4. Open a web browser on port 8000 of the Docker host.

OpenShift
---------

The OpenShift instructions assume you have already created an account at
OpenShift (http://openshift.redhat.com) and are currently logged in to the
OpenShift dashboard.
 
Note that the OpenShift UI doesn't give good visual feedback when creating
applications and so you may be presented with a blank screen for some time.
Just be patient and it will eventually return.

1. Click `Deploy (Python 2.7) <https://openshift.redhat.com/app/console/application_types/custom?name=whiskeyjumpstartkallithea&initial_git_url=https://github.com/GrahamDumpleton/whiskey-jumpstart-kallithea.git&cartridges[]=python-2.7&cartridges[]=postgresql-9.2>`_.
2. Click the "Continue to application overview page" after the application
   has been deployed.
3. Click on the name of your application to open it