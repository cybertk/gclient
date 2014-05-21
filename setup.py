from distutils.core import setup

setup(
    name='gclient',
    version='0.7',
    author='Quanlong He',
    author_email='kyan.ql.he@gmail.com',
    scripts=['bin/gclient'],
    packages=['depot_tools', 'depot_tools.third_party.colorama', 'depot_tools.third_party.repo'],
    url='https://github.com/cybertk/gclient',
    license='BSD-style License, see LICENSE.txt',
    description='Meta-checkout tool managing both subversion and git checkouts. It is similar to repo tool except that it works on Linux, OS X, and Windows and supports both svn and git. On the other hand, gclient doesn\'t integrate any code review functionality.',
    long_description=open('README.txt').read(),
)
