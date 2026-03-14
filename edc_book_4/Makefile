# EDC Book IV: Cluster Structure from Topological Pinning
# Makefile for build automation

.PHONY: all build release-pdf verify clean help

# Default target
all: build

# Standard build (local, no versioning)
build:
	@echo "Building main.pdf (local build)..."
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -interaction=nonstopmode main.tex
	@echo "Build complete: main.pdf"

# Release build with versioned artifact
release-pdf:
	@echo "Building versioned release artifact..."
	@chmod +x tools/build_release_pdf.sh
	./tools/build_release_pdf.sh

# Verify no ambiguous PDFs
verify:
	@chmod +x tools/verify_no_ambiguous_pdf.sh
	./tools/verify_no_ambiguous_pdf.sh

# QA scan (contamination + path leaks + undefined refs)
qa-scan:
	@echo "=== QA Scan ==="
	@echo ""
	@echo "Undefined refs:"
	@grep -c "LaTeX Warning: Reference.*undefined" main.log 2>/dev/null || echo "0"
	@echo ""
	@echo "Contamination scan (Layer A):"
	@grep -rE "tetrahed" chapters/*.tex 2>/dev/null | grep -v "%" | wc -l | xargs echo "  tetrahed hits:"
	@echo ""
	@echo "Path leak scan:"
	@pdftotext main.pdf - 2>/dev/null | grep -c "/Users/" || echo "0"
	@echo ""
	@echo "Placeholders scan:"
	@grep -rE "\[Content pending\]|\?\?" chapters/*.tex 2>/dev/null | wc -l | xargs echo "  placeholder hits:"

# Clean build artifacts
clean:
	rm -f main.pdf main.aux main.log main.out main.toc main.lof main.lot
	rm -f build_info.tex
	@echo "Cleaned build artifacts (dist/ preserved)"

# Deep clean including dist
distclean: clean
	rm -rf dist/
	@echo "Cleaned all artifacts including dist/"

# Help
help:
	@echo "EDC Book IV Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  build        - Standard local build (main.pdf)"
	@echo "  release-pdf  - Versioned release build to dist/"
	@echo "  verify       - Verify release artifacts exist"
	@echo "  qa-scan      - Run QA checks (refs, contamination, leaks)"
	@echo "  clean        - Remove build artifacts (keep dist/)"
	@echo "  distclean    - Remove all artifacts including dist/"
	@echo "  help         - Show this help"
