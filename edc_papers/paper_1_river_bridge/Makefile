PAPER=main
OUTDIR=build

all: $(OUTDIR) pdf

$(OUTDIR):
	mkdir -p $(OUTDIR)

pdf:
	xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(OUTDIR) $(PAPER).tex
	bibtex $(OUTDIR)/$(PAPER) || true
	xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(OUTDIR) $(PAPER).tex
	xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(OUTDIR) $(PAPER).tex
	cp $(OUTDIR)/$(PAPER).pdf $(PAPER)_river_bridge_v17.49.pdf

clean:
	rm -rf $(OUTDIR) *.pdf
