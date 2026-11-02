# Delivery receipt — SDD / AVA presentation publication — 2026-11-02

Status: Needs acceptance — prepared for explicitly authorized Pages publication; remaining manual checks below.
Repository / canonical branch: simonridd/demo-playbacks, main.
Working branch: codex/publish-sdd-ava-stories-20261102. Final commit is this publication PR head.
PR / merge: Bounded publication PR; merge and hosted verification recorded in the PR history.

Goal and scope: Publish both complete independent AVA stories under `previews/sdd-ava-creation/`. Hide the previous collection from home/library discovery while preserving its repository content and direct URLs. No provider mutations or new calls.

Audience artifacts:
- IPI two-story introduction with full in-place story viewing and a combined HTML download.
- Alder & Vale: eight chapters, evolving specification, twenty retained screenshots, thirteen official report datasets and the completed call playback in chapter eight.
- Second AVA Build: unchanged Harbour Borough Library standalone from the accepted source, with its genuine 3/3 evaluation and stated limitations.
- Alder & Vale call: curated Studio recreation and demonstration notification, followed by genuine retained agent-workspace footage. Correct quote shown as a labelled later capture. Both the clean MP4 and annotated player are available.

Source projects: simonridd/demo-resources PR #17 (Alder & Vale) and PR #18 (Harbour). Publication does not imply these source PRs have merged or that all native acceptance is complete.

Validation:
- Embedded story documents match the separately published documents; executable JavaScript parses; JSON nesting and script-closing escaping checked.
- No private filesystem paths, credential patterns, raw call files or provider session exports selected for publication.
- Local Chrome opens both stories; chapter-eight nested call reaches ready state 4 and plays. Closing/switching unloads the old iframe, preventing overlapping audio.
- Actual combined download contains both complete stories and the embedded call. Direct offline opening is a remaining manual check, not claimed passed.
- Home/library show only the featured stories; previous collection cards and navigation are absent.
- All 67 other pre-existing tracked files remain byte-identical. The previous library listing is additionally retained in `docs/retained-library-20261102.html` for restoration. Existing demo, workshop, Relay and historical presentation URLs remain.
- Final Alder source validation, 187 units and production build passed. Repository fixture-browser outcome is recorded in the source receipt; these tests are not claimed as hosted or carrier acceptance.

Observed browser viewport: 2560 × 1272. The viewport override did not produce a real narrow viewport, so new narrow acceptance is not claimed. Earlier standalone-source mobile verification keeps its original scope. Fullscreen and listening to the complete rendered call remain manual checks; the user approved the audition voices and accepted the transcription.

Deployment: GitHub Pages serves repository-root main. No external service or API is needed by the presentation. `publication.json` fingerprints every audience file. `tools/build-sdd-presentation.py` rebuilds from the selected curated standalone inputs; original raw recordings and private production bundles are excluded.

Rollback: Revert the bounded publication commit/PR to restore the previous discovery pages. Alternatively restore the retained library listing. All previous demo content stays in place.

Disposition: Authorized audience publication with explicit evidence boundaries; not a claim of production insurance service, carrier SMS, complete Knowledge/Copilot acceptance or broad AVA reliability.
