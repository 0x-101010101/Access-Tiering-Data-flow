# Improving production access on NEAR Intents

This repository is a collection of docs and other materials for a work stream which improves how production access, data flow, security and more works on NEAR Intents.

[`docs/`](docs/) holds the markdown, in a tree of directories named for their subject. [`presentation/`](presentation/) holds the pitch.

## Why the pitch exists

Past product-market fit we cannot keep accumulating technical debt, and stopping that needs a long-term compass. Production access still sits with a few people, so every hire, service, and partner widens the gap.

## Documents

The same proposal is written up in three documents: a short summary of the deck, a high-level spec, and the in-detail spec.

- [PowerPoint summary doc](https://docs.google.com/document/d/1408uf5Z7i0wViC1feHKkeAybmlwI35aOd-moPH_3LsI/edit?tab=t.of4xm3ncgov)
- [High level proposal spec](https://docs.google.com/document/d/1nsRUd36Z9Fr6lJzCpT2wGKe9P-lbA8TaCSgIMaFmTqo/edit?tab=t.0)
- [In-details proposal spec](https://docs.google.com/document/d/1UT0EgvUuLHaF_aiPpMdGyOOcgZdqZV75nlHrkzGDyIw/edit?tab=t.0#heading=h.c9fvdfgmya1p)

## YouTube recording

The PowerPoint is recorded on YouTube: [YouTube recording](https://youtu.be/WVJ1W1VxKyY). It is long, so play it at 2× or 3×.

## Clone and open on a Mac

```sh
git clone https://github.com/0x-101010101/ReBac-Presentation.git
cd ReBac-Presentation
open presentation/deck/standalone.html
```

`open` hands the file to the default browser. Nothing else needs installing. To rebuild the deck after editing slides, run `make` inside `presentation/`.
