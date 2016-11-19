bgp-spamd
#########

Provision spamd with spam list distributed via bpg. For more information visit
`bgp-spamd.net <http://bgp-spamd.net/>`_. Configuration of PF is more custom and
out of scope for this role, however one can include the configuration snippet
created by this role by adding the following to your :code:`pf.conf`.

.. code::

    include "/etc/pf.conf.bgp-spamd"

This will add 2 PF tables, :code:`spamd-white` and :code:`bgp-spamd-bypass`,
both contain whitelisted IP addresses of mail senders. You can allow them
through and send the rest to the spam trap by adding the following line to
your :code:`pf.conf`.

.. code::

    pass in quick proto tcp from { <bgp-spamd-bypass>, <spamd-white> } to port smtp
    pass in quick proto tcp to (egress:0) port smtp rdr-to 127.0.0.1 port spamd

Requirements
------------

See :code:`meta/main.yml`, :code:`tests/requirements.yml` and assertions at
the top of :code:`tasks/main.yml`.

Role Variables
--------------

See :code:`defaults/main.yml`.

Dependencies
------------

See :code:`meta/main.yml`.

Example Playbook
----------------

See :code:`tests/playbook.yml`.

Testing
-------

Testing requires Virtualbox and Vagrant and Python 2.7. Install the Python
dependencies, add pre-commit hooks by running:

.. code:: shell

    pip install -r tests/requirements.txt
    pre-commit install

To run the full test suite:

.. code:: shell

    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD) -p .molecule/roles
    molecule test --platform all
    pre-commit run --all-files

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.
