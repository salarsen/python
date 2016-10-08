import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin",  "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

    return_str = []
    for word_search in words:
#        print regex + " - " + word_search
        if re.search(regex,word_search):
            return_str.append(word_search) #[word for word in words if re.search(regex, word)

    return (regex,return_str)

#print get_matching_words("v")
#print get_matching_words("ss")
#print get_matching_words("e$")
# print get_matching_words("b.b")
# print get_matching_words("b.*.b")
# print get_matching_words("b.*b")
# print get_matching_words("a.*e.*i.*o.*u")
#print get_matching_words("r*e*g*u*l*a*r*e*x*p*r*e*s*s*i*o*n")
print get_matching_words(r"((\w)\2)") # this will pull numbers too
print get_matching_words(r"(([a-z])\2)") # this will only pull lowercase characters
