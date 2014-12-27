#FROM grahamdumpleton/mod-wsgi-docker:python-2.7-onbuild
FROM mod-wsgi-docker:python-2.7-onbuild

CMD [ "--application-type", "paste", "/app/kallithea-runtime/production.ini" ]
