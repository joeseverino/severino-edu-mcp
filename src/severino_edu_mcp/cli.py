"""The argparse CLI surface — the shell face of the same brain as the MCP.

``severino-edu-mcp`` with no subcommand serves MCP over stdio (the registered
Claude Code server); subcommands run one governed service call and print JSON.
CLI never calls MCP; both faces compose the same governance context.
"""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="severino-edu-mcp",
        description=(
            "Education vault MCP server; subcommands expose governed reads "
            "for build-time consumers."
        ),
    )
    sub = parser.add_subparsers(dest="command")

    export = sub.add_parser(
        "export",
        help=(
            "Emit the education dataset (institutions + courses with their "
            "`## Site` bullets) as JSON."
        ),
    )
    export.add_argument("--pretty", action="store_true", help="Pretty-print the JSON.")

    return parser
