# 05 - Assignment 01 - Try Pip
### pip install Django

Installs Django

### pip list

Lists all Pip Modules

### pip install Django (We know you already ran this one. What information do you see returned in terminal after this command?)

Successfully installed Django-1.11.5 pytz-2017.2

### pip freeze (What's the difference between freeze and list?)

First cd into your Desktop directory (cd ~/Desktop), then run this command: pip freeze > requirements.txt. What do you see when you ls? What's inside this file?

You see the same as pip list - a list of all the modules currently installed.

### pip uninstall Django

uninstalls Django

message: Successfully uninstalled Django-1.11.5

### pip show Django

pip show Django (didn't do anything)

(reinstalled Django)

and then: pip show Django

Name: Django
Version: 1.11.5
Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Home-page: https://www.djangoproject.com/
Author: Django Software Foundation
Author-email: foundation@djangoproject.com
License: BSD
Location: c:\python27\lib\site-packages
Requires: pytz

### pip search Flask. This one might take a moment to execute.

sample output - looks like all modules Flask.

flask-ldap3-login (0.9.13)                     - LDAP Support for Flask in
                                                 Python3/2
Flask-Micropub (0.2.6)                         - Adds support for Micropub
                                                 clients.
flask-ripozo (1.0.4)                           - An extension for ripozo and
                                                 that brings
                                                 HATEOAS/REST/Hypermedia apis
                                                 to flask
Flask-GoogleMaps (0.2.5)                       - FlaskGoogleMaps - Google Maps
                                                 Extension for Flask
flask-resty-tenants (0.5.3)                    - Flask Resty Authorization
                                                 module for multitenancy
Flask-QRcode (1.0.1)                           - An concise flask extension to
                                                 render QR codes
Flask-JinjaHelpers (0.3.7)                     - Various helpers for Flask
                                                 based Jinja2 templates.
Flask-PyMongo (0.5.1)                          - PyMongo support for Flask
                                                 applications
Flask-Sijax (0.4.1)                            - An extension for the Flask
                                                 microframework that adds
                                                 Sijax support.
Flask-WXPay (0.1.12)                           - Flask Extension for WeChat
                                                 Pay.
Flask-Navigate (0.2.2)                         - Another flask extension that
                                                 provides Navigation menus.
Flask-Testing (0.6.2)                          - Unit testing for Flask
Flask-Holster (0.3.4)                          - Rigid MVC content negotiation
                                                 for Flask
Flask-Material (0.1.1)                         - An extension that includes
                                                 Materialize CSS
                                                 (http://materializecss.com/)
                                                 in your project, without any
                                                 boilerplate code.
flask-mwoauth (0.3.61)                         - Flask blueprint to connect to
                                                 a MediaWiki OAuth server
Flask-MustacheJS (0.6.0)                       - Mustache integration in
                                                 Flask, with Jinja and client-
                                                 side libraries.
flask-swagger (0.2.13)                         - Extract swagger specs from
                                                 your flask project
Flask-Imagine (0.5)                            - Extension which provides easy
                                                 image manipulation support in
                                                 Flask applications.
Flask-SQLAlchemy (2.2)                         - Adds SQLAlchemy support to
                                                 your Flask application
Frozen-Flask (0.15)                            - Freezes a Flask application
                                                 into a set of static files.
Flask-PW (1.0.3)                               - Peewee ORM integration for
                                                 Flask framework
flask-musers (0.5.4)                           - Flask app for store user in
                                                 MongoDB and simple views for
                                                 login, logout and
                                                 registration.
Flask-Pypi-Proxy (0.5.1)                       - A Pypi proxy
Flask-JSONAPIView (0.1.0)                      - DEPRECATED: This library has
                                                 been renamed to Flask-RESTy
Flask-Validator (1.2.3)                        - Data validator for Flask and
                                                 SQL-Alchemy, working at Model
                                                 component with events
twopi-flask-utils (1.1.8)                      - A set of utilities to make
                                                 working with flask web
                                                 applications easier.
Flask-LwAdmin (0.6.3)                          - Flask-LwAdmin is minimalistic
                                                 administrative interface
                                                 building extension for the
                                                 Flask framework
flask-whooshee (0.5.0)                         - Flask-SQLAlchemy - Whoosh
                                                 Integration
flask-restful-swagger (0.19)                   - Extrarct swagger specs from
                                                 your flast-restful project
Flask-Login (0.4.0)                            - User session management for
                                                 Flask
Flask-Injector (0.10.0)                        - Adds Injector, a Dependency
                                                 Injection framework, support
                                                 to Flask.
Flask-MongoAlchemy (0.7.2)                     - Add Flask support for MongoDB
                                                 using MongoAlchemy.
Flask-GoogleLogin (0.3.1)                      - Extends Flask-Login to use
                                                 Google's OAuth2 authorization
flask-mongoengine (0.9.3)                      - Flask-MongoEngine is a Flask
                                                 extension that provides
                                                 integration with MongoEngine
                                                 and WTF model forms.
Flask-Perm (0.2.8)                             - Flask Permission Management
                                                 Extension
flask-zeus (0.2.1)                             - UNKNOWN
Flask-MarcoPolo (0.6.3)                        - Flask-MarcoPolo  Flask-
                                                 MarcoPolo is a Flask
                                                 extension that adds structure
                                                 to both your views and
                                                 templates, by mapping them to
                                                 each other to provide a rapid
                                                 application development
                                                 framework. The extension also
                                                 comes with Flask-Classy,
                                                 Flask-Assets, Flask-Mail,
                                                 JQuery 2.x, Bootstrap 3.x,
                                                 Font-Awesome, Bootswatch
                                                 templates. The extension also
                                                 provides pre-made templates
                                                 for error pages and macros.
                                                 https://github.com/mardix
                                                 /flask-marcopolo
pytest-flask (0.10.0)                          - A set of py.test fixtures to
                                                 test Flask applications.
Flask-paginate (0.5.0)                         - Simple paginate support for
                                                 flask
Flask-LoginManager (1.1.6)                     - Flask-Loginmanager supports
                                                 multiple roles and
                                                 permissions for Flask,
                                                 inspired by Flask-Login
Flask-OAuthlib (0.9.4)                         - OAuthlib for Flask
Flask-REST-JSONAPI (0.12.6)                    - Flask extension to create
                                                 REST web api according to
                                                 JSONAPI 1.0 specification
                                                 with Flask, Marshmallow
                                                 and data provider of your
                                                 choice (SQLAlchemy, MongoDB,
                                                 ...)
Flask-Maple (0.5.0)                            - captcha ,bootstrap,easy login
                                                 and more flask tips.
Flask-HTTPAuth (3.2.3)                         - Basic and Digest HTTP
                                                 authentication for Flask
                                                 routes
Flask-Slither (1.1.7)                          - A small library between
                                                 MongoDB and JSON API
                                                 endpoints
Flask (0.12.2)                                 - A microframework based on
                                                 Werkzeug, Jinja2 and good
                                                 intentions
  INSTALLED: 0.12.2 (latest)
Flask-Jerify (0.0.23)                          - Validate JSON requests
                                                 against schemas
Flask-Script (2.0.6)                           - Scripting support for Flask
GitHub-Flask (3.1.7)                           - GitHub extension for Flask
                                                 microframework
Flask-SeaSurf (0.2.2)                          - An updated CSRF extension for
                                                 Flask.
Flask-Restless (1.0.0b1)                       - A Flask extension for easy
                                                 ReSTful API generation
Flask-LDAPConn (0.6.13)                        - Pure python, LDAP connection
                                                 and ORM for Flask
                                                 Applications
Flask-Resize (2.0.3)                           - Flask extension for resizing
                                                 images in code and templates
Flask-Migrate (2.1.1)                          - SQLAlchemy database
                                                 migrations for Flask
                                                 applications using Alembic
Flask-WTF-FlexWidgets (0.1.25)                 - A flask extension that
                                                 provides customizable WTF
                                                 widgets and macros.
flask-peewee (0.6.7)                           - Peewee integration for flask
Flask-Security (3.0.0)                         - Simple security for Flask
                                                 apps.
Flask-Mail (0.9.1)                             - Flask extension for sending
                                                 email
Flask-RESTful (0.3.6)                          - Simple framework for creating
                                                 REST APIs
Flask-Table (0.4.1)                            - HTML tables for use with the
                                                 Flask micro-framework
flask-restplus (0.10.1)                        - Fully featured framework for
                                                 fast, easy and documented API
                                                 development with Flask
Flask-S3 (0.3.3)                               - Seamlessly serve the static
                                                 files of your Flask app from
                                                 Amazon S3
flask-transmute (1.3.0)                        - a flask plugin to generate
                                                 routes from objects.
Flask-uWSGI-WebSocket (0.6.0)                  - High-performance WebSockets
                                                 for your Flask apps powered
                                                 by uWSGI.
Flask-Stormpath (0.4.8)                        - Simple and secure user
                                                 authentication for Flask via
                                                 Stormpath.
flask-magic (0.0.53)                           - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
flask-io (1.12.0)                              - Flask-IO is a library for
                                                 parsing Flask request
                                                 arguments into parameters and
                                                 for serialization of complex
                                                 objects into Flask response.
Flask-Wizard (0.4.15)                          - Rapid and easy chatbot
                                                 development in Python for
                                                 multiple channels
Flask-RESTy (0.11.6)                           - Building blocks for REST APIs
                                                 for Flask
Flask-WTF (0.14.2)                             - Simple integration of Flask
                                                 and WTForms.
Flask-User (0.6.19)                            - Customizable User
                                                 Authentication and
                                                 Management, and more.
Flask-Limiter (0.9.5.1)                        - Rate limiting for flask
                                                 applications
flask-restaction (0.25.3)                      - A web framwork born to create
                                                 RESTful API
Flask-SocketIO (2.9.2)                         - Socket.IO integration for
                                                 Flask applications
Flask-Potion (0.14.1)                          - Powerful REST API framework
                                                 for Flask and SQLAlchemy
Flask-Restler (1.10.0)                         - Build REST API for Flask
                                                 using Marshmallow.
flask-xxl (0.9.20)                             - quick way to design large
                                                 flask projects
microcosm-flask (0.82.0)                       - Opinionated persistence with
                                                 FlaskQL
flask2postman (1.4.3)                          - Generate a Postman collection
                                                 from your Flask application
flask_accept (0.0.3)                           - Custom Accept header routing
                                                 support for Flask
flask_aide (0.0.1)                             - demo
flask_alcohol (0.2.2)                          - Automatically generate API
                                                 routes from Flask-SQLAlchemy
                                                 models
flask_ample (0.0.1)                            - basic setup of ample for
                                                 flask
flask_api_builder (0.2.0)                      - A shortcut for stubbing out
                                                 your RESTful Flask APIs
flask_app_generator (0.1.0)                    - Flask Project Generator
flask_autorest (0.1.5)                         - auto create restful apis for
                                                 database, with the help of
                                                 dataset.
flask_backstage (0.2.1)                        - A backstage framework with
                                                 very few code.
flask_base64_msm_session (1.0.2)               - Use base64 encoder on
                                                 memcached server. And it will
                                                 use memcached on session
flask_basic_roles (0.2)                        - A plugin for adding very
                                                 simple users + roles to a
                                                 flask app
flask_cache_external_assets (0.2.0)            - Flask extension for caching
                                                 external assets
flask_checkargs (0.1.2)                        - A module to simplify checking
                                                 arguments in Flask apps
flask_chip (0.1.2)                             - A token generator for Flask
                                                 apps.
flask_clapi (0.2.0)                            - CLAPI wrapper
flask_cm (0.8.1)                               - Cloud Mesh: managing multiple
                                                 virtual machines in Clouds
flask_datatables (0.6.17)                      - Integrates SQLAlchemy with
                                                 DataTables (framework Flask)
flask_dino_utils (0.1.11)                      - Flask utils package to use it
                                                 among with Flask-Classy and
                                                 marshmallow
flask_doc (0.2.5)                              - Write API document when you
                                                 coding, Test your API when
                                                 you press last word
                                                 immediately
flask_error (0.1)                              - A simple and extensible way
                                                 of displaying error messages.
flask_ext_migrate (1.0.1)                      - A sourcecode manipulation
                                                 tool for converting imports.
flask_extras (4.0.3)                           - Assorted useful flask views,
                                                 blueprints, Jinja2 template
                                                 filters, and templates/macros
flask_flaskwork (0.1.11)                       - A Flask plugin to talk with
                                                 the Flaskwork Chrome
                                                 extension.
flask_frink (0.0.1)                            - Add Flask-Security datastore
                                                 functionality to Frink.
flask_github_proxy (0.0.2)                     - Plugin to build services to
                                                 push data from a website to
                                                 github with PullRequests
                                                 confirmation
flask_helpers (0.1)                            - Useful stuff for Flask
                                                 application
flask_introspect (0.0.1)                       - basic setup of ample for
                                                 flask
flask_json_multidict (1.0.0)                   - Convert Flask's
                                                 `request.get_json` dict into
                                                 a MultiDict like
                                                 `request.form`
flask_json_resource (0.2.18)                   - UNKNOWN
flask_jsondash (6.2.3)                         - Easily configurable, chart
                                                 dashboards from any arbitrary
                                                 API endpoint. JSON config
                                                 only. Ready to go.
flask_jsontools (0.1.1-0)                      - JSON API tools for Flask
Flask_LDAP_View (0.3)                          - A library to restrict your
                                                 flask pages by LDAP groups
flask_locust (0.0.2-alpha)                     - SQL-Migrations for your
                                                 Application
flask_markdown2 (0.0.3)                        - A flask extension that adds a
                                                 {% markdown %} tag to
                                                 templates.
flask_nameko (1.4.0)                           - A wrapper for using nameko
                                                 services with Flask
flask_neglog (0.0.2)                           - demo
flask_nemo (1.0.1)                             - Flask Extension to browse CTS
                                                 Repository
flask_ogm (1.1.0a9)                            - Add support for the py2neo
                                                 Object Graph Mapper to your
                                                 app
flask_open_directory (0.1.1)                   - MacOS OpenDirectory
                                                 Authorization Middleware for
                                                 Flask
flask_params (1.0.1)                           - Processes the Request params
                                                 for Flask served as a Python
                                                 library
flask_profiler (1.5)                           - API endpoint profiler for
                                                 Flask framework
flask_raven (0.0.4)                            - A flask extension for the
                                                 University of Cambridge's
                                                 authentication system
flask_rdf (0.2.0)                              - Flask decorator to output RDF
                                                 using content negotiation
flask_react (0.0.5)                            - Auto setup tool for flask and
                                                 react project
flask_render_specific_template (1.0)           - This library allows Flask
                                                 developers to dynamically
                                                 select the template directory
                                                 used for rendering
flask_replicated (1.2)                         - Flask SqlAlchemy router for
                                                 stateful master-slave
                                                 replication
flask_reqparse (2.2.1)                         - flask_reqparse is a simple
                                                 wrapper around flask request
                                                 module that helps to parse
                                                 args efficently.
flask_rest_toolkit (0.0.1)                     - A set of tools to create
                                                 simple Flask REST web
                                                 services and APIs
flask_restframework (0.1.1)                    - Web APIs for Flask, made
                                                 easy, inspired from Django
                                                 DRF.
flask_restful_jsonschema (0.1.1)               - Provides a wrapper which
                                                 provides valid json to
                                                 Resource methods.
flask_restful_url_generator (0.0.4)            - flask-restful URLs list
flask_resty_swagger (0.1.3)                    - Generate swagger
                                                 documentation from flask-
                                                 resty service
flask_sandboy (0.0.3)                          - Automated REST APIs for
                                                 SQLAlchemy models
flask_script_extras (0.1.4)                    - extras commands to Flask-
                                                 Script.
flask_servatus (0.1.3)                         - A port of djangos storages
                                                 framework for use with flask
                                                 applications
flask_servicenow (0.1.1)                       - ServiceNow REST API Flask
                                                 extension
flask_siilo (0.1.2)                            - A simple storage for Flask
                                                 based on siilo.
flask_simple_sitemap (0.0.3)                   -
flask_simplelogin (0.0.6)                      - Flask Simple Login - Login
                                                 Extension for Flask
flask_simplerest (1.0.3)                       - A Flask extension for easy
                                                 ReSTful API generation
flask_singleview (0.2.1)                       - A flask micro extension for
                                                 building single-view web
                                                 apps.
flask_slackbot (0.2.1)                         - Deal with slack outgoing
                                                 webhook
flask_sqla_debug (0.2)                         - Helpers for debugging flask
                                                 and sqlalchemy performance
flask_tlsauth (0.1.3)                          - Flask extension implementing
                                                 TLS Authentication - simple
                                                 client certificate CA
                                                 inclusive
flask_trace (0.0.4)                            - Log trace decorator function
                                                 for Flask
flask_tryton (0.6)                             - Adds Tryton support to Flask
                                                 application
flask_util_js (0.2.25)                         - flask's util in javascript.
                                                 such as url_for etc.
flask_web_args (0.1.2)                         - A library to help easily
                                                 parse/validate web arguments
                                                 with Flask
flask_wx (0.0.1)                               - A simple and brief utility
                                                 tools framework
flask_yamlpage (0.0.6)                         - Flatpages in yaml syntax
flaskcbv (1.4.11)                              - FlaskCBV is Alternative
                                                 Framework for working with
                                                 flask with the class Based
                                                 Views approach (CBV)
flaskchatterbot (0.1.0)                        - An open-source web based
                                                 Python chat bot in Flask.
flaskckeditor (1.6)                            - flaskå?Zå?°å¿«é?Yé>+æ^?ckeditorç¼-è_`åT"
FlaskCms (0.0.4)                               - UNKNOWN
FlaskDeferredHandler (0.1)                     - A Flask handler for the
                                                 Google Appengine's deferred
                                                 library
flasker (0.1.45)                               - Flask, SQLAlchemy, and Celery
                                                 integration
FlaskEx (0.0.66)                               - UNKNOWN
flaskhmac (1.2.1)                              - Provides easy integration of
                                                 the HMAC signatures for your
                                                 REST Flask Applications.
flaskinit (0.0.1)                              - Bootstraps Flask projects
flaskit (0.1.0)                                - Utilies for Flask
                                                 application.
flaskJSONRPCServer (0.9.3)                     - A Python JSON-RPC over HTTP
                                                 with flask and gevent
flaskle (0.4)                                  - bottle-like utility
                                                 decorators for flask
pumpwood-flaskmisc (0.0.0.2)                   - Misceletiuns fucntions and
                                                 class to help development of
                                                 PumpWood on Flash
flaskmogrify (0.0.9)                           - Flaskmogrify, a simple Flask
                                                 single pageapplication to
                                                 convert (w/ Ajax) user-pasted
                                                 text using an arbitrary text
                                                 conversion function.
flaskpress-themes (0.1.5)                      - Provides infrastructure for
                                                 theming FlaskPress
                                                 applications
flaskpress (0.0.1)                             - Python Flask CMS
flaskpress-speaklater (1.3.0)                  - Implements a lazy string for
                                                 python for use with gettext
FlaskPusher (1.0.1)                            - Adds Pusher support for your
                                                 Flask application.
flaskrestframework (0.1.4)                     - Web APIs for Flask, made
                                                 easy.
flaskrestgen (0.4)                             - A restful API generator for
                                                 flask/sqlalchemy declarative
                                                 models.
FlaskSearch (0.1)                              - Powerful search functionality
                                                 for Flask apps via
                                                 ElasticSearch
flaskserver (0.1.1)                            - simple web server with Flask
flasksr (0.6)                                  - Start streaming HTTP
                                                 Responses based on your page
                                                 layout for Flask and improve
                                                 Time for First Paint.
flaskstrap (0.3.6)                             - Easily create a flask, nginx,
                                                 uwsgi and bootstrap project
                                                 ready for deployment
flaskup (0.3.2)                                - A simple Flask application to
                                                 share files.
FlaskWarts (0.1a8)                             - Assortment of various
                                                 utilities for Flask
                                                 applications
flaskwork (0.1.1)                              - UNKNOWN
Flasky (0.1.0)                                 - Lazy man's Flask Application
FlaskyTornado (0.0.42)                         - A microframework based on
                                                 Tornado and Flask and good
                                                 intentions
flatly (0.3)                                   - Pyramid scaffold that is
                                                 flat.  Kind of like Flask.
fleaker (0.4.2)                                - Tools and extensions to make
                                                 Flask development easier.
flekky (0.4.1)                                 - Static website generator
                                                 inspired by jekyll based on
                                                 flask.
flexrest (0.1.9)                               - Flexible Flask Rest Api
FliKISS (0.1)                                  - Wiki engine based on Markdown
                                                 flat files powered by Flask
flump (0.11.1)                                 - REST API builder using Flask
                                                 routing and Marshmallow
                                                 schemas.
flymph (0.1.3)                                 - Flask as Lymph Web API
gitlab-freak (1.0.0a1)                         - A Flask server that allows
                                                 you to interact with Trello
                                                 from your own Gitlab, and
                                                 keep track of your projects
                                                 dependencies.
Fregger (0.10.6)                               - Automatically generate
                                                 Swagger docs for Flask-
                                                 Restful.
frl (0.0.4)                                    - flask/requests logging
froth (0.0.1)                                  - Data Visualization Template
                                                 Engine for Django/Flask=
frs (0.0.0.dev11)                              - Flask-RESTful
                                                 Swagger(-driven) Validation
fss (0.2.1)                                    - Compile Flask/Jinja2 site
                                                 into static html content
funkyserver (0.1)                              - FunkyServer is simple package
                                                 to create Flask servers in
                                                 background processes.
Funnel (0.1)                                   - Flask extension for Beaker
fuser (1.0.4)                                  - A library to handle user
                                                 related tasks in Flask
fvsd (1.0.3)                                   - Flask+VueJS+SemanticUI+Docker
                                                 CLI boilerplate.
gdbgui (0.7.9.5)                               - browser-based gdb frontend
                                                 using Flask and JavaScript to
                                                 visually debug C, C++, Go, or
                                                 Rust
getolaf (1.0.2)                                - A static site generator based
                                                 on flask and markdown
git-golem (0.1)                                - Git web interface using
                                                 libgit2 and flask
git-webhook (0.0.6)                            - ä½¿ç"" Python Flask + SQLAchemy +
                                                 Celery + Redis + React
                                                 å¼?å?`çs,ç""äºZè¿.é?Yæ?-å»ºå1¶ä½¿ç"" WebHook
                                                 è¿>è¡Oè╪ªåS"åO-éƒ"ç½²å'Oè¿?ç»'ï¼Oæ"_æO? Github / GitLab
                                                 / Gogs / GitOsca?,
Glask (0.0.23)                                 - An extension for flask
                                                 applications with best
                                                 practices.
glassblower (0.2.5)                            - The Best Flask Boilerplate
                                                 Framework
Gluino (0.4)                                   - port of web2py libs to
                                                 bottle, flask, pyramid,
                                                 tornado (includes copy of
                                                 modules from the web2py
                                                 framework)
goblet (0.3.5)                                 - Git web interface using
                                                 libgit2 and flask
google_forms (0.3)                             - Flask web proxy for Google
                                                 forms
groundwork-sphinx-theme (1.0.5)                - Sphinx theme for groundwork
                                                 projects (Based on
                                                 flask_theme)
halef-SETU (0.0.5)                             - halef-SETU provides an easy
                                                 wrapper around SKLL models
                                                 for statistical language
                                                 understanding as well as an
                                                 easy to API based on Flask
happymongo (0.1.1)                             - Python module for making it
                                                 easy and consistent to
                                                 connect to MongoDB via
                                                 PyMongo either in Flask or in
                                                 a non-flask application
Harambe (0.10.0)                               - A mid stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha, Cors.
                                                 Supports HTML, Markdown and
                                                 Jade and more
haven (1.1.107)                                - flask's style binary server
                                                 framework
py-healthcheck (1.6.1)                         - Adds healthcheck endpoints to
                                                 Flask or Tornado apps
healthcheck (1.3.2)                            - Adds healthcheck endpoints to
                                                 Flask apps
hflossk (0.5.10)                               - HFOSS course materials via
                                                 flask
highfield (1.0.21)                             - Structured flask with mongo
HipPocket (0.1.2a)                             - A wrapper around Flask to
                                                 ease the development of
                                                 larger applications
horn ((latest release))                        - Hy Macros for Flask
http-server-livereload (1.1.0)                 - A monkey patch of http.server
                                                 to call livereload when
                                                 server_forever is called.
                                                 This is compatible with flask
                                                 reload and tiny-lr (grunt
                                                 watch).
hxl-proxy (1.3)                                - Flask-based web proxy for HXL
jac (0.16.1)                                   - A Jinja extension (compatible
                                                 with Flask and other
                                                 frameworks) to compile and/or
                                                 compress your assets.
Jalapeno (0.1.4)                               - Static Site Generator based
                                                 on Flask
jiac (0.2.1)                                   - A Jinja extension (compatible
                                                 with Flask) to compile and/or
                                                 compress your assets inline.
jobmonitor (0.0.5)                             - Physics-orientated job
                                                 monitoring over HTTP with
                                                 Flask.
json-validator (1.0)                           - Provide decorator for
                                                 validating json parameters
                                                 passed to function. Can be
                                                 used for validation of json
                                                 parameters sent to Flask.
py-json-rpc (0.0.3)                            - Decorator based toolkit to
                                                 use JSONRPC easy like Flask
Juice (0.0.23)                                 - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
JYFlask (0.1)                                  - Jing Yun Flask
Keg (0.6.0)                                    - A web framework built on
                                                 Flask & SQLAlchemy.
                                                 Somewhere North of Flask but
                                                 South of Django.
KegBouncer (2.2.3)                             - A three-tiered permissions
                                                 model for KegElements built
                                                 atop Flask-User
kipavois (0.1.2)                               - Flask proxy over Kibana with
                                                 KiPavois
kit (0.2.15)                                   - Flask, Celery, SQLAlchemy
                                                 integration framework.
kola (1.5.6)                                   - flask's style json server
                                                 framework
kube_shields (0.0.6)                           - kube shields flask frontend.
zeus-lab804 (0.1.2)                            - Fast create scaffold of
                                                 flask.
Lagring (0.2.7.1)                              - Asset storage for Flask
Lapin (0.01a1)                                 - A flask-based web framework
lapti (0.0.1)                                  - Simple utils for flask and
                                                 peewee projects
latexrender (0.3.6)                            - A simple Flask app for
                                                 rendering latex snippets into
                                                 images.
lever (0.2.6)                                  - A tool for exposing
                                                 SQLAlchemy models in Flask
                                                 via REST
littlefish (0.0.13)                            - Flask webapp utility
                                                 functions by Little Fish
                                                 Solutions LTD
python-rabbitmq-logging (0.0.3)                - Send logs to RabbitMQ from
                                                 Python/Flask
logy (0.1)                                     - A flask based web application
                                                 for central logging
lraudit (0.1.1)                                - Adds auditing to LR Flask
                                                 apps
lrutilities (0.1.2)                            - Utilities for LR Flask apps
lrutils (0.1.4)                                - Utilities for LR Flask apps
mack (0.1.1)                                   - A simple Flask project
                                                 generator
madame (0.1.2.a)                               - RESTful API for MongoDB built
                                                 on Flask
magic-xxl (0.6.1)                              - A collection librairies to
                                                 work with Flask-Magic
tornado-mail (0.4.0)                           - A email plugin for tornado.
                                                 It is a fake Flask_mail.
Mambo (1.0.0b21)                               - A mid stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
mana (4.8)                                     - the missing startproject
                                                 command for Flask
mana0 (0.10)                                   - my flask toolkit
mana2 (0.15)                                   - my flask toolkit
mana3 (0.15)                                   - my flask toolkit
mana4 (0.15)                                   - my flask toolkit
simple-site-manager (0.1.7)                    - Manage multiple lighttpd and
                                                 Django or Flask websites on a
                                                 single machine.
script-manager (0.1.0)                         - A command-line interface.
                                                 Just a simple and crude
                                                 implementation of Flask-
                                                 Script.
mandrill_webhooks (0.1.0)                      - Flask Webhooks
manhattan_dispatch (0.0.4)                     - A middleware dispatcher for
                                                 Flask based on             we
                                                 rkzeug.wsgi.DispatcherMiddlew
                                                 are.
markov_autocomplete (1.0.1)                    - Autocomplete model easy to
                                                 integrate with Flask apps
mediaflask (0.2.1)                             - Download audio from online
                                                 videos.
mediatumbabel (0.1.1)                          - flask-babel port to provide
                                                 i18n for mediaTUM (+jinja2)
                                                 with some improvements
meteorpi_server (0.1.5)                        - HTTP server based on Flask
                                                 providing a remote API
Microbe (1.2)                                  - Micro Blog Engine inspired by
                                                 Pelican and powered by Flask
oauth-middleware (0.3.3)                       - Simple flask_oauthlib based
                                                 middleware for WSGI app to
                                                 preform oauth
simple-migrate (0.0.3)                         - A simple database migrate
                                                 tool for flask
mimerender (0.6.0)                             - RESTful HTTP Content
                                                 Negotiation for Flask,
                                                 Bottle, web.py and webapp2
                                                 (Google App Engine)
mkflask_module (0.1.1)                         - Python module
Mlask (0.2)                                    - manage.py for Flask
Mocha (0.9.0)                                  - A mid stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha, Cors.
                                                 Supports HTML, Markdown and
                                                 Jade and more
moesifwsgi (1.0.0)                             - Moesif Middleware for Python
                                                 WSGI based flatforms (Flask,
                                                 Bottle & Others)
moflask (0.1)                                  - Re-usable flask utilities.
pyramid-mongoengine (0.0.9)                    - Mongoengine Pyramid extension
                                                 based in flask-mongoengine
redis-monitor (1.0.3)                          - ä½¿ç""Flaskå¼?å?`çs,ä,?ä,ª web å?_è§+åO-çs, redis
                                                 ç>`æZ§ç"<åº?ï¼Oå?_ä»¥æY¥ço< redis çs,æo?åS¡åT"ä¿¡æ?_a??årzæ-¶ç>`æZ§
                                                 redis çs,æ¶^æ?_å☼,ç?+ opsa??å+.å-~å? ç""a??cpu
                                                 æ¶^è?-ï¼Oä»¥å?S redis è?"é?sæ-¶é-'a?, A web
                                                 visualization redis
                                                 monitoring program.
                                                 Performance optimized and
                                                 very easy to install and
                                                 deploy. the monitor data come
                                                 from redis.info().
myflaskr (0.0.1)                               - A test upload for PyPI
nails (0.1.0)                                  - A python MVC framework built
                                                 with Flask
NCTU-Oauth (0.1.0)                             - adds NCTU-Oauth support to
                                                 flask
notes-pico (0.8.5)                             - A note-taking example web
                                                 application for Picoweb web
                                                 pico-framework. (Ported from
                                                 Flask original)
nyt-pyiap (0.0.11)                             - Python utility functions and
                                                 Django/Flask middlewares for
                                                 validating JWT tokens from
                                                 Google's Identity-Aware Proxy
odinweb.flask (0.4.0)                          - Toolkit for building web
                                                 API's using Odin and Flask.
ofcourse (0.2.5)                               - Python courseware with Flask
                                                 on OpenShift
onyx_sqlalchemy (3.2)                          - flask_sqlalchemy for Onyx
onyxbabel (0.0.3)                              - Ramake of the Flask_BabelEX
                                                 for Onyx
Openedoo-Script-Test (0.1.2)                   - Scripting support for Flask
openedoo (1.1.0.19)                            - openedoo is backend service
                                                 for education base on flask
palmer (0.0.4)                                 - Redice Flask Boost Library.
                                                 Inspired by flask-api.
paqmind.flask-paqforms (1.0.0)                 - UNKNOWN
paqmind.flask-routes (0.2.4)                   - Class-based routes for Flask
paqmind.flask-views (0.5.1)                    - Class-based views for Flask
sanic-patched (0.4.1)                          - A microframework based on
                                                 uvloop, httptools, and
                                                 learnings of flask
perfume (0.2)                                  - Simple Object Oriented layer
                                                 for Flask.
permission (0.4.1)                             - Simple and flexible
                                                 permission control for Flask
                                                 app.
phial (0.2.0)                                  - A static website generator
                                                 that takes motivation from
                                                 Flask and Jekyll.
Phial-Toolset (1.0.2)                          - Non-intrusive toolset to
                                                 easily use
                                                 Flask/Peewee/Celery
phovea_security_flask (0.1.0)                  - UNKNOWN
PlatformoClient (0.0.7)                        - æ"¶é>+Flaskçs,è_·æ±,å"?åº"æ-¶é-'å1¶å?`é??è╪3logstash
plush_web (0.1.0)                              - Micro framework inspirated by
                                                 Sinatra, Express and Flask.
podhub.meh (0.1.12)                            - Flask framework with
                                                 defaults.
Pontus (0.2.1)                                 - Flask utility for Amazon S3.
ponywhoosh (1.7.6)                             - Your database now searchable.
                                                 The backend behind the Flask-
                                                 PonyWhoosh.
Portfolio-py (0.0.1)                           - Portfolio is a Flask based
                                                 framework that adds structure
                                                 and map your views and
                                                 templates together for rapid
                                                 application development
pour (0.2.1)                                   - A lightweight Flask app
                                                 generator.
preflask (0.2)                                 - flask & preprocessors,
                                                 together, forever <3
Prestige (0.0.1)                               - Pylot is a Flask extension
                                                 that adds structure and map
                                                 your views and templates
                                                 together for rapid
                                                 application development
proxapy (0.1.5)                                - Simple API proxy that uses
                                                 Flask/requests/gunicorn.
py3web (0.3.14)                                - Django lets you write web
                                                 apps in Django. Flask lets
                                                 you write web apps in Flask.
                                                 Py3web lets you write web
                                                 apps in Python.
py_blueprints (1.0.1)                          - Flask ready to go blueprints
pygrest (0.3)                                  - Build REST APIs with Neo4j
                                                 and Flask, as quickly as
                                                 possible!
Pylot (0.0.4)                                  - Pylot is a Flask extension
                                                 that adds structure and map
                                                 your views and templates
                                                 together for rapid
                                                 application development
PyMessager (1.0.0)                             - A Python SDK and Flask API to
                                                 develop chatbot on Facebook
                                                 Message Platform
pyros_config (0.2.0)                           - Classes to manage a server
                                                 configuration. Heavily
                                                 inspired by flask
python-thumbnails (0.5.1)                      - Thumbnails for Django, Flask
                                                 and other Python projects.
PyTyrion (1.0.1)                               - æ"_æO?Tornadoa??Djangoa??Bottlea??Flask
                                                 çs,Webè¡"å?éªOè_?
pyxley (0.1.0)                                 - Python tools for building
                                                 Flask-based web applications
qiniufs (1.0.1)                                - qiniu file uploader for
                                                 flask!
Quart (0.2.0)                                  - A Python asyncio web
                                                 microframework with the same
                                                 API as Flask
quorum (0.5.12)                                - Quorum Extensions for Flask
rapidserv (2.0.0)                              - A non-blocking Flask-like Web
                                                 Framework in python.
Redberry (0.0.7.5)                             - Flask Blueprint for adding
                                                 simple CMS functionality
relask (0.1.0)                                 - A Relay-based web development
                                                 kit on Flask
reportexport (0.0.3)                           - A Flask microservice that
                                                 produces reports out of a
                                                 database in xml and pdf
                                                 format.
RESTfulEf (0.1.1)                              - A generic restful api
                                                 generator based on elixir and
                                                 flask
Tornado-Restless (0.4.5)                       - flask-restless adopted for
                                                 tornado
restpager (0.1)                                - A RESTful pager class for
                                                 Flask
revise (0.0.3)                                 - Simple Schemas for Flask JSON
                                                 Validation
ripozo (1.3.0)                                 - ReSTful API framework with
                                                 HATEOAS support and
                                                 compatibility with Flask,
                                                 Django, SQLAlchemy and more.
rororo (1.0.0)                                 - Collection of utilities,
                                                 helpers, and principles for
                                                 building Python backend
                                                 applications. Supports
                                                 aiohttp.web, Flask, and your
                                                 web-framework
serverless-runlocal (0.1.2)                    - Serverless configuration
                                                 parser to run your serverless
                                                 function as Flask.
Sanic (0.6.0)                                  - A microframework based on
                                                 uvloop, httptools, and
                                                 learnings of flask
sbswebsite (0.0.23)                            - Flask based project to create
                                                 a personal site
sga (0.1.39)                                   - make it easier to use pyga
                                                 for web develop. and make
                                                 pyga compatible with flask
                                                 and django.
Shaft (0.0.8)                                  - A mid stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha, Cors.
                                                 Supports HTML, Markdown and
                                                 Jade and more
Shake (1.6.4)                                  - A lightweight web framework
                                                 based on Werkzeug and Jinja2
                                                 as an alternative to Flask
ShelfCMS (0.12.25)                             - Enhancing flask
                                                 microframework with beautiful
                                                 admin and cms-like features
shiftboiler (0.1.6)                            - Best practices setup for
                                                 webapps, apis and cli
                                                 applications with flask
simple_flask_server (0.0.2)                    - Flask equivalent of python -m
                                                 SimpleHTTPServer.
simple_openid (1.0.6)                          - Simple OpenID. One-line setup
                                                 for OpenID login for Flask.
simpleapi (0.0.9)                              - A simple API-framework to
                                                 provide an easy to use,
                                                 consistent and portable
                                                 client/server-architecture
                                                 (for django, flask and a lot
                                                 more).
SimpleFlask (0.1.0)                            - Simple Flask application.
SimpleFlaskBlueprint (0.1.1)                   - Simple Flask blueprint.
SimpleSQLProxy (1.0)                           - A simple sqlproxy for SQL
                                                 LITE databases based on flask
skaffold (0.1)                                 - Flask/SQLAlchemy Admin
                                                 Scaffold
slask (0.1.1)                                  - A Flask app to republish to
                                                 Slack
Slingr (0.0.13)                                - Web development framework
                                                 that builds and serves Cobs
                                                 (deployable web
                                                 applications), running on top
                                                 of Flask
SmallScrewdriver (1.0.2)                       - SmallScrewdriver is python
                                                 texture packer library, with
                                                 frontend's on PySide GUI,
                                                 Flask/React.js, and console
solidwebpush (1.2.1)                           - This package lets your server
                                                 send Web Push Notifications
                                                 to your clients. NOTE: No
                                                 particular web framework are
                                                 required (e.g. Django, Flask,
                                                 Pyramid, etc.), since it was
                                                 originally designed to run on
                                                 a Raspberry Pi with no web
                                                 server installed (only a bare
                                                 Python program listening on a
                                                 port for HTTP requests).
spill (0.0.1a0)                                - A utility for generating
                                                 Flask scaffolding and
                                                 boilerplate.
spouk_utils (0.1)                              - some utils for flask
                                                 distributions
StasFliKISS (0.1.2)                            - Wiki engine based on Markdown
                                                 flat files powered by Flask.
                                                 Fork from StasEvseev.
StatesofUSA (0.1)                              - An API built on  Flask-
                                                 RESTful that returns with the
                                                 names of all the states in
                                                 USA.
sucrose (0.1)                                  - mircroservice library using
                                                 flask and rabbitmq
tahoe (1.0.3.1)                                - A Flask-based framework that
                                                 handles the tedious things
talisman (0.1.0)                               - HTTP security headers for
                                                 Flask.
teleflask (0.0.8)                              - Easily create Telegram bots
                                                 with pytgbot and flask.
                                                 Webhooks made easy.
testflask (0.5)                                - Test flask applications
                                                 easily.
testflask1 (0.1)                               - testflask1 dependency
Thorium (0.2.16)                               - A Python framework for
                                                 RESTful API interfaces in
                                                 Flask
tiddly (1.0.11)                                - Flask-Tiddly is a minimal,
                                                 prototype RESTful server for
                                                 basic CRUD transactions.
tifa (0.2.3)                                   - a modern flask scaffolding
tinflask (0.0.2)                               - Simple wrapper around flask
                                                 that uses environment
                                                 variables for host, port,
                                                 endpoint prefix. Also uses
                                                 the py-hancock library for
                                                 the ability to sign
                                                 endpoints. Endpoints for
                                                 `time`, `ping`, and `status`
                                                 are automatically added as
                                                 well.
tinysmtp (0.1.2)                               - Basically Flask-Mail without
                                                 the Flask part
Toucan (0.0.0)                                 - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
trappist (0.2.0)                               - Mount your Flask or WSGI app
                                                 in your Django app.
tumbler (0.0.23)                               - Tumbler is a simple layer
                                                 that leverage flask with nice
                                                 logs and automated settings
                                                 management
txflask (0.1)                                  - txflask makes working with
                                                 Twisted Web as easy as
                                                 working with flask
tyron (0.2.4)                                  - Gevent redis/pubsub event
                                                 notifier written in flask and
                                                 gevent
update_checker_app (0.6)                       - Flask Application that
                                                 provides the interface to the
                                                 update_checker package.
uppsell (0.1)                                  - A Flask-based e-commerce API
                                                 and a django-backed admin for
                                                 managing them.
vassal_deployer (0.0.2)                        - uwsgi and nginx flask app
                                                 vassal manager for containers
vuuvv (0.0.1)                                  - A web framework using flask,
                                                 like ror.
webargs (1.8.1)                                - A friendly library for
                                                 parsing and validating HTTP
                                                 request arguments, with
                                                 built-in support for popular
                                                 web frameworks, including
                                                 Flask, Django, Bottle,
                                                 Tornado, Pyramid, webapp2,
                                                 Falcon, and aiohttp.
webdeployer (0.0.4)                            - Personal Deployer for site
                                                 created with Flask and Django
weber_utils (1.2.2)                            - Utilities for the Weber flask
                                                 template
Webmaster (0.0.2)                              - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
WebPortfolio (0.2.6)                           - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
webspanner (0.1.0)                             - Spanner is a micro web
                                                 framework based on asyncio
                                                 inspired by Flask &
                                                 Express.js.
webstarts (2.4.0)                              - Entry point for modern
                                                 flask/gunicorn/sentry/celery
                                                 web applications
wfgfw (0.0.6)                                  - word filter for gfw, include
                                                 plugin for flask. download
                                                 keywords: https://github.com/
                                                 observerss/textfilter
wheelshop (0.1)                                - your python wheels on a PyPI
                                                 compatible server using flask
                                                 and S3
whs.utils.flask (0.2.0)                        - Some Flask utils, targeting
                                                 REST services
WTCrud (0.1dev)                                - CRUD forms for WTForms using
                                                 Flask, Jinja2, SQLAlchemy
xstat (0.1.9)                                  - make statsd work with flask,
                                                 django, maple or other server
yell (0.3.2)                                   - User notification library
                                                 with pluggable backends.
                                                 Compatible with popular
                                                 frameworks such as Django,
                                                 Flask, Celery.
Zask (1.9.5)                                   - Basic framework to use with
                                                 ZeroRPC inspired by Flask
zforms (1.8)                                   - Tiny Flask form validation
                                                 library.
Zolenmeyer (0.1)                               - Stupid personally customized
                                                 Flask