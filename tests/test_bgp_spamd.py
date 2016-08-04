def test_spamd_service(Service):
    assert Service('spamd').is_running


def test_spamd_config(File):
    assert File('/etc/rc.conf.local').contains('spamd_flags=')


def test_bgpd_config(File, Sudo):
    with Sudo():
        assert File('/etc/bgpd.conf').contains('spamdAS')


def test_pf_anchor(File, Command, Sudo):
    assert File('/etc/pf.conf.bgp-spamd').exists
    with Sudo():
        assert Command('/sbin/pfctl -f /etc/pf.conf').rc == 0


def test_spamd_socket(Socket):
    assert Socket('tcp://127.0.0.1:8025').is_listening


def test_bgpd_user(User, File):
    assert User('_bgpd').exists
    assert File('/etc/mail/aliases').contains('_bgpd: root')


def test_spamd_user(User, File):
    assert User('_spamd').exists
    assert File('/etc/mail/aliases').contains('_spamd: root')


def test_allowed_domains(File):
    assert File('/etc/mail/spamd.alloweddomains').exists
