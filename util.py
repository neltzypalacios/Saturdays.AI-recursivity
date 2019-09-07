#conda install fire -c conda-forge

def print_name():
    print(__name__)

#Decorador para evitar repetir funciones
def _corner_case_decorator(func):
    def wrap(self, i, j, *args, **kwargs):
        if j>=i or j==0:
            return 1
        return func(self, i=i, j=j, *args, **kwargs)
    return wrap
#Termina decorador

#Decorador 2
def caching(func):
    cache = {}
    def wrapper(self, **kwargs):
        key = hash(frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        cache[key] = func(self, **kwargs)
        return wrapper(self, **kwargs)
    return wrapper
#Termina decorador 2

class TriangleBuilder(object):
    CACHE = {}

    def save(self, i, j, value):
        self.CACHE[(i, j)] = lambda: value
        return value

#Add due decorador
    @_corner_case_decorator
#End due decorador
    def get(self, i, j, default=lambda: None):
        return self.CACHE.get((i, j), default)()

#Add due decorador
    @_corner_case_decorator
#End due decorador
    def create(self, i, j):
## para decorador se quita if... return 1
#Remove due decorador
#        if j>=i or j==0:
#            return 1
#End due decorador
        upper_left = self.get_or_create(i=i-1, j=j-1)
        upper_center = self.get_or_create(i=i-1, j=j)
        return self.save(i=i, j=j, value=upper_center+upper_left)

    def get_or_create(self, i, j):
        return self.get(i, j, default=lambda: self.create(i,j))

    def get_row(self, index):
        return [str(self.get_or_create(index, j)) for j in range(index+1)]
