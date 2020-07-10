#!/bin/bash
set -e
# This script builds variable and static fonts.
# It contains all the steps needed to build new fonts,
# so font builds are repeatable and documented.
#
# To build new fonts, open a Unix-like terminal in the "sources" directory
# of this project and run the script:
#
# $ sh build.sh
#
# Also, if you are updating the font for Google Fonts, you can
# use the "-gf" flag to run additional pull-request-helper
# commands as well. Just remember to change the "pr_dir"
# file path variable if you aren't building to ~/Google/fonts/ofl/.../:
#
# $ sh build.sh -gf
#
# The default settings should produce output that will conform
# to the Google Fonts Spec [1] and pass all FontBakery QA Tests [2].
# However, the Build Script Settings below are designed to be easily
# modified for other platforms and use cases.
#
# This script requires Python3 [3] and a Unix-like
# environment(Mac, GNU+Linux, WSL), with a BASH-like shell.
# All Python dependencies will be installed in a temporary
# virtual environment by the script. Please see the
# Google Fonts Spec [1] and the FontBakery QA Tools [2] for more info.
#
# Script by Eli H. If you have questions, please send an email [4].
#
# [1] https://github.com/googlefonts/gf-docs/tree/master/Spec
# [2] https://pypi.org/project/fontbakery/
# [3] https://www.python.org/
# [4] elih@protonmail.com

#########################
# BUILD SCRIPT SETTINGS #
#########################
alias activate_py_venv=". build-venv/bin/activate"  # Starts a Python 3 virtual environment when invoked
output_dir="fonts"                      # Where the output from this script goes
family_name="Blue Ocean"                # Font family name for output files
glyphs_source="BlueOcean.glyphs"        # Set the source file to build from
make_new_venv=true                      # Set to `true` if you want to build and activate a python3 virtual environment
#build_static_fonts=true                # Set to `true` if you want to build static fonts
#autohint=false                         # Set to `true` if you want to use auto-hinting (ttfautohint)
nohinting=true                          # Set to `true` if you want the fonts unhinted

################
# BUILD SCRIPT #
################
echo ""
echo "[INFO] Starting build script for the $family_name font family"

if [ "$1" = "-gf" ]; then
  echo "[INFO] Also, preparing a pull request to Google Fonts at ~/Google/fonts/ofl";
  echo ""
fi

if [ "$make_new_venv" = true ]; then
  echo "[INFO] Building a new Python3 virtual environment"
  python3 -m venv build-venv > /dev/null
  echo "[INFO] Activating the Python3 virtual environment"
  activate_py_venv > /dev/null
  echo "[INFO] Python3 setup..."
  pip install --upgrade pip > /dev/null
  pip install --upgrade -r ../requirements.txt > /dev/null
  echo ""
  echo "[INFO] Done with Python3 virtual environment setup"
  # which python  # Test to see if the VENV setup worked
  echo ""
fi

for sources in $glyphs_source; do
  echo "[TEST] Queued source file: $sources"
done

for sources in $glyphs_source; do
  echo "[INFO] Building $sources variable fonts with Fontmake..."
  fontmake -g $sources -o variable \
    --output-path ../$output_dir/ttf/BlueOcean.ttf \
    --verbose ERROR
done

echo "[INFO] Fixing variable font DSIG tables"
if gftools fix-dsig -f ../fonts/ttf/*.ttf >/dev/null; then
  echo "[INFO] DSIG fixed for variable fonts"
else
  echo "[ERROR] GFtools is not working, please update or install: https://github.com/googlefonts/gftools"
fi

if [ "$nohinting" = true ]; then
  for font in ../fonts/ttf/*.ttf; do
    echo "[INFO] Fixing nonhinting for $font ";
    gftools fix-nonhinting $font ../fonts/ttf/temp.ttf >/dev/null
    mv ../fonts/ttf/temp.ttf $font
    rm -rf ../fonts/ttf/*backup-fonttools-prep-gasp.ttf
  done
fi

echo "[INFO] Removing build directories";
rm -rf master_ufo

if [ "$1" = "-gf" ]; then
  echo "[TODO] Google Fonts PR script goes here";
fi

if [ "$make_new_venv" = true ]; then
  echo "[INFO] Removing Python3 virtual environment"
  rm -rf build-venv
fi