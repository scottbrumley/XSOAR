import demistomock as demisto
from CommonServerPython import *
from CommonServerUserPython import *

dev = demisto.args()['dev']
demisto.results("Hello "+dev)
