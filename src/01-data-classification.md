# <span class="prefix">Data Classification:</span> a T2 reader sees the log line, minus secret fields {#data-classification .vision .stay-dark}

<div class="columns"><div class="column log">

```json
{ "svc": "1click-manager",
  "tier": 2,
  "msg": "swap failed",
  "corr_id": "c-7f3a",
  "s.amount":  { "tier": 1, "v": "…" },
  "s.ip":      { "tier": 1, "v": "…" },
  "s.seed":    { "tier": 0, "v": "…" } }
```

</div><div class="column log">

**A T2 reader sees**

```json
{ "svc": "1click-manager",
  "tier": 2,
  "msg": "swap failed",
  "corr_id": "c-7f3a" }
```

the line and the trace, **minus** what is above their tier

</div></div>

<p class="dest">This picture is version 2. Version 1 still labels the whole service.</p>

::: notes
On the left is the same failed swap, one 1click-manager log line, with an amount, an IP, and a seed. On the right a tier 2 reader sees the line and the trace, and those three fields are gone. This picture is version 2. Version 1 still labels the whole service.
:::
