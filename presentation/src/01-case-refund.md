# <span class="prefix">Refunds And Sanctioned Liquidity</span>Manual Refunds / AML release with one front door. {#case-refund .vision .stay-dark}

<p class="kicker">Case study one</p>

<div class="diagram dot" style="width:100%"><svg
 viewBox="0.00 0.00 794.00 221.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 217)">
<title>%3</title>
<polygon fill="white" stroke="transparent" points="-4,4 -4,-217 790,-217 790,4 -4,4"/>
<g id="clust1" class="cluster fragment" data-fragment-index="0">
<title>cluster_who</title>
<polygon fill="none" stroke="#9ca3af" stroke-dasharray="5,2" points="0,-8 0,-205 146,-205 146,-8 0,-8"/>
<text text-anchor="middle" x="73" y="-189.8" font-family="Helvetica,sans-Serif" font-size="14.00">people and agents</text>
</g>
<!-- e -->
<g id="node1" class="node fragment" data-fragment-index="0">
<title>e</title>
<path fill="#eef2ff" stroke="#6366f1" d="M98,-174C98,-174 47,-174 47,-174 41,-174 35,-168 35,-162 35,-162 35,-150 35,-150 35,-144 41,-138 47,-138 47,-138 98,-138 98,-138 104,-138 110,-144 110,-150 110,-150 110,-162 110,-162 110,-168 104,-174 98,-174"/>
<text text-anchor="middle" x="72.5" y="-152.6" font-family="Helvetica,sans-Serif" font-size="13.00">engineer</text>
</g>
<!-- gw -->
<g id="node4" class="node fragment" data-fragment-index="1">
<title>gw</title>
<path fill="#eef2ff" stroke="#2563eb" d="M459,-120C459,-120 187,-120 187,-120 181,-120 175,-114 175,-108 175,-108 175,-82 175,-82 175,-76 181,-70 187,-70 187,-70 459,-70 459,-70 465,-70 471,-76 471,-82 471,-82 471,-108 471,-108 471,-114 465,-120 459,-120"/>
<text text-anchor="middle" x="323" y="-105.6" font-family="Helvetica,sans-Serif" font-size="13.00">gateway (bastion)</text>
<text text-anchor="middle" x="323" y="-91.6" font-family="Helvetica,sans-Serif" font-size="13.00">v4: exec + DB sessions, where we choose</text>
<text text-anchor="middle" x="323" y="-77.6" font-family="Helvetica,sans-Serif" font-size="13.00">v5: the only path</text>
</g>
<!-- e&#45;&gt;gw -->
<g id="edge1" class="edge fragment" data-fragment-index="0">
<title>e&#45;&gt;gw</title>
<path fill="none" stroke="#6b7280" d="M110.17,-147C137.43,-140.31 176.14,-130.81 213.02,-121.75"/>
<polygon fill="#6b7280" stroke="#6b7280" points="213.67,-124.11 219.89,-120.07 212.5,-119.36 213.67,-124.11"/>
</g>
<!-- l -->
<g id="node2" class="node fragment" data-fragment-index="0">
<title>l</title>
<path fill="#eef2ff" stroke="#6366f1" d="M87.5,-113C87.5,-113 57.5,-113 57.5,-113 51.5,-113 45.5,-107 45.5,-101 45.5,-101 45.5,-89 45.5,-89 45.5,-83 51.5,-77 57.5,-77 57.5,-77 87.5,-77 87.5,-77 93.5,-77 99.5,-83 99.5,-89 99.5,-89 99.5,-101 99.5,-101 99.5,-107 93.5,-113 87.5,-113"/>
<text text-anchor="middle" x="72.5" y="-91.6" font-family="Helvetica,sans-Serif" font-size="13.00">lead</text>
</g>
<!-- l&#45;&gt;gw -->
<g id="edge2" class="edge fragment" data-fragment-index="0">
<title>l&#45;&gt;gw</title>
<path fill="none" stroke="#6b7280" d="M99.62,-95C117.01,-95 141.44,-95 167.77,-95"/>
<polygon fill="#6b7280" stroke="#6b7280" points="167.88,-97.45 174.88,-95 167.88,-92.55 167.88,-97.45"/>
</g>
<!-- ag -->
<g id="node3" class="node fragment" data-fragment-index="0">
<title>ag</title>
<path fill="#eef2ff" stroke="#6366f1" d="M88,-52C88,-52 57,-52 57,-52 51,-52 45,-46 45,-40 45,-40 45,-28 45,-28 45,-22 51,-16 57,-16 57,-16 88,-16 88,-16 94,-16 100,-22 100,-28 100,-28 100,-40 100,-40 100,-46 94,-52 88,-52"/>
<text text-anchor="middle" x="72.5" y="-30.6" font-family="Helvetica,sans-Serif" font-size="13.00">agent</text>
</g>
<!-- ag&#45;&gt;gw -->
<g id="edge3" class="edge fragment" data-fragment-index="0">
<title>ag&#45;&gt;gw</title>
<path fill="none" stroke="#6b7280" d="M100.09,-40.53C127.31,-47.21 171.43,-58.04 213.18,-68.29"/>
<polygon fill="#6b7280" stroke="#6b7280" points="212.74,-70.7 220.12,-69.99 213.91,-65.94 212.74,-70.7"/>
</g>
<!-- pr -->
<g id="node5" class="node fragment" data-fragment-index="2">
<title>pr</title>
<path fill="#eef2ff" stroke="#6366f1" d="M737.5,-118C737.5,-118 641.5,-118 641.5,-118 635.5,-118 629.5,-112 629.5,-106 629.5,-106 629.5,-94 629.5,-94 629.5,-88 635.5,-82 641.5,-82 641.5,-82 737.5,-82 737.5,-82 743.5,-82 749.5,-88 749.5,-94 749.5,-94 749.5,-106 749.5,-106 749.5,-112 743.5,-118 737.5,-118"/>
<text text-anchor="middle" x="689.5" y="-103.6" font-family="Helvetica,sans-Serif" font-size="13.00">production</text>
<text text-anchor="middle" x="689.5" y="-89.6" font-family="Helvetica,sans-Serif" font-size="13.00">exec · DB · logs</text>
</g>
<!-- gw&#45;&gt;pr -->
<g id="edge4" class="edge fragment" data-fragment-index="2">
<title>gw&#45;&gt;pr</title>
<path fill="none" stroke="#6b7280" d="M471.21,-97.02C523.5,-97.74 579.8,-98.51 621.99,-99.09"/>
<polygon fill="#6b7280" stroke="#6b7280" points="622.13,-101.54 629.16,-99.19 622.2,-96.64 622.13,-101.54"/>
</g>
<!-- at -->
<g id="node6" class="node fragment" data-fragment-index="3">
<title>at</title>
<path fill="#eef2ff" stroke="#059669" d="M774,-49C774,-49 605,-49 605,-49 599,-49 593,-43 593,-37 593,-37 593,-25 593,-25 593,-19 599,-13 605,-13 605,-13 774,-13 774,-13 780,-13 786,-19 786,-25 786,-25 786,-37 786,-37 786,-43 780,-49 774,-49"/>
<text text-anchor="middle" x="689.5" y="-34.6" font-family="Helvetica,sans-Serif" font-size="13.00">refund job</text>
<text text-anchor="middle" x="689.5" y="-20.6" font-family="Helvetica,sans-Serif" font-size="13.00">(attested: proves its code)</text>
</g>
<!-- gw&#45;&gt;at -->
<g id="edge5" class="edge fragment" data-fragment-index="3">
<title>gw&#45;&gt;at</title>
<path fill="none" stroke="#6b7280" d="M466.49,-69.98C506.18,-63.01 548.5,-55.58 585.44,-49.09"/>
<polygon fill="#6b7280" stroke="#6b7280" points="586.29,-51.43 592.76,-47.81 585.44,-46.61 586.29,-51.43"/>
<text text-anchor="middle" x="532" y="-68.8" font-family="Times,serif" font-size="14.00"> trigger</text>
</g>
<!-- s -->
<g id="node7" class="node fragment" data-fragment-index="3">
<title>s</title>
<path fill="#fef2f2" stroke="#dc2626" d="M363,-36.73C363,-38.53 345.07,-40 323,-40 300.93,-40 283,-38.53 283,-36.73 283,-36.73 283,-7.27 283,-7.27 283,-5.47 300.93,-4 323,-4 345.07,-4 363,-5.47 363,-7.27 363,-7.27 363,-36.73 363,-36.73"/>
<path fill="none" stroke="#dc2626" d="M363,-36.73C363,-34.92 345.07,-33.45 323,-33.45 300.93,-33.45 283,-34.92 283,-36.73"/>
<text text-anchor="middle" x="323" y="-18.6" font-family="Helvetica,sans-Serif" font-size="13.00">seed (T0)</text>
</g>
<!-- s&#45;&gt;at -->
<g id="edge6" class="edge fragment" data-fragment-index="3">
<title>s&#45;&gt;at</title>
<path fill="none" stroke="#6b7280" d="M363.15,-20.68C412.55,-19.29 500.12,-17.71 575,-21 578.55,-21.16 582.17,-21.34 585.81,-21.55"/>
<polygon fill="#6b7280" stroke="#6b7280" points="585.73,-24 592.87,-21.97 586.02,-19.1 585.73,-24"/>
<text text-anchor="middle" x="532" y="-24.8" font-family="Times,serif" font-size="14.00"> used inside</text>
</g>
</g>
</svg>
</div>

<p class="dest">The person with the role triggers the refund. The seed is used inside the job, and no one sees it. Potentially could be expanded to managed Liquidity situations for AML funds release</p>

::: notes
Today a person goes and sees the keys. There is no other way to refund. Case study one is the other way. Space brings the diagram in four parts: people and agents, then the bastion, then production, then the seed and the refund job. The arrow still leaves the slide. People and agents come through one bastion. In version 4 it records exec and database sessions where we choose. In version 5 it is the only path. The refund job is attested, so it proves its code. The seed is tier 0, used inside the job, and it never comes back to the person who triggered it.
:::

## Review · say today's refund before the door {#case-refund--review .vision .stay-dark .review}

<p class="kicker">Not for the room. 22 Oct. Remove before the pitch.</p>

- **Heard.** Nowadays a person goes and sees the keys. There is no mechanism to do the refund any other way.
- **On the face now.** The diagram is unchanged except the gateway and the refund job, which now use the same solid fill as the other boxes. Say this, then the diagram: "Today a person goes and sees the keys. There is no other way to refund." The spoken word is bastion. The box still reads "gateway (bastion)."

::: notes
Review slide for the 22 Oct notes. Skip it in the room.
:::
