# Access Tiering & Data Flow

A reveal.js pitch for production access on NEAR Intents. The argument is that past product-market fit the company cannot keep accumulating technical debt, and that stopping requires a long-term compass: who may read production data, how sensitive that data is, and a record of the privileged read.

The compass is one system, moved in several tracks at once.

- **ReBAC.** What a person can read is their role, applied to how sensitive the data is. The team that owns the service grants the role.
- **Data classification.** Sensitivity is declared once, where the data is produced, and it travels with the data.
- **Data auditability.** Every privileged read, grant, and command: who can see what, who saw what, and why.
- **Data flow.** A view of the data moving through Intents, not only of the service that runs it.

Access is decided by the data's sensitivity and the person's role.

## Why the pitch exists

Four costs sit under that compass.

- Engineering velocity is not uniform. Many developers cannot see production, so every read is a request to a few people, and the debt compounds with every hire, service, and partner.
- Trust sits in a few engineers, not in the infrastructure. Those people come and go. The system should stay.
- Standing access to every project, every user, and the seed is bound to a few laptops. One compromised machine is the whole system.
- Confidentiality has no dial yet. Nothing classifies what is sensitive, no role says who may read it, and no record says who did. Those three are the dial.

The work already in front of the people who hold production stays. The old path stays up until the new one is the path people actually use. The far end is years out. Version 1 is the small first chunk, on tools the account already has.

## What the room walks through

`src/ORDER` is the running order. Right arrow is the pitch. Down arrow adds detail: the first step down is light, the next is heavier. Some of those down-slides are rehearsal notes, marked "Not for the room."

1. **Open.** Two lines (the debt, and the compass), then the model: roles, classification, the record, and data flow. Four cases sit under the long-term picture: a refund and a sanctioned-liquidity release, teams that scale their own depth, a user under investigation, and an agent that can burn Intents or run inside a sealed room.
2. **Where we are.** The four costs above, then what this meeting is: a direction held for a few years, beside work already in flight. Nothing here lands in 2026.
3. **Five versions.** The quarters are a pace, not a commitment. Version 3 can start while version 2 is still moving services.
   - **v1 · Q1 2027 · Hybrid.** The service is the tier. Simple roles. Sensitivity on the line waits. A known compromise: one sensitive line on an otherwise ordinary service stays labelled with the service.
   - **v2 · Q2–Q3 2027 · ReBAC R&D.** The label moves onto the line, one service at a time.
   - **v3 · Q4 2027 · Security hardening.** Sensitive access is opened, then it expires. A hardware key confirms a person was there.
   - **v4 · Q1–Q2 2028 · Bastion.** A bastion in front of server commands. Direct access stays while the bastion is tested.
   - **v5 · Q4 2028 and beyond · No backdoor.** After that testing, the direct path comes out.
4. **The leave-behind.** Ten yes-or-no rows, Today through v5. A tick means that question is yes, and it stays yes. A cross means not yet. The limit sits in the question. A refund that never shows the seed, and one confidential trace, stay off the grid. Version 5 makes them possible. Building them is not part of version 5.
5. **Close.** The five steps are the path back to the four cards (data integrity, refunds, independent team scaling, an environment for agents). Then AI factories and confidential inference. Then one sentence: ban agents and a fire lasts a week; let people run them and the same fire is fixed in a day, with no record and no fence. If this is worth doing for people, it is worth a hundred times more for agents.

## Clone and open on a Mac

Viewing needs no extra install. reveal.js, the fonts, and the stylesheet are in the repo. The built page is `deck/standalone.html`.

```sh
git clone https://github.com/0x-101010101/ReBac-Presentation.git
cd ReBac-Presentation
open deck/standalone.html
```

`open` hands the file to the default browser. Serve it only if you want a URL. The page works from the file itself.

| Key | What it does |
| --- | --- |
| → ← | Next or previous slide in the pitch. Fragments on the slide are skipped. |
| ↓ ↑ | Detail under the current slide, light first, then heavier. |
| Space | Next fragment on the current slide (a card fading in, and so on). |
| S | Speaker notes. |
| O | Overview. |
| ? | Help. |
| Esc | Slide overview grid. |

## Rebuild after editing

Slides are markdown in `src/`. One file per slide. `src/ORDER` lists them, and a `## label` line names an overview group. macOS Python 3 is enough for the build. Pandoc is the one thing to install.

```sh
brew install pandoc
make
open deck/standalone.html
```

`make` refreshes `deck/standalone.html` and `NARRATION-TRANSCRIPT.generated.md`. It writes `build/`, which is gitignored. `make check` checks the transcript, links, and speaker notes.

Narration audio is not in this copy. Generating it (`make setup`, then `make audio`) pulls a local speech model and is described in [MAINTAINERS.md](MAINTAINERS.md). `make pdf` writes one page per slide and needs Chromium.

Third-party notices are in [NOTICE](NOTICE).
