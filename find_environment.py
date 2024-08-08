import os

def find_virtualenvs(base_dir):
    envs = []
    for root, dirs, files in os.walk(base_dir):
        if 'bin' in dirs and 'activate' in os.listdir(os.path.join(root, 'bin')):
            envs.append(root)
    return envs

base_dirs = ['~', '~/envs', '~/.pyenv']  # Adicione outros diretórios onde você possa ter criado ambientes
for base_dir in base_dirs:
    base_dir = os.path.expanduser(base_dir)
    envs = find_virtualenvs(base_dir)
    print(f"Virtual environments in {base_dir}:")
    for env in envs:
        print(f"  - {env}")
