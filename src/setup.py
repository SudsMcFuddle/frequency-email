from distutils.core import setup
import py2exe


setup(
	name = "Frequency",
	version = "0.1",
	windows = [
		{
			"script": "frequency.py",
			"icon_resources": [(1, "icons/Frequency.ico")]
		}
	],
	script_args = ["py2exe"],
	data_files = [ ("icons",["icons/Frequency.ico",
							 'icons/email.png',
							 'icons/email_add.png',
							 'icons/email_delete.png',
							 'icons/email_attach.png',
							 'icons/email_edit.png',
							 'icons/door_in.png',
							 'icons/user.png',
							 'icons/wrench.png',
							 ])
	],
	options = {
		"py2exe": {
			"dist_dir":"../dist"
		}
	}
)
