import argparse, sys

from ansible_role_installer.ari import run

desc = """
role_install -p playbook.yml                                        # Install all playbook dependencies under 'install_roles:'
role_install -e git+ssh://github.com/github_owner/github_repo.git   # Install this repository
"""

def main():
    parser = argparse.ArgumentParser(description="Ansible Role Installer", usage=desc)
    parser.add_argument('-p', help='playbook', required=False)
    parser.add_argument('-e', help='repository URL', required=False)
    parser.add_argument('-r', help='ansible roles path', required=False, default='roles/')
    args = parser.parse_args()
    if not args.p and not args.e:
        sys.exit(parser.print_help())
    run(playbook=args.p, repository=args.e, path=args.r)

if __name__ == '__main__':
    main()
