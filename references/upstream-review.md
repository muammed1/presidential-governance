# Upstream and licensing review

Reviewed 2026-10-24 using the official sources below. These are mutable upstream URLs; recheck the actual installed revision before integrating. This package does not install or execute upstream code. Review establishes documented packaging/invocation constraints, not host compatibility.

| Source | Observed constraint / design use |
|---|---|
| [Agent Skills specification](https://agentskills.io/specification) | SKILL.md YAML name/description, matching directory name, optional resources and progressive loading; this package uses minimal metadata with MIT and a version string |
| [grill-with-docs entrypoint](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) | Explicit invocation restriction and two underlying skill dependencies; integration must inspect actual installed rules |
| [grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) | Interview/confirmation requirements, environmental exploration and subagent instruction; none supplies permission under this skill |
| [domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md) | Glossary/ADR conventions and immediate write instructions; preserve existing project layout and documentation approval gates |
| [upstream MIT license](https://github.com/mattpocock/skills/blob/main/LICENSE) | Copyright 2026 Matt Pocock; notice required if incorporating substantial source portions |

The discovery fallback, record model, templates, helper and instructions here are original implementation of the supplied design. No upstream skill source or substantial portion is bundled. The links/attribution identify optional integration sources. If future contributions incorporate third-party material, preserve the applicable copyright/license notice alongside it and record the incorporated source/revision. MIT applies to original package content only; external services and separately installed skills retain their own terms.
