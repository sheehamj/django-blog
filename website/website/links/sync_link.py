import sys, os



sys.path.append('/usr/local/lib/python2.7/dist-packages/django')

sys.path.append('/home/sheehan/website')

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'



from website.links import utils

client = utils.DeliciousClient('sheehamj','garmin10')

data = client.fetch()

utils.create_link(data)

