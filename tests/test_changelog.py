import re

def test_changelog_has_version():
    with open("CHANGELOG.md", "r", encoding="utf-8") as f:
        content = f.read()
    # 简单检查是否包含“## [x.y.z]”
    assert re.search(r"## \[\d+\.\d+\.\d+\]", content)
