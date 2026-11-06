---
name: skill-improver
description: Improve an existing Claude Code skill by testing it the way it will actually run - a clean subagent with no conversation context dry-runs it, reports every doubt and contradiction, and a portability pass splits generic doctrine from machine-specific setup. Use it whenever the user wants to improve, harden, debug, test or make portable a skill that already exists - "improve this skill", "dry-run the skill", "test it with a fresh agent", "make it installable for others", "mejora esta skill", "haz un dry-run", "hazla portable", "/skill-improver" - even when they only say the skill "didn't do what I expected". Do not use it to create a new skill from scratch; hand that to an installed creator skill (skill-creator or similar).
allowed-tools: Read, Glob, Grep, Edit, Write, Bash, Task, Agent
---

# Skill Improver

The author of a skill cannot test it by reading it. Whoever wrote it fills
every gap from memory without noticing; the agent that runs it next week has
no such memory. The only honest test is the one that reproduces that
condition: a fresh subagent with no conversation context, given the skill
and a realistic scenario, reporting what the skill actually made it do and
everything it had to guess. This skill runs that test, fixes what it finds,
and finishes with a portability pass so the skill survives being installed
on someone else's machine.

The cycle is: find the editable source, dry-run with a clean subagent,
verify the report against the files, fix, make it portable, re-test.

## 1. Find the skill and its editable source

Locate the skill's files and read all of them: SKILL.md, every file under
`references/` and `scripts/`, any hook it ships. Contradictions between
those files are a primary target of the dry run, so you need them all in
view before judging the report.

Installed copies and editable sources are often different folders. On
machines where skills install by file copy rather than symlink (Windows
installs commonly do), an edit inside the installed folder dies on the next
upgrade or reinstall. Find where the source of truth lives - a repository,
a templates folder, a plugin checkout. The installed copy rarely says: an
install route often copies only the skill subfolder and leaves the README
behind. Look first in the user's own CLAUDE.md files (a local map - see
step 5 - or a workspace layout note), reading them from disk rather than
trusting the copies injected into context, which can predate an edit made
this session; then search the workspace for another copy of the skill's
SKILL.md, then ask the user. Edit the source, and
reinstall at the end by the same route the skill normally installs; that
route is a local-map fact, and the source's README usually records it. If
the only copy is the installed one, say so: the user may want to give it a
home first.

## 2. Price the dry run, then launch it

A clean-subagent dry run costs real money - on the order of a hundred
thousand tokens per pass. The current reference figure, its origin and how
to re-measure live in `references/dry-run-protocol.md`, which keeps the
only copy of the number. State the estimated cost in plain chat and get the
user's yes before launching, every time; a no leaves the dry run as the
pending step. One pass per iteration is the default; only scenarios that
exercise genuinely different paths justify parallel passes.

The protocol - scenario design, the subagent prompt template, the exact
rules and report format - is in `references/dry-run-protocol.md`. Read it
before dispatching. In short: the subagent gets the path of the editable
source - the copy the fixes will land in - a realistic scenario built from
the skill's own trigger phrases, strict read-only rules, and the
instruction to follow the skill up to its plan-or-confirmation step and
stop there, then report the plan, every tool used, every doubt, every
invention, every contradiction between the skill's files, and every name
that does not resolve.

## 3. Verify the report against the files

The subagent's report is a list of claims, not a list of facts. Before
fixing anything, check each key claim on disk: does the contradiction it
quotes actually appear in those two files? Does the file it says is missing
actually not exist? A finding that does not survive this check gets noted
as noise and dropped. This step is cheap and it is what keeps a single dry
run trustworthy.

Classify what survives:

- **Doubts** - the skill assumes knowledge the agent does not have. Fix by
  writing the fact down at the level where it is needed, or by making the
  skill discover it.
- **Inventions** - the skill forced the agent to make something up (a path,
  a name, a threshold). Same fix, higher urgency: inventions become silent
  wrong behavior.
- **Contradictions** - two of the skill's files disagree. Decide which is
  right, fix the other, and check whether the duplication itself should go:
  each fact wants to live in exactly one file.
- **Near-misses** - the skill cites a name (another skill, a command, a
  path) that does not resolve exactly on this machine. Names drift; where a
  skill must point at other tools, teach the matching pattern ("the
  installed skill whose description covers X") and keep concrete names as
  hints or examples, not as the answer.

## 4. Fix

Edit, do not append: change the line that already covers the idea rather
than adding a clarifying paragraph next to it. Put each fact at the lowest
level that still reaches the agent in time - description for triggering,
SKILL.md body for what every run needs, `references/` for what some runs
need behind a line saying when to read it.

Two checks that dry runs keep catching, worth making every time:

- **allowed-tools covers the flow.** If the skill promises a
  one-confirmation flow, its frontmatter `allowed-tools` must list every
  tool its steps use; a missing tool turns the single confirmation into a
  permission prompt per step, which breaks the skill's own contract.
- **The description carries the triggers.** Concrete user phrases, in every
  language the user actually types, belong in the description - it is the
  only part loaded before the skill triggers.

## 5. Portability pass

A skill is portable when anyone can install it and nothing in it is a lie
on their machine. Split the content in two:

- **Generic doctrine** stays in SKILL.md and `references/`: the method, the
  categories, the patterns, worked examples. Where the author's own setup
  appears as an example, label it as exactly that - a worked example, not
  the expected state.
- **Machine-specific facts** move to a **local map**: a section in the
  user's own CLAUDE.md (global or project) or claude.ai Project
  instructions, named after the skill, holding the paths, installed-tool
  names, quirks and choices of that machine. The skill reads its local map
  first; when one exists it replaces discovery, and when none exists the
  skill falls back to discovering and may offer to write the map. The map
  survives skill upgrades because it lives outside the skill's folder -
  that is the whole point on copy-installed machines. claude.ai reads no
  CLAUDE.md: there the map goes in Project instructions or the user's
  preferences, or in a `Local map for this install` section added to the
  packaged copy of SKILL.md before upload (never to the source), keeping
  only what makes sense without a disk. When the skill under repair has a
  local map, teach it to recognise that section too.

Measured numbers need a lifecycle note. A token cost or timing measured on
the author's machine is honest only with its origin attached ("measured on
X, 2026-11") and an instruction to re-measure when it matters. A bare
number in a catalogue reads as universal and goes stale invisibly.

## 6. Re-test

Run the dry run again with a fresh clean subagent - same protocol, same or
equivalent scenario, same price rule. Compare the two reports: findings
that disappeared are fixed; findings that persist mean the fix did not
land; new findings mean a fix introduced them. Report the comparison to the
user with the before and after, and stop. Whether another iteration is
worth another pass at the same price is their call, not yours.

## What this skill does not do

- Create skills from scratch - that is a creator skill's job (the installed
  skill whose description covers creating skills from scratch; for example
  skill-creator).
- Run quantitative eval suites or benchmark variance - skill-creator ships
  that machinery already.
- Edit installed copies that an upgrade will overwrite (gstack installs,
  plugin folders) - it finds the editable source instead, and says so when
  there is none.
