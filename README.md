# severino-edu-mcp

MCP server for a Georgia Tech / education Obsidian vault (courses, course notes,
assignments), built on [vault-engine](https://github.com/joeseverino/vault-engine)
with the education schema profile. Launched with `SVMC_CONFIG` pointing at the
education vault.

```bash
uv tool install .
claude mcp add severino-edu-mcp --env SVMC_CONFIG=~/.config/severino-edu-mcp/config.toml -- severino-edu-mcp
```

## The education dataset

The vault's publishable projection — institutions (top-level indexed folders
whose `index.md` carries `institution` + `slug`) and their courses (row facts
from frontmatter: `code`, `title`, `term`, `status`, optional `short_title`;
public bullets from each course's `## Site` section) — is one governed
service with two faces:

```bash
severino-edu-mcp export [--pretty]   # CLI face, for build-time consumers
```

and the `education_dataset` MCP tool for AI sessions. The export fails closed
on schema drift — a status outside the education profile, a course missing
`code`/`term`, an institution note without `slug` — so consumers never build
from drifted facts.

Downstream consumers read the export, never the vault:
[jseverino.com](https://github.com/joeseverino/jseverino.com)'s `sync-content`
builds the `/education/` pages from it, and
[resume-engine](https://github.com/joeseverino/resume-engine)'s
`reconcile-coursework` rewrites the resume's "Relevant Coursework" lines from
it. With no subcommand the executable serves MCP over stdio, so the Claude
Code registration above is unchanged; the CLI defaults to the same
install-standard config when `SVMC_CONFIG` is unset.
