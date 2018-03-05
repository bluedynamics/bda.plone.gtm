from bda.plone.gtm.interfaces import IGTMData
from bda.plone.gtm.interfaces import IGTMSettings
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from plone.app.layout.viewlets.common import ViewletBase
import json


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
        # render empty if not GTM enabled
        if not settings.enabled:
            return u''
        # return GTM loader script snippet with configured layer name and
        # container ID
        return GTM_SCRIPT % dict(
            layer_name=settings.layer_name,
            container_id=settings.container_id
        )


class GTMDataViewlet(ViewletBase, GTMSettings):
    """Google Tag Manager data viewlet.
    """

    def render(self):
        """Render script tag pushing context related data to GTM layer.
        """
        settings = self.settings
        # render empty if not GTM enabled
        if not settings.enabled:
            return u''
        # lookup GTM data
        data = IGTMData(self.context).data
        # render empty if no data to track
        if not data:
            return u''
        # ensure data is list of dicts
        if not isinstance(data, list):
            assert isinstance(data, dict)
            data = [data]
        # collect data.push calls
        pushs = list()
        for d in data:
            pushs.append(u'%(layer_name)s.push(%(data)s);' % dict(
                layer_name=settings.layer_name,
                data=json.dumps(d)
            ))
        # return noscript fallback and script snipped containing push calls
        # to data layer
        return u'%(no_script)s<script>%(pushs)s</script>' % dict(
            no_script=GTM_NO_SCRIPT % dict(container_id=settings.container_id),
            pushs=u','.join(pushs)
        )
