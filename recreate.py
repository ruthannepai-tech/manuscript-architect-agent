#!/usr/bin/env python
"""Recreate the Manuscript Architect specialist in a Claude Science workspace.

Run the body of this script inside the Claude Science `repl` tool (where the
`host` object is available). It reads profile.json (same directory) and calls
host.agents.create with the stored identity and full access.
"""
import json, os

def recreate(host):
    p = json.load(open(os.path.join(os.path.dirname(__file__), "profile.json")))
    rec = host.agents.create(
        p["name"],
        p["display_name"],
        p["description"],
        system_prompt=p["system_prompt"],
        # skill_names left unset -> full live catalog + all connectors
    )
    print("created:", rec["name"], "| unrestricted:", rec.get("unrestricted"))
    print("Next: create the env with the spec in profile.json['recommended_env'],")
    print("then host.agents.switch('%s') to use it." % p["name"])
    return rec

# In the repl tool, simply run:
#   exec(open("recreate.py").read()); recreate(host)
