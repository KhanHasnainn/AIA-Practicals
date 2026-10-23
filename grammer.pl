

sentence --> subject, verb, noun_phrase, prep_phrase.


subject --> pronoun.
pronoun --> [i]; [you]; [we]; [they].


verb --> [am]; [are]; [was]; [were].


noun_phrase --> determiner, noun.
noun_phrase --> noun.


determiner --> [a]; [the].
noun --> [student]; [students].


prep_phrase --> preposition, proper_noun.
preposition --> [of].
proper_noun --> [rj].





Output:-?- phrase(sentence, [i,am,a,student,of,rj]).
true.
