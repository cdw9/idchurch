from sixfeetup.utils import helpers as sfutils


def importVariousInitial(context):
    """Run the setup handlers for the initial profile"""
    if context.readDataFile('idchurch_policy-initial.txt') is None:
        return
    members = [
        {'id': 'staff',
         'password': 'pi9Veevoo',
         'roles': ['Manager', 'Member'],
         'properties': {
             'email': 'changeme@example.com',
             'fullname': 'idchurch Staff',
             'username': 'staff'
         }
        }
    ]
    sfutils.addUserAccounts(members)


def importVarious(context):
    """Run the setup handlers for the default profile"""
    if context.readDataFile('idchurch_policy-default.txt') is None:
        return
    # automagically run a plone migration if needed
    sfutils.runPortalMigration()
    # automagically run the upgrade steps for this package
    sfutils.runUpgradeSteps(u'idchurch.policy:default')
    sfutils.refreshAssetRegistry()
