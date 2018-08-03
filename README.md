[![Build Status](https://travis-ci.org/slated/ansible-cron-role.svg?branch=master)](https://travis-ci.org/slated/ansible-cron-role)


Role Name
=========

Install cronjob.

Requirements
------------

An install Ubuntu server.

Role Variables
--------------
```
cron_tasks
cron_vars
```

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
        - ansible-role-cron
      vars:
        cron_tasks:
          - name: "rescore"
            minute: 55
            hour: 23
            weekday: "Mon,Thu"
            day: "*"
            month: "*"
            job: "env > /tmp/env"
        cron_vars:
          - name: MAILTO
            value: mail@example.com
