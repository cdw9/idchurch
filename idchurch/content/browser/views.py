from plone import api
from plone.dexterity.browser.view import DefaultView
from plone.memoize import ram
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView


class SermonView(DefaultView):
    """ The default view for talks
    """


class SermonListView(BrowserView):
    """ A list of sermons
    """

    def _sermons_cachekey(method, self):
        """ cache sermons until modified
        """
        catalog = api.portal.get_tool('portal_catalog')
        brains = catalog(portal_type='sermon')
        cachekey = sum([int(i.modified) for i in brains])
        return cachekey
    
    @ram.cache(_sermons_cachekey)
    import pdb; pdb.set_trace()
    def sermons(self):
        """ Get a listing of the sermons
        """
        results = []
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())

        brains = portal_catalog(portal_type="sermon",
                                path=current_path,
                                sort_on="getObjPositionInParent",
                                sort_order="reverse")
        for brain in brains:
            obj = brain.getObject()
            results.append({
                'title': brain.Title,
                'url': brain.getURL(),
                'sermon_series': obj.sermon_series,
                'preacher': obj.preacher,
                'date_delivered': obj.date_delivered,
                })
        return results
