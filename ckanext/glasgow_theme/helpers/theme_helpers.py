from pylons import config, cache
import sqlalchemy.exc

import ckan.logic as logic
import ckan.lib.maintain as maintain
import ckan.lib.search as search
import ckan.lib.base as base
import ckan.model as model
import ckan.lib.helpers as h
from datetime import datetime, timedelta

from ckan.common import _, g, c


## Get all packages
def get_package_count():

  context = {'model': model, 'session': model.Session}
  data_dict = {
      'q': '*:*',
      'fq': 'capacity:"public"'
  }
  query = logic.get_action('package_search')(
      context, data_dict)
  return query['count']
  
## Gets list of organizations  
def get_organization_count():
  context = {}
  data_dict = {}
  query = logic.get_action('organization_list')(
      context, data_dict)
  return len(query)

## get this months datasets  
def get_this_month():
  
  query = model.Session.query(model.Package).filter(model.Package.metadata_modified >= datetime.now() - timedelta(365/12)).count()
  
  return query
  
  
def homepage_items():
  
  homepage_items = {
    "package_count":get_package_count,
    "organization_count":get_organization_count,
    "this_month":get_this_month,
  }
  
  return homepage_items
  