import wikipedia 

# Wikipedia extraction is bug-prone, 
# so the functionality of this class  
# is left out for now 

class WikiExtractor(object):

    def __init__(self):
        pass

    def further_info_on_entity(self, entity):
        url, two_liner = None, None
        try:
            if entity != None:
                two_liner = wikipedia.summary(entity, sentences=2)
                url = wikipedia.page(entity).url
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options
            best_guess = options[0]
            two_liner = wikipedia.summary(best_guess, sentences=2)
            url = wikipedia.page(best_guess).url

        return (url, two_liner)