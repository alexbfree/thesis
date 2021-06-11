#!/usr/bin/env python3

import sys
import subprocess
from bs4 import BeautifulSoup
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from shutil import copy
from distutils import dir_util
import frontmatter
import glob
import argparse

WEBSITE_PATH = "./out/website"
OUT_PATH = "./out"
SRC_PATH = "./src"

# Builds the entire thesis
def buildThesis(format):
    print("Building Thesis in {}".format(format))
    # Output path
    outputPath = "{}/{}/".format(OUT_PATH, format)

    # Check for and create the folder
    subprocess.run(["mkdir", "-p", outputPath])

    # Create the file name now so it's easier to output to args
    filename = "thesis.{}".format(format)

    # define args now
    args = ["pandoc", "src/index.md", "src/frontmatter.md"]


    # Add chapters dynamically based on a pattern, count the chapters and them add in sequence based on number (not on filename order in the list)

    for i in range(getChapterCount()):
        args.append("src/chapter-{}.md".format(i+1))


    # Finish the bulk of arguments
    args.append("src/bibliography.md") # this always comes last after the chapters
    args.extend(["-s", "--toc", "--toc-depth=2", "--filter=pandoc-citeproc", "--self-contained", "--number-sections", "--output={}{}".format(outputPath, filename)])

    # Add for pdf (avoid latex pdfs)

    if format == "pdf":
        args.append("-t")
        args.append("html5")

    #print('command is:')
    #print(args)

    # Build
    subprocess.run(args)

    print("\tThesis built under " + outputPath+filename)

# Builds filename.md into filename.format; numberOffset may be set to change the section numbers
def buildFile(filename, format, chapterNumber=None):
    print("Building {} in {}".format(filename, format))

    # Define the output path where the file will be built, using the format argument and make the directory if it doesn't exist
    outputPath = "{}/{}/".format(OUT_PATH, format)
    subprocess.run(["mkdir", "-p", outputPath])

    # Define the output filename
    outputFile = "{}.{}".format(filename,format)

    # Build the initial pandoc command to build the file
    args = ["pandoc", "src/index.md", "src/{}.md".format(filename), "src/bibliography.md" , "--output={}{}".format(outputPath,outputFile), "-s", "--toc", "--filter=pandoc-citeproc", "--self-contained", "--number-sections"]

    # Append the pdf args for if they try to build a PDF file
    if format == "pdf":
        args.append("-t")
        args.append("html5")

    # Append the args for offsetting the section number (chapter number minus 1)
    if not chapterNumber == None:
        args.append("--number-offset={}".format(int(chapterNumber) - 1))

    # Run the pandoc command
    subprocess.run(args)

    print("\tBuilt {}{}".format(outputPath, outputFile))

# Builds a single chapter
def buildChapter(chapterNumber, format):

    # Get the filename to pass down
    filename = "chapter-{}".format(chapterNumber)

    # Run the buildFile command, pass down the chapterNumber to offset properly
    buildFile(filename, format, chapterNumber)


# Iterates and builds all individual chapters as separate files.
def buildChapters(format):
    # Add chapters dynamically based on a pattern, count the chapters and them add in sequence based on number (not on filename order in the list)

    for i in range(getChapterCount()):
        # print("Building Chapter %s" % str(i+1))
        buildChapter(str(i+1), format)

# Builds the HTML coversheet for the thesis
def buildCoversheet(outputPath):
    print("Building Coversheet")

    # Load the template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template("index.html")

    # Load index.md frontmatter and parse it to get title and author info

    config = frontmatter.load('./src/index.md')

    thesis_title = config['title']
    thesis_author = config['author']
    thesis_source = config['thesis-source']
    build_formats = config['website-build-formats']
    download_button_format = config['download-button-format']

    # Get the last updated
    date = datetime.now()
    last_updated = date.strftime("%A %d %B %Y at %H:%M")

    # Get a list of items to include in the table row
    items = []

    # To find the title the best way forward is to nab the title from the HTML file as that's easier to parse than Markdown

    # Open the thesis file, it's cheaper to parse the file once and nab the title in the loop
    html_file = open('./out/html/thesis.html')

    html_content = html_file.read()
    html_file.close()
    soup = BeautifulSoup(html_content, 'html.parser') # Parse it


    for i in range(getChapterCount()):
        chap = i+1
        item = {}
        item["file"] = "chapter-{}".format(chap)

        if chap==1:
            item["title"]="1 Introduction"
        elif chap==2:
            item["title"]="2 Literature Review"
        elif chap==3:
            item["title"]="3 Methodology"
        elif chap==4:
            item["title"]="4 Case Study One: Accessing and Using Civic Data in Early Help"
        elif chap==5:
            item["title"]="5 Case Study Two: The Human Experience of GDPR"
        elif chap==6:
            item["title"]="6 Bridge: An Understanding of Human Data Relations"
        elif chap==7:
            item["title"]="7 Case Study Three: Personal Data Interface Design & Development"
        elif chap==8:
            item["title"]="8 Discussion: Designing Better Human Data Relations" #alt: Next Steps Towards a Human-Centric Future
        else:
            item["title"] = "Chapter {}".format(chap)

        #foundh1 = soup.find("h1", id="chapter-{}".format(i+1))
        #if foundh1 is not None:
        #  title = foundh1.contents # Nab the h1 element with the chapter title
        #      item["title"] = "{}{}".format(title[0]+1,title[1])

        items.append(item)

    #print("\tItems array is:")
    #print(items)

    #biblio = {}
    #biblio["file"] = "bibliography"
    #biblio["title"] = soup.find("h1", id="bibliography").contents[]
    #items.append(biblio)

    # Write the file
    output = open(outputPath + "index.html", "w")
    output.write(template.render(thesis_title=thesis_title, thesis_author=thesis_author,last_updated=last_updated, thesis_source=thesis_source, items=items, build_formats=build_formats, download_button_format=download_button_format))
    output.close()

    print("\tCoversheet built under ./out/website/index.html")

# Builds the website along with cover page
def buildWebsite():
    # Check for and create the folder
    subprocess.run(["mkdir", "-p", WEBSITE_PATH])

    # Load the config file
    config = frontmatter.load('./src/index.md')

    # Copy the styles file
    copy("./src/styles.css", WEBSITE_PATH)

    # First build in HTML for the web, then loop over the format list and build for that
    buildThesis("html")
    buildChapters("html")
    buildFile("frontmatter", "html")
    dir_util.copy_tree("{}/{}/".format(OUT_PATH, "html"), "{}/{}/".format(WEBSITE_PATH, "html") )

    for format in config['website-build-formats']:
        # Build the thesis + the individual chapters separately
        buildThesis(format)
        buildChapters(format)
        buildFile("frontmatter", format)

        # Move the new files over to the website directory
        dir_util.copy_tree("{}/{}/".format(OUT_PATH, format), "{}/{}/".format(WEBSITE_PATH, format) )


    # Generate cover sheet
    buildCoversheet("{}/".format(WEBSITE_PATH))

# Returns a count of all chapters, used in loops to manipulate chapters dynamically
def getChapterCount():
    pattern = "chapter-[0-9]*.md"

    return len(glob.glob("{}/{}".format(SRC_PATH, pattern)))


    # deploy it to github pages
    #print("\nStashing any changes so we don't commit them...");
    #subprocess.run(["git","stash"]);
    #print("\nAuto-deploying to github pages...")
    #subprocess.run(["git","add","out/website/html/*.*"]);
    #subprocess.run(["git","add","out/website/odt/*.*"]);
    #subprocess.run(["git","add","out/website/docx/*.*"]);
    #subprocess.run(["git","add","out/website/*.*"]);
    #subprocess.run(["git","commit","-m","Auto-deploying website to github pages"]);
    #subprocess.run(["git","subtree","push","--prefix","out/website","origin","gh-pages"]);
    #print("\nUnstashing any changes we stashed before commit...");
    #subprocess.run(["git","stash","pop"]);


# Main function to check arguments
def main(argv):

    # Define a top level parser for commands
    parser = argparse.ArgumentParser(description="Markdown Thesis: Write your thesis in markdown and manage conversions into other formats")

    # The command line options differ for each command so we create subparsers for each
    subparsers = parser.add_subparsers(dest="subparser",help="Sub-command help")

    # Parser for building individual chapters
    chapter_parser = subparsers.add_parser("chapter", help="Builds an individual chapter in [format]")
    chapter_parser.add_argument("chapter_number", type=int, help="The number of the chapter you want to build")
    chapter_parser.add_argument("format", type=str, help="The format you want to build into e.g. html or docx")

    # Parser for building the frontmatter
    frontmatter_parser = subparsers.add_parser("frontmatter", help="Builds only frontmatter.md in [format]")
    frontmatter_parser.add_argument("format", type=str, help="The format you want to build into e.g. html or docx")

    # Parser for building the entire thesis or all chapters simultaneously
    thesis_parser = subparsers.add_parser("thesis", help="Builds the entire thesis in an appropriate format")
    thesis_parser.add_argument("format", type=str, help="The format you want to build into e.g. html or docx")

    # Parser for building all chapters at once
    chapters_parser = subparsers.add_parser("chapters", help="Builds all chapters in [format]")
    chapters_parser.add_argument("format", type=str, help="The format you want to build into e.g. html or docx")

    # Parser for building an entire website
    website_parser = subparsers.add_parser("website", help="Generates a website including a frontpage and html, docx, and odt versions of each chapter and entire thesis")

    # Run
    args = parser.parse_args()
    markdown_thesis(args)

# Takes the result of args and passes it down to the relevant function
def markdown_thesis(args):

    if args.subparser == "thesis":
        print("Building Thesis in {}\n======\n".format(args.format))
        buildThesis(args.format)

    elif args.subparser == "chapters":
        print("Building all chapters in {}\n======\n".format(args.format))
        buildChapters(args.format)

    elif args.subparser == "website":
        print ("Building website \n======\n")
        buildWebsite()

    elif args.subparser == "chapter":
        print("Building Chapter in {}\n======\n".format(args.format))
        buildChapter(args.chapter_number, args.format)

    elif args.subparser == "frontmatter":
        print("Building frontmatter in {}\n======\n".format(args.format))
        # buildFrontmatter(args.format)
        buildFile("frontmatter", args.format)


main(sys.argv)
print("\n=====\nEnd")
