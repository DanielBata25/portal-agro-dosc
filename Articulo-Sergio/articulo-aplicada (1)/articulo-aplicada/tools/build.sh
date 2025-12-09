#!/usr/bin/env bash
# Fail fast and surface pipeline errors
set -euo pipefail

# Add TeX Live to PATH
export PATH="/opt/texlive/bin:$PATH"

mkdir -p build

target="${1:-all}"

case "$target" in
  ieee|all)
    echo "[build] Compiling IEEE"
    latexmk -silent -file-line-error -outdir=build -xelatex main_ieee.tex
    [ "$target" = "ieee" ] && exit 0
    ;;
esac

case "$target" in
  acm|all)
    echo "[build] Compiling ACM"
    latexmk -silent -file-line-error -outdir=build -bibtex -xelatex main_acm.tex
    [ "$target" = "acm" ] && exit 0
    ;;
esac

case "$target" in
  apa7|all)
    echo "[build] Compiling APA7"
    latexmk -silent -file-line-error -outdir=build -xelatex main_apa7.tex
    [ "$target" = "apa7" ] && exit 0
    ;;
esac

if [ "$target" != "all" ] && [ "$target" != "ieee" ] && [ "$target" != "acm" ] && [ "$target" != "apa7" ]; then
  echo "Usage: $0 [ieee|acm|apa7|all]" >&2
  exit 1
fi

echo "[build] PDFs available in build/"
