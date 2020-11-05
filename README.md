# Markdown Thesis
A simple build script for managing a thesis in markdown. You *must* have Pandoc installed to make use of it, as it effectively acts as a wrapper for a complex pandoc command.

## Installation

1. Fork the repo or clone and set your own remote
2. In the repo run `pip3 install -r requirements.txt` to gather the python requirements for the build script

## Use
Write in the `src` folder, in markdown. Name your chapters with the format `chapter-X.md`. You can then run `build.py` to build for various formats. You can build by either entire thesis + format or chapter + format. Since you're using pandoc under the hood it will therefore accept all formats pandoc can convert to from markdown. PDF rendering is done via HTML5 as LaTeX doesn't like SVG files naturally; this may change with an update and custom latex templates. You can then build the thesis using `build.py chapter X $FORMAT`

e.g. `./build.py chapter 1 html` produces a HTML rendering of Chapter 1, `./build.py chapter 6 odt` will give you an OpenDocument file of Chapter 6.

There are two special options:
  + `build.py chapters $FORMAT` generates every chapter individually in the given format.
  + `build.py website` generates a website with coversheet. Example output at: [thesis.mrshll.uk](https://thesis.mrshll.uk)

Use `src/index.md` to set the variables for your thesis and build scripts. The build script uses precisely one extra variable which is `thesis-source` and this should take a url to a git repo where you'll be storing your thesis. Check out the [pandoc documentation](https://pandoc.org/MANUAL.html) for additional variables.

Scripts will build into an `out` directory and then a subdirectory for their specific format e.g. `out/html` or `out/odt`. `/out` is ignored by git, so you need to run a build script to acquire the desired format.

Currently the script enables `--toc` to its default depth to generate a table of contents, and also `--number-sections`. For some reason the latter only works in the HTML rendering!

`/templates` currently contains the coversheet template used by the `website` command but may in future contain custom LaTeX templates for nice PDF rendering. Pandoc is run with the `--self-contained` flag to pull in any resources to the output file.

## HTML Styles
Most styles are provided by [PureCSS](https://purecss.io/). This provides a *minimal* and *responsive* html page; which is really what this script is optimised for. There are additional styles for both print and web contained in `styles.css` which are designed to make everything look just a bit nicer. Pandoc cannot generate PureCSS classes and grids by default so these styles make text a bit more readable and make tables, quotes, and images read a bit better.

The pages are *mostly* responsive insofar as they're pretty brutalist and rely on HTML's natural scalability to fit onto most viewscreens. On mobile the margin is a tad wider than it needs to be, and if this bothers you adjust it in `src/styles.css`

## Tips for writing
+ Make sure to grab a copy of [BetterBibTeX](https://retorque.re/zotero-better-bibtex/installation/) for Zotero to handle generating nicer citation keys.
