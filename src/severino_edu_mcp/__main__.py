"""Entry point: ``python -m severino_edu_mcp`` and the console script."""

from __future__ import annotations

import os
from pathlib import Path

from .cli import build_parser

# The MCP registration passes SVMC_CONFIG explicitly; the CLI defaults to the
# install-standard config so `severino-edu-mcp export` works from any consumer
# (jseverino.com sync-content, resume-engine's coursework reconciler) without
# env plumbing. An explicit SVMC_CONFIG always wins.
_DEFAULT_CONFIG = Path("~/.config/severino-edu-mcp/config.toml")


def main() -> None:
    args = build_parser().parse_args()

    if os.environ.get("SVMC_CONFIG") is None and _DEFAULT_CONFIG.expanduser().is_file():
        os.environ["SVMC_CONFIG"] = str(_DEFAULT_CONFIG.expanduser())

    if args.command == "export":
        from vault_engine import jsonio
        from vault_engine.context import GovernanceContext
        from vault_engine.schema import EDUCATION_PROFILE

        from .education import education_dataset

        ctx = GovernanceContext.load(profile=EDUCATION_PROFILE)
        result = education_dataset(ctx.loader, ctx.profile.statuses)
        print(jsonio.dumps(result, pretty=args.pretty))
        raise SystemExit(0 if result.get("ok") else 1)

    from .server import run

    run()


if __name__ == "__main__":
    main()
