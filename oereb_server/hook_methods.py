# -*- coding: utf-8 -*-
import datetime
from pyramid.path import DottedNameResolver
from pyramid_oereb import Config, database_adapter
from pyramid_oereb.lib.records.office import OfficeRecord

def get_surveying_data_provider(real_estate):
    """
    Args:
        real_estate (pyramid_oereb.lib.records.real_estate.RealEstateRecord): The real estate for which the
            provider of the surveying data should be delivered.
    Returns:
        provider (pyramid_oereb.lib.records.office.OfficeRecord): The provider who produced the used
            surveying data.
    """
    params = Config.get_real_estate_config().get('source').get('params')
    session = database_adapter.get_session(params.get('db_connection'))
    try:
        model = DottedNameResolver().resolve(params.get('model'))
        re = session.query(model).filter(model.egrid == real_estate.egrid).one()
        provider = OfficeRecord(re.data_provider)
        return provider
    finally:
        session.close()


def get_surveying_data_update_date(real_estate):
    """
    Gets the date of the latest update of the used survey data data for the
    situation map. The method you find here is only matching the standard configuration. But you can provide
    your own one if your configuration is different. The only thing you need to take into account is that the
    input of this method is always and only a real estate record. And the output of this method must be a
    datetime.date object.
    Args:
        real_estate (pyramid_oereb.lib.records.real_estate.RealEstateRecord): The real
            estate for which the last update date of the base data should be indicated
    Returns:
        update_date (datetime.datetime): The date of the last update of the cadastral base data
    """
    params = Config.get_real_estate_config().get('source').get('params')
    session = database_adapter.get_session(params.get('db_connection'))
    try:
        model = DottedNameResolver().resolve(params.get('model'))
        re = session.query(model).filter(model.egrid == real_estate.egrid).one()
        return datetime.datetime.combine(re.currentness, datetime.time.min)
    finally:
        session.close()
