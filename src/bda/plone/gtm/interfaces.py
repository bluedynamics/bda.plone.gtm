# -*- coding: utf-8 -*-
from bda.plone.gtm import message_factory as _
from zope import schema
from zope.interface import Interface


class IGTMExtensionLayer(Interface):
    """Browser layer for bda.plone.gtm.
    """


class IGTMSettings(Interface):
    """Google Tag manager Settings.
    """

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
