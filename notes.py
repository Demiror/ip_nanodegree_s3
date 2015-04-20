import webbrowser

class Concept():
    def __init__(self, concept_title, concept_description, concept_image, concept_youtube):
        self.title = concept_title
        self.description = concept_description
        self.concept_image_url = concept_image
        self.concept_youtube_url = concept_youtube

    def show_trailer(self):
        webbrowser.open(self.concept_youtube_url)
