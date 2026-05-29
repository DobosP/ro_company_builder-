#!/usr/bin/env python3
"""finsim CLI — run a venture financial projection from a JSON config.

Examples:
    python tools/finsim/run.py ventures/energy-storage/finsim.json
    python tools/finsim/run.py ventures/energy-storage/finsim.json --out ventures/energy-storage/finsim-report.md
    python tools/finsim/run.py tools/finsim/configs/saas-app.example.json --regime cit --csv /tmp/p.csv
"""
from __future__ import annotations

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import finsim  # noqa: E402
import report  # noqa: E402


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Run a venture financial projection (finsim).")
    p.add_argument("config", help="path to a venture JSON config")
    p.add_argument("--out", help="write a Markdown report to this path")
    p.add_argument("--csv", help="write a CSV of the projection to this path")
    p.add_argument("--regime", choices=["auto", "micro", "cit", "none"], help="override tax_regime")
    p.add_argument("--quiet", action="store_true", help="suppress the console summary")
    args = p.parse_args(argv)

    cfg = finsim.load_config(args.config)
    if args.regime:
        cfg["tax_regime"] = args.regime
    results = finsim.project(cfg)

    if not args.quiet:
        print(report.render_console(results))
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(report.render_markdown(results))
        print(f"[finsim] wrote {args.out}")
    if args.csv:
        with open(args.csv, "w", encoding="utf-8") as fh:
            fh.write(report.render_csv(results))
        print(f"[finsim] wrote {args.csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
