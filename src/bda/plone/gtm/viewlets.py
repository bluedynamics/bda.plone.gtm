from bda.plone.gtm.interfaces import IGTMSettings
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from plone.app.layout.viewlets.common import ViewletBase


GTM_SCRIPT = """
<script>%(layer_name)s = [];</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','%(layer_name)s','%(container_id)s');</script>
<!-- End Google Tag Manager -->
"""

GTM_NO_SCRIPT = """
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=%(container_id)s"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""


class GTMSettings(object):
    """Google Tag Manager settings mixin.
    """

    @property
    def settings(self):
        registry = getUtility(IRegistry)
        return registry.forInterface(IGTMSettings)


class GTMLoaderViewlet(ViewletBase, GTMSettings):
    """Google Tag Manager loader viewlet.
    """

    def render(self):
        settings = self.settings
        return GTM_SCRIPT % dict(
            layer_name=settings.layer_name,
            container_id=settings.container_id
        )


class GTMDataViewlet(ViewletBase, GTMSettings):
    """Google Tag Manager data viewlet.
    """

    @property
    def data(self):
        """Context related data as dict to push to GTM data layer.
        """
        return {}

    def render(self):
        """Render script tag pushing context related data to GTM layer.
        """
        settings = self.settings
        tags = list()
        for k, v in self.data:
            tags.append("'%(k)s':'%(v)s'" % dict(k=k, v=v))
        return u'%(no_script)s<script>%(layer_name)s.push({%(data)s})</script>' % dict(
            no_script=GTM_NO_SCRIPT % dict(container_id=settings.container_id),
            layer_name=self.settings.layer_name,
            data=u','.join(tags)
        )
