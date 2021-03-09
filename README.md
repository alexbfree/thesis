# Markdown Thesis
A simple build script for managing a thesis in markdown. You *must* have [Pandoc](https://pandoc.org/) installed to make use of it, as it effectively acts as a wrapper for a complex pandoc command.

## Installation

1. Fork the repo or clone and set your own remote
2. In the repo run `pip3 install -r requirements.txt` to gather the python requirements for the build script

## Use
Write in the `src` folder, in markdown. Name your chapters with the format `chapter-X.md`. You can then run `build.py` to build for various formats. You can build by either entire thesis + format or chapter + format. e.g. `./build.py chapter 1 html` produces a HTML rendering of Chapter 1, `./build.py chapter 6 odt` will give you an OpenDocument file of Chapter 6.

Since you're using pandoc under the hood it will accept all formats pandoc can convert to from markdown. PDF rendering is done via HTML5 as LaTeX doesn't like SVG files naturally; this may change with an update and custom latex templates.

The two main commands:

* `build.py chapter X $FORMAT` builds `src/chapter-X.md` in `$FORMAT`
* `build.py thesis $FORMAT` builds the whole thesis in `$FORMAT`

There are three additional commands:
  + `build.py chapters $FORMAT` generates every chapter individually in the given format.
  + `build.py frontmatter $FORMAT` generates a frontmatter file from `src/frontmatter.md` in $FORMAT
  + `build.py website` generates a website with coversheet. Example output at: [thesis.mrshll.uk](https://thesis.mrshll.uk). This takes a few variables to set a few things.

Scripts will build into an `out` directory and then a subdirectory for their specific format e.g. `out/html` or `out/odt`. `/out` is ignored by git, so you need to run a build script to acquire the desired format.

Currently the script enables `--toc` to its default depth to generate a table of contents, and also `--number-sections`. For some reason the latter only works in the HTML rendering!

`/templates` currently contains the coversheet template used by the `website` command but may in future contain custom LaTeX templates for nice PDF rendering. Pandoc is run with the `--self-contained` flag to pull in any resources to the output file.

## Variables

Use `src/index.md` to set the variables for your thesis and build scripts. Most of these variables come from the pandoc docs and are collected in `src/index.md` so that they don't need to be repeated across multiple files or embedded in `build.py`. When building a file, `src/index.md` will *always* be included first to pull in these variables.

### Pandoc Variables
* `title` sets the title of your thesis
* `author` your author name
* `bibliography` is the file where your bibtex file lives; it's automatically set to `src/thesis.bib`
* `css` is a YAML List of css files. By default `src/pure-min.css` and `src/styles.css` are included. If you want to add more layers of css or change some around; here's where to do it.
* `link-citations` is defaulted to `true`. Setting to `false` will mean that citations in generated files will not be hyperlinked to their entries in your bibliography.
* `csl` sets the style file for your bibliography. It's defaulted to `src/harvard-newcastle-university.csl`. You can find others [here](https://www.zotero.org/styles).

### Custom variables
The build script uses a few more variables to support it generating the website via the `website` command.

* `thesis-source` is a URL which can take people to the git repo where you store your thesis
* `download-button-format` takes a format string (e.g. *odt* or *docx*) and set the target of the Download Button on the website homepage
* `website-build-formats` is a YAML list of formats that you want your thesis to be available in via the generated website. By default `odt` and `docx` are included, but it will take any valid pandoc format.



## HTML Styles
Most styles are provided by [PureCSS](https://purecss.io/). This provides a *minimal* and *responsive* html page; which is really what this script is optimised for. There are additional styles for both print and web contained in `styles.css` which are designed to make everything look just a bit nicer. Pandoc cannot generate PureCSS classes and grids by default so these styles make text a bit more readable and make tables, quotes, and images read a bit better.

The pages are *mostly* responsive insofar as they're pretty brutalist and rely on HTML's natural scalability to fit onto most viewscreens. On mobile the margin is a tad wider than it needs to be, and if this bothers you adjust it in `src/styles.css`

## Tips for writing
+ Make sure to grab a copy of [BetterBibTeX](https://retorque.re/zotero-better-bibtex/installation/) for Zotero to handle generating nicer citation keys.

## Acknowledgements
This thesis repository structure re-uses the scripts and structural approach of [Matt Marshall](http://mrshll.uk/about#contact) and his repo at https://gitlab.com/mrshll1001/markdown-thesis - thanks Marshall!
