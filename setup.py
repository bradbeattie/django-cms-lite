from setuptools import setup, find_packages

setup(
    name='django-cms-lite',
    version='2015.04.22.0',
    description='Simple Django CMS with very limited functionality.',
    long_description='Renders discovered HTML tempaltes as CMS pages.',
    author='Brad Beattie',
    author_email='bradbeattie@gmail.com',
    url='https://github.com/bradbeattie/django-cms-lite',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    package_data = { '': ['README.rst'] },
    install_requires=['django'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
