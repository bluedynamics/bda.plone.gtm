# -*- coding: utf-8 -*-
from bda.plone.gtm import message_factory as _
from zope import schema
from zope.interface import Attribute
from zope.interface import Interface


class IGTMExtensionLayer(Interface):
    """Browser layer for bda.plone.gtm.
    """


class IGTMData(Interface):
    """Data adapter for Google Tag Manager.

    If GTM is enabled, the data viewlet looks up an ``IGTMData`` adapter
    for the current context.
    """

    data = Attribute('Dictionary or list of dictionaries containing the '
                     'data which gets pushed to GTM data layer.')


class IGTMSettings(Interface):
    """Google Tag manager Settings.
    """

    enabled = schema.Bool(
        title=_('enabled', default='Enabled'),
        description=_(
            'enabled_help',
            default='Google Tag Manager enabled'
        ),
        default=False
    )

    container_id = schema.TextLine(
        title=_('container_id', default='Container ID'),
        description=_(
            'container_id_help',
            default='Google Tag Manager Container ID'
        )
    )

    layer_name = schema.TextLine(
        title=_('layer_name', default='Layer Name'),
        description=_(
            'layer_name_help',
            default='Google Tag Manager Data Layer Name'
        ),
        default=u'dataLayer'
    )
