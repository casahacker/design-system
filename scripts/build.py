#!/usr/bin/env python
"""Casa Hacker DS · Master build orchestrator.

Single command rebuild de todas as páginas estáticas + search index.

Uso:
    py scripts/build.py             # rebuild completo
    py scripts/build.py --quick     # só foundations + components + search
    py scripts/build.py --check     # valida sem regerar

Saída: roda todos os generators em sequência e termina com search-index
atualizado. Exit code != 0 se algum gen falhar.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GENERATORS = [
    ("foundations",      "gen_foundation.py"),
    ("components-a",     "gen_components_a.py"),
    ("components-b",     "gen_components_b.py"),
    ("components-new",   "gen_components_new.py"),
    ("patterns",         "gen_patterns.py"),
    ("dataviz",          "gen_dataviz.py"),
    ("brand+help",       "gen_brand.py"),
    ("impressos",        "gen_impressos.py"),
    ("hackerclubes",     "gen_hackerclubes.py"),  # roda APÓS gen_brand · sobrescreve
    ("search-index",     "gen_search_index.py"),
    ("sitemap",          "gen_sitemap.py"),
]
QUICK_SUBSET = {"foundations", "components-a", "components-b", "components-new", "search-index", "sitemap"}


def run(name, script, env_overrides=None):
    cmd = [sys.executable, str(ROOT / "scripts" / script)]
    env = {**__import__('os').environ}
    env["PYTHONIOENCODING"] = "utf-8"
    if env_overrides:
        env.update(env_overrides)
    print(f"\n=== {name} ===")
    result = subprocess.run(cmd, env=env, cwd=ROOT)
    return result.returncode == 0


def main():
    quick = "--quick" in sys.argv
    check = "--check" in sys.argv
    if check:
        # Apenas valida que generators existem
        missing = [s for _, s in GENERATORS if not (ROOT / "scripts" / s).exists()]
        if missing:
            print("FALTA:", missing)
            return 1
        print(f"OK · {len(GENERATORS)} generators encontrados")
        return 0

    targets = [(n, s) for n, s in GENERATORS if (not quick or n in QUICK_SUBSET)]
    ok = True
    for name, script in targets:
        if not run(name, script):
            print(f"!! falha em {name}")
            ok = False
            break
    if ok:
        print(f"\n✓ build completo · {len(targets)} generators")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
