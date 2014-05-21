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
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development ",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",

    ],
    keywords='git svn repo',
    description='Meta-checkout tool managing both subversion and git checkouts.',
)
