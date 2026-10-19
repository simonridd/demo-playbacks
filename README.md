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

The voice simulation is Journey 3 / slide 14. Its 1m47s WAV is embedded and plays on request. A separate voice card opens the same recording directly. Both voices are synthesised; no live bot transfer is claimed.

The Download demo control is available on the story opening, slide header and outcomes. The saved file includes every capture, Messenger conversation, original recording and saved document. Recipients open it directly in a browser. It starts at the opening with playback stopped, has no library-folder dependency, and can export itself again.

## Commercial earthworks and logistics yard

`demos/holcim-commercial-earthworks/` follows a website enquiry through the outbound campaign and contact record to an agent callback and after-call work. It contains 23 annotated scenes, a 3m12s continuous video, and a self-contained offline player. The supplied prepared voices are aligned to the selected capture. The recording notes describe the requested training-row cleanup and caller-label correction, early checklist completion and knowledge-result review.

## Council road resurfacing and lower-carbon materials

`demos/holcim-council-road-low-carbon/` is a separate 1m34s Genesys agent playback with eight prepared dialogue turns, timed knowledge and checklist annotations, and after-call work. It includes a standalone offline player and continuous MP4.
