# Dry-run protocol

How to test a skill with a clean subagent: design the scenario, write the
dispatch prompt, read the report. Read this before every dispatch, including
the re-test - the value of the method is that every pass runs under the same
rules.

## Why a clean subagent

The subagent reproduces the skill's real operating condition: a session that
knows nothing about the skill's history, the author's intent, or this
conversation. Anything the skill fails to say, the subagent must guess - and
unlike a future user's session, this one is instructed to report every guess
instead of papering over it. You are not testing whether the task can be
done; you are testing whether the skill's text alone is enough to do it.

Run it through the subagent-dispatch tool (Task or Agent, whichever this
session has), type general-purpose. Some dispatch tools run only in the
background and notify on completion; either way, wait for the report before
touching the skill. Do not use a fork or any context-inheriting variant:
inherited context is exactly what the test must exclude. Clean is relative, though: a dispatched subagent still inherits
the user's CLAUDE.md files, which may describe the skill under test - its
local map above all. Rule 4 of the dispatch template turns that leakage
into findings instead of silent help.

## Cost, stated first

State the price before launching, every time. Reference figure: ~120k tokens
per pass, measured on the author's machine in 2026-11 against a mid-sized
skill (a SKILL.md plus one catalogue reference); a larger skill or a chattier
model moves it. On a machine's first run there is no local figure yet: use
the reference figure as the estimate and say whose it is. After each run,
note the real cost where the tool reports one and use it for the next
estimate; a figure that must outlive this session goes in this skill's own
local map (step 5 of SKILL.md), the one place later sessions look. The
user's answer to the price may be "not now" - then the dry run simply
becomes the pending step, and say so.

## Scenario design

Build one realistic scenario from the skill's own trigger phrases: the user
message that would fire the skill, plus the state the skill expects to find.
Realistic means concrete - actual-looking paths, a plausible session history
summarized in two lines, the kind of loose phrasing users actually type - not
a textbook restatement of the skill's description.

The scenario must give the subagent enough world to act in, and no more. If
the skill expects to discover installed tools, do not list them in the
scenario; discovering them is part of what is under test. If the skill needs
files that genuinely exist on this machine, point at the real ones read-only
rather than inventing fakes.

## The dispatch prompt

Point the subagent at the editable source - the copy the fixes will land
in. If the installed copy differs from it, that staleness is itself a
finding to put in front of the user alongside the plan.

Adapt this template; keep every numbered rule.

```
You are testing a skill. You have no other context - that is deliberate.

Skill under test: read every file under <absolute path to the skill's
editable source>, starting with SKILL.md.

Scenario: <the realistic scenario. Example: 'The user says: "<trigger-style
message>". The session so far: <two lines>. The workspace root is <path>.'>

Follow the skill exactly as written, under these rules:

1. READ-ONLY. You may Read, Glob, Grep, and run commands that only read
   (ls, git status, script --dry-run). You must not Write, Edit, delete,
   install, or run anything that changes state. If the skill orders a
   write, record what you would have written and move on.
2. STOP AT THE PLAN. Follow the skill up to its plan-or-confirmation step
   and stop there. If the skill has no such step, stop immediately before
   its first side effect. Do not ask the user anything; where the skill
   would ask, record the question you would have asked.
3. NO GAP-FILLING WITHOUT A RECORD. Whenever the skill assumes something
   you do not know, or you must invent a value to continue, invent the
   minimum - and record it.
4. IGNORE WHAT YOU ALREADY KNOW. Your own system context (CLAUDE.md
   files, memory) may mention the skill under test - a local map, setup
   notes. Treat those sections as absent while following the skill, and
   record each place where they would have filled a gap.

Then report, in this order:

A. THE PLAN - what you would have proposed or asked at the stopping point,
   verbatim.
B. TOOLS - every tool you used and every tool the skill told you to use,
   including ones you could not run.
C. DOUBTS - each point where the skill assumed knowledge you did not have.
   Quote the line that assumes it.
D. INVENTIONS - each value you had to make up to continue, and what you
   chose.
E. CONTRADICTIONS - each place two of the skill's files disagree, quoting
   both.
F. NEAR-MISSES - each name the skill cites (skill, command, path, file)
   that did not resolve exactly as written on this machine.

An empty section is a finding too: write "none".
```

## Reading the report

Treat every finding as a claim and verify it on disk before acting - the
subagent can misquote, misread, or hallucinate a contradiction. The
verification pass is cheap (a handful of Reads) and is what lets one dry run
stand in for many.

Signals worth weighing beyond the findings themselves:

- **The plan is the headline.** Compare the plan in section A with the plan
  the skill's files led you to expect, and show both to the user - who is
  often the author and knows what was intended. A subagent that produced a
  confident, wrong plan found a worse bug than any single doubt in
  section C.
- **Tools versus frontmatter.** Check section B against the skill's
  `allowed-tools`. Any tool the flow needs that the frontmatter omits will
  surface as a permission prompt in real use.
- **Doubts cluster.** Three doubts about the same area usually mean one
  missing paragraph, not three missing sentences.
- **Silence is information.** A section the subagent left empty where you
  expected findings may mean the scenario did not reach that part of the
  skill - consider whether the re-test needs a different scenario, and say
  so when reporting.

## The re-test

Same protocol, fresh subagent, after the fixes land. Use the same scenario
unless the first run's silences showed it missed a path worth exercising.
Compare reports finding by finding: gone, persisting, or new. Persisting
findings mean the fix did not land where the agent looks; new findings mean
a fix broke something. Both go back through verify-then-fix before any
further pass is proposed.
