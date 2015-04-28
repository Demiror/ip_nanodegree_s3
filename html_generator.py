import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Plato Was Classist</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }

        .concept-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .concept-tile:hover {
            background-color: #EEE;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>

</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Intro to Programming: Stage 3</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {concept_tiles}
    </div>
  </body>
</html>
'''

# A single concept entry html template
concept_tile_content = '''
<div class="col-md-6 col-lg-4 concept-tile text-center">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{concept_title}</h2>
    <p>{concept_description}<p>
</div>
'''

def create_concept_tiles_content(concepts):
    # The HTML content for this section of the page
    content = ''
    for concept in concepts:

        # Append the tile for the concept with its content filled in
        content += concept_tile_content.format(
            concept_title=concept.title,
            concept_description=concept.description,
            poster_image_url=concept.poster_image_url,
        )
    return content

def open_notes_page(concepts):
  # Create or overwrite the output file
  output_file = open('class_notes.html', 'w')

  # Replace the placeholder for the concept tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(concept_tiles=create_concept_tiles_content(concepts))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible