
import wikipedia

def wiki_search(name):

    wikipedia.search(name)

    ny = wikipedia.page(name)
    print ny.title

    info = ny.content
    first_paragraph=[]
    for things in info:





        if things != "=":

            first_paragraph.append(things.encode("ascii"))
        else:
            break



#    print ny.image
    print "".join(first_paragraph)

wiki_search(name)