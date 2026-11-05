# <span class="prefix">Data Flow:</span> topological view of data flow {#data-control-flow .vision .stay-dark}

<p class="hook">Granular data control through Data classification, RBAC Access & Auditability combined</p>

| time | who | command | predicate | output |
|---|---|---|---|---|
| 03:12 | on-call | `kubectl logs near-listener --since=1h` | — | 🔒 sealed |
| 03:14 | on-call | `kubectl exec near-listener -- sh` | — | 🔒 sealed |
| 03:20 | on-call | `psql … select count(*) from deposits where …` | **passing** | 🔒 sealed |
| 09:05 | reviewer | **reveal** 03:20 output · reason: "incident review" · 1 co-signer | — | ✓ opened, recorded |

<p class="dest">The check comes back. The rows stay sealed. This reaches forward into security, risk mitigation, Legal investigations, confidential user data flows</p>

::: notes
Point at the lock, then at the result. At 03:12 and 03:14 the outputs stay sealed. At 03:20 the check comes back passing, and the rows stay sealed. At 09:05 a reviewer opens that output, with a reason and one co-signer, and the opening is recorded. Emergency access still ends by itself, someone else is told now, and a named reviewer closes it. That is a recorded exception, not a back door. This picture is version 4.
:::

## Review · point at the lock {#data-control-flow--review-sealed .vision .stay-dark .review}

<p class="kicker">Not for the room. 22 Oct. Remove before the pitch.</p>

- **Heard.** The sealed outputs look right. Put the reader's eye on the lock. The output stays locked, and a predicate column shows "passing" or "37%".
- **On the face now.** A predicate column. At 03:20 it reads passing, and the output stays 🔒 sealed. Under the table: "The check comes back. The rows stay sealed. This reaches forward into security, risk mitigation, Legal investigations, confidential user data flows."
- The 09:05 reveal stays the exception, with a reason and a co-signer. The liquor-store version of this idea stays a down under "Wouldn't it be nice."

::: notes
Review slide for the 22 Oct notes. Skip it in the room.
:::

## Review · the short slide that names ReBAC {#data-control-flow--review-rebac .vision .stay-dark .review}

<p class="kicker">Not for the room. 22 Oct. Remove before the pitch.</p>

- **Heard.** One short slide, after the listener has seen annotated data, the flow, and the DAG. "This leads us to ReBAC: reasoning about access through the relationship graph."
- **Where it sits now.** On the graph slide, before this one. The animation is the failed swap: the quote and the intent meet in the on-call trace, and the trace keeps T1. KYT returns passing. This table stays the log. Do not add a second definition here.
- Zanzibar is the reference if someone asks for the paper. It stays off the face.

::: notes
Review slide for the 22 Oct notes. Skip it in the room.
:::
