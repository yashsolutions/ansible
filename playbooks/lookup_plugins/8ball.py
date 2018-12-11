from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import httplib
import json

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class LookupModule(LookupBase):

    def run(self, questions, variables=None, **kwargs):
	# https://8ball.delegator.com/magic/JSON/
	response = []
	try:
		for question in questions:
			conn = httplib.HTTPSConnection("8ball.delegator.com")
			conn.request("GET", "/magic/JSON/" + question)
			response.append(json.loads(conn.getresponse().read())['magic']['answer'])

	except Exception as e:
		raise AnsibleError(e)

	return response
