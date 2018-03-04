from Products.Five import BrowserView
from bda.plone.gtm.interfaces import IGTMSettings
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from plone.app.layout.viewlets.common import ViewletBase


GTM_SCRIPT = """
<script>{layer_name} = [];</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','{layer_name}','{container_id}');</script>
<!-- End Google Tag Manager -->
"""

GTM_NO_SCRIPT = """
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={container_id}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""


class GTMSettings(object):

    @property
    def settings(self):
        registry = getUtility(IRegistry)
        return registry.forInterface(IGTMSettings)


class GTMIntegration(BrowserView, GTMSettings):
    """Google Tag Manager Integration view.
    """

    def script(self):
        settings = self.settings
        return GTM_SCRIPT.format(
            layer_name=settings.layer_name,
            container_id=settings.container_id
        )

    def noscript(self):
        settings = self.settings
        return GTM_NO_SCRIPT.format(container_id=settings.container_id)


class GTMViewlet(ViewletBase, GTMSettings):
    """Context specific Google Tag Manager viewlet.
    """

    @property
    def data(self):
        """Context related data as dict to push to GTM data layer.
        """
        return {}

    def render(self):
        """Render script tag pushing context related data to GTM layer.
        """
        tags = list()
        for k, v in self.data:
            tags.append("'{k}':'{v}'".format(k=k, v=v))
        return u'<script>{layer_name}.push({{{data}}})</script>'.format(
            self.settings.layer_name,
            u','.join(tags)
        )
