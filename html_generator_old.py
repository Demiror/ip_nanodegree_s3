class_notes = [['', 
                    ''],
                ]



def generate_concept_HTML(concept_title, concept_description):
    html_concept_title = '''
<div class="col-md-12 drop-shadow">
    <h2 class="concept-title">''' + concept_title + "</h2>"
    
    html_concept_description = '''
    <div class="concept-description">
        ''' + concept_description + '''
    </div>
</div>'''
    
    full_html_text = html_concept_title + html_concept_description
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

def make_HTML_for_many_concepts(list_of_concepts):
    html = '''
<!doctype html>

<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>The Distinct Differences Between OOP and OPP</title>
        <link rel="stylesheet" href="http://normalize-css.googlecode.com/svn/trunk/normalize.css">
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <link rel="stylesheet" href="css/main.css">

    </head>

    <body>
        <div class="container">'''
    for i in list_of_concepts:
        html += make_HTML(i)
    html += '''
        </div>
    </body>
</html>'''
    return html

print make_HTML_for_many_concepts(class_notes)
