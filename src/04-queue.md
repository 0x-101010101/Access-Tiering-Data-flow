# Today, the work waits on a few people {#queue .case .stay-dark}

<p class="kicker">Where we are.</p>

<div class="cards band">
<div class="card">
<h3>The queue</h3>
<p>Bug fixes, debugging, and deploys wait on the same few people.</p>
</div>
<div class="card">
<h3>Found in the outage</h3>
<p>We learn who cannot act while it is on fire. Sometimes that person is asleep.</p>
</div>
<div class="card">
<h3>The log stayed shut</h3>
<p>The people on the bug could not open it. It waited on someone who already had access.</p>
</div>
<div class="card">
<h3>One line, for days</h3>
<p>A one-line error sat for days. A wrong out-of-memory theory filled the wait.</p>
</div>
</div>

::: notes
Bug fixes, debugging, and deploys wait on the same few people. We learn who cannot act while the outage is on, sometimes because that person is asleep. The people on the bug could not open the log. It waited on someone who already had access. A one-line error sat for days, and a wrong out-of-memory theory filled the wait. Who holds the access, and who gets to learn production, is the next slide.

**More:**

The one-line error is the proof you come back to on version 1. A non-lead should be able to read it the same week.
:::

## Review · if the room hears "one person" {#queue--review .case .review .stay-dark}

<p class="kicker">Not for the room. 22 Oct. Remove before the pitch.</p>

- **Heard.** Calling out that everything relies on one person is fair. Someone may hear it as territory. Be ready to clarify. He was fine with you saying it.
- **Your words.** The face is the queue, the outage, the shut log, and the one line that sat for days. In the 19 Oct session, at 00:22:27, you said everything goes through a handful of people and there is no formalisation. Neither face names a person.
- **Suggested, if someone reacts.** "The work waits on the access, and today that access sits with a few people. Those people are how production has stayed up. The missing piece is a role someone else can hold."
- The next slide carries the line he liked, the path out. This slide stays the queue. The clarification lives here so you have it without softening the fact.

::: notes
Review slide for the 22 Oct notes. Skip it in the room.
:::

## The queue, in one incident {#queue--one-incident .case .stay-dark}

<p class="depth">A little more</p>

- A one-line production error sat for days.
- A wrong out-of-memory theory went around while it sat.
- Reading the log waited on someone who already had access. The people who could have checked it could not open it.

::: notes
One production error was a single line, and it sat for days. A wrong out-of-memory theory filled the gap. The people debugging it could not open the log themselves.
:::

## No drill before the fire {#queue--no-role .case .stay-dark}

<p class="depth mid">More</p>

- The gap shows up in the outage. Nothing finds it earlier.
- The people who could have checked the line could not open it themselves.

::: notes
The gap shows up in the outage because nothing drills it earlier. The people debugging the line could not open the log.
:::

## The same week {#queue--who-learns .case .stay-dark}

<p class="depth high">In detail</p>

- The one-line error is what version 1 has to unlock.
- A non-lead reads that log the same week, without asking the two people who can open anything.

::: notes
The one-line error is the proof for version 1. A non-lead reads that log the same week, without asking the two people who can open it.
:::

