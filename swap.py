import re, sys
sys.stdout.reconfigure(encoding="utf-8")
p = "index.html"
s = open(p, encoding="utf-8").read()

start = s.index('    <!-- ============ 项目一 ============ -->')
mid   = s.index('    <!-- ============ 项目二 ============ -->')
end   = s.index('  </div>\n</section>', mid)

block1 = s[start:mid]
block2 = s[mid:end]

# 交换两块，并修正注释编号
block1 = block1.replace('项目一', '项目二')
block2 = block2.replace('项目二', '项目一')

s = s[:start] + block2 + block1 + s[end:]
open(p, "w", encoding="utf-8").write(s)
print("SWAPPED: RAG 现在在前")
