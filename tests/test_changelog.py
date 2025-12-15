import os
import re

def test_changelog_has_version():
    # 获取 tests 文件所在目录
    tests_dir = os.path.dirname(__file__)
    # 仓库根目录
    repo_root = os.path.abspath(os.path.join(tests_dir, '..'))
    # CHANGELOG.md 的绝对路径
    changelog_path = os.path.join(repo_root, 'CHANGELOG.md')

    with open(changelog_path, 'r', encoding='utf-8') as f:
        content = f.read()

    assert re.search(r"## \[\d+\.\d+\.\d+\]", content)
