gclient
=======

gclient is a meta-checkout tool managing both subversion and git checkouts. It is similar to repo tool except that it works on Linux, OS X, and Windows and supports both svn and git. On the other hand, gclient doesn't integrate any code review functionality.

It's extrated from Chomium's depot_tools, see http://src.chromium.org/svn/trunk/tools/depot_tools/

Features
-------

gclient is a python script to manage a workspace of modular dependencies that are each checked out independently from different subversion or git repositories. Features are:

* Dependencies can be specified on a per-OS basis.
* Dependencies can be specified relative to their parent dependency.
* Variables can be used to abstract concepts.
* Hooks can be specified to be run after a checkout.
* .gclient and DEPS are python scripts, you can hack in easily or add additional configuration data.


.gclient file
-------------

It's the master file. It is, in fact, a python script. It specifies the following variables:

* solutions: an array of dictionaries specifying the projects that will be fetched.
* hooks: additional hooks to be run when this meta checkout is synced.
* target_os: an optional array of (target) operating systems to fetch OS-specific dependencies for.

Additional variables are ignored.

Each project described in the solutions array can contain an optional DEPS file that will be processed. The .gclient file is generated with gclient config <url> or by hand. Each solutions entry is a dictionary that can contain the following variables:

* name: really, the path of the checkout.
* url: the remote repository to fetch/clone.
* custom_deps: (optional) override the dependencies specified in the deps and deps_os variables in child DEPS files. Useful when you want to fetch a writable checkout instead of the default read-only checkout of a dependency, e.g. you work on native_client from a chromium checkout.
* custom_vars: (optional) override the variables defined in vars in child DEPS files. Example: override the WebKit version used for a chromium checkout.
* safesync_url: (optional) url to fetch to retrieve the revision to sync this checkout to.

.gclient example
----------------

http://dev.chromium.org/developers/contributing-to-webkit explains how to hack your own .gclient file to modify the checkout to fetch from webkit's trunk instead of the version specified by chromium. 
DEPS file

A DEPS file specifies dependencies of a project. It is in fact a python script. It specifies the following variables:

* deps: a dictionary of child dependencies to fetch.
* deps_os: a dictionary of OSes for OS-specific dependencies, each containing a dictionary of child dependencies to fetch.
* vars: a dictionary of variables to define. Mainly useful to easily override a batch of revisions at once.
* hooks: hooks to run after a sync.
* use_relative_paths: relative paths should specify the checkout relative to this directory instead of the root gclient checkout.

Additional variables are ignored. Special keywords are:

* File(): used for dependencies, specify to expect to checkout a file instead of a directory.
* From(): used to fetch a dependency definition from another DEPS file, for chaining.
* Var(): replace this string with a variable defined in vars or overridden.
Pinned deps

Each dependency checkout URL can (and usually does) contain a revision number or git hash, which means you're going to check out and build from that specific revision of the module in question. We call that pinned deps. The advantage is that you can build from a known working revision, even if it comes from a completely different SCM repository or going back in time. The drawback is you have to update the revision number(s) constantly, what we call deps rolls.

DEPS examples
=============

Webkit's WebKit/chromium/DEPS and Chromium's src/DEPS are fairly complex examples that will show all the possibilities of a DEPS file.
