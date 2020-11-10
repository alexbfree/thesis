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

WEBSITE_PATH = "./out/website/"
OUT_PATH = "./out"
SRC_PATH = "./src"

# Builds the entire thesis
def buildThesis(format):

    # Output path
    outputPath = "{}/{}/".format(OUT_PATH, format)

    # Check for and create the folder
    subprocess.run(["mkdir", "-p", outputPath])

    # Create the file name now so it's easier to output to args
    filename = "thesis.{}".format(format)

    # define args now
    args = ["pandoc", "src/index.md"]


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

    # Build
    subprocess.run(args)

    print("Thesis built under " + outputPath+filename)

# Builds a single chapter

def buildChapter(chapterNumber, format):

    outputPath = "{}/{}/".format(OUT_PATH, format)

    # Make the directory for the output if not exists
    subprocess.run(["mkdir", "-p", outputPath])

    # Define filename
    filename = "chapter-{}.{}".format(chapterNumber, format)

    # define pandoc args
    args = ["pandoc", "src/index.md", "src/chapter-{}.md".format(chapterNumber), "src/bibliography.md" , "--output={}{}".format(outputPath,filename), "-s", "--toc", "--filter=pandoc-citeproc", "--self-contained", "--number-sections"]

    # Append the args for offsetting the section number (chapter number minus 1)
    args.append("--number-offset={}".format(int(chapterNumber) - 1))

    # Append the pdf args
    if format == "pdf":
        args.append("-t")
        args.append("html5")

    # Run the pandoc command
    subprocess.run(args)

    print("Built %s" % outputPath+filename)

# Iterates and builds all individual chapters as separate files.
def buildChapters(format):

    # Add chapters dynamically based on a pattern, count the chapters and them add in sequence based on number (not on filename order in the list)

    for i in range(getChapterCount()):
        print("Building Chapter %s" % str(i+1))
        buildChapter(str(i+1), format)

# Builds the HTML coversheet for the thesis
def buildCoversheet(outputPath):
    # Load the template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template("index.html")

    # Load index.md frontmatter and parse it to get title and author info

    config = frontmatter.load('./src/index.md')

    thesis_title = config['title']
    thesis_author = config['author']

    # Get the last updated
    date = datetime.now()
    last_updated = date.strftime("%A %d %B %Y at %H:%M")

    # Get a list of items to include in the table row
    items = []

    # To find the title the best way forward is to nab the title from the HTML file as that's easier to parse than Markdown

    html_file = open('./out/html/thesis.html') # Open the thesis filel it's cheaper to parse the file once and nab the title in the loop

    html_content = html_file.read()
    html_file.close()
    soup = BeautifulSoup(html_content, 'html.parser') # Parse it


    for i in range(getChapterCount()):
        item = {}
        item["file"] = "chapter-{}".format(i+1)

        title = soup.find("h1", id="chapter-{}".format(i+1)).contents # Nab the h1 element with the chapter title
        item["title"] = "{}{}".format(title[0],title[1])

        items.append(item)


    # Write the file
    output = open(outputPath + "index.html", "w")
    output.write(template.render(thesis_title=thesis_title, thesis_author=thesis_author,last_updated=last_updated, items=items))
    output.close()

# Builds the website along with cover page
def buildWebsite():
    # Check for and create the folder
    subprocess.run(["mkdir", "-p", WEBSITE_PATH])

    # Build the various copies of the thesis
    buildThesis("html")
    buildThesis("odt")
    buildThesis("docx")

    # Build chapters separately. It's nice to break things up for people.
    buildChapters("html")
    buildChapters("odt")
    buildChapters("docx")

    # Copy files (note: is there a better way to do this?)
    copy("./src/styles.css", WEBSITE_PATH)

    dir_util.copy_tree("{}/html/".format(OUT_PATH), WEBSITE_PATH+"html/")
    dir_util.copy_tree("{}/odt/".format(OUT_PATH), WEBSITE_PATH+"odt/")
    dir_util.copy_tree("{}/docx/".format(OUT_PATH), WEBSITE_PATH+"docx/")

    # Generate cover sheet
    buildCoversheet(WEBSITE_PATH)

# Returns a count of all chapters, used in loops to manipulate chapters dynamically
def getChapterCount():
    pattern = "chapter-[0-9]*.md"

    return len(glob.glob("{}/{}".format(SRC_PATH, pattern)))



# Main function to check arguments
def main(argv):
    if argv[1] == "chapter":
        buildChapter(argv[2], argv[3])
    elif argv[1] == "thesis":
        buildThesis(argv[2])
    elif argv[1] == "chapters":
        buildChapters(argv[2])
    elif argv[1] == "website":
        buildWebsite()
    elif argv[1] == "coversheet":
        buildCoversheet(WEBSITE_PATH)


main(sys.argv)
print("\nEnd")
