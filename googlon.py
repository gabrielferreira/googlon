import math

def OrdenaGooglon(s, _sequence):
    return str.join(' ', sorted(set(s.split(' ')), key = lambda a: [_sequence.index(i) for i in a]))

def GetPreposicoes(s, _foo):
    return filter(lambda a: a.__len__() == 3 and (not _foo.__contains__(a[a.__len__() - 1])) and a.find('h') < 0, s.split(' '))

def GetVerbos(s, _foo):
    return filter(lambda a: a.__len__() >= 7 and (not _foo.__contains__(a[a.__len__() - 1])), s.split(' '))

def GetVerbosPrimeiraPessoa(s, _foo):
    return filter(lambda a: _foo.__contains__(a[0]), GetVerbos(s, _foo))

def ConverteParaNumeroGooglon(s, _sequence):
    d = 0
    for i in xrange(s.__len__()):
        n = _sequence.find(s[i])
        d += n * int(math.pow(20, i))
    return d

def GetNumeroGooglon(s, _sequence, min, div):
    a = set(s.split(' '))
    result = []
    for i in a:
        n = ConverteParaNumeroGooglon(i, _sequence)
        if n >= min and (n % div == 0 or n % div == 4):
            result.append(n)
    return result