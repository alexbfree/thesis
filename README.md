# Markdown Thesis
A simple build script for managing a thesis in markdown. You *must* have Pandoc installed to make use of it, as it effectively acts as a wrapper for a complex pandoc command.

## Use
Write in the `src` folder, in markdown. Name your chapters with the format `chapter-X.md`. You can then run `build.py` to build for various formats. You can build by either entire thesis + format or chapter + format. Since you're using pandoc under the hood it will therefore accept all formats pandoc can convert to from markdown. PDF rendering is done via HTML5 as LaTeX doesn't like SVG files naturally.

Use `src/index.md` to set the variables for your thesis and build scripts. The build script doesn't use any special variables, so check out the [pandoc documentation](https://pandoc.org/MANUAL.html).

e.g. `./build.py chapter 1 html` produces a HTML rendering of Chapter 1, `./build.py chapter 6 odt` will give you an OpenDocument file of Chapter 6.

There are two special options:
  + `build.py chapters $FORMAT` generates every chapter individually in the given format.
  + `build.py website` generates a website with coversheet. Example output at: [thesis.mrshll.uk](https://thesis.mrshll.uk)

Scripts will build into an `out` directory and then a subdirectory for their specific format e.g. `out/html` or `out/odt`. `/out` is ignored by git, so you need to run a build script to acquire the desired format.

Currently the script enables `--toc` to its default depth to generate a table of contents, and also `--number-sections`. For some reason the latter only works in the HTML rendering!

`/templates` currently contains the coversheet template used by the `website` command but may in future contain custom LaTeX templates for nice PDF rendering. Pandoc is run with the `--self-contained` flag to pull in any resources to the output file.

## Tips for writing
+ Make sure to grab a copy of [BetterBibTeX](https://retorque.re/zotero-better-bibtex/installation/) for Zotero to handle generating nicer citation keys.
+ BetterBibTeX is great, but its default citation key format has changed three times since beginning this thesis so you'll need to fiddle with it.
+ Preferences -> BetterBibTeX and then change citation key format to `[auth:lower][shorttitle3_3][year]`
