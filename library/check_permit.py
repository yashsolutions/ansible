#!/usr/bin/python

from ansible.module_utils.basic import *

def main():
	module_args = {
		'name': { 'type': 'str', 'required': True },
		'age': { 'type': 'int', 'required': True }
	}
	module = AnsibleModule(
		argument_spec = module_args,
		supports_check_mode=True
	)

	name = module.params['name']
	age = module.params['age']

	try:
		response = 'APPROVED TO DRIVE' if age >= 16 else 'DENIED LICENSE'
		with open('/tmp/drivers.txt', 'a') as driver_file:
			driver_file.write(name + " : " + str(age) + " : " + response)

		module.exit_json(changed=False, message=response)
	except Exception as e:
		module.fail_json(changed=False, message=str(e))

if __name__ == '__main__':
	main()
