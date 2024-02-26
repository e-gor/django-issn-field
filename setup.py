from setuptools import setup

long_description='Provides django model field to store and validate ISSN numbers.'

setup(
	name='django-issn-field',
	version='0.5.3',
	description='Provides a model and form fields to manage and validate ISSN numbers',
        long_description=long_description,

	url='https://github.com/e-gor/django-issn-field',
	author='secnot, e-gor',

	license='LPGLv3.0',

        keywords=['django', 'issn', 'field'],

	classifiers=[
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
	'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'], 

	# Package
	packages = ['issn_field'],
        package_data={'issn_field': ['locale/*/LC_MESSAGES/django.*']},
	install_requires = ['Django', 'python-stdnum>=1.5', 'six'],
	zip_safe = False,
	include_package_data=True,
)
