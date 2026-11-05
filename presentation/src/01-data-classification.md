# <span class="prefix">Data Classification:</span> a T2 reader sees the log line, minus secret fields {#data-classification .vision .stay-dark}

<div class="columns"><div class="column log">

```json
{ "svc": "1click-manager",
  "tier": 2,
  "msg": "swap failed",
  "corr_id": "c-7f3a",
  "swap_type": "confidential",
  "s.amount":            { "tier": 1, "v": "…" },
  "s.ip":                { "tier": 1, "v": "…" },
  "s.recipient_address": { "tier": 1, "v": "…" },
  "s.refund_to":         { "tier": 1, "v": "…" } }
```

</div><div class="column log">

**A T2 reader sees**

```json
{ "svc": "1click-manager",
  "tier": 2,
  "msg": "swap failed",
  "corr_id": "c-7f3a",
  "swap_type": "confidential" }
```

the line and the trace, **minus** what is above their tier

</div></div>

<p class="dest">This picture is version 2. Version 1 still labels the whole service.</p>

::: notes
On the left is the same failed swap, one 1click-manager log line. The swap type, confidential, is an ordinary field. The amount, the IP, the recipient address, and the refund address are tier 1. On the right a tier 2 reader sees the line, the trace, and that it was a confidential swap, and the four tier 1 fields are gone. This picture is version 2. Version 1 still labels the whole service.
:::
