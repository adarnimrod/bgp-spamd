bgp-spamd
#########

Provision spamd with spam list distributed via bpg. For more information visit
`bgp-spamd.net <http://bgp-spamd.net/>`_. Configuration of PF is more custom and
out of scope for this role, however a PF anchor can be used by adding the
following to your :code:`pf.conf`.

.. code::

    anchor bgp-spamd
    load anchor bgp-spamd from "/etc/pf.conf.bgp-spamd"

This will add 2 PF tables, :code:`spamd-white` and :code:`bgp-spamd-bypass`,
both contain whitelisted IP addresses of mail senders. You can allow them
through by adding the following line to your :code:`pf.conf`.

.. code::

    pass in quick proto tcp from { <bgp-spamd-bypass>, <spamd-white> } to port smtp

Requirements
------------

See :code:`meta/main.yml` and assertions at top of :code:`tasks/main.yml`.

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

To install the dependencies:

.. code:: shell

    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD)

To run the full test suite:

.. code:: shell

    molecule test

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

- Log to syslog.
- At the end flush handlers and wait for services to start?
- Use PF anchors if possible.
- Assertions.
- Tests.
- Use dhparams?
- Alias email to root.
