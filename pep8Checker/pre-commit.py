#!/usr/bin/env python
# Source: https://gist.github.com/1376856 + www.sporteasy.net

import os
import re
import subprocess
import sys

modified = re.compile('^(?:M|A)(\s+)(?P<name>.*)')

CHECKS = [
    {
        'output': 'Checking for pdbs...',
        'command': 'grep -n "import pdb" %s',
        'ignore_files': ['.*pre-commit'],
        'print_filename': True,
    },
    {
        'output': 'Checking for ipdbs...',
        'command': 'grep -n "import ipdb" %s',
        'ignore_files': ['.*pre-commit'],
        'print_filename': True,
    },
    {
        'output': 'Checking for print statements...',
        'command': 'grep -n print %s | grep -v -i "blueprint"',
        'match_files': ['.*\.py$'],
        'ignore_files': ['.*migrations.*', '.*management/commands.*', '.*manage.py', '.*/scripts/.*'],
        'print_filename': True,
    },
    {
        'output': 'Checking for console.log()...',
        'command': 'grep -n console.log %s',
        'match_files': ['.*yipit/.*\.js$'],
        'print_filename': True,
    },
]


def matches_file(file_name, match_files):
    return any(re.compile(match_file).match(file_name) for match_file in match_files)


def check_files(files, check, repo_root):
    result = 0
    print((check['output']))
    for file_name in files:
        if not 'match_files' in check or matches_file(file_name, check['match_files']):
            if not 'ignore_files' in check or not matches_file(file_name, check['ignore_files']):
                process = subprocess.Popen(check['command'] % (
                    repo_root + '/' + file_name), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                out, err = process.communicate()
                if out or err:
                    if check['print_filename']:
                        prefix = '\t%s:' % file_name
                    else:
                        prefix = '\t'
                    output_lines = ['%s%s' % (prefix, line) for line in out.splitlines()]
                    print(('\n'.join(output_lines)))
                    if err:
                        print(err)
                    result = 1
    return result


def exit_on_err(result):
    if result:
        print('\033[1;31mCommit aborted\033[0;39m')
        sys.exit(result)


def main(all_files):
    p = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE)
    out, _ = p.communicate()
    repo_root = out.splitlines()[0]

    files = []
    if all_files:
        for root, dirs, file_names in os.walk('.'):
            for file_name in file_names:
                files.append(os.path.join(root, file_name))
    else:
        p = subprocess.Popen(['git', 'status', '--porcelain'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            match = modified.match(line)
            if match:
                files.append(match.group('name'))

    result = 0

    p = subprocess.Popen(['find', repo_root, '-name', 'manage.py'], stdout=subprocess.PIPE)
    out, _ = p.communicate()
    manage = out.splitlines()[0]

    print('Running Django Code Validator...')
    return_code = subprocess.call('$VIRTUAL_ENV/bin/python %s validate' % manage, shell=True)
    result = return_code or result

    #exit_on_err(result)

    for check in CHECKS:
        return_code = check_files(files, check, repo_root) or result
        result = return_code or result

    #exit_on_err(result)

    print('Running pep8 Validator...')
    p = subprocess.Popen('py.test -q --pep8 aaee_front/', shell=True, stdout=subprocess.PIPE)
    out, _ = p.communicate()
    pep8 = out.splitlines()
    if len(pep8) > 2:  # When all is OK for pep8, output = 2 lines.
        for line in pep8:
            print(line)
            #exit_on_err(1)
        return_code = 1
        result = return_code or result

    exit_on_err(result)

if __name__ == '__main__':
    all_files = False
    if len(sys.argv) > 1 and sys.argv[1] == '--all-files':
        all_files = True
    main(all_files)
