import en as en
import string

__author__ = 'User'


PRP = {
    'I': 'me',
    'he': 'him',
    'she': 'her',
    'we': 'us',
    'they': 'them',
}

single_singular_verbs_dict = {
    'is': 'are',
    'was': 'were',
}

plural_singular_verbs_dict = {
    'are': 'is',
    'were': 'was',
}

singular_verbs = {
    "is", "are", "were", "was", "the", "be", "am"
}

verb_types = {
    "VBD", "VB", "VBP", "VBG", "VBG", "VBZ"
}


noun_types = {
    "NN", "PRP", "NNS", "NNP"
}


"""
"""
def cleanText(sen):
    for ch in string.punctuation:
        sen = sen.replace(ch, '')
    return sen


"""
Gets a sentence (that contains a tmura) and writes it into the tmura.txt file, so we will have a corpus
"""
def writeToOurCorpus(sentence):
    text_file = open("tmura.txt", "a")
    text_file.write(sentence + "\n")
    text_file.close()


"""
"""
def get_word_past_participle(word):
    return en.verb.past_participle(word)


"""
"""
def get_passive_word_present_participle(word):
    return get_word_past_participle(en.verb.past(word)) #No it is not a mistake- it is the same


"""
"""
def make_string(list):
    return " ".join(str(x) for x in list)


"""
"""
def switch_PRP(sent, noun):
    if noun.lower() in PRP:
        newnNoun = PRP[noun.lower()]
        sent[sent.index(noun)] = newnNoun
        noun = newnNoun
    return sent, noun


"""
"""
def find_switching_Parts(sent):
    parsed = en.sentence.tag(sent)
    dt = False
    i1 = 0
    i2 = 0
    shortPart = ""
    list = []
    for word in parsed:
        if (word[1] == "DT"):
            dt = True
        if (word[1] in noun_types):
            shortPart += word[0]
            list.append(shortPart)
            shortPart = ""
            dt = False
        if dt == True:
            shortPart += word[0] + " "
    return list


"""
"""
def find_first_noun(sent):
    parsed = en.sentence.tag(sent)
    for word in parsed:
        if (word[1] in noun_types):
            return word[0]
    return "Didn't find"


"""
"""
def find_first_verb(sent):
    parsed = en.sentence.tag(sent)
    for word in parsed:
        if word[1] in verb_types and word[0] not in singular_verbs:
            return word[0]
    return "Didn't find"


"""
"""
def find_first_verb_third_singular(sent):
    parsed = en.sentence.tag(sent)
    for word in parsed:
        if (word[1] in verb_types) and (word[0] not in singular_verbs):
            return word[0]
    return "Didn't find"


"""
"""
def third_singular_past_turn_to_passive(sent):
    sent = sent.lower()
    list = find_switching_Parts(sent)
    if len(list) != 2:
        return list

    firstNoun = find_first_noun(list[0])
    secondNoun = find_first_noun(list[1])
    sent = sent.replace(list[1], list[0], 1)
    sent = sent.replace(list[0], list[1], 1)
    verb = find_first_verb(sent)
    sent = sent.replace(verb, get_word_past_participle(verb))
    verb = find_first_verb_third_singular(sent)
    newSent = sent.split()
    newSent, firstNoun = switch_PRP(newSent, list[0])
    splited1 = firstNoun.split()
    splited2 = secondNoun.split()
    newSent.insert(newSent.index(splited2[0]) + 1, "was")
    newSent.insert(newSent.index(splited1[0]), "by")
    newSent = make_string(newSent)
    newSent = newSent.replace(newSent[0], newSent[0].upper(), 1)
    return newSent

"""
"""
def present_turn_to_passive(sent):
    sent = sent.lower()
    list = find_switching_Parts(sent)
    if len(list) != 2:
        return list

    firstNoun = find_first_noun(list[0])
    secondNoun = find_first_noun(list[1])
    sent = sent.replace(list[1], list[0], 1)
    sent = sent.replace(list[0], list[1], 1)
    verb = find_first_verb(sent)
    sent = sent.replace(verb, get_passive_word_present_participle(verb))
    verb = find_first_verb_third_singular(sent)
    newSent = sent.split()
    newSent, firstNoun = switch_PRP(newSent, list[0])
    splited1 = firstNoun.split()
    splited2 = secondNoun.split()
    newSent.insert(newSent.index(splited2[0]) + 2, "being")
    newSent.insert(newSent.index(splited1[0]), "by")
    newSent = make_string(newSent)
    newSent = newSent.replace(newSent[0], newSent[0].upper(), 1)
    return newSent


"""
"""
def future_turn_to_passive(sent):
    sent = sent.lower()
    list = find_switching_Parts(sent)
    if len(list) != 2:
        return list

    firstNoun = find_first_noun(list[0])
    secondNoun = find_first_noun(list[1])
    sent = sent.replace(list[1], list[0], 1)
    sent = sent.replace(list[0], list[1], 1)
    verb = find_first_verb(sent)
    sent = sent.replace(verb, get_passive_word_present_participle(verb))
    verb = find_first_verb_third_singular(sent)
    newSent = sent.split()
    newSent, firstNoun = switch_PRP(newSent, list[0])
    splited1 = firstNoun.split()
    splited2 = secondNoun.split()
    newSent.insert(newSent.index(splited2[0]) + 2, "be")
    newSent.insert(newSent.index(splited1[0]), "by")
    newSent = make_string(newSent)
    newSent = newSent.replace(newSent[0], newSent[0].upper(), 1)
    return newSent


"""
"""
def third_singular_present_turn_to_passive(sent):
    sent = sent.lower()
    list = find_switching_Parts(sent)
    firstNoun = find_first_noun(list[0])
    secondNoun = find_first_noun(list[1])
    sent = sent.replace(list[1], list[0], 1)
    sent = sent.replace(list[0], list[1], 1)
    verb = find_first_verb_third_singular(sent)
    sent = sent.replace(verb, get_passive_word_present_participle(verb))
    verb = find_first_verb_third_singular(sent)
    newSent = sent.split()
    newSent, firstNoun = switch_PRP(newSent, list[0])
    splited1 = firstNoun.split()
    splited2 = secondNoun.split()
    newSent.insert(newSent.index(splited2[0]) + 1, "is")
    newSent.insert(newSent.index(splited1[0]), "by")
    newSent = make_string(newSent)
    newSent = newSent.replace(newSent[0], newSent[0].upper(), 1)
    return newSent


"""
"""
def past_turn_to_passive(sent):
    sent = sent.lower()
    list = find_switching_Parts(sent)
    firstNoun = find_first_noun(list[0])
    secondNoun = find_first_noun(list[1])
    sent = sent.replace(list[1], list[0], 1)
    sent = sent.replace(list[0], list[1], 1)
    verb = find_first_verb_third_singular(sent)
    sent = sent.replace(verb, get_passive_word_present_participle(verb))
    verb = get_passive_word_present_participle(verb)
    newSent = sent.split()
    newSent, firstNoun = switch_PRP(newSent, list[0])
    splited1 = firstNoun.split()
    splited2 = secondNoun.split()
    if (en.sentence.tag(secondNoun)[0][1] == "NNS") and newSent[newSent.index(verb) - 1] in single_singular_verbs_dict:
        newSent[newSent.index(verb) - 1] = single_singular_verbs_dict[newSent[newSent.index(verb) - 1]]
    elif (en.sentence.tag(secondNoun)[0][1] != "NNS") and newSent[newSent.index(verb) - 1] in plural_singular_verbs_dict:
        newSent[newSent.index(verb) - 1] = plural_singular_verbs_dict[newSent[newSent.index(verb) - 1]]
    newSent.insert(newSent.index(splited1[0]), "by")
    newSent = make_string(newSent)
    newSent = newSent.replace(newSent[0], newSent[0].upper(), 1)
    return newSent


"""
"""
def third_singular_future_turn_to_passive(sent):
    sent = sent.lower()
    list = find_switching_Parts(sent)
    if len(list) != 2:
        return list

    firstNoun = find_first_noun(list[0])
    secondNoun = find_first_noun(list[1])
    sent = sent.replace(list[1], list[0], 1)
    sent = sent.replace(list[0], list[1], 1)
    verb = find_first_verb_third_singular(sent)
    sent = sent.replace(verb, en.verb.past_participle(verb))
    verb = find_first_verb_third_singular(sent)
    newSent = sent.split()
    newSent, firstNoun = switch_PRP(newSent, list[0])
    splited1 = firstNoun.split()
    splited2 = secondNoun.split()
    #newSent.insert(newSent.index(splited2[0]) + 2, "be")
    newSent.insert(newSent.index(splited1[0]), "by")
    newSent = make_string(newSent)
    newSent = newSent.replace(newSent[0], newSent[0].upper(), 1)
    return newSent


"""
    Checks if we have 2 nound and 1 verbs- so we can cahnge it from active to passive.
"""
def can_I_convert_frome_active_to_passive(sent):
    nouns = 0
    verbs = 0
    theVerb = ""
    for word in en.sentence.tag(sent):
        verbs += (word[1] in verb_types and word[0] not in singular_verbs)
        nouns += (word[1] in noun_types)
    return (nouns == 2 and verbs == 1)


def turn_to_passive(sent):
    if can_I_convert_frome_active_to_passive(sent) == False:
        return "None"

    had_singulat = ""
    verb = ""
    for word in en.sentence.tag(sent):
        if (word[1] in verb_types and word[0] not in singular_verbs):
            verb = word[0]
        if word[0] in singular_verbs and (en.verb.tense(word[0]) == "1st singular past" or en.verb.tense(word[0]) == "past plural"):
            had_singulat = "past"
        elif word[0] in singular_verbs and (en.verb.tense(word[0]) == "3rd singular present" or en.verb.tense(word[0]) == "2nd singular present" or en.verb.tense(word[0]) == "1st singular present"):
            had_singulat = "present"
        elif word[0] in singular_verbs and en.verb.tense(word[0]) == "infinitive":
            had_singulat = "future"

    if (en.verb.is_present(verb) or en.verb.tense(verb) == "infinitive") and had_singulat != "":
        if had_singulat == "past":
            return past_turn_to_passive(sent)
        elif had_singulat == "present":
            return present_turn_to_passive(sent)
        elif had_singulat == "future":
            return third_singular_future_turn_to_passive(sent)
    else:
        if en.verb.is_past(verb):
            return third_singular_past_turn_to_passive(sent)
        elif en.verb.is_present(verb):
            return third_singular_present_turn_to_passive(sent)
        elif en.verb.tense(verb) == "infinitive":
            return future_turn_to_passive(sent)
    return ""


def main():
    sent = "Obama will be eating an apple"
    if can_I_convert_frome_active_to_passive(sent) == True:
        print "org = " + sent
        print "new = " + turn_to_passive(sent)


"""
    #sent2 = "David washed his new car"
    sent3 = "He eats the smart and sexy sandwich every week"

    sent = cleanText(sent)
    sent3 = cleanText(sent3)

"""

"""with open("newSent.txt", 'w') as newF:
    with open("sentences.txt", 'r') as f:
        sentence = f.read()
    f.close()
    sentences = sentence.split('\n')
    for sent in sentences:
        print(change_sentence(sent))
        newF.write(change_sentence(sent) + "\n")

newF.close()"""


if __name__ == '__main__':
    main()
