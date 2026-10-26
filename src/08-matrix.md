# What becomes true {#matrix .closing .stay-dark}

<p class="kicker">A tick is yes, and it stays yes. A cross is no. v1 is short, v2 is middle, and v3 to v5 are long.</p>

<table class="matrix">
<thead>
<tr><th></th><th>Today</th><th>v1</th><th>v2</th><th>v3</th><th>v4</th><th>v5</th></tr>
</thead>
<tbody>
<tr><td>An engineer opens ordinary logs the day they join, without asking</td><td class="no">✗</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td></tr>
<tr><td>Their lead grants that by adding them to one role</td><td class="no">✗</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td></tr>
<tr><td>Three people in the domain can approve a sensitive read</td><td class="no">✗</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td></tr>
<tr><td>A service with no tier cannot ship</td><td class="no">✗</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td></tr>
<tr><td>On a service that has moved, sensitive fields stay absent</td><td class="no">✗</td><td class="no">✗</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td></tr>
<tr><td>A log line on that service has an expiry a hold can extend</td><td class="no">✗</td><td class="no">✗</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td></tr>
<tr><td>We can name the fields a read touched, and we do not keep the rows</td><td class="no">✗</td><td class="no">✗</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td></tr>
<tr><td>Sensitive access stays closed until a window opens</td><td class="no">✗</td><td class="no">✗</td><td class="no">✗</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td></tr>
<tr><td>A gateway command is on the record, typed apart from the output</td><td class="no">✗</td><td class="no">✗</td><td class="no">✗</td><td class="no">✗</td><td class="yes">✓</td><td class="yes">✓</td></tr>
<tr><td>No direct path remains</td><td class="no">✗</td><td class="no">✗</td><td class="no">✗</td><td class="no">✗</td><td class="no">✗</td><td class="yes">✓</td></tr>
</tbody>
</table>

::: notes
Two ways of starting were set down, because each one blocks the first benefit. Labelling every log line, in all thirty services, before anyone new can read anything, waits on a shared logger and on every sensitivity kind. The first engineer stays blocked until that work is finished. Doing that fully in one service makes that service correct, and the company does not feel the change.

Version 1 is the third path. Vlad joins the bridge team on Monday. His lead adds him to one role, bridge engineer. That role may read tier 2 and tier 3. He opens the ordinary logs the same day. He does not ask Anton. Point at the first two rows. The third row is the same Monday: three people in his domain can approve a sensitive read. Today that pool is two. The fourth row is the gate. A service with no tier cannot ship.

poa-bridge-manager is the compromise, said out loud. One line logs a key-lifecycle event, and the rest is ordinary. In version 1 the service is labelled as a whole, so the ordinary part stays closed, or that line leaks. The fifth row stays a cross until version 2, because the question is a service that has moved. Once this service has moved, Vlad reads the ordinary lines and the sensitive fields are absent. A service that is fine with the version 1 label stays there. Done, for version 2, is that service. The sixth row ticks with it. A line on that service has an expiry a hold can extend.

The seventh row stays a cross in version 1. Version 1 records the query, and it does not name the fields. From version 2 we can name which fields sat above the reader's role. A tick on that row still does not mean we keep the values.

Sensitive access stays open for leads through version 2, so the eighth row is a cross until version 3. On a Tuesday afternoon Anton opens a window, confirms with a hardware key, and a second person is told at that moment. The grant expires on its own. The key is a stepping stone. A touch proves a person was there. It does not prove what they approved. A standard key has no screen, so on a laptop that is already compromised the program that talks to the key can lie about the payload. Version 3 can run beside version 2.

A command on a server is unrecorded through version 3. Version 4 puts a gateway in front and leaves the direct path open, so the ninth row ticks and the tenth stays a cross. People use the gateway. When it fails, they use the path they already have. The direct path comes down only after the gateway has been the normal way for a long stretch. The friction is the comfort. The person on call goes through a door so a stolen laptop is no longer enough.

Version 5 is that same door, once it is the only one. The tenth row ticks because there is nowhere else to run a command. A refund that never shows the seed, and one confidential trace for one hour, are not on this table. Version 5 makes them possible. Building them is not part of version 5. Leave the table up through this. Take it down before the close.

**More:**

Down is how to read a cell, then the two rejected paths with Vlad and poa-bridge-manager, then the key cut and the parallel door. Do not mention agents while this slide is up.
:::

## Review · the row says bastion {#matrix--review .closing .review .stay-dark}

<p class="kicker">Not for the room. 22 Oct. Remove before the pitch.</p>

- **Heard.** The word on the door is bastion server. Break-glass is how the direct path lives while it is being measured down to zero.
- **Your words.** The ninth row is "A gateway command is on the record, typed apart from the output." A later down says gateway. The rest of the ten rows match the source. Version 1 stays a cross on naming the fields. The refund and the one-hour trace stay off the grid.
- **Suggested row.** "A bastion command is on the record, typed apart from the output." Spoken, on that row: the direct path is still open, a session on it is not recorded, and that path is measured, break-glass first, until people are comfortable.
- Leave the table up through version 5. Take it down before the close. That part of the telling stays.

::: notes
Review slide for the 22 Oct notes. Skip it in the room.
:::

## How to read a cell {#matrix--how-to-read .closing .stay-dark}

<p class="depth">A little more</p>

- A tick means the question is yes, and it stays yes in later columns. A cross means that question is not yet true.
- The limit is in the question. A service that has moved. The fields, and not the rows. A command that went through the gateway, typed apart from the output.
- Version 1 records the query. The fields row stays a cross there. A tick from version 2 names the fields. It does not mean the values were kept.
- A refund that never shows the seed, and one confidential trace, are not rows. Version 5 makes them possible. Building either one is not part of version 5.

::: notes
A tick means yes, and it stays yes. A cross means not yet. The limit sits in the question: a service that has moved, the fields and not the rows, a command that went through the gateway. Version 1 records the query, so the fields row stays a cross until version 2, and a tick there still does not keep the values. The refund and the one trace are spoken with version 5. They are not on the grid.
:::

## Why version 1 is the third path {#matrix--third-path .closing .stay-dark}

<p class="depth mid">More</p>

- Labelling every line, in all thirty services, before anyone new can read. The first engineer stays blocked until a shared logger and every sensitivity kind exist.
- Doing that fully in one service. That service becomes correct. The other services stay as they are, so a second team still has no role to join.
- Version 1 is roles on one tier per service. The roles survive into version 2. They are not rebuilt when the label moves from the service onto the line.
- Vlad joins the bridge team on Monday. His lead adds him to bridge engineer once. He reads tier 2 and tier 3 the same day. poa-bridge-manager stays labelled as a whole: one key-lifecycle line, and the rest ordinary. Either the ordinary part stays closed, or that line leaks. The moved-service row ticks when version 2 moves that one service.

::: notes
Labelling every line across every service blocks the first engineer until the logger exists. Doing that fully in one service makes that service correct and leaves everyone else where they are. Version 1 is a role on one tier per service, and poa-bridge-manager stays labelled as a whole until version 2 moves it. That is when the moved-service row ticks.
:::

## The window, then the door {#matrix--window-door .closing .stay-dark}

<p class="depth high">In detail</p>

- Tuesday afternoon. Anton does not hold sensitive access open. He opens a window, confirms with a hardware key, a second person is told, and the grant expires. Any current tier 1 holder can approve another engineer's temporary request.
- The key is a stepping stone. A touch proves a person was there. It does not prove what they approved. The key has no screen. On a laptop that is already compromised, the program that talks to the key can lie about the payload, and a second touch can be prompted as if the first failed. An unexpected second touch is a stop. A stolen laptop finds the window closed. A compromised laptop during an open window is not covered by the key alone.
- Version 4 puts a gateway in front of server commands and database queries. The direct path stays open, and a session that goes around the gateway is not recorded. People use the gateway. When it fails, they use the path they already have. The direct path comes down only after the gateway has been the normal way for a long stretch. The gateway row ticks here. The direct-path row stays a cross.
- The friction is the comfort. The person on call goes through a door so a stolen laptop is no longer enough.
- Version 5 removes that path. The direct-path row ticks because there is nowhere else to run a command. The refund and the one confidential trace stay off this table.

::: notes
Anton opens a window on Tuesday, confirms with a hardware key, and a second person is told. A touch proves he was there, and it does not prove what he approved, because the key has no screen. Version 4 records a command only when it went through the gateway, so that row ticks while the direct path is still a cross. Version 5 ticks the direct-path row because that path is gone. The refund and the one trace stay off the table.
:::

