Ansible Role Installer
======================

Install roles directly from Git repositories into your projects Ansible roles/ directory.
Basically equivalent to ansible-galaxy*, except requirements are defined within the playbook.

```
role_install -p playbook.yml
role_install -e ssh://github.com/github_owner/github_repo.git 

# playbook.yml defines
install_roles:
  - {uri: 'ssh://github.com/github_owner/github_repo.git'}
```

[*] $ ansible-galaxy install -r requirements.yml --roles-path=roles/ --ignore-errors
