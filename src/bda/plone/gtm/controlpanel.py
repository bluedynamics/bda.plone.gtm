from bda.plone.gtm import message_factory as _
from bda.plone.gtm.interfaces import IGTMSettings
from plone.app.registry.browser import controlpanel


class GTMSettingsEditForm(controlpanel.RegistryEditForm):
    schema = IGTMSettings
    label = _(u"Google Tag Manager Settings")
    description = _(u"")


class GTMSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = GTMSettingsEditForm
