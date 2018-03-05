=============
bda.plone.gtm
=============

Google Tag Manager Integration.


Installation and Configuration
==============================

- Depend your installation to ``bda.plone.gtm``.

- Install ``bda.plone.gtm`` via Plone Add-ons control panel.

- Naviagte to "Site Setup" -> "Add-on Configuration" -> "Google Tag Manager Settings".

- Set "Enabled" checkbox and enter "Container ID". Optionally edit "Layer Name"
  to your needs. This integration package handles the layer name properly.
  Anyway you need to be aware that any 3rd party JS using this package may
  depend hardcoded to the default layer name, so be careful with changing this
  setting.


Providing Data
==============

``bda.plone.gtm`` by default tracks nothing. To track something useful,
``bda.plone.gtm.interfaces.IGTMData`` adapters needs to be provided for the
relevant context.

The adapter implementation looks like:

.. code-block:: python

    from a.package.interfaces import IMyContextInterface
    from bda.plone.gtm.interfaces import IGTMData
    from zope.component import adapter
    from zope.interface import implementer

    @implementer(IGTMData)
    @adapter(IMyContextInterface)
    class MyContextGTMData(object):

        def __init__(self, context):
            self.context = context

        @property
        def data(self):
            # data is a dict or a list of dicts.
            return {
                'pageTitle': 'Home',
                'visitorType': 'high-value'
            }

Register the data adapter:

.. code-block:: xml

    <configure xmlns="http://namespaces.zope.org/zope">

      <!-- GTM data adapter -->
      <adapter factory=".data.MyContextGTMData" />

    </configure>


Contributors
============

- Robert Niederreiter (Author)
