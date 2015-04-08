import os

from django.conf import settings

from app import constants, errors

def get_version_components(string):
	major = 0
	minor = 0
	build = 0
	match = constants.RE_REV_NUM.search(string)
	if not match:
		raise errors.InvalidVersionError(string)
	else:
		groups = match.groups()
		major = int(groups[0])
		if groups[1]: minor = int(groups[1])
		if groups[2]: build = int(groups[2])

	return (major, minor, build)

def get_absolute_path(dir_name):
	return os.path.join(settings.BASE_DIR, dir_name)