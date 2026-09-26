from pypdf import PdfReader
import re

r = PdfReader("the-art-basel-and-ubs-art-market-report-2026-by-arts-economics.pdf")
out = []
for i, p in enumerate(r.pages, 1):
    t = p.extract_text() or ""
    t = t.replace("\u00a0", " ")
    out.append(f"\n\n===== PAGE {i} =====\n{t}")

with open("report.txt", "w", encoding="utf-8") as f:
    f.write("".join(out))
print("done", sum(len(x) for x in out))
