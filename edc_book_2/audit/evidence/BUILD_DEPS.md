# Build Dependencies — Book 2

**Date**: 2026-01-25
**Branch**: book2-opr-registry-v1

---

## Required Software

### LaTeX Distribution

| Dependency | Version | Purpose |
|------------|---------|---------|
| **xelatex** | TeX Live 2023+ or MacTeX | Unicode-safe compilation |
| **latexmk** | 4.76+ | Build automation |
| **biber** | 2.17+ | Bibliography processing (if needed) |

### Verification Tools

| Dependency | Version | Purpose |
|------------|---------|---------|
| **pdfinfo** | poppler-utils | Page count verification |
| **shasum** or **sha256sum** | any | Hash verification |

### Python (for scripts)

| Dependency | Version | Purpose |
|------------|---------|---------|
| **python** | 3.8+ | Audit and REPRO scripts |
| **numpy** | 1.20+ | Numerical computation |
| **matplotlib** | 3.5+ | Figure generation (optional) |
| **scipy** | 1.7+ | BVP solving (optional) |

---

## Installation

### macOS (Homebrew + MacTeX)

```bash
# Install MacTeX (full distribution)
brew install --cask mactex

# Install poppler for pdfinfo
brew install poppler

# Python dependencies
pip install numpy matplotlib scipy
```

### Ubuntu/Debian

```bash
# Install TeX Live full
sudo apt-get install texlive-full latexmk

# Install poppler for pdfinfo
sudo apt-get install poppler-utils

# Python dependencies
pip install numpy matplotlib scipy
```

### Conda Environment

```bash
conda create -n edc python=3.10 numpy matplotlib scipy
conda activate edc
# LaTeX must be installed separately
```

---

## Verification Commands

### Check LaTeX installation

```bash
xelatex --version
latexmk --version
biber --version
```

### Check verification tools

```bash
pdfinfo --version
shasum --version
```

### Check Python

```bash
python --version
python -c "import numpy; print(numpy.__version__)"
```

---

## Build Commands

### Full build

```bash
cd edc_book_2
bash tools/build.sh --verify
```

### Gates only (no build)

```bash
bash tools/gate_notation.sh
bash tools/gate_canon.sh
```

### Build with gate verification

```bash
bash tools/gate_build.sh
```

---

## Known Issues

### Issue: xelatex not found

**Solution**: Install MacTeX or TeX Live full distribution. The minimal texlive-base package is insufficient.

### Issue: Font not found

**Solution**: XeLaTeX requires system fonts. Ensure fontspec package can find Latin Modern or similar.

### Issue: pdfinfo not found

**Solution**: Install poppler-utils. Page count verification will be skipped if unavailable.

---

## CI/CD Integration

For GitHub Actions:

```yaml
- name: Install TeX Live
  uses: xu-cheng/latex-action@v2
  with:
    root_file: src/main.tex
    compiler: xelatex
    args: -interaction=nonstopmode -halt-on-error
```

---

*Generated: 2026-01-25*
