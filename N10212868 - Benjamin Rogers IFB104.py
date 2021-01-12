
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10212867
#    Student name: Benjamin Rogers
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  The Best, Then and Now
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application that allows the user to preview and print lists of
#  top-ten rankings.  See the instruction sheet accompanying this
#  file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.  YOU MAY NOT USE
# ANY NON-STANDARD MODULES SUCH AS 'Beautiful Soup' OR 'Pillow'.  ONLY
# MODULES THAT COME WITH A STANDARD PYTHON 3 INSTALLATION MAY BE
# USED.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce a
# meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.

#------------------ Main Menu ---------------------------------------#
main_menu = Tk()
main_menu.configure(background='white')
main_menu.geometry('700x400')
photo = PhotoImage(file="toptuneslogo.png")
photolabel = Label(main_menu, image=photo, borderwidth=0, relief="solid")
photolabel.pack(side='right', padx = 10)


# Show which radio button the user has selected
def choice_selection():
    global choice
    choice = selection.get()

# Directs user to appropriate preview screens
def preview_controller():
    if choice == 1:
        btn1_preview()
    elif choice == 2:
        btn2_preview()
    elif choice == 3:
        btn3_preview()
    elif choice == 4:
        btn4_preview()
    elif choice == 5:
        btn5_preview()
    else:
        btn6_preview()

# Directs user to appropriate export screens
def export_controller():
    if choice == 1:
        btn1_export()
    elif choice == 2:
        btn2_export()
    elif choice == 3:
        btn3_export()
    elif choice == 4:
        btn4_export()
    elif choice == 5:
        btn5_export()
    else:
        btn6_export()

# Activates save function for each screen
def save_controller():
    if choice == 1:
        btn1_save()
    elif choice == 2:
        btn2_save()
    elif choice == 3:
        btn3_save()
    elif choice == 4:
        btn4_save()
    elif choice == 5:
        btn5_save()
    else:
        btn6_save()

# Set variable type for 'Selection'
selection = IntVar()

# Radio Buttons for Billboard pages
button1 = Radiobutton(main_menu, text = 'Previous', value = 1, font = ('Arial', 15), background='white', variable = selection, command = choice_selection)
button1.place(x=15, y=50)
button2 = Radiobutton(main_menu, text = 'Current', value = 2, font = ('Arial', 15), background='white', variable = selection, command = choice_selection)
button2.place(x=130, y=50)

# Radio Buttons for Aria pages
button3 = Radiobutton(main_menu, text = 'Previous', value = 3, font = ('Arial', 15), background='white', variable = selection, command = choice_selection)
button3.place(x=15, y=150)
button4 = Radiobutton(main_menu, text = 'Current', value = 4, font = ('Arial', 15), background='white', variable = selection, command = choice_selection)
button4.place(x=130, y=150)

# Radio Buttons for Canada pages
button5 = Radiobutton(main_menu, text = 'Previous', value = 5, font = ('Arial', 15), background='white', variable = selection, command = choice_selection)
button5.place(x=15, y=250)
button6 = Radiobutton(main_menu, text = 'Current', value = 6, font = ('Arial', 15), background='white', variable = selection, command = choice_selection)
button6.place(x=130, y=250)

# Labels for each pages' options
label1 = Label(main_menu, text = "Official charts singles", font = ('Arial 18 bold'), background='white', fg='green')
label1.place(x=15,y=20)
label2 = Label(main_menu, text = "Aria top singles", font = ('Arial 18 bold'), background='white', fg='red')
label2.place(x=15,y=120)
label3 = Label(main_menu, text = "Canadian top singles", font = ('Arial 18 bold'), background='white', fg='purple')
label3.place(x=15,y=220)

#--------------- Setup the reading of the html files -----------------#

# Offcialcharts Previous
html_file = 'officialcharts.html'
html_code = open(html_file).read()
official_list = []
top_official = re.findall('<a href=\"\/search\/singles\/[a-zA-Z1234567890-]*.+/\">([a-zA-Z1234567890-]*\s?.+)</a>', str(html_code))
official_list.append(top_official)
official_list_previous = [w.replace('&amp;', '&') for w in official_list[0]]


# Officialcharts Current
url_current_official = 'https://www.officialcharts.com/charts/dance-singles-chart/'
html_current_official = urlopen(url_current_official)
webtext_current_official = html_current_official.read().decode('utf-8')
official_list_cur = []
top_official_current = re.findall('<a href=\"\/search\/singles\/[a-zA-Z1234567890-]*.+/\">([a-zA-Z1234567890-]*\s?.+)</a>', str(webtext_current_official))
official_list_cur.append(top_official_current)
official_list_current = [w.replace('&amp;', '&') for w in official_list_cur[0]]

# Aria charts Previous
html_aria = 'ariaartist.html'
aria_code = open(html_aria).read().encode('utf-8')
aria_list = []
top_aria = re.findall('<div class=\"item-title\">([a-zA-Z1234567890-]*[\/]?\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*)<\/div>', str(aria_code))
aria_list.append(top_aria)

# Aria charts Current
url_current_aria = 'https://www.ariacharts.com.au/charts/australian-artist-singles-chart'
html_current_aria = urlopen(url_current_aria)
webtext_current_aria = html_current_aria.read().decode('utf-8')
current_list_aria = []
top_current_aria = re.findall('<div class=\"item-title\">([a-zA-Z1234567890-]*[\/]?\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*)<\/div>', str(webtext_current_aria))
current_list_aria.append(top_current_aria)

# Canada charts Previous 
html_canada = 'canadasingles.html'
canada_code = open(html_canada).read()
canada_list = []
top_canada = re.findall('<a href=\"https://acharts\.co/song/[0-9]*\" itemprop=\"url\"><span itemprop=\"name\">([a-zA-Z1234567890-]*[\/]?\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*)<\/span>', str(canada_code))
canada_list.append(top_canada)

# Canada Singles Current
url_current_canada = 'https://acharts.co/canada_singles_top_100'
html_current_canada = urlopen(url_current_canada)
webtext_current_canada = html_current_canada.read()
current_list_canada = []
top_current_canada = re.findall('<a href=\"https://acharts\.co/song/[0-9]*\" itemprop=\"url\"><span itemprop=\"name\">([a-zA-Z1234567890-]*[\/]?\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*)<\/span>', str(webtext_current_canada))
current_list_canada.append(top_current_canada)

#------------------ Open popup windows for each page ----------------- #

# Open previous list for Officialcharts
def btn1_preview():
    # Setup window
    preview_window_official = Toplevel()
    preview_window_official.geometry('750x400')
    preview_window_official.configure(background='white')
    
    # Main text for window
    main_text = Label(preview_window_official, text = 'Previous Officialcharts Top Singles', font = ('Arial 18 bold'), background='white', fg='green')
    main_text.place(x=170, y=15)

    # Loop through list and make labels for each item
    y_coord_official = 70
    for item in official_list_previous[:10]:
        Label_test = Label(preview_window_official, text = item, font = ('Arial', 15), background='white', fg='black')
        Label_test.place(x=430, y=y_coord_official)
        y_coord_official = y_coord_official + 30

    # Numbering for the list
    numbering = [1,2,3,4,5,6,7,8,9,10]
    num_coord = 70
    for number in numbering:
        Number_label = Label(preview_window_official, text = number, font = ('Arial 15 bold'), background='white', fg='red')
        Number_label.place(x=405, y=num_coord)
        num_coord = num_coord + 30
        
    # Place Officialcharts logo in window
    official_image = PhotoImage(file="officialcharts.PNG")
    photolabel = Label(preview_window_official, image=official_image, borderwidth=0, relief="solid")
    photolabel.place(x=100, y=55)

    # Change title of window
    preview_window_official.title('Previous Officialcharts Top Singles')
    preview_window_official.mainloop()

# Open current list for Officialcharts
def btn2_preview():
    # Setup window
    preview_window_official_2 = Toplevel()
    preview_window_official_2.geometry('750x400')
    preview_window_official_2.configure(background='white')

    # Main text for window
    main_text_official = Label(preview_window_official_2, text = 'Current Officialcharts Top Singles', font = ('Arial 18 bold'), background='white', fg='green')
    main_text_official.place(x=170, y=15)

    # Loop through list and make labels for each item
    y_coord_official_current = 70
    for item in official_list_current[:10]:
        Label_official_current = Label(preview_window_official_2, text = item, font = ('Arial', 15), background='white', fg='black')
        Label_official_current.place(x=430, y=y_coord_official_current)
        y_coord_official_current = y_coord_official_current + 30

    # Numbering for the list
    numbering_official_current = [1,2,3,4,5,6,7,8,9,10]
    num_coord_current = 70
    for number in numbering_official_current:
        Number_label_current = Label(preview_window_official_2, text = number, font = ('Arial 15 bold'), background='white', fg='red')
        Number_label_current.place(x=405, y=num_coord_current)
        num_coord_current = num_coord_current + 30
        
    # Place Officialcharts logo in window
    official_image_2 = PhotoImage(file="officialcharts.PNG")
    photolabel_current = Label(preview_window_official_2, image=official_image_2, borderwidth=0, relief="solid")
    photolabel_current.place(x=100, y=55)

    # Change title of window
    preview_window_official_2.title('Current Officialcharts Top singles')
    preview_window_official_2.mainloop()

# Open previous list for Aria charts
def btn3_preview():
    # Setup window
    preview_window_aria = Toplevel()
    preview_window_aria.geometry('700x400')
    preview_window_aria.configure(background='white')
    
    # Main text for window
    main_text_aria = Label(preview_window_aria, text = 'Previous Aria Australia Top Singles', font = ('Arial 18 bold'), background='white', fg='red')
    main_text_aria.place(x=170, y=15)

    # Loop through list and make labels for each item
    y_coord_aria = 70
    for item in aria_list[0][:10]:
        Label_items = Label(preview_window_aria, text = item, font = ('Arial', 15), background='white', fg='black')
        Label_items.place(x=430, y=y_coord_aria)
        y_coord_aria = y_coord_aria + 30

    # Numbering for the list
    numbering_aria = [1,2,3,4,5,6,7,8,9,10]
    num_coord_aria = 70
    for number in numbering_aria:
        Number_label_aria = Label(preview_window_aria, text = number, font = ('Arial 15 bold'), background='white', fg='red')
        Number_label_aria.place(x=405, y=num_coord_aria)
        num_coord_aria = num_coord_aria + 30
        
    # Place Aria charts logo
    aria_image = PhotoImage(file="arialogo2.PNG")
    photolabelaria = Label(preview_window_aria, image=aria_image, borderwidth=0, relief="solid")
    photolabelaria.place(x=100, y=75)

    # Change title of window
    preview_window_aria.title('Previous Aria Australia Top Singles')
    preview_window_aria.mainloop()

# Open current list for Aria 
def btn4_preview():
    # Setup window
    preview_window_aria_2 = Toplevel()
    preview_window_aria_2.geometry('700x400')
    preview_window_aria_2.configure(background='white')

    # Main text for window
    main_text_aria_2 = Label(preview_window_aria_2, text = 'Current Aria Australia Top Singles', font = ('Arial 18 bold'), background='white', fg='red')
    main_text_aria_2.place(x=170, y=15)

    # Loop through list and make labels for each item
    y_coord_aria_current = 70
    for item in current_list_aria[0][:10]:
        Label_aria_current = Label(preview_window_aria_2, text = item, font = ('Arial', 15), background='white', fg='black')
        Label_aria_current.place(x=430, y=y_coord_aria_current)
        y_coord_aria_current = y_coord_aria_current + 30

    # Numbering for the list
    numbering_aria_current = [1,2,3,4,5,6,7,8,9,10]
    num_coord_aria_current = 70
    for number in numbering_aria_current:
        Number_label_aria_current = Label(preview_window_aria_2, text = number, font = ('Arial 15 bold'), background='white', fg='red')
        Number_label_aria_current.place(x=405, y=num_coord_aria_current)
        num_coord_aria_current = num_coord_aria_current + 30
        
    # Place Aria charts logo
    aria_image_2 = PhotoImage(file="arialogo2.PNG")
    photolabelaria_current = Label(preview_window_aria_2, image=aria_image_2, borderwidth=0, relief="solid")
    photolabelaria_current.place(x=100, y=75)

    # Change title of window
    preview_window_aria_2.title('Current Aria Australia Top Singles')
    preview_window_aria_2.mainloop()

# Open previous list for Canada charts
def btn5_preview():
    # Setup window
    preview_window_canada = Toplevel()
    preview_window_canada.geometry('700x400')
    preview_window_canada.configure(background='white')

    # Main text for window
    main_text_canada = Label(preview_window_canada, text = 'Previous Canada Top Singles', font = ('Arial 18 bold'), background='white', fg='black')
    main_text_canada.place(x=170, y=15)

    # Loop through list and make labels for each item
    y_coord_canada = 70
    for item in canada_list[0][:10]:
        Label_items_canada = Label(preview_window_canada, text = item, font = ('Arial', 15), background='white', fg='black')
        Label_items_canada.place(x=430, y=y_coord_canada)
        y_coord_canada = y_coord_canada + 30

    # Numbering for the list
    numbering_canada = [1,2,3,4,5,6,7,8,9,10]
    num_coord_canada = 70
    for number in numbering_canada:
        Number_label_canada = Label(preview_window_canada, text = number, font = ('Arial 15 bold'), background='white', fg='red')
        Number_label_canada.place(x=405, y=num_coord_canada)
        num_coord_canada = num_coord_canada + 30
        
    # Place Canada charts logo
    canada_image = PhotoImage(file="canada2.PNG")
    photolabelcanada = Label(preview_window_canada, image=canada_image, borderwidth=0, relief="solid")
    photolabelcanada.place(x=60, y=75)

    # Change title of window
    preview_window_canada.title('Previous Canada Top Singles')
    preview_window_canada.mainloop()

# Open current list for Canada charts 
def btn6_preview():
    # Setup window
    preview_window_canada_2 = Toplevel()
    preview_window_canada_2.geometry('700x400')
    preview_window_canada_2.configure(background='white')

    # Main text for window
    main_text_canada_2 = Label(preview_window_canada_2, text = 'Current Canada Top Singles', font = ('Arial 18 bold'), background='white', fg='black')
    main_text_canada_2.place(x=170, y=15)

    # Loop through list and make labels for each item
    y_coord_canada_current = 70
    for item in current_list_canada[0][:10]:
        Label_items_canada_current = Label(preview_window_canada_2, text = item, font = ('Arial', 15), background='white', fg='black')
        Label_items_canada_current.place(x=430, y=y_coord_canada_current)
        y_coord_canada_current = y_coord_canada_current + 30

    # Numbering for the list
    numbering_canada_current = [1,2,3,4,5,6,7,8,9,10]
    num_coord_canada_current = 70
    for number in numbering_canada_current:
        Number_label_canada_2 = Label(preview_window_canada_2, text = number, font = ('Arial 15 bold'), background='white', fg='red')
        Number_label_canada_2.place(x=405, y=num_coord_canada_current)
        num_coord_canada_current = num_coord_canada_current + 30
        
    # Place Canada charts logo
    canada_image_2 = PhotoImage(file="canada2.PNG")
    photolabelcanada_2 = Label(preview_window_canada_2, image=canada_image_2, borderwidth=0, relief="solid")
    photolabelcanada_2.place(x=60, y=75)

    # Change title of window
    preview_window_canada_2.title('Current Canada Top Singles')
    preview_window_canada_2.mainloop()
    
# ------------------- Exporting contents to HTML pages ------------------#

# Template for the HTML
html_template = """<!DOCTYPE html>
<html>
  <head>
    <meta charset = 'UTF-8'>
    <title>***TITLE***</title>
  </head>

  <body>
      <h1><center>***TITLE***</center></h1>
      <p><center><h2>***DATE***</h2><center></p>
      <p><center>***IMG***<center></p>
      
      <table style="width:50%" border="1" cellpadding="10">
          <tr>
            <th>Rank</th>
            <th>Song Name</th> 
            <th>***EXTRA***</th>
          </tr>
          <tr>
            <td>1</td>
            <td>***SONG_ONE***</td>
            <td>***EXTRA_ONE***</td>
          </tr>
          <tr>
            <td>2</td>
            <td>***SONG_TWO***</td>
            <td>***EXTRA_TWO***</td>
          </tr>
          <tr>
            <td>3</td>
            <td>***SONG_THREE***</td>
            <td>***EXTRA_THREE***</td>
          </tr>
           <tr>
            <td>4</td>
            <td>***SONG_FOUR***</td>
            <td>***EXTRA_FOUR***</td>
          </tr>
           <tr>
            <td>5</td>
            <td>***SONG_FIVE***</td>
            <td>***EXTRA_FIVE***</td>
          </tr>
           <tr>
            <td>6</td>
            <td>***SONG_SIX***</td>
            <td>***EXTRA_SIX***</td>
          </tr>
           <tr>
            <td>7</td>
            <td>***SONG_SEVEN***</td>
            <td>***EXTRA_SEVEN***</td>
          </tr>
           <tr>
            <td>8</td>
            <td>***SONG_EIGHT***</td>
            <td>***EXTRA_EIGHT***</td>
          </tr>
           <tr>
            <td>9</td>
            <td>***SONG_NINE***</td>
            <td>***EXTRA_NINE***</td>
          </tr>
           <tr>
            <td>10</td>
            <td>***SONG_TEN***</td>
            <td>***EXTRA_TEN***</td>
          </tr>
</table>
        <p><center>This information was sourced from <a href="***LINK***">***LINKTEXT***</a><center></p>
  </body>
</html>
"""
# Title on export screens remains the same so needs to be global
global title_top
title_top = 'Export Top Songs'

#--------------Find date & Images for Previous Officialcharts page------------------------#

global date_previous

# Find previous date 
date_previous = re.findall('<\/h1>\n\n[\" \"]*<p class=\"article-date\".\n[ ]*([a-zA-Z\" \"1234567890,]*)', str(html_code))

# Find previous images 
official_list_img = []
top_official_img = re.findall('<div class=\"cover\".+\s*(<img src=\".+\>)', str(html_code))
official_list_img.append(top_official_img)

#--------------Find date & Images for Current Officialcharts page-------------------------#

global date_current

# Find current date 
date_current = re.findall('<\/h1>\n\n[\" \"]*<p class=\"article-date\".\n[ ]*([a-zA-Z\" \"1234567890,]*)', str(webtext_current_official))

# Find current images 
official_list_img_cur = []
top_official_img_cur = re.findall('<div class=\"cover\".+\s*(<img src=\".+\>)', str(webtext_current_official))
official_list_img_cur.append(top_official_img_cur)

#-------------Find date & Artists  for Previous Aria charts page--------------------------#

global date_aria_previous

# Find previous date
date_aria_previous = re.findall('<li class=\"date-display\">([a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890,-]*\s?[a-zA-Z1234567890-]*\s?)', str(aria_code))

# Find previous artists 
previous_artists = []
find_artists = re.findall('<div class=\"artist-name\">([a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890.-]*\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*)</div>', str(aria_code))
previous_artists.append(find_artists)

#-------------Find date & Artists for Current Aria charts page----------------------------#

global date_aria_current

# Find current date
date_aria_current = re.findall('<li class=\"date-display\">([a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890,-]*\s?[a-zA-Z1234567890-]*\s?)', str(webtext_current_aria))

# Find current artists
current_artists = []
find_artists_current = re.findall('<div class=\"artist-name\">([a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890.-]*\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*\s?[a-zA-Z1234567890-]*)</div>', str(webtext_current_aria))
current_artists.append(find_artists_current)

#-------------Find date & videos for Previous Canada charts page---------------------------#

global date_canada

# Find previous date
date_canada = re.findall('<time itemprop=\"datePublished\" datetime=\"[0123456789-]*\">(.*)</time>', str(canada_code))

# Find previous videos
videos = []
find_previous_videos = re.findall('<td class=\"cImg Ico Video\">\s*?<a href=\"(.+)\">\s?</a>', str(canada_code))
videos.append(find_previous_videos)
videos_previous = ['<a href="https://acharts.co/'+item+'">Link to music video</a>' for item in videos[0]]

#-------------Find date & videos for Current Canada charts page--------------------------#

global date_canada_current

# Find currrent date 
date_canada_current = re.findall('<time itemprop=\"datePublished\" datetime=\"[0123456789-]*\">(.*)</time>', str(webtext_current_canada))

# Find current videos
videos_current = []
find_videos_current = re.findall('<td class=\"cImg Ico Video\">\s*?<a href=\"(.+)\">\s?</a>', str(webtext_current_canada.decode('utf-8')))
videos_current.append(find_videos_current)
videos_current =['<a href="https://acharts.co/'+item+'">Link to music video</a>' for item in videos_current[0]]

#------------------ Open export windows for each page ----------------- #
global songs_replace
songs_replace = ['***SONG_ONE***', '***SONG_TWO***', '***SONG_THREE***',
                         '***SONG_FOUR***', '***SONG_FIVE***', '***SONG_SIX***',
                         '***SONG_SEVEN***', '***SONG_EIGHT***', '***SONG_NINE***', '***SONG_TEN***']

extra_replace = ['***EXTRA_ONE***', '***EXTRA_TWO***', '***EXTRA_THREE***', '***EXTRA_FOUR***',
                 '***EXTRA_FIVE***', '***EXTRA_SIX***', '***EXTRA_SEVEN***','***EXTRA_EIGHT***',
                 '***EXTRA_NINE***', '***EXTRA_TEN***']

# Function to close and write after each page is exported
def close_and_write(file):
    html_doc = open(title_top + '.html', 'w', encoding = 'UTF-8')
    html_doc.write(file)
    html_doc.close()
    
# Export previous Officialcharts Page
def btn1_export():
        # Set title
        title = 'Previous Officialcharts Top Singles'
        # Official charts logo
        img = '<img src="officialcharts.PNG" alt="Officialcharts" height="300" width="300">'
        # Set date
        date = str(', '.join(date_previous))
        
        # Replace the blanks in the HTML template
        html_code = html_template.replace('***TITLE***', title)
        html_code = html_code.replace('***DATE***', date)
        html_code = html_code.replace('***IMG***', img)
        html_code = html_code.replace('***EXTRA***', 'Cover Art')
        
        # Replace each song name in HTML template
        song_rank = 0
        for song in songs_replace:
            html_code = html_code.replace(songs_replace[song_rank], official_list[0][song_rank])
            song_rank = song_rank + 1

        # Replace each song image in HTML template
        extra_rank = 0
        for item in extra_replace:
            html_code = html_code.replace(extra_replace[extra_rank], official_list_img[0][extra_rank])
            extra_rank = extra_rank + 1

        # Replace link at bottom of page
        html_code = html_code.replace('***LINK***',  '/IFB104 ASSIGNMENT 2/officialcharts.html')
        html_code = html_code.replace('***LINKTEXT***',  '/IFB104 ASSIGNMENT 2/officialcharts.html')
        
        # Write the HTML code to a Unicode text file and close
        close_and_write(html_code)
        
# Export current Officialcharts Page
def btn2_export():
        # Set title
        title_off_current = 'Current Officialcharts Top Singles'
        # Officialcharts logo
        img = '<img src="officialcharts.PNG" alt="Officialcharts" height="300" width="300">'
        # Set date
        date = str(', '.join(date_current))
        
        # Replace the blanks in the HTML template
        html_code = html_template.replace('***TITLE***', title_off_current)
        html_code = html_code.replace('***DATE***', date)
        html_code = html_code.replace('***IMG***', img)
        html_code = html_code.replace('***EXTRA***', 'Cover Art')

        # Replace each song name in HTML template
        song_rank = 0
        for song in songs_replace:
            html_code = html_code.replace(songs_replace[song_rank], official_list_current[song_rank])
            song_rank = song_rank + 1

        # Replace each song image in HTML template
        extra_rank = 0
        for item in extra_replace:
            html_code = html_code.replace(extra_replace[extra_rank], official_list_img_cur[0][extra_rank])
            extra_rank = extra_rank + 1
        
        # Replace link at bottom of page
        html_code = html_code.replace('***LINK***',  'https://www.officialcharts.com/charts/dance-singles-chart/')
        html_code = html_code.replace('***LINKTEXT***',  'https://www.officialcharts.com/charts/dance-singles-chart/')

        # Write the HTML code to a Unicode text file and close
        close_and_write(html_code)

# Export previous Aria charts Page
def btn3_export():
        # Set title
        title_aria_previous = 'Previous Aria Austrlia Top Singles'
        # Aria charts logo
        img = '<img src="arialogo2.PNG" alt="arialogo" height="300" width="300">'
        # Set date
        date = str(', '.join(date_aria_previous))
        
        # Replace the blanks in the HTML template
        html_code = html_template.replace('***TITLE***', title_aria_previous)
        html_code = html_code.replace('***DATE***', date)
        html_code = html_code.replace('***IMG***', img)
        html_code = html_code.replace('***EXTRA***', 'Artist Name')

        # Replace each song name in HTML template
        song_rank = 0
        for song in songs_replace:
            html_code = html_code.replace(songs_replace[song_rank], aria_list[0][song_rank])
            song_rank = song_rank + 1

        # Replace each song image in HTML template
        extra_rank = 0
        for item in extra_replace:
            html_code = html_code.replace(extra_replace[extra_rank], previous_artists[0][extra_rank])
            extra_rank = extra_rank + 1
        
        # Replace link at bottom of page
        html_code = html_code.replace('***LINK***',  '/IFB104 ASSIGNMENT 2/ariaartist.html')
        html_code = html_code.replace('***LINKTEXT***',  '/IFB104 ASSIGNMENT 2/ariaartist.html')
        
        # Write the HTML code to a Unicode text file and close
        close_and_write(html_code)

# Export current Aria charts Page
def btn4_export():
        # Set title
        title_aria_current = 'Current Aria Austrlia Top Singles'
        # Aria charts logo
        img = '<img src="arialogo2.PNG" alt="arialogo" height="300" width="300">'
        # Set date
        date = str(', '.join(date_aria_current))
        
        # Replace the blanks in the HTML template
        html_code = html_template.replace('***TITLE***', title_aria_current)
        html_code = html_code.replace('***DATE***', date)
        html_code = html_code.replace('***IMG***', img)
        html_code = html_code.replace('***EXTRA***', 'Artist Name')

        # Replace each song name in HTML template
        song_rank = 0
        for song in songs_replace:
            html_code = html_code.replace(songs_replace[song_rank], current_list_aria[0][song_rank])
            song_rank = song_rank + 1

        # Replace each song image in HTML template
        extra_rank = 0
        for item in extra_replace:
            html_code = html_code.replace(extra_replace[extra_rank], current_artists[0][extra_rank])
            extra_rank = extra_rank + 1

        # Replace link at bottom of page
        html_code = html_code.replace('***LINK***',  'https://www.ariacharts.com.au/charts/australian-artist-singles-chart')
        html_code = html_code.replace('***LINKTEXT***',  'https://www.ariacharts.com.au/charts/australian-artist-singles-chart')
        
        # Write the HTML code to a Unicode text file and close
        close_and_write(html_code)

# Export previous Canada charts Page
def btn5_export():
        # Set title
        title_canada_previous = 'Previous Canada Top Singles'
        # Canada charts logo
        img = '<img src="canada2.PNG" alt="canadalogo" height="300" width="300">'
        # Set date
        date = str(', '.join(date_canada))
        
        # Replace the blanks in the HTML template
        html_code = html_template.replace('***TITLE***', title_canada_previous)
        html_code = html_code.replace('***DATE***', date)
        html_code = html_code.replace('***IMG***', img)
        html_code = html_code.replace('***EXTRA***', 'Music Video')

        # Replace each song name in HTML template
        song_rank = 0
        for song in songs_replace:
            html_code = html_code.replace(songs_replace[song_rank], canada_list[0][song_rank])
            song_rank = song_rank + 1

        # Replace each song image in HTML template
        extra_rank = 0
        for item in extra_replace:
            html_code = html_code.replace(extra_replace[extra_rank], videos_previous[extra_rank])
            extra_rank = extra_rank + 1

        # Replace link at bottom of page
        html_code = html_code.replace('***LINK***',  '/IFB104 ASSIGNMENT 2/canadasingles.html')
        html_code = html_code.replace('***LINKTEXT***',  '/IFB104 ASSIGNMENT 2/canadasingles.html')
        
        # Write the HTML code to a Unicode text file
        html_doc = open(title_top + '.html', 'w', encoding = 'UTF-8')
        html_doc.write(html_code)
        html_doc.close()

# Export current Canada charts Page
def btn6_export():
        # Set title
        title_canada_current = 'Current Canada Top Singles'
        # Canada charts logo
        img = '<img src="canada2.PNG" alt="canadalogo" height="300" width="300">'
        # Set date 
        date = str(', '.join(date_canada_current))
        
        # Replace the blanks in the HTML template
        html_code = html_template.replace('***TITLE***', title_canada_current)
        html_code = html_code.replace('***DATE***', date)
        html_code = html_code.replace('***IMG***', img)
        html_code = html_code.replace('***EXTRA***', 'Music Video')

        # Replace each song name in HTML template
        song_rank = 0
        for song in songs_replace:
            html_code = html_code.replace(songs_replace[song_rank], current_list_canada[0][song_rank])
            song_rank = song_rank + 1

        # Replace each song image in HTML template
        extra_rank = 0
        for item in extra_replace:
            html_code = html_code.replace(extra_replace[extra_rank], videos_current[extra_rank])
            extra_rank = extra_rank + 1

        # Replace link at bottom of page
        html_code = html_code.replace('***LINK***',  'https://acharts.co/canada_singles_top_100')
        html_code = html_code.replace('***LINKTEXT***',  'https://acharts.co/canada_singles_top_100')
        
        # Write the HTML code to a Unicode text file and close
        close_and_write(html_code)

#-------------------------Store data in database --------------------------------#

# Commit changes to database and close connection
def commit_and_save(connect, database):
    connect.commit()
    database.close()
    connect.close()
        
# Insert previous Officalcharts values into database
def btn1_save():
    connection = connect(database = 'top_ten.db')
    top_ten_db = connection.cursor()
    for order in range(10):
        orders = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        top_ten_db.execute("""INSERT INTO top_ten(publication_date, ranking, item, main_attribute)
                                    VALUES(?, ?, ?, ?)""", (str(date_previous[0]), str(orders[order]), str(official_list_previous[order]), str(official_list_img[0][order])))
    commit_and_save(connection, top_ten_db) # Commit changes 

# Insert current Officalcharts values into database
def btn2_save():
    connection = connect(database = 'top_ten.db')
    top_ten_db = connection.cursor()
    for order in range(10):
        orders = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        top_ten_db.execute("""INSERT INTO top_ten(publication_date, ranking, item, main_attribute)
                                    VALUES(?, ?, ?, ?)""", (str(date_current[0]), str(orders[order]), str(official_list_current[order]), str(official_list_img_cur[0][order])))
    commit_and_save(connection, top_ten_db)# Commit changes 


# Insert previous aria charts values into database
def btn3_save():
    connection = connect(database = 'top_ten.db')
    top_ten_db = connection.cursor()
    for order in range(10):
        orders = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        top_ten_db.execute("""INSERT INTO top_ten(publication_date, ranking, item, main_attribute)
                                    VALUES(?, ?, ?, ?)""", (str(date_aria_previous[0]), str(orders[order]), str(aria_list[0][order]), str(previous_artists[0][order])))
    commit_and_save(connection, top_ten_db)# Commit changes 


# Insert current aria charts values into database
def btn4_save():
    connection = connect(database = 'top_ten.db')
    top_ten_db = connection.cursor()
    for order in range(10):
        orders = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        top_ten_db.execute("""INSERT INTO top_ten(publication_date, ranking, item, main_attribute)
                                    VALUES(?, ?, ?, ?)""", (str(date_aria_current[0]), str(orders[order]), str(current_list_aria[0][order]), str(current_artists[0][order])))
    commit_and_save(connection, top_ten_db)


# Insert previous Canada charts values into database
def btn5_save():
    connection = connect(database = 'top_ten.db')
    top_ten_db = connection.cursor()
    for order in range(10):
        orders = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        top_ten_db.execute("""INSERT INTO top_ten(publication_date, ranking, item, main_attribute)
                                    VALUES(?, ?, ?, ?)""", (str(date_canada[0]), str(orders[order]), str(canada_list[0][order]), str("https://acharts.co"+videos[0][order])))
    commit_and_save(connection, top_ten_db)# Commit changes 


# Insert current Canada charts values into database
def btn6_save():
    connection = connect(database = 'top_ten.db')
    top_ten_db = connection.cursor()
    for order in range(10):
        orders = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        top_ten_db.execute("""INSERT INTO top_ten(publication_date, ranking, item, main_attribute)
                                    VALUES(?, ?, ?, ?)""", (str(date_canada_current[0]), str(orders[order]), str(current_list_canada[0][order]), str("https://acharts.co"+videos_current[0][order])))
    commit_and_save(connection, top_ten_db)# Commit changes 

    
#--------------------- Place Preview, Export & Save Buttons----------------------#
    
preview_button = Button(main_menu, text = 'Preview', font = ('Arial', 15), command = preview_controller)
preview_button.place(x=15,y=310)

export_button = Button(main_menu, text = 'Export', font = ('Arial', 15), command = export_controller)
export_button.place(x=110,y=310)

save_button = Button(main_menu, text = 'Save', font = ('Arial', 15), command = save_controller)
save_button.place(x=60,y=355)






