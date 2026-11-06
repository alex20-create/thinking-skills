# Depth checklists

The questions an expert asks without being told. Use the sections that fit the task; a checklist is a pre-mortem, not a form to fill in. Adapted from the `ambition-lenses` engineering checklists by James Fincher (MIT).

## Systems

- What are the components and the contracts between them? What does each one assume about the others?
- What are the invariants, and where are they enforced?
- Failure modes: what happens on timeout, partial failure, retry, duplicate delivery, out-of-order events, clock skew, or a dependency being down?
- Is every operation that can be retried idempotent?
- Under overload, is there backpressure, or do queues grow until something dies?
- Blast radius: if this breaks, what else breaks? Can it be rolled back?
- Observability: how would anyone know it's broken before a user reports it?
- State: where does it live, who owns it, and what happens to it during a deploy or crash?
- Security boundaries: where does untrusted input enter, and where is it validated?

## Code

- Read the real code paths, call sites and tests before changing anything.
- Reproduce the bug before fixing it. Write the failing test first when you can.
- Fix at the source of the bad state, not where it finally crashes.
- Search for sibling call sites that share the same flaw.
- Keep the diff small and reversible. Change one thing at a time.
- Check the actual version of every library or API you touch.
- Handle edge cases explicitly: empty, null, huge, unicode, concurrent, negative, zero.

## Data

- Look at the raw data first: row count, schema, types, a sample of rows, nulls, duplicates.
- Check distributions, not just means: skew, long tails, outliers, bimodality.
- Know the base rate before judging any rate.
- Look for leakage, survivorship bias, selection bias and time-travel (using future information).
- Ask whether a difference is bigger than normal variation before calling it real. Use a test or an interval, not eyeballing.
- Compute every number in code and keep the query or script so it is reproducible.
- Ask what decision the analysis feeds, and lead with what bears on it.

## ML and LLM features

- Is a model the right tool, or would a rule, a lookup or a query do it better and cheaper?
- Define the evaluation before building: a labeled set, a metric, a baseline.
- Inspect real failure cases, not just aggregate scores.
- Know the cost per call, latency and failure behavior at expected volume.
- For LLM outputs: constrain the format, validate the output, and plan for refusals, hallucinations and prompt injection from untrusted input.
- Version prompts, models and datasets so results can be reproduced.

## Scale and performance

- Measure before optimizing. Profile to find the real hotspot.
- Find the binding constraint (CPU, memory, I/O, network, locks, a single-threaded section, a human approval step).
- Amdahl's law: the serial part caps the speedup.
- Little's law: items in system = arrival rate x time in system. If latency rises, queues grow.
- Ask what happens at 10x, 100x and 1000x: users, rows, requests per second, cost per month.
- Expect power laws: a few keys, users or endpoints carry most of the traffic.
- Know the complexity of the hot path. An O(n^2) loop is fine at n=100 and an outage at n=1,000,000.
- Cost is a scaling dimension too. Estimate the bill at target scale.

## Self-check before reporting done

- Did I verify against reality (run, query, read), or am I reporting what I believe?
- Did I compute the numbers, or estimate them?
- Did I check current docs and versions for anything that changes over time?
- Did I re-read the files I edited, rather than relying on memory of them?
- Is my stated confidence matched to my evidence?
