# severino-edu-mcp

MCP server for a Georgia Tech / education Obsidian vault (courses, course notes,
assignments), built on [vault-engine](https://github.com/joeseverino/vault-engine)
with the education schema profile. Launched with `SVMC_CONFIG` pointing at the
education vault.

```bash
uv tool install .
claude mcp add severino-edu-mcp --env SVMC_CONFIG=~/.config/severino-edu-mcp/config.toml -- severino-edu-mcp
```
