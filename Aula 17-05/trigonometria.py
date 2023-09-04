def hip(catO, catA):
    return (catO**2 + catA**2)**0.5
def seno(catO, catA):
    h = hip(catO, catA)
    return catO/h
def cosseno(catO, catA):
    h = hip(catO, catA)
    return catA/h
def tang(catO, catA):
    return seno(catO, catA) / cosseno(catO, catA)
