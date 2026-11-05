Oct 19, 2026
Evan McG + Gabe
Invited Evan McGrane Gabriel Coleman
Attachments Evan McG + Gabe
Meeting records Transcript 


Summary
Presentation strategy planning and access control roadmaps were discussed, focusing on security and AI automation.

Presentation Strategy and Tools
Presenters should establish reassurance and focus on high-level principles to avoid bike-shedding. Reveal.js features and vector graphics tools were reviewed for effective delivery.

Access Control Roadmap
A multi-version access control roadmap was outlined, progressing from basic service tiers to hardware keys and bastion servers. Security vulnerabilities and confidentiality business value were also examined.

AI Agent Automation
Deterministic rule-based symbolic reasoning was proposed to enable secure AI agent automation. Structured data flow types act as essential fuel for AI agents operating within confidential compute.


Decisions
Aligned
Proposal structure emphasizing initial constraints and care The participants agreed to structure future proposals by first addressing known constraints and care points before presenting the vision and details.
Exclusion of implementation details from high-level proposals The team aligned on excluding low-level implementation details from high-level proposals to prevent unproductive bike-shedding.
Revision of hardware key security framing The participants agreed to update the security narrative to explicitly address the structural limitations and false sense of security associated with standard hardware keys.
Integration of time horizons and long-term ambition The team agreed to incorporate time scales and explicit acknowledgments of long-term ambition into the multi-version roadmap presentation.
Implementation of bastion server gateway architecture The team aligned on introducing a bastion server gateway to execute operations and manage data access securely with full auditing.
Gradual parallel rollout of bastion server Participants agreed to use a gradual, parallel rollout strategy for the bastion server to ensure backwards compatibility and prevent user blockers.


Next steps
[Evan McGrane] Analyze Security Cases: Brainstorm and document edge cases concerning hardware key authentication and security vulnerabilities to address the false sense of security fallacy.
[Evan McGrane] Update Documentation: Remove the auditing and transparency section from version 3 of the project proposal document.
[Evan McGrane] Emphasize Alignment: Add emphasis on the alignment between the security vision and current project goals during the upcoming call.
[Evan McGrane] Label Timeframes: Insert labels for short-term, midterm, and long-term milestones next to the headings for version 1, version 2, and version 4 in the document.
[Evan McGrane] Add Disclaimer: Include a formal disclaimer in the documentation stating that the content represents a vision rather than formal technical specifications.
[Evan McGrane] Create Table of Contents: Generate and add a table of contents to the beginning of the 16 page document to improve navigation.
[Evan McGrane] Formalize Document: Digest the meeting discussion and formalize the text within the one-page document to propose to the partner.
[Evan McGrane] Prepare Presentation: Record and refine the presentation pitch based on the discussed vision. Send the final version to Gabriel for feedback.
[Evan McGrane] Create Slide Deck: Develop a slide deck to accompany the presentation of the strategic vision.
[Evan McGrane] Practice Pitch: Practice the presentation by using the transcript and character profiles for Axel and Anton as prompts for an AI model. Respond to generated questions to improve the sharpness and delivery of the pitch.


Details
Presentation Structure and Reassuring Leadership: Gabriel Coleman noted that when presenting proposals to team leads or leadership, presenters should first establish reassurance by acknowledging existing constraints and ergonomics, followed by the vision and guidance, because leadership often shifts into a critical reviewer mindset (00:02:39). Evan McGrane agreed, noting that this approach helps mitigate tunnel vision and pushback from peers and leadership during reviews (00:05:19).

Avoiding Implementation Bike-Shedding and Leveraging the IKEA Effect: Gabriel Coleman emphasized that presenters should focus on high-level principles rather than specific implementation details, such as Google Cloud configurations, to prevent unproductive bike-shedding from hands-on developers (00:06:30). Furthermore, Gabriel Coleman introduced the IKEA effect, explaining that leaving space for undefined puzzle pieces and inviting peers into co-creative tasks increases their long-term attachment and care for the solution. Evan McGrane acknowledged alignment on keeping implementation discussions separate for future calls (00:07:45).

Technical Features of Reveal.js Presentations: Gabriel Coleman demonstrated the features of the Reveal.js presentation repository, highlighting its two-dimensional navigation system that allows moving left and right for main slides and up and down for backup slides (00:09:48). Additionally, Gabriel Coleman explained that an integrated JavaScript plugin can record microphone audio while presenting, chunk the audio per slide, and generate a downloadable zip file to provide a playback experience with synthesized speaker notes (00:12:33).

Presentation Delivery, Video Sharing, and Playback Speeds: Gabriel Coleman noted that presentation videos can be shared via Slack and meeting notes for asynchronous viewing, supporting playback speed adjustments up to 2x or more. Evan McGrane and Gabriel Coleman discussed listening habits, with Gabriel Coleman noting that high information density requires slower listening speeds while familiar or dense material can be consumed at 2x or higher speeds (00:15:36) (00:18:35).


Current Access Control Deficits and Roadmap Overview: Evan McGrane reviewed the current state of access control, highlighting that access is entirely informal and routed through a small handful of people without any established formalization, contrasting sharply with the proposed vision (00:22:27). Gabriel Coleman requested a structured table to help envision the multi-version breakdown of the access control implementation roadmap (00:21:32).


Version 1 Access Control Strategy and Service-Tier Simplification: Evan McGrane proposed a hybrid, time-efficient approach for Version 1 of the access control system to capture low-hanging fruit early (00:23:43). Instead of implementing a complex asynchronous graph and role-based access control across all logs immediately, Version 1 simplifies the scope by applying basic roles to services based on predefined tiers, significantly reducing engineering and testing time while delivering early tangible benefits (00:24:43).


Version 2 Access Control Strategy and Data Sensitivity Research and Development: Evan McGrane outlined Version 2 as a research and development phase focused on shifting the organizational perspective from control-flow services to data-flow sensitivity (00:27:22) (00:32:15). This version involves defining a broader role-based access control graph and data sensitivity measures, implemented horizontally through case studies like Click Manager without disrupting ongoing workflows (00:28:37).


Version 3 Defense-in-Depth and Hardware Key Implementation: Evan McGrane described Version 3 as introducing hardware keys (YubiKeys) for leadership personnel and requiring approval grants as a low-effort defense-in-depth measure (00:33:19). This mechanism ensures that if a leader's laptop is compromised, hackers cannot access everything immediately or are limited by time-outs (00:34:33).


Security Vulnerabilities and Psychological Risks of Hardware Keys: Gabriel Coleman raised critical structural security concerns regarding hardware keys, pointing out that YubiKeys lack an independent display to show what is actually being approved, making them vulnerable to binary interception malware on compromised computers (00:35:50) (00:39:20). Gabriel Coleman warned that relying solely on hardware keys creates a false sense of security that lowers user guardrails, suggesting mitigations such as secondary display devices or peer monitoring and rate-limiting (00:37:02).

Framing Long-Term Visions and Time Scales: Gabriel Coleman suggested that far-fetched long-term visions should be introduced with clear acknowledgments of their ambition and mapped explicitly onto short-term, medium-term, and long-term time scales (00:50:36). Evan McGrane agreed that this framing prevents listener skepticism and reduces the bias that ambitious targets are unattainable (00:52:15).

Version 4 Bastion Servers and Military-Grade Access Control: Evan McGrane introduced Version 4, which involves implementing a gateway or Bastion server to eliminate direct production data viewing, establishing a military-grade access control and operational security model (00:54:16) (00:57:52). Gabriel Coleman noted that this aligns with high-level organizational transformations and internal standards (00:56:01).

Business Justification and Market Differentiation for Confidentiality: Gabriel Coleman argued that Diffuse uses confidentiality as a market differentiator to attract customers seeking privacy, and raising internal security standards to military-grade access control is necessary to stay ahead of competitors attempting to catch up (00:56:01) (00:59:15). Evan McGrane noted the importance of anticipating leadership scrutiny regarding business value and revenue generation (00:57:52).

Vision and Competitive Edge for Confidential Intents: Evan McGrane and Gabriel Coleman discussed aligning the proposed data handling vision with the "confidential intents" narrative to mitigate security risks like sensitive data leaks and public relations crises (01:00:30). Gabriel Coleman argued that solving hard technical problems provides a competitive edge that leaves almost no competitors worldwide except Google, enabling them to capture more market share (01:01:45).

Communicating Confidentiality and Predicate Analysis: Gabriel Coleman proposed explaining the system through predicate analysis—where users can check data results or eligibility without exposing raw data—using a liquor store analogy where users prove eligible age instead of revealing full personal credentials (01:03:51). Gabriel Coleman and Evan McGrane noted that this approach supports hard security because data hidden from users is also hidden from hackers infiltrating computer systems (01:06:17).

Gateway and Bastion Server Architecture: Evan McGrane outlined Version 4 of the system, introducing a gateway or bastion server runtime where all operations and procedures for data handling can be implemented (01:06:17). Evan McGrane explained that this enables complete auditing and tracking of commands, helping resolve security incidents by verifying exactly who ran specific commands, such as checking if Axel was active on their laptop (01:07:53).

Gradual Implementation and Backwards Compatibility: Evan McGrane and Gabriel Coleman agreed that the transition to the bastion server should be done in parallel with existing systems, ensuring backwards compatibility and a gradual rollout where normal access can be phased out only after 100% stable usage of the bastion server (01:09:50). Evan McGrane noted that Version 5 will result in an independently horizontally scaling, role-based access management system with audited data flows across Near Intents (01:11:00).

Non-Negotiable Requirements for Crypto Cards and Payments: Evan McGrane asserted that the confidential data architecture is a non-negotiable requirement for physical crypto cards and Near payments to protect user data and comply with increasingly strict legal and compliance standards (01:12:14). Gabriel Coleman added that physical products attract a different user group with heightened privacy expectations (01:13:35).

Tooling for Visual Presentations and Vector Graphics: Gabriel Coleman recommended using Recraft (specifically Recraft 4.1 Pro for 25 cents or standard for 4 cents via applicate.com using a GitHub login and API key) to generate sharp SVG vector drawings for slides rather than low-quality raster images, which can then be edited using Inkscape (01:16:37). Evan McGrane agreed to evaluate these tools and consider incorporating visual diagrams or tables into the presentation (01:15:40) (01:18:27).

Refining Presentation Structure and Disclaimers: Evan McGrane and Gabriel Coleman planned to update the documentation by adding clear disclaimers stating the project is a long-term vision broken into parallel steps rather than technical documentation for an overnight change (01:18:27). Evan McGrane noted they will add short-, mid-, and long-term tags to headings (V1, V2, V3) and include a table of contents and page numbers (01:19:37).

Operational Friction and Psychological Comfort: Gabriel Coleman shared their philosophy that security and reliability should focus on environmental design rather than restrictive friction, reducing human stress, tunnel vision, and blind spots to decrease bugs caused by human error (01:21:43). Gabriel Coleman noted that while the bastion server introduces operational friction, it provides immense psychological comfort by protecting operators from hack vulnerabilities (01:23:01).

AI Factories and Confidential AI Inference: Gabriel Coleman introduced the strategic accelerator of AI software factories, proposing that the developed security foundations are vital for managing AI agents that perform automated debugging and release engineering using confidential AI inference without exposing data to external providers like Anthropic or OpenAI (01:24:10). Evan McGrane recognized that this provides a safe environment for operators to use AI agents during production emergencies (01:25:21).

Rule-Based Symbolic Reasoning versus Statistical Inference: Gabriel Coleman contrasted statistical inference models (like Claude's auto-approve) with the proposed deterministic, rule-based symbolic reasoning system over data flow types (01:27:53). Gabriel Coleman explained that this allows defining data sensitivity granularities (such as aggregate level 5 or higher) so AI agents can operate safely on autopilot while high-sensitivity actions are automatically rejected or routed to humans (01:29:16).

Strategic Mic Drop for CTO Axel: Gabriel Coleman suggested positioning the AI agent automation argument as the final "mic drop" at the end of the presentation to CTO Axel, highlighting that systems built for human operators will scale exponentially in value for AI agents in future software creation (01:30:28). Evan McGrane and Gabriel Coleman agreed that running agents within confidential compute allows them to investigate issues and return verified aggregates of level 5 sensitivity or lower without exposing raw data (01:33:02).

Data Sensitivity Annotation and Agent Fuel: Evan McGrane and Gabriel Coleman discussed how building a complex data flow tree through source code sensitivity labeling allows AI agents to reason effectively using structured rules and constraints (01:35:35). Gabriel Coleman emphasized that this structured data acts as essential fuel for AI agents as organizations grow (01:36:30).

Strategic Pivot from Product-Market Fit to Technical Debt: Gabriel Coleman formulated a key opening argument for the vision: at the current curve past product-market fit and growth, the organization cannot afford to accumulate technical debt, making a long-term strategic compass essential. Evan McGrane agreed to use this point as the impactful opener for the presentation (01:38:37).

Stakeholder Psychology for Presentation Delivery: Evan McGrane and Gabriel Coleman analyzed key stakeholders, noting that Axel requires a structured progression from vision to strategy to tactics, while Anton needs reassurance that the long-term vision is chunked into manageable steps that will not disrupt ongoing operations (01:42:59). Evan McGrane planned to practice concise presentation delivery and test recordings with peers or AI tools to refine their messaging (01:42:03) (01:44:56).


You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes
How is the quality of these specific notes? Take a short survey to let us know your feedback, including how helpful the notes were for your needs.
