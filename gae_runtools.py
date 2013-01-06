"""
  gae_runtools
  ~~~~~~~~~~~~~~~~~~~

  Flask extension for working with the App Engine sdk.

  :copyright: (c) 2012 by gregorynicholas.
  :license: MIT, see LICENSE for more details.
"""
import logging

def enable_jinja2_debugging():
  '''Enables blacklisted modules that help Jinja2 debugging.'''
  try:
    # Enables better debugging info for errors in Jinja2 templates.
    from google.appengine.tools.dev_appserver import HardenedModulesHook
    HardenedModulesHook._WHITE_LIST_C_MODULES += ['_ctypes', 'gestalt']
  except Exception, e:
    logging.error(
      'Failed to enable jinja2 debug. Exception encountered: "' + str(e) + '".')

def enable_appstats(app):
  '''Utility function that enables appstats middleware.'''
  try:
    from google.appengine.ext.appstats.recording import appstats_wsgi_middleware
    app.app = appstats_wsgi_middleware(app.app)
  except Exception, e:
    logging.error(
      'Failed to initialize AppStats. Exception encountered: "' + str(e) + '".')
  return app

def enable_apptrace(app):
  '''Utility function that enables apptrace middleware.'''
  try:
    from libs.apptrace import middleware
    middleware.Config.URL_PATTERNS = ['^/$']
    app.app = middleware.apptrace_middleware(app.app)
  except Exception, e:
    logging.error(
      'Failed to initialize AppTrace. Exception encountered: "' + str(e) + '".')
  return app

def get_app_config(partition='dev'):
  from os import path
  from google.appengine.api import app_identity
  app_id = '~%s-%s' % (partition, app_identity.get_application_id())
  from google.appengine.tools import dev_appserver
  root_path = path.abspath(path.join(path.dirname(__file__), '../../'))
  gaeconfig, _, _ = dev_appserver.LoadAppConfig(root_path, {})
  sdk_version = dev_appserver.GetVersionObject()
  version_id = str(gaeconfig.version) + '.' + str(sdk_version.get('timestamp'))
  return gaeconfig, sdk_version, app_id, version_id
