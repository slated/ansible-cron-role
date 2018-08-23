import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_crontab_file(host):
    c = host.command('crontab -l').stdout
    assert 'MAILTO=mail@example.com' in c
    assert '#Ansible: test' in c
    assert '55 23 * * Mon,Thu /tmp/test.sh > /tmp/env' in c
