Contributing Guidelines
=======================

Please follow these guidelines for contributing to this project.

Repository Management
---------------------

- Fork this project into your own repository.
- Follow the `version control`_ guidelines.
- No changes should reach the ``main`` branch except by way of a
  `pull request`_.

Submitting Issues
~~~~~~~~~~~~~~~~~

`Create an issue`_ to report bugs or request enhancements. Better yet, you're
encouraged to fix the problem yourself and submit a `pull request`_.

Bug Reports
+++++++++++

When reporting a bug, please provide the steps to reproduce the problem and any
details that could be important such as whether this is the first time this has
happened or whether others are experiencing it.

Pull Requests
+++++++++++++

Pull requests must remain focused on fixing or addressing one thing (see
`topic branch`_ model). Make sure your pull request contains a clear title and
description. Test coverage should not drop as a result. If you add code, you
add tests.

Be sure to follow the guidelines on `writing code`_ if you want your work
considered for inclusion.

Handling Pull Requests
~~~~~~~~~~~~~~~~~~~~~~

- Pull requests **must** include:

  - Title describing the change
  - Description explaining the change in detail
  - Tests

- A maintainer will respond to Pull Requests with one of:

  - 'Ship It', 'LGTM', 🚢, or some other affirmation
  - What must be changed
  - Won't accept and why

Nota Bene
+++++++++

- Submitting a `draft pull request`_ is a good way to get feedback from
  maintainers if you are unsure of the changes you are making.
- A pull request that has been approved may not be merged immediately.
- You may be asked to rebase or squash your commits to keep an orderly version
  control history.

.. _version control:

Using Version Control
~~~~~~~~~~~~~~~~~~~~~

- `Fork`_ the `central repository`_ and work from a clone of your own fork.
- Follow the `topic branch`_ model and submit pull requests from branches named
  according to their purpose.
- Review the `GitHub Flow`_ documentation and, in general, try to stick to the
  principles outlined there.

.. _writing code:

Writing Code
------------

Writing code is a creative process and there will always be exceptions to the
rules, but it's good to maintain certain standards. In general, please follow
these code conventions.

Coding Style
~~~~~~~~~~~~

- Code in this project **must** be formatted with `black`_.
- Code in this project **must** be linted with `flake8`_.
- Try to follow :pep:`8` guidelines.
- Try to respect the style of existing code.

Coding style checks are bundled into the static analysis automation in this
repository's `tox`_ configuration. To validate your coding style run

.. code-block:: sh

   tox -e static

Test Environment
~~~~~~~~~~~~~~~~

- Code **must** be tested. Write or update related unit tests so you don't have
  to manually retest the same thing many times.
- Tests for this project are written using the `pytest`_ framework and executed
  via `tox`_. While it isn't always achievable this project strives to maintain
  💯% test coverage.
- In addition to unit testing code in this project is statically type checked
  using `mypy`_, formatted with `black`_, linted using `flake8`_, and security
  checked with `bandit`_.

Here are some example invocations for running unit tests/static analysis.

.. code-block:: sh

   tox                        # Build and test the project
   tox -e py39                # in a specific environment
   tox -e py39 -- --pdb       # with extra options,
                              # or
   tox -e py39 --devenv venv  # create a development environment
   venv/bin/python -V         # and call scripts/binaries in it.

Documentation
~~~~~~~~~~~~~

- Public interfaces **must** be thoroughly documented. At a minimum this
  includes inputs, return types, exceptions raised, and surprising behavior
  like state changes.
- Documentation for this project is written in `reStructuredText`_ with the
  `Google style`_ and generated with `Sphinx`_.
  
To generate documentation run

.. code-block:: sh

    tox -e docs


.. _Create an issue: https://help.github.com/articles/creating-an-issue
.. _pull request: https://help.github.com/articles/using-pull-requests/
.. _draft pull request: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests#draft-pull-requests
.. _topic branch: https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows#Topic-Branches
.. _Fork: https://help.github.com/articles/fork-a-repo/
.. _central repository: https://github.com/reillysiemens/ipython-style-gruvbox/
.. _GitHub Flow: https://guides.github.com/introduction/flow/
.. _pytest: https://docs.pytest.org/en/latest/
.. _tox: https://tox.readthedocs.io/en/latest/
.. _mypy: http://www.mypy-lang.org/
.. _black: https://black.readthedocs.io/en/stable/
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _bandit: https://bandit.readthedocs.io/en/latest/
.. _reStructuredText: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Google style: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
.. _Sphinx: http://www.sphinx-doc.org/en/master/index.html
