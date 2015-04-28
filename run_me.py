import html_generator
import notes

oop = notes.Concept("OOP, Yeah You Know Me!",
                        "<strong>Object Oriented Programming</strong> is a means of abstraction which greatly increases the programmer's ability to avoid repetition.  What does that mean?  Well, let's say you have a programmer named <a href='http://en.wikipedia.org/wiki/Demiurge'>Demi</a>, and she wants to write a program called existence.py.  Well, she could then set about writing code for every individual being and thing in existence.  However that doesn't sound too efficient, now does it?",
                        "https://cdn.tutsplus.com/gamedev/authors/legacy/Steven%20Lambert/2012/10/28/object-oriented-programming-gamedev.png")

classes = notes.Concept("Classes: On Platonic Idealism",
                     "When Demi is writing her program she gets excited to have horses.  She likes horses, and her existence is gonna have 'em (she plans on marketing her game to <a href='http://www.urbandictionary.com/define.php?term=Brony'>Bronies</a>).  Now, when she's thinking about how to go about coding her horses she starts thinking about how horses are, for the most part, very similar and she'd basically have to re-write very similar chunks of code over and over.  What if she used a template called Equus_ferus_caballus?  This template could have all the common features of horse already outlined, and then whenever she needed a new <strong>object</strong> or horse she could just make an <strong>instance</strong> of it with this...  <strong>class</strong>.  This idea of a template is a class in programming.  Plato deserves royalties.",
                     "images/plato.jpg")

instances = notes.Concept("Instances: Exploring Your Uniqueness",
                     "So, class instances have some nifty features.  First, when we create an instance of a class we're actually calling the __init__() function inside of the class, which is known as the class' <strong>constructor</strong>.  Now, let's we're still working with that horse class, and we want horses that have different colors.  We can have <strong>instance variables</strong> that could define an individual instance's color when we create the instance.  We could even make some weird horse that's has colors like some weird horse-zebra chimera.  What's more, we can have variables that all instances can share called <strong>class variables</strong>.  And finally, let's say we want our horses to be able to whinny.  We can have an <strong>instance method</strong> called whinny() that is basically a function that instances of the horse class would be able to do.",
                     "http://www.wired.com/images_blogs/underwire/images/2007/07/05/0102090491100.jpg")

modules = notes.Concept("Modular Modules",
                     "Now, let's say that Demi has a programmer friend <a href='http://en.wikipedia.org/wiki/Mara_(demon)'>Mara</a>, and Mara wants to write her own existence program, but she wants to use Demi's horse class.  She tells Demi to save it as a separate file from her existence.py file, call it life.py, and now they can import it into their separate existences.  This life.py is now a <strong>module</strong> that they can both use in their individual programs.",
                     "https://s-media-cache-ak0.pinimg.com/236x/00/4c/b4/004cb4b550cb81ab9af24df33fd3164e.jpg")

inheritance = notes.Concept("Inheriting from Parent to Child",
                     "Mara didn't want to leave Demi's work alone.  Mara wants ponies.  She wants it to have the same features of horse, but also have a instance variable for cuteness.  So, Mara creates a child class to Demi's parent horse class by including a call to the horse class constructor in the pony class constructor.  This allows the child to inherit all the features of the parent class, like color and the ability to whinny().  This is known as <strong>inheritance</strong>.Lastly, let's say we want the pony's whinny to be a little different from her dad's.  We can re-create the whinny() function inside of the child class.  When we do this and call the function on a child instance, then the child version will be used.  This is called <strong>method overriding</strong>.  Now, ponies can whinny and be cute while doing it.  Bronies are probably excited somewhere.",
                     "images/horse_pony.jpg")


class_notes = [oop, classes, instances, modules, inheritance]
html_generator.open_notes_page(class_notes)
