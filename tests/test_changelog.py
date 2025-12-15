import os
import re

def test_changelog_has_version():
    # get the directory of the current test file
    tests_dir = os.path.dirname(__file__)
    # get the repository root directory
    repo_root = os.path.abspath(os.path.join(tests_dir, '..'))
    # get the absolute path of CHANGELOG.md
    changelog_path = os.path.join(repo_root, 'CHANGELOG.md')

    with open(changelog_path, 'r', encoding='utf-8') as f:
        content = f.read()

    assert re.search(r"## \[\d+\.\d+\.\d+\]", content)
