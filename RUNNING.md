# Running and verifying the archive
## Verify the supplied materials without training
From the repository root, run:
```bash
python tools/check_archive.py
```
This uses only Python's standard library, parses Python/notebook files and checks the supplemental-source checksums. It does not import model libraries, scrape sites, fit models or establish reproduction of published metrics.

## Set up basic analysis tools
Use a separate virtual environment and install the basic analysis dependencies:
```bash
python -m venv .venv
# Activate .venv for your operating system, then:
python -m pip install -r requirements-analysis.txt
```
This unpinned list reflects the basic source imports; it is not an exact historical environment lock and does not guarantee compatibility of optional deep-learning variants.

## Project workflow and remaining dependencies
Start with the original final-submission EE470 training/test scripts under source/ee470/470_PROJE_SON_HAL_KODLAR!!!!!!; other EE470 notebooks are separately preserved experiments. Install a mutually compatible TensorFlow/Keras environment for the archived APIs, and replace original Windows/Linux/Colab dataset and model paths. Training images and model weights must be supplied separately. Read docs/DATASET_ACCESS_AND_SPLITS.md first: only the current 500-image instructor test folder has zero exact overlap with train; the smaller named experiment folders are train subsets. CS523 report results are archived evidence; its full original training pipeline is not recovered.

## Evidence and scope
Original source archives and results are preserved. Packaging validation is separate from running the research. Missing original code, external data or hardware dependencies are documented rather than replaced with invented implementations.
