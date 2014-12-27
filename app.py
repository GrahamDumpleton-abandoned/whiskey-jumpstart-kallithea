import mod_wsgi.openshift

mod_wsgi.openshift.start("--application-type", "paste",
    "/app/kallithea-runtime/production.ini")
