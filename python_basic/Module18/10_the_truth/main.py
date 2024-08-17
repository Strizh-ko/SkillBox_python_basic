def replacement(word, sym1, sym2):
    while sym1 in word:
        word_list = [sym2 if char == sym1 else char for char in word]
        word = ''.join(word_list[:])
    return word

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
text = text.upper()

message_index = [alphabet.index(char) if char in alphabet else char for char in text]
new_message = ""
for char_i in message_index:
    if char_i in range(26):
        new_message += alphabet[(char_i + 25) % 26]
    else:
        new_message += char_i

new_message_list = new_message.split()
sentence = []
shift = 3
for word in new_message_list:
    if "+" or "(" in word:
        word = replacement(word, "+", '"')
        word = replacement(word, "(", "'")
    new_word = word[len(word) - shift % len(word):] + word[:len(word) - shift % len(word)]
    if '/' in new_word:
        shift += 1
        new_word = replacement(new_word, "/", ".")
        sentence.append(new_word)
        print(' '.join(sentence))
        sentence = []
    else:
        sentence.append(new_word)
print(' '.join(sentence))