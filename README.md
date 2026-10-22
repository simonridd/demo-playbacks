# Demo Playbacks

A static library of captured customer journeys. Open a demo card to replay its abbreviated walkthrough without a live Genesys login.

## Available demos

- **Holcim customer journeys** — 14 slides covering a website enquiry and agent callback, then a webchat with Copilot knowledge, checklist progress, wrap-up suggestions and summary-to-quote generation, plus a labelled prerecorded AVA voice enquiry.
- Playback: `demos/holcim/index.html`
- Generated quote: `demos/holcim/riverside-quote.html`
- Exact AI-generated chat summary: `demos/holcim/holcim-chat-summary.txt`

The playback embeds its screenshots and quotation, so it also works as a downloaded HTML file. Keep the separate quotation beside it for the optional document link.

## Presenting

Use **Next/Back** or the arrow keys. The top navigation jumps between journeys. **Overview** selects a slide, **Enlarge** opens a capture at readable size, and **Notes** shows the capture context. **Play** advances every 12 seconds. Press `F` for fullscreen, `N` for notes, `O` for overview, or `P` for playback.

## Publishing

GitHub Pages serves the repository root from `main`. The `.nojekyll` file keeps the site buildless. No API credentials, SDK session tokens or live backend are required.

The redesigned Holcim player starts with an audience, project brief and route selection,
then closes each journey with retained evidence, limits and an inspection action.
Original `#slide-1` through `#slide-14` links remain valid. The catalog and each player offer **Download demo** to save one named HTML file
for sharing and offline use; the saved quotation and exact summary
remain separate downloads. Audio starts only after a play action and is labelled a simulation.

For repeat publication, build the approved private manifest and its story sidecar into scratch
space using `build_playback.py`. Merge its `catalog-entry.json` into `demos/catalog.json`
by the stable `holcim` ID, retaining other entries and the exact summary document link.
Regenerate the homepage with `build_catalog.py`, run `check_output.py`, inspect the diff
and check all routes under the repository prefix before pushing. The production README's
single-demo worked example is not a replacement catalog for this two-demo library.

Publication acceptance fixes to browser history, responsive toolbars and catalog downloads
are retained with the private DSS1-PUBLISH rebuild evidence. Apply that private source patch
when reproducing this release. Captures, the quotation, summary and both players' audio
were reused without synthesis or new live capture.

## Adding a demo

1. Add its playback and documents under `demos/<slug>/`.
2. Add a cover image under `assets/`.
3. Add metadata to `demos/catalog.json` and a matching card in `index.html`.
4. Check relative links under the GitHub Pages repository prefix.

The first demo uses a fictional Riverside project. Its quote uses the existing demo price list, and the pending technical checks remain on the document. Presenter notes distinguish live conversation output from fixed demo script context.

The voice simulation is Journey 3 / slide 14. Its 1m46s WAV is embedded and plays on request. A separate voice card opens the same recording directly. Both voices are synthesised; no live bot transfer is claimed.

The Download demo control is available on the story opening, slide header and outcomes. The saved file includes every capture, Messenger conversation, original recording and saved document. Recipients open it directly in a browser. It starts at the opening with playback stopped, has no library-folder dependency, and can export itself again.

## Commercial earthworks and logistics yard

`demos/holcim-commercial-earthworks/` follows a website enquiry through the outbound campaign and contact record to an agent callback and after-call work. It contains 23 annotated scenes, a 3m12s continuous video, and a self-contained offline player. The supplied prepared voices are aligned to the selected capture. The recording notes describe the requested training-row cleanup and caller-label correction, early checklist completion and knowledge-result review.

## Consolidated Holcim presentation

The root `index.html` is a seven-section presentation: title, introduction, the four concerns from the PowerPoint, how Genesys helps, Jamie Taylor and Emily Carter, three project scenarios plus AVA, and a closing slide mapping the demonstrations back to the four concerns. The previous library remains at `library.html`; all earlier playback URLs remain available.

Scenario 1 is always Residential Housing Extension at `demos/holcim-agent-copilot/`, using the 22 October residential take 3 (132.9 seconds, 15 annotated moments, with the simultaneous recorded phone player). Scenario 2 is Commercial Earthworks and Logistics Yard at `demos/holcim-commercial-earthworks/` (191.73 seconds). Scenario 3 Web Messenger is Council Green Corridor at `demos/holcim-council-green-corridor/` (109 seconds). Scenario 3 Audio is the separate council road recording at `demos/holcim-council-road-low-carbon/` (122.6 seconds), using the approved 22 October take 1. Both Messenger and Audio are available within Scenario 3.

The root presentation loads one annotated player at a time inside an iframe. Closing it unloads the player and stops its media. Hash links `#scenario-1`, `#scenario-2`, `#scenario-3-messenger`, `#scenario-3-audio` and `#together` support direct entry. Preserve the scenario mapping when rebuilding the legacy catalog: `build_catalog.py` must not replace the new presentation. Learning and problem statements are authored demo themes; the closing slide describes illustrated workflows without claiming measured results.

`holcim-presentation.html` is the single-file offline edition (approximately 45 MB), embedding all five playback choices, portraits, videos and logos. It does not require a server or network connection for playback. The homepage footer links to it.

## Council road resurfacing and lower-carbon materials

`demos/holcim-council-road-low-carbon/` is the 22 October council-road take 1 (about 2m03s), with 15 moments, the original recorded phone player, full workspace framing, persistent section highlights, and completed after-call work. The unrelated Motor Insurance pane is cosmetically masked; original dialogue, recognition, checklist outcomes and generated summary are retained. The hosted route and combined presentation use this same take. It includes a standalone player and clean continuous MP4.

## PowerPoint narrative and portraits

The October 19 revision uses the four concerns from slide 3 of the supplied `Holcim_Demo_Customer_Journeys_Jamie_Taylor_IPI_v2 (1).pptx`: manual lead follow-up, context across systems, time spent on post-call notes, and knowledge transfer and coaching. The former problems slide now explains Agent Copilot, campaigns and bots/AVA. The conclusion maps back to those same four concerns. Jamie and Emily’s fictional portraits are the original embedded images from slides 6 and 4, retained as `assets/jamie-taylor.jpeg` and `assets/emily-carter.png`. No Daniel character is introduced in the new narrative. The AVA voice illustration retains its original recording and labels.

A fourth demo choice opens the user-selected AVA voice playback at `demos/holcim-voice/#slide-1` without replacing the three project scenarios or their existing URLs. The standalone presentation includes that AVA playback and both portrait files.

## IPI presentation treatment

The presentation uses a predominantly white canvas with the IPI logo palette: slate `#384d5d` and mint `#63ab8f`, plus a darker green for readable accent text. The partnership label is `Holcim | IPI`. The final slide states the customer and adviser outcomes directly, without references to individual scenarios. Source recordings and customer logos retain their existing appearance.

The introduction gives a short overview of Genesys across the contact centre: inbound voice and digital service, outbound campaigns, virtual assistants and Agent Copilot. Character and scenario details appear later in the presentation.

## Playback controls and AVA acknowledgement

Space toggles audio/video playback and Left/Right move one scene, including when a playback button or the presentation toolbar has focus. Text fields and native form controls keep their own keyboard behavior. The consolidated file exposes the same controls offline.

The AVA recording now uses Jamie’s revised acknowledgement, “Yes, that's right. Thanks for your help.” Only ALEX-07 was regenerated with the existing approved voice configuration. The other audio samples are unchanged. The transcript, conversation timing, confirmation context and embedded WAV checksum match the revised 105.675-second recording. The original AVA voice and full customer-journey pages share the updated recording. The requested caption clause about proving a live transfer has been removed.

The fourth learning point is now “Consistent delivery and cross-selling,” following the owner’s revision. Demo cards have aligned action rows, no durations or update note, and two equal-width Messenger/Audio buttons for Scenario 3.
