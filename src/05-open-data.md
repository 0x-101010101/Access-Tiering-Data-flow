# Today, sensitive data is already in the open {#open-data .case .stay-dark}

<p class="kicker">Where we are.</p>

<div class="cards band">
<div class="card">
<h3>A confidential swap</h3>
<p>Open the service and see every user, or the partner gets no answer. Both legs exist together only in our logs.</p>
</div>
<div class="card">
<h3>A stuck deposit</h3>
<p>The pull request prints the seed. A person derives the key by hand.</p>
</div>
<div class="card">
<h3>A lead laptop</h3>
<p>The attacker needs no second break-in. The whole project, no limit, no record.</p>
</div>
<div class="card">
<h3>No view of the data</h3>
<p>We see services. "Confidential" is the only label. Nothing says how sensitive a piece of data is.</p>
</div>
</div>

::: notes
A partner's confidential swap fails. To explain why, someone opens the service and can see every user's data. The alternative is that the partner gets no answer. A stuck deposit is refunded by a pull request that prints the seed, and a person derives the private key by hand. A lead's laptop is hacked and the attacker has the whole project, with no limit and no record. We have no view of the data flowing through Intents. We see services.

**More:**

The laptop is the public claim. An internal incident becomes "Intents is not confidential" because we cannot say what was taken or who to warn. Do not mention agents. That line is the last slide.
:::

## Review · the line he asked to rethink {#open-data--review .case .review .stay-dark}

<p class="kicker">Not for the room. 22 Oct. Remove before the pitch.</p>

- **Heard.** "It's a lie that it's confidential" is too strong. It holds in a strict technical sense. In the room it is also a business and a legal word, and the business objectives are still to be aligned. He wrote a replacement: the capability to raise confidentiality as far as the business wants, a level up when that decision is made.
- **Your words.** That sentence is not in the 19 Oct transcript. The closest line on this slide is the speaker note: an incident becomes a public claim that Intents is not confidential, because we cannot say what was taken or who to warn. The cards themselves state procedures: every user, the seed, the laptop, no classification.
- **Suggested.** The four cards stay. They are procedures. The spoken line "it is a lie" comes off. If the vision needs the positive half, it is said on "Wouldn't it be nice," beside the competition line: "We can raise how confidential a read is, as far as the business wants, and move up a level when that decision is made."
- The stuck-deposit card is the refund he also marked. Add the clause in the spoken line: there is no other mechanism today. The case-study slide says the same sentence before its diagram.

::: notes
Review slide for the 22 Oct notes. Skip it in the room.
:::

## Two jobs that expose too much {#open-data--two-jobs .case .stay-dark}

<p class="depth">A little more</p>

- A failed confidential swap. The trace the partner needs is in a service that also holds every other user. There is no way to open one without the other.
- A stuck deposit. The refund logs the seed, a person reads it, and a person derives the key. A person holding a key is the weakest mechanism we have.
- Both are ordinary work. They are not break-ins. The exposure is the procedure.

::: notes
A failed confidential swap cannot be explained without opening every user's data. A stuck deposit is refunded by printing the seed and deriving the key by hand. Both are ordinary procedures, and both expose too much.
:::

## The laptop is a public claim {#open-data--laptop .case .stay-dark}

<p class="depth mid">More</p>

- A lead's laptop is compromised. The attacker has what the lead has: the project, with no limit on what is read and no record of what was read.
- Afterwards we cannot say what was taken. We cannot say which users to warn.
- That is the path from an internal incident to a public claim that Intents is not confidential. The product's promise and the laptop are the same story.

::: notes
A compromised lead laptop takes the whole project, with no record of what was read. We cannot name what was taken or who to warn. That is how an internal incident becomes a public claim that Intents is not confidential.
:::

## What we cannot see {#open-data--cannot-see .case .stay-dark}

<p class="depth high">In detail</p>

- There is no classification. "Confidential" is the only label. Legal exposure and what an attacker could do with the data are not separated. Fields that identify a person only when combined are unmarked.
- Logs are never deleted, because nothing says when they may die. Cost grows. A legal hold has nothing to attach to, because nothing carries an expiry to extend.
- We see services, not data. We cannot say what moved through Intents, or how sensitive a given piece is. Later controls have nothing to bind to.

::: notes
Sensitivity is undefined, so legal exposure and attacker capability are the same label, and logs never expire. We see services rather than data.
:::

