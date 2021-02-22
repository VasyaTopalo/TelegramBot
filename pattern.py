
def pattern(message):
    templates = ['привіт', 'скільки буде', 'який курс євро', 'який курс долара', 'який курс рубля', 'скажи мені курси валют', 'яка погода в']
    m = [i for i in message]
    m2 = [None]
    m2.extend(m)

    for i in templates:
        index = templates.index(i)
        template = [j for j in i]
        template2 = [j for j in i]

        c = 0
        c2 = 0

        for j in range(0, len(template)):
            if len(m) > len(template):
                while len(template) != len(m):
                    template.append(None)
            elif len(m) < len(template):
                while len(m) != len(template):
                    m.append(None)

            if template[j] == m[j]:
                c += 1

        c = (c * 100) / len(templates[index])
        if c >= 75:
            return templates[index]

        for j in range(0, len(template2)):
            if len(m2) > len(template2):
                while len(template2) != len(m2):
                    template2.append(None)
            elif len(m2) < len(template2):
                while len(m2) != len(template2):
                    m2.append(None)

            if template2[j] == m2[j]:
                c2 += 1
        c2 = (c2 * 100) / len(templates[index])

        if c2 >= 75 :
            return templates[index]

