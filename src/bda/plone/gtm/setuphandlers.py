# -*- coding:utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return ['bda.plone.gtm:install-base']


@implementer(INonInstallable)
class HiddenProducts(object):
    def getNonInstallableProducts(self):
        """Do not show on QuickInstaller's list of installable products.
        """
        return ['bda.plone.gtm:install-base']