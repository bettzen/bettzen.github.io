# -*- coding: utf-8 -*-
"""精确定位 content 中含中文 tags 的文件 + docs/tags 中文目录"""
import os, re

CONTENT = r"D:\bettzen\blowfish-final\content"
DOCS_TAGS = r"D:\bettzen\blowfish-final\docs\tags"

# 1. 扫描 content 所有 md 的 front matter tags
print("=== content 中含中文 tags 的文件 ===")
found = []
for root, dirs, files in os.walk(CONTENT):
    for fn in files:
        if not fn.endswith(".md"):
            continue
        p = os.path.join(root, fn)
        with open(p, encoding="utf-8") as f:
            c = f.read()
        m = re.search(r'^tags\s*[:=]\s*(\[.*?\])', c, re.M | re.S)
        if not m:
            continue
        tags = m.group(1)
        if re.search(r'[\u4e00-\u9fff]', tags):
            found.append(p.replace("D:\\bettzen\\blowfish-final\\", ""))
for f in found:
    print("  ", f)
print("  共", len(found), "个")

# 2. docs/tags 中文目录
print("\n=== docs/tags 中文/异常目录 ===")
cn = [d for d in os.listdir(DOCS_TAGS) if re.search(r'[\u4e00-\u9fff]', d) or d == "---"]
print("  数量:", len(cn))
for d in sorted(cn)[:15]:
    print("  ", d)
