# <span class="prefix">Bullet Proof Sandbox To Faciliate Agents:</span> a finding comes out, not the data {#sealed-ask .vision .stay-dark}

<div class="diagram" style="width:100%"><svg viewBox="0 0 1150 548" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="ask-r" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#F2F2F1"/></marker>
<marker id="ask-u" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#F2F2F1"/></marker>
<marker id="ask-d" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#00EC97"/></marker>
</defs>
<rect x="8" y="6" width="1134" height="400" rx="16" fill="#0B0D0D" stroke="#00EC97" stroke-width="1.6" stroke-dasharray="5 5"/>
<text x="28" y="30" font-size="14" font-weight="500" text-anchor="start" style="fill:#00EC97">ENCRYPTED SPACE  ·  reachable only through the bastion</text>
<rect x="28" y="46" width="268" height="132" rx="12" fill="#161919" stroke="#262A2A" stroke-width="1.4"/>
<text x="46" y="92" font-size="20" font-weight="500" text-anchor="start" style="fill:#F2F2F1">Agent enclave</text>
<text x="46" y="118" font-size="13" font-weight="400" text-anchor="start" style="fill:#8A9090">TEE · AI agents work directly</text>
<text x="46" y="136" font-size="13" font-weight="400" text-anchor="start" style="fill:#8A9090">on raw data</text>
<g transform="translate(250,58)" fill="none" stroke="#8A9090" stroke-width="1.6">
<rect x="3" y="8" width="12" height="9" rx="1.6"/>
<path d="M6 8 V5.6 a3 3 0 0 1 6 0 V8"/>
</g>
<rect x="312" y="86" width="156" height="44" rx="4" fill="#0A2E26"/>
<g stroke="#00EC97" stroke-width="3">
<line x1="328" y1="94" x2="328" y2="122"/>
<line x1="344" y1="94" x2="344" y2="122"/>
<line x1="360" y1="94" x2="360" y2="122"/>
<line x1="376" y1="94" x2="376" y2="122"/>
<line x1="392" y1="94" x2="392" y2="122"/>
<line x1="408" y1="94" x2="408" y2="122"/>
<line x1="424" y1="94" x2="424" y2="122"/>
<line x1="440" y1="94" x2="440" y2="122"/>
<line x1="456" y1="94" x2="456" y2="122"/>
</g>
<text x="390" y="152" font-size="13" font-weight="400" text-anchor="middle" style="fill:#00EC97">encrypted channel</text>
<rect x="484" y="46" width="268" height="132" rx="12" fill="#161919" stroke="#262A2A" stroke-width="1.4"/>
<text x="502" y="92" font-size="20" font-weight="500" text-anchor="start" style="fill:#F2F2F1">Sealed LLM</text>
<text x="502" y="118" font-size="13" font-weight="400" text-anchor="start" style="fill:#8A9090">GPU TEE · prompts and answers</text>
<text x="502" y="136" font-size="13" font-weight="400" text-anchor="start" style="fill:#8A9090">never leave in clear</text>
<g transform="translate(706,58)" fill="none" stroke="#8A9090" stroke-width="1.6">
<rect x="3" y="8" width="12" height="9" rx="1.6"/>
<path d="M6 8 V5.6 a3 3 0 0 1 6 0 V8"/>
</g>
<line x1="162" y1="208" x2="162" y2="184" stroke="#8A9090" stroke-width="1.6" marker-end="url(#ask-u)"/>
<rect x="28" y="214" width="724" height="100" rx="12" fill="#161919" stroke="#E8C24A" stroke-width="1.6"/>
<text x="48" y="258" font-size="20" font-weight="500" text-anchor="start" style="fill:#F2F2F1">Raw production data and logs</text>
<text x="48" y="286" font-size="14" font-weight="400" text-anchor="start" style="fill:#8A9090">transactions · auth logs · service logs · read-only for the agents</text>
<text x="36" y="372" font-size="13" font-weight="400" text-anchor="start" style="fill:#00EC97">This loop may repeat: ask for more data, another method, or higher confidence.</text>
<rect x="768" y="42" width="352" height="348" rx="12" fill="#161919" stroke="#262A2A" stroke-width="1.4"/>
<text x="786" y="68" font-size="14" font-weight="500" text-anchor="start" style="fill:#00EC97">ACCESS LOG  ·  hash-chained</text>
<rect x="778" y="78" width="328" height="30" rx="6" fill="#050606" stroke="#262A2A" stroke-width="1"/>
<text x="792" y="98" font-size="13" font-weight="400" text-anchor="start" style="fill:#8A9090">#0  genesis</text>
<text x="1092" y="98" font-size="13" font-weight="400" text-anchor="end" style="fill:#8A9090">0000  ←  ————</text>
<rect x="778" y="114" width="328" height="30" rx="6" fill="#050606" stroke="#262A2A" stroke-width="1"/>
<text x="792" y="134" font-size="13" font-weight="400" text-anchor="start" style="fill:#8A9090">#1  IN</text>
<text x="1092" y="134" font-size="13" font-weight="400" text-anchor="end" style="fill:#8A9090">3f9a  ←  0000</text>
<rect x="778" y="150" width="328" height="30" rx="6" fill="#050606" stroke="#262A2A" stroke-width="1"/>
<text x="792" y="170" font-size="13" font-weight="400" text-anchor="start" style="fill:#00EC97">#2  OUT low</text>
<text x="1092" y="170" font-size="13" font-weight="400" text-anchor="end" style="fill:#00EC97">8c21  ←  3f9a</text>
<rect x="778" y="186" width="328" height="30" rx="6" fill="#050606" stroke="#262A2A" stroke-width="1"/>
<text x="792" y="206" font-size="13" font-weight="400" text-anchor="start" style="fill:#8A9090">#3  IN</text>
<text x="1092" y="206" font-size="13" font-weight="400" text-anchor="end" style="fill:#8A9090">d47e  ←  8c21</text>
<rect x="778" y="222" width="328" height="30" rx="6" fill="#050606" stroke="#262A2A" stroke-width="1"/>
<text x="792" y="242" font-size="13" font-weight="400" text-anchor="start" style="fill:#00EC97">#4  OUT low</text>
<text x="1092" y="242" font-size="13" font-weight="400" text-anchor="end" style="fill:#00EC97">1b06  ←  d47e</text>
<rect x="8" y="424" width="392" height="116" rx="12" fill="#161919" stroke="#262A2A" stroke-width="1.4"/>
<text x="26" y="458" font-size="14" font-weight="500" text-anchor="start" style="fill:#F2F2F1">IN  ·  via bastion</text>
<text x="26" y="484" font-size="14" font-weight="400" text-anchor="start" style="fill:#F2F2F1">“Cross-check with a second method.”</text>
<rect x="748" y="424" width="394" height="116" rx="12" fill="#161919" stroke="#262A2A" stroke-width="1.4"/>
<text x="766" y="458" font-size="14" font-weight="500" text-anchor="start" style="fill:#00EC97">OUT  ·  sensitivity low</text>
<text x="766" y="484" font-size="14" font-weight="400" text-anchor="start" style="fill:#F2F2F1">Statistical test, one account.</text>
<text x="766" y="504" font-size="14" font-weight="400" text-anchor="start" style="fill:#F2F2F1">Confidence 91%, then 97%.</text>
<text x="766" y="524" font-size="14" font-weight="400" text-anchor="start" style="fill:#F2F2F1">No raw records.</text>
<rect x="428" y="428" width="292" height="108" rx="12" fill="#161919" stroke="#F2F2F1" stroke-width="1.8"/>
<text x="574" y="468" font-size="18" font-weight="500" text-anchor="middle" style="fill:#F2F2F1">Bastion server</text>
<text x="574" y="492" font-size="13" font-weight="400" text-anchor="middle" style="fill:#8A9090">the only door: commands in,</text>
<text x="574" y="510" font-size="13" font-weight="400" text-anchor="middle" style="fill:#8A9090">outputs out</text>
<line x1="400" y1="482" x2="424" y2="482" stroke="#F2F2F1" stroke-width="1.6" marker-end="url(#ask-r)"/>
<line x1="720" y1="482" x2="744" y2="482" stroke="#00EC97" stroke-width="1.6" marker-end="url(#ask-d)"/>
<line x1="556" y1="424" x2="556" y2="410" stroke="#F2F2F1" stroke-width="1.6" marker-end="url(#ask-u)"/>
<line x1="590" y1="410" x2="590" y2="424" stroke="#00EC97" stroke-width="1.6" marker-end="url(#ask-d)"/>
</svg></div>

::: notes
What leaves is not the data. A statistical method found one account, with a stated confidence. It holds only aggregates and a method, so it is marked low sensitivity and is safe to read. They ask again: cross-check with a second method. Confidence rises from 91 percent to 97 percent. The loop can repeat. Every exchange is another link, four so far after the genesis entry.
:::
