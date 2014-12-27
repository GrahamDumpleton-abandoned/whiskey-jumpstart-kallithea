=============================
Whiskey Jumpstart - Kallithea
=============================

This is a Whiskey jumpstart example for Kallithea.

To get it running follow the steps outlined below for each deployment type.

The adminstrator login name is 'admin'. The default password is
'whiskeyrules'. Ensure you change the password straight away.

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

Note that with the way that Fig is being configured to host the
application, a fresh database and directory for respositories will be
created each time it is started. In order to have persistence across
runs then further work would be required to create data only containers
for the database and repositories and mount them against the containers
when started.

OpenShift
---------

The OpenShift instructions assume you have already created an account at
OpenShift (http://openshift.redhat.com) and are currently logged in to the
OpenShift dashboard.
 
Note that the use of the OpenShift web based workflow for creation of an
application appears to fail for this application at this time. The problem
is perhaps simply a timeout issue due to the application taking too long
to be created. So instead of using the quick start deploy link, follow the
manual instructions at the bottom of the page.

1. Click `Deploy (Python 2.7) <https://openshift.redhat.com/app/console/application_types/custom?name=whiskeyjumpstartkallithea&initial_git_url=https://github.com/GrahamDumpleton/whiskey-jumpstart-kallithea.git&cartridges[]=python-2.7&cartridges[]=postgresql-9.2>`_.
2. Click the "Continue to application overview page" after the application
   has been deployed.
3. Click on the name of your application to open it

Note that when deploying to OpenShift, the 'scaling' option should NOT be
selected as the data directory used to hold any repositories is not shared
across gears if they happen to be deployed to different hosts.

To deploy manually use the following steps.

1. Check out this repository.
2. Create an OpenShift application using the ``python-2.7`` and
   ``postgresql-9.2`` cartridges::
   
    rhc app-create whiskeyjumpstartkallithea python-2.7 postgresql-9.2 --no-git

3. Add the OpenShift git repository as a remote to the local repository,
   changing ``xxx`` to be the application ID in the command::
   
   git remote add openshift ssh://xxx@whiskeyjumpstartkallithea-grahamdumpleton.rhcloud.com/~/git/whiskeyjumpstartkallithea.git/

4. Force push the local repository up to the OpenShift repository.

The deployment will take some time and the web site will not be available
immediately after the push completes, so be a little bit patient.
