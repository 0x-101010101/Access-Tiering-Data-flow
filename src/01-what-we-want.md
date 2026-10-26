# Model Definition: Roles for people, tiers for data {#what-we-want .vision}

<p class="kicker">The vision. It will change as each stage lands.</p>

<p class="hook">Several tracks, one system.</p>

<div class="cards">
<div class="card">
<h3>Roles around the data</h3>
<p>What a person can read is their role, applied to how sensitive the data is. The team that owns the service grants the role.</p>
</div>
<div class="card">
<h3>Data classification</h3>
<p>Sensitivity is declared once, where the data is produced, and it travels with the data.</p>
</div>
<div class="card">
<h3>On the record</h3>
<p>Every privileged read, grant, and command. Who can see what, who saw what, and why.</p>
</div>
<div class="card">
<h3>Data flow</h3>
<p>A view of the data moving through Intents, not only of the service that runs it.</p>
</div>
</div>

<p class="dest">Not by who they know, and not by who is awake.</p>

::: notes
What follows is the vision. Several tracks move at once. They are one system, which is why they are in one room. It will change as each stage lands. You are invited into the direction. What a person can read is their role, applied to how sensitive the data is. The team that owns the service grants the role, and it expires on its own. Sensitivity is declared once, where the data is produced, and it travels with the data. Every privileged read, grant, and command is on the record. The view is the data moving through Intents, not only the service that runs it. Access is decided by the data's sensitivity and the person's role, not by who they know or who is awake.

**More:**

The two lines over the cards are the frame. Stay until the room can say them. The next slide is the relationship graph. The log line follows, then the compromised laptop, then the data-flow close. Down is today against one way it could feel, then a crash, then a confidential swap. Do not open agents.
:::

## Review · invite them into one system {#what-we-want--review .vision .review}

<p class="kicker">Not for the room. 22 Oct. Remove before the pitch.</p>

- **Heard.** Set the mental model at the start. This is a longer journey, several tracks in parallel, connecting into one coherent system, which is why they are shown together. Invite them into the vision. The slides are a direction and a work in progress. They evolve as each stage lands.
- **On the face now.** "The vision. It will change as each stage lands." "Several tracks, one system." The four cards are the cleaned sentences. The last line is unchanged.
- **Still spoken.** "They are one system, which is why they are in one room. You are invited into the direction."
- ReBAC is named once, on the next slide, on the failed confidential swap.

::: notes
Review slide for the 22 Oct notes. Skip it in the room.
:::

## Today, and one way it could feel {#what-we-want--could-feel .vision}

<p class="depth">A little more</p>

<div class="columns"><div class="column before">

**today**

- **Who can look.** Access sits with a few roles.
- **Who approves.** The same few roles.
- **What is recorded.** Reads and commands are missing from the record.
- **A stolen laptop.** It can expose the lead's project access.
- **Outputs.** The person running it may see them.
- **Learning.** Only tenured engineers touch production.

</div><div class="column after">

**could feel**

- **Who can look.** Tier 2 and tier 3 by role. Tier 0 and tier 1 stay time-boxed and approved.
- **Who approves.** At least three people in the domain. A colleague, live.
- **What is recorded.** A record growing toward every privileged read, grant, and command.
- **A stolen laptop.** A live grant is still a window. Version 1 records the query, not the rows.
- **Outputs.** Sealed, and revealed only when needed.
- **Learning.** A graduation path.

</div></div>

::: notes
Six rows, and the left is today. The right is one way it could feel. Who can look, who approves, what is recorded, a stolen laptop, the outputs, and how a new person learns production.
:::

## In a restricted cluster, a non-critical crash waits for someone with access {#what-we-want--listener .vision}

<p class="depth high">In detail</p>

<div class="columns"><div class="column before">

**today**

- the engineer pings a lead for logs
- one error took days; an OOM theory was going around
- the real error: one line

</div><div class="column after">

**could feel**

- the engineer could read permitted T2/T3 logs
- the error could be inspected sooner
- fewer requests to a lead

</div></div>

::: notes
A service that is not critical crashes inside a restricted cluster. The engineer asks a lead, and one line sat for days while a wrong out-of-memory theory went around. A reader role for that tier lets the engineer open the log.
:::

## A partner's confidential swap failed; partner engineering must explain why {#what-we-want--swap .vision}

<p class="depth high">In detail</p>

<div class="columns"><div class="column before">

**today**

- confidential logs may need lead access
- the engineer may lack log access
- broader access may expose unrelated swaps

</div><div class="column after">

**could feel**

- the engineer asks for one trace, by correlation id, for one hour
- an approval expires by itself
- the reveal leaves a record

</div></div>

<p class="dest">That way through is a later version.</p>

::: notes
A partner's confidential swap fails, and someone has to explain why. Today the choice is no access, or every other user's swaps. One way it could feel is one trace for one hour, approved, then gone, and the read stays on the record. That way through is a later version.
:::

