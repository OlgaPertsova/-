def index():
    with open('temples\index.html') as temples:
        return temples.read()

def blog():
    with open('temples\blog.html') as temples:
        return temples.read()
