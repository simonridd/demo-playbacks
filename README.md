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

## Adding a demo

1. Add its playback and documents under `demos/<slug>/`.
2. Add a cover image under `assets/`.
3. Add metadata to `demos/catalog.json` and a matching card in `index.html`.
4. Check relative links under the GitHub Pages repository prefix.

The first demo uses a fictional Riverside project. Its quote uses the existing demo price list, and the pending technical checks remain on the document. Presenter notes distinguish live conversation output from fixed demo script context.

The voice simulation is Journey 3 / slide 14. Its 1m47s WAV is embedded and plays on request. A separate voice card opens the same recording directly. Both voices are synthesised; no live bot transfer is claimed.
