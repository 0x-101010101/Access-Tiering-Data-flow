# <span class="prefix">Bullet Proof Sandbox To Faciliate Agents:</span> the audit: inputs visible, sealed outputs stay sealed {#sealed-audit .vision .stay-dark}

<div class="diagram" style="width:100%"><svg viewBox="0 0 1150 150" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="aud-r" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#F2F2F1"/></marker>
<marker id="aud-c" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#00EC97"/></marker>
</defs>
<rect x="8" y="16" width="392" height="118" rx="12" fill="#161919" stroke="#262A2A" stroke-width="1.4"/>
<text x="26" y="58" font-size="15" font-weight="500" text-anchor="start" style="fill:#F2F2F1">IN  ·  via bastion</text>
<text x="26" y="90" font-size="15" font-weight="400" text-anchor="start" style="fill:#F2F2F1">“Show us the access audit log.”</text>
<rect x="428" y="22" width="292" height="106" rx="12" fill="#161919" stroke="#F2F2F1" stroke-width="1.8"/>
<text x="574" y="68" font-size="18" font-weight="500" text-anchor="middle" style="fill:#F2F2F1">Bastion server</text>
<text x="574" y="96" font-size="14" font-weight="400" text-anchor="middle" style="fill:#8A9090">the only door</text>
<rect x="748" y="16" width="394" height="118" rx="12" fill="#0B0D0D" stroke="#00EC97" stroke-width="1.6" stroke-dasharray="5 5"/>
<text x="766" y="58" font-size="15" font-weight="500" text-anchor="start" style="fill:#00EC97">ENCRYPTED SPACE</text>
<text x="766" y="88" font-size="14" font-weight="400" text-anchor="start" style="fill:#F2F2F1">reads its hash-chained log,</text>
<text x="766" y="108" font-size="14" font-weight="400" text-anchor="start" style="fill:#F2F2F1">entries #0–#7</text>
<line x1="400" y1="75" x2="424" y2="75" stroke="#F2F2F1" stroke-width="1.6" marker-end="url(#aud-r)"/>
<line x1="720" y1="75" x2="744" y2="75" stroke="#00EC97" stroke-width="1.6" marker-end="url(#aud-c)"/>
</svg></div>

<p class="audit-caption">OUT · via bastion · access audit log</p>

| # | Input, visible to auditors | Output | Safe to reveal |
|---|---|---|---|
| 1 | Investigate the raw data: who caused the incident? | Test result, confidence 91% | low · aggregates only · log #2 |
| 2 | Cross-check with a second method. | Same account, confidence 97% | low · aggregates only · log #4 |
| 3 | Reveal the account behind the finding. | <span class="sealed">SEALED</span> · see log #6 | 1 account ID · 2 reviewers |
| 4 | Show us the access audit log. | this table | metadata only · log #8 |

<p class="dest">Auditors see every question, and the metadata of every answer. A sealed output shows that it happened, to whom, and its log hash.</p>

::: notes
An auditor sends one more prompt through the bastion: show us the access audit log. What comes back, through the same door, is this table. The input column is the prompts, in the clear. The early findings are low sensitivity, so the method and the confidence are on the page. The reveal is sealed, with a pointer to its log entry, what kind of data left, how much, and who received it. The last row is this table itself. Every row is a link in the hash chain, so an access cannot be added or removed after the fact.
:::
