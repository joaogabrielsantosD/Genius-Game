# Project Overview

```bash
project/
├── src/           # .tdf (AHDL source) and .bdf (block diagrams) files
│   ├── top.tdf    # Top-level Entity
│   └── modules/   # Reusable modules
├── test/          # Unity tests
├── sim/           # Testbenches and simulation vectors (.vwf, .tbl)
├── constraints/   # Pinout files (.qsf, .acf)
├── docs/          # Schematics, specifications
└── README.md
```

- Can use the ```src/top.tdf``` (AHDL file) or ```tests/top_test.bdf``` (Block Diagram file) to flash the firmware.

### Top Block Diagram
[<img src="docs/top_test.png" alt="Top Block Diagram" width="500" />](docs/top_test.png)

### Top RTL connection using Blocks Diagrams
[<img src="docs/subtop_test.png" alt="Top RTL Block Diagram" width="500" />](docs/subtop_test.png)
