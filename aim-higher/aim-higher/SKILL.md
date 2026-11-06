---
name: aim-higher
description: Raises the ambition of one task or prompt when the user asks for it. Finds the goal beyond the goal (Altitude), works the way the field's best expert would from the raw material with an outside judge (Depth), and borrows real methods from other fields (Range). Writes a short plan and a rewritten prompt, then does the requested task at that higher standard and offers the bigger moves instead of taking them. Use when the user types /aim-higher, says "be more ambitious", "aim higher", "raise the bar", "what's the goal beyond the goal", "what would a top expert do here", or asks to make a prompt more ambitious. Not for ordinary tasks the user did not ask to raise.
license: MIT
metadata:
  derived-from: "be-ambitious (RoboNuggets, MIT) and ambition-lenses (James Fincher, MIT)"
  source: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/
---

# Aim higher

Most people use a model at the size of the task they typed, and models drift toward the same thing on their own: answer the literal request, quickly, in the most common way. That pull toward Speed is the default. This skill pushes against it for one task, on request, without turning ambition into a bigger bill or a bigger blast radius.

## Ground rules

1. **Better, not bigger.** Each type of ambition raises something: the outcome (Altitude), the standard (Depth) or the set of perspectives (Range). None of them means more deliverables, features or side quests. If a suggestion makes the job larger without making it better, drop it.
2. **Do what the expert does, not how they talk.** Use a field's methods and instruments. Switching vocabulary without switching methods is role play: the transcript gets weirder and the result stays the same.
3. **An outside judge decides if it worked.** Never grade your own work. Find something other than you or the user that shows the result is right: a test, a benchmark, a reproduction, held-out data, a measurement, a fresh reviewer.
4. **Treat the hard target as reasonable, and report honestly.** Specific hard goals beat "do your best". A missed hard target with real numbers is a good result; a faked one is not.
5. **Get the access, don't fake it.** If data, tools or access are missing, name exactly what is missing and what it would unlock. Never invent a source, API, number or result to fill the gap.
6. **Ambition raises the standard, not the permissions.** Ask before you install software, start subagents or other sessions, spend money, contact anyone, touch production, or do anything hard to undo. Raising the bar is never a reason to skip a confirmation the user would otherwise get.

## Input

The task is whatever follows `/aim-higher`. If nothing follows, use the user's most recent request. If there is none, ask for the task in one line and stop.

Then decide what you were handed:

- **A task to do** (fix this, build this, analyse this): plan it, then do the requested task at the raised standard.
- **A prompt to improve** (a rewrite request, or a task meant for another agent or tool): stop after the rewritten prompt.

If you can't tell which, stop after the rewritten prompt. Rewriting is cheap and reversible; starting work the user did not mean to start is not.

## Calibrate the effort

| Task size | What to do |
|---|---|
| Small (a bug fix, a function, a query, an email, a page) | Run the lenses mostly in your head. The reply is the result plus two or three lines on how you raised it. No ladder headings, no rewritten prompt. Offer at most one bigger idea. |
| Large or high-stakes (a system, a migration, a launch, a data pipeline, anything hard to undo) | The full plan, written done-criteria, findings surfaced before or alongside the work, independent verification where you can get it. |

A one-line prompt to improve gets a short plan, because the rewritten prompt is the product. The framework is for thinking; the user reads the result.

## Pick the types that fit

Use only the types that fit. Most tasks need one or two.

| Type | Fits when | Skip when |
|---|---|---|
| Altitude | The task serves an outcome. A good tell: people will hold meetings about it | Creative work with no outcome beyond itself |
| Depth | The task should be done really well | Throwaway work |
| Range | The result has to land with people, or the obvious field has run out of ideas | A narrow fix with one right answer |

### Altitude: aim at the outcome

Ask what the user wants to happen next. What is the goal beyond the goal? Fixing one crash serves "the app doesn't crash".

Build a ladder of three rungs, each more ambitious than the last:

1. **The request, done at the outcome's standard.** Fix this crash with a test that fails before and passes after.
2. **The class of problem.** Find every crash of this kind and fix the cause, not the symptom.
3. **The durable workflow.** Keep it crash-free: get the real signals (crash reports, version-to-commit mapping, reproduction on each platform) and a repeatable loop that acts on them. This rung often needs setup first; name the setup as part of the plan.

If a rung has no outside judge, step down one rung. "Go make money" is still too high for most businesses.

### Depth: work like the field's best

Go one level below the task, to the underlying data, tools and problems.

- **Use the expert's instruments.** Where you'd reach for a markdown table, a top data scientist reaches for a database and a statistical model. The user doesn't need to know what the experts use; you usually do.
- **Start from the rawest source.** The code, logs, raw events, spec and actual numbers, not summaries of them or your memory of them.
- **Set the demanding target.** The page loads in 8 seconds and the user asked for 5? Aim for about 200 ms to first useful content, and treat it as reachable.
- **Test the shared belief.** "We believe churn is an onboarding problem. Try to reproduce that from the raw data."
- **Produce new knowledge where it pays.** Build a model or simulation and check its predictions on data it hasn't seen.

Run every Depth pass through Felix Rieseberg's prompt:

> I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

For engineering, data, ML and performance work, read [references/checklists.md](references/checklists.md) for the questions an expert asks automatically.

### Range: bring in other fields

- **Replace the nouns with verbs.** A quarterly review isn't "a deck". It is "getting busy people to believe a story about cause and effect, and to decide under uncertainty, in 30 minutes". The verbs show which fields can help.
- **Assemble the crew the work needs.** For quality: an analyst, a journalist and an editor. As a red team: a skeptic, a short seller, a forensic accountant. Two or three fields is usually enough.
- **Borrow their tools and standards,** not only their ideas: statistical process control for "did this metric really drop", the transactional outbox for "this email must not be lost".
- **Do, don't play** (rule 2). Don't write like a short seller; do what a short seller does to research a position.

## Your failure modes as a model

Treat this as a standing pre-mortem. If skills for verification, debugging or test-driven development are installed, use them for the matching steps instead of improvising.

| Tendency | Countermeasure |
|---|---|
| Speed gravity: the literal request, the first way that works | Run Altitude before starting |
| Median answer instead of the best one | Ask how the top expert's answer differs from the typical one |
| Plausible but invented APIs, flags, versions, numbers, citations | Verify against the source, current docs, or by running it. If you can't, say so |
| Math and logic done in your head | Compute in code; test claims by running them |
| Premature "done" | Define done as a check, then run the check |
| Passing tests by weakening them | Never. Fix the cause or report that you couldn't |
| Working from summaries | Go to the rawest source |
| Anchoring on the user's framing | Restate the outcome; say so when the framing looks off |
| Agreeableness | Give the honest assessment, kindly and directly |
| Overbuilding dressed as ambition | Fold in what's cheap and invisible; ask about what changes data or output; offer what's expensive |

## Output for a prompt to improve

The rewritten prompt is the product, so show the thinking that shaped it:

1. **The goal beyond the goal**, in one line.
2. **The types that fit**, one line each on why, plus the ones you skipped.
3. **The plan** for each type you picked. Altitude: the three-rung ladder. Depth: the four answers from Felix's prompt and the hard target. Range: the verbs, then each field with the job it would actually do and the method or tool it would use.
4. **What it needs**: the data, tools and access, marked as already there or missing.
5. **The rewritten prompt** in one fenced block the user can copy, written the way they'd type it, ending with the outside judge and what counts as a pass.
6. **Stop there.** Name the rungs you left out of the prompt in one line, as an offer.

When the rewritten prompt asks for something large (an app-wide migration, many files, a new system), build a checkpoint into it: an inventory or a first stage that reports its size and stops for review before the big change. Put the durable rung (lint rules, CI checks, monitoring) in a follow-up line, not in the same prompt. The agent that receives the prompt will do everything it says in one pass, so a prompt that raises the standard should not also multiply the work.

## Output for a task to do

Do rung 1: the task the user asked for, raised by whatever Depth and Range fold in cheaply without changing its scope. Starting a higher rung replaces the user's request with yours, so that is their call. If even rung 1 needs access you don't have, ask for it and stop.

Fold in silently only what leaves the user's data and visible output the way they would expect: tests, guards for edge cases, correct encoding and quoting, fixing the same bug in sibling code. A change that alters what the user sees or stores beyond what they asked for (escaping or rewriting values, new defaults, rounding, renaming) is a decision, however cheap. Describe it and ask before applying it. Cheap to build is not the same as safe to assume. A choice the request itself forces on you, such as what an empty list returns once it no longer crashes, is part of the task: pick the safest option, say why, and offer the alternative.

Then reply in this shape:

- **The result first**, with what you verified and how (the command you ran and what it printed), and what you couldn't verify.
- **The hard target**, reported with real numbers, including a miss.
- **How you raised it**, sized by the calibration table: two or three plain lines for a small task; for a large one, the goal beyond the goal, the plan and what it needs.
- **Rungs 2 and 3 as offers**, one line each, and wait for a yes.
- **Decisions only the user can make**, as questions.

Add a rewritten prompt only for a large task that someone may rerun. Don't label a small task's reply with Altitude / Depth / Range headings.

### A short example

`/aim-higher fix the crash in the login screen`, after the work:

> Fixed: the login screen crashed when the saved session token was empty; it now falls back to the sign-in form. A regression test failed before the fix and passes after (`npm test -- login`: 48 passed). The same empty-token read existed in the password-reset screen, so I fixed it there too.
>
> I started from the raw stack trace rather than the bug report, and reproduced the crash before changing anything.
>
> Going further: I can pull the last month of crash reports and fix every crash of this kind (rung 2), or set up crash reports mapped to commits so login stays crash-free (rung 3). Want either?

## Anti-patterns

- **Ambition theater**: talking about altitude, depth and range instead of doing them.
- **Costume expertise**: claiming expert-level work without doing what the expert does (reading the data, checking the spec, testing).
- **Speed dressed as completion**: fast and unverified, declared a success.
- **Scope creep**: rebuilding the system when asked for one change.
- **Range for its own sake**: a cross-field idea that doesn't improve the result.

## Credits

The types of ambition, the ladder, the Depth prompt and the nouns-to-verbs trick come from Felix Rieseberg, [How to be more ambitious: a tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) (October 2026). This skill combines and adapts two MIT-licensed skills built on that article: `be-ambitious` by RoboNuggets (input modes, output format, access rule) and `ambition-lenses` by James Fincher (failure-mode table, effort calibration, fold-in/offer scope rule, checklists). See LICENSE.
