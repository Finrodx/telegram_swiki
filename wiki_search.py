
import wikipedia

def wiki_search(name):

    wikipedia.search(name)

    ny = wikipedia.page(name)

    pic = ny.images
    print ny.title

    info = ny.content
    first_paragraph=[]
    for things in info:

        if things != "=":

            first_paragraph.append(things.encode("ascii"))
        else:
            break


    first_paragraph="".join(first_paragraph)
    first_paragraph = first_paragraph.replace("\n", " ")



    return first_paragraph, pic[0]


    wiki_search(name)

