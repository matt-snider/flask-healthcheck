from distutils.core import setup


setup(
    name='Flask-Healthcheck',
    version='0.1.2',
    description='Healthchecks for flask applications made easy',
    author='Matt Snider',
    author_email='matt.snider@alum.utoronto.ca',
    url='https://github.com/matt-snider/flask-healthcheck',
    packages=['flask_healthcheck'],
    install_requires=['flask'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

