from bda.plone.gtm.interfaces import IGTMData
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer


@implementer(IGTMData)
@adapter(Interface)
class DefaultGTMData(object):
    """Default Google Tag Manager data adapter.

    By default, no data gets pushed to GTM data layer.
    """
    data = None

    def __init__(self, context):
        self.context = context
