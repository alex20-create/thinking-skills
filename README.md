# thinking-skills

`aim-higher` and `skill-improver`: two skills for [Claude Code](https://claude.com/claude-code) that work on the work itself rather than on a domain. One raises the ambition of a task before doing it; the other improves an existing skill after it exists. Neither calls into the other, but both are meta in the same way, and this repo keeps them together for that reason.

## Which one to use

| | `aim-higher` | `skill-improver` |
|---|---|---|
| When | Before doing a task, when the user asks to raise the bar | After a skill exists, to harden, debug or make it portable |
| Looks at | The task or prompt itself: the goal beyond the goal, what an expert in the field would do, methods borrowed from elsewhere | The skill's own instructions, run cold by a subagent with no conversation context |
| Produces | A short plan and a rewritten prompt, then the task done at that higher standard, with the bigger moves offered instead of taken | A list of doubts and contradictions the dry run hit, verified fixes, and a portability pass separating generic doctrine from machine-specific setup |

## What is in the box

| Path | What it is |
|---|---|
| `aim-higher/` | The skill, its evals |
| `skill-improver/` | The skill |

## License

MIT, see [LICENSE](LICENSE).
