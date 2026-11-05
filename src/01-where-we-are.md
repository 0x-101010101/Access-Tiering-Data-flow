# <span class="prefix">Current state of NEAR Intents:</span> Where we are {#where-we-are .concept .light}

<p class="kicker">Why this vision.</p>

<p class="hook">Let's ground ourselves back to reality.</p>

<div class="cards">
<div class="card fragment fade-up">
<h3>Engineering velocity is not uniform</h3>
<p>Many Developers cannot see production. Every read is a request to few people, and the debt compounds with every hire, service, and partner.</p>
</div>
<div class="card fragment fade-up">
<h3>We trust people, not systems</h3>
<p>Our trust sits in a few engineers, not in our infrastructure. A robust system takes that pressure off them, and lets us rely on infra that stays rather than people who come and go.</p>
</div>
<div class="card fragment fade-up">
<h3>Organisational security risk</h3>
<p>Standing access to every project, every user, and the seed is bound to a few people's laptops. One compromised machine is the whole system.</p>
</div>
<div class="card fragment fade-up">
<h3>Confidentiality has no dial yet</h3>
<p>Nothing classifies what is sensitive, no role says who may read it, no record says who did. Those three are the dial that raises confidentiality as far as the business wants.</p>
</div>
</div>

<p class="dest">The work relies on a few people. This is the path out, and the capability that raises the bar as far as the business wants.</p>

::: notes
Let's ground ourselves back to reality. This is why the vision. One thing first: none of this is a fault of the people who hold production today. They are how it has stayed up. It is what a process with no roles produces, and the process is the subject. Four problems, four cards. Engineering velocity is not uniform. A few people move at full speed in production; everyone else waits on them. About thirty services run in a handful of projects, and two people can open them, so every read by anyone else is a request, and the engineer who shipped a change cannot watch it run. That debt compounds: every hire, service, and partner widens the surface, and access, logging, and server access are being fixed as separate projects. We trust people, not systems. Right now our trust sits in a few engineers, not in our infrastructure. Imagine a migration of confidential intents that touches services owned by three teams. A step goes wrong in production, no team can see it, each works from its own theory, and the fix is small once a lead has an hour to read the logs. Nothing about the fix needed those people, only their access. That is a lot of pressure on a few people, and people come and go. A robust system takes that pressure off them, and lets us rely on infrastructure that stays. Organisational security risk. Standing access to every project, every user, and the seed is bound to a few people's laptops, so one compromised machine is the whole system, with no scope, no expiry, and no record. And confidentiality has no dial yet. Nothing classifies what is sensitive, no role says who may read it, and no record says who did, so today there is no setting to turn. The three pieces of the model are that dial: data classification says what is sensitive, ReBAC says who may read it, and auditability proves who did. Together they are a technical capability: we can raise confidentiality, access and encryption, as far as the business objectives want, with the next level available on a switch when that decision is made. If confidentiality is the business thesis, that capability is the edge.

Then the line, both hinges. The work relies on a few people. This is the path out, and the capability that raises the bar as far as the business wants.

**More:**

Space brings the four cards in, in reading order: velocity, trust, security, the confidentiality dial. This is the whole problem section now; the four expansion slides came off 30 Oct, and their evidence lives in this script. No named person on the face; "two people" and "a handful" are structural facts. The arrow still leaves the slide. The last line is already up. Down is the reassurance: the fire stays, the old path stays, and version 1 is the small first chunk. Then what this meeting is, and what is not a commitment for this year.
:::

## Review · both halves in one breath {#where-we-are--review .concept .review .light}

<p class="kicker">Not for the room. 22 Oct. Remove before the pitch.</p>

- **Heard.** You said it will not be done this year or next year. He wants the next sentence in the same breath: it will not be fully done in a year or two, and that is why it is broken into steps that keep improving.
- **On the face now.** The line under the four cards closes on two hinges (30 Oct): a path out for people, and a bar on confidentiality we can raise as far as the business wants. The four expansion slides came off the same day; this is the whole problem section. The four cards: engineering velocity and impact is hindered (debt compounding sits under it), we trust people, not systems (30 Oct, was business continuity, then no team can own its production; the migration hypothetical is its evidence), organisational security risk (access bound to a few laptops), confidentiality has no dial yet (30 Oct, the gap named without blame, in Gabe's register from the 22 Oct note, tied to classification, ReBAC, and auditability; was "the promise cannot be proven"). No face names a person; the fault is the process. The down "Not a commitment for this year" says it will not be fully done in a year or two, and that is why it is broken into steps, each step an improvement we keep. "End of the decade" is off that bullet. The quarters on the roadmap stay the pace (30 Oct: v1 Q1 2027, v2 Q2–Q3 2027, v3 Q4 2027, v4 H1 2028, v5 Q4 2028 and beyond). Versions 3 to 5 stay a direction, not a promise.

::: notes
Review slide for the 22 Oct notes. Skip it in the room.
:::

## The fire stays {#where-we-are--the-fire .concept .light}

<p class="depth">A little more</p>

- Nothing here disturbs the work already in front of the people who hold production.
- The old path stays up. It comes down only after the new one is the path people actually use.
- Version 1 is small, on tools the account already has. The far end is years out, and fuzzy.

::: notes
After the problems, the care list. The fire in front of the people who hold production is untouched. The old path stays until the new one is what people use. Version 1 is the small first chunk. The far end is not a commitment for this year.
:::

## What this meeting is {#where-we-are--what-this-meeting-is .concept .light}

<p class="depth mid">More</p>

- A direction, held for a few years, taken beside the work already in flight.
- No weekend cut-over, and no build spec in this room.
- The far end is allowed to stay fuzzy. The first chunk is small.
- What we optimise for along the way: flexible, ergonomic, run by the teams themselves, one step at a time.

::: notes
This meeting sets a direction over years. It runs beside current work. It is not a specification and it is not a cut-over. The far end stays fuzzy, and the first chunk stays small.
:::

## Not a commitment for this year {#where-we-are--not-this-year .concept .light}

<p class="depth high">In detail</p>

- Version 1 is short. It is the first chunk, and it uses tools the account already has.
- Version 2 is the middle. It is allowed to take a while.
- It will not be fully done in a year or two. That is why it is broken into steps, and each step is an improvement we keep.
- Naming them now is how the first step points the right way. Version 1 starts in Q1 2027; nothing here lands this year.

::: notes
It will not be fully done in a year or two. That is why it is broken into steps, and each step is an improvement we keep. Versions 3 to 5 are named so the first step has a direction. They are not a promise to finish them on the quarter named.
:::

