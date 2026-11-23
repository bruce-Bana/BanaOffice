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

# BanaOffice

**BanaOffice is an independent office-suite project based on the Apache OpenOffice source code.**

The goal is to develop a dependable, Windows-first productivity suite with three core applications:

- **BanaWriter** — word processing and document creation.
- **BanaSheets** — spreadsheets, formulas, charts and data analysis.
- **BanaSlides** — presentations and slide design.

The current repository is a source fork of Apache OpenOffice. The upstream codebase is large and contains the existing office applications and shared platform libraries. BanaOffice-specific product work is being introduced incrementally; the presence of the upstream source does not mean that all BanaOffice branding, features, installers or release validation are complete.

## Project status

| Area | Current state |
| --- | --- |
| Upstream source | Apache OpenOffice source fork on the `trunk` branch |
| Licensing | Upstream license and NOTICE files retained |
| Project identity | BanaOffice repository identity and project documentation |
| Windows build research | Windows/MSVC build investigation documented in [win10-msvc](win10-msvc/README.md) |
| Automated checks | Pre-commit workflow |
| BanaWriter / BanaSheets / BanaSlides product rebrand | In progress; not yet complete |
| Installer and signed releases | Not yet delivered |
| Runtime and compatibility certification | Not yet completed |

See [BanaOffice project status](docs/BANAOFFICE_STATUS.md) for the implementation roadmap and release gates.

## Build from source

BanaOffice inherits Apache OpenOffice's substantial native build system and third-party dependencies. A full build is not a lightweight single-command compilation and can take several hours after all platform prerequisites have been installed.

Start with the upstream [Apache OpenOffice building guide](https://wiki.openoffice.org/wiki/Documentation/Building_Guide_AOO). The repository's Windows-specific investigation and known limitations are documented in [win10-msvc/README.md](win10-msvc/README.md).

The general Unix-like build sequence from the upstream project is:

```sh
cd main
autoconf
./configure <configure_switches>
./bootstrap
. ./*.Set.sh
cd instsetoo_native
build --all
```

The exact configure options and prerequisites depend on the target operating system and toolchain. Do not treat a successful compile as proof that the generated applications install or run correctly; installation, startup, document round-trip and UNO/runtime tests are separate release gates.

## Development checks

Install the small development-tool set and run the repository checks:

```sh
python -m pip install -r requirements-dev.txt
pre-commit run --all-files
```

GitHub Actions runs these checks for pull requests and pushes to the default development branch.

## Licensing and attribution

BanaOffice is based on Apache OpenOffice. Existing source files, copyright notices, LICENSE files, NOTICE files and third-party attributions must be preserved. New and modified files must retain applicable notices. Third-party components may have additional license terms; consult the relevant component's license files before redistributing binaries.

BanaOffice is an independent project and is not endorsed by or affiliated with the Apache Software Foundation. Apache, Apache OpenOffice and their respective logos are trademarks of the Apache Software Foundation. The BanaOffice name and branding do not change the licensing or attribution obligations of the inherited source.

## Project links

- [BanaOffice website](https://bruce-bana.github.io/BanaOffice/)
- [Source repository](https://github.com/bruce-Bana/BanaOffice)
- [Apache OpenOffice upstream](https://github.com/apache/openoffice)
- [Apache License 2.0](LICENSE)
