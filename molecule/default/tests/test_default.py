import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_crontab_file(host):
    c = host.command('crontab -l').stdout
    assert 'MAILTO=mail@example.com' in c
    assert '#Ansible: rescore' in c
    assert '55 23 * * Mon,Thu env > /tmp/env' in c
