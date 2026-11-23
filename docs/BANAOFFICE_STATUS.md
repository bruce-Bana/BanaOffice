<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
-->

# BanaOffice implementation status

This document separates inherited upstream capabilities from work that must be completed before a BanaOffice release.

## Baseline

- [x] Fork the official Apache OpenOffice source repository.
- [x] Keep the upstream source history and licensing material.
- [x] Establish BanaOffice project documentation.
- [x] Add pull-request and push automation for development checks.
- [x] Add a responsive project website under `docs/` and a GitHub Pages deployment workflow.
- [x] Add dependency-free regression tests for the project website.
- [ ] Enable GitHub Pages in repository settings and verify the first hosted deployment.
- [ ] Record a reproducible upstream commit baseline and a documented update policy.
- [ ] Complete a component-by-component source, build and runtime audit.

## Product identity and application experience

- [ ] Define BanaOffice versioning, product metadata and release naming.
- [ ] Rebrand application names, About dialogs, splash screens, installer UI, shortcuts, file associations and product resources without removing required upstream attribution.
- [ ] Create a consistent BanaOffice visual identity and icon set.
- [ ] Verify that all inherited application names and upstream product references are handled correctly.
- [ ] Audit third-party notices and redistribution obligations for every shipped component.

## Applications


### BanaWriter

- [ ] Verify create, edit, save, reopen, print and export workflows.
- [ ] Verify DOCX and ODT import/export round trips.
- [ ] Add BanaOffice-specific usability improvements only with regression coverage.


### BanaSheets

- [ ] Verify formulas, recalculation, charts, sorting, filtering and large workbooks.
- [ ] Verify XLSX and ODS import/export round trips.
- [ ] Add BanaOffice-specific usability improvements only with regression coverage.


### BanaSlides

- [ ] Verify slide creation, layouts, themes, transitions, media and presenter workflows.
- [ ] Verify PPTX and ODP import/export round trips.
- [ ] Add BanaOffice-specific usability improvements only with regression coverage.

## Windows build and release engineering

- [ ] Turn the Windows/MSVC investigation into a reproducible, clean-run build recipe.
- [ ] Resolve the documented x86 UNO bridge exception-propagation failure (`getCaughtException() failed!`).
- [ ] Correct installer runtime staging: the investigation documents that VC90 CRT files are staged while the modern VC runtime/UCRT required by the build is missing from a clean-machine install.
- [ ] Validate the build on a clean Windows runner with pinned toolchain versions.
- [ ] Build and install both x64 and (if retained) x86 configurations.
- [ ] Run startup, smoke, document round-trip and UNO bridge tests.
- [ ] Package a BanaOffice-branded installer and portable archive.
- [ ] Generate checksums, software bill of materials and release notes.
- [ ] Sign release artifacts when a signing identity is available.

## CI and quality gates

- [x] Run pre-commit checks on pull requests and pushes to `trunk`.
- [ ] Add focused unit and component tests for BanaOffice-specific code.
- [ ] Add full build jobs only after their toolchains and resource requirements are reproducible.
- [ ] Add installer validation and document-format regression tests.
- [ ] Require all release gates to pass before publishing a stable release.

## Known Windows validation blockers

The `win10-msvc` investigation reports that compilation and MSI generation completed with VS2019, but explicitly states that the MSI was not installed or runtime-validated. Its only executed runtime test, `testtools/source/bridgetest`, fails with `getCaughtException() failed!`. It also documents that the installer stages obsolete VC90 runtime files instead of the modern runtime required by the compiled product. These are release blockers, not completed build validation.

## Release rule

Do not label a build as a stable BanaOffice release until the installer has been installed on a clean supported Windows environment, all three applications have launched, core document workflows have passed, and the required license/NOTICE materials are included.
