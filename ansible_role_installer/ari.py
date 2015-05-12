import subprocess, yaml

def read_playbook(playbook):
    r = yaml.safe_load(open(playbook, 'r'))
    return r[0].get('vars', {}).get('install_roles', []) if r else []

def download_role(uri, name=None, path='roles/', cwd=None):
    name = name or uri.split('/')[-1].replace('.git', '')
    command = 'git clone --depth=1 {} {}{}'.format(uri, path, name)
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        print(output.strip())
    except Exception, e:
        if 'already exists' in e.output:
            pass
        else:
            print(e)

def cleanup(path):
    clean_command = 'find {} -name .git -print0|xargs -0 rm -rf'.format(path)
    output = subprocess.check_output(clean_command, shell=True)

def run(playbook=None, repository=None, path='roles/'):
    if not path or 'roles' not in path:
        raise Exception("Must specify a roles folder as target path")

    if playbook:
        for role in read_playbook(playbook):
            download_role(uri=role['uri'], name=role.get('name'), path=path)

    if repository:
        name = repository.split('/')[-1].replace('.git', '')
        download_role(uri=repository, name=name, path=path)

    cleanup(path)

