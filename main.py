#triangulo de apscal
#i
#1
#11
#121
#1331
#14641 j

import fire
import logging

from util import TriangleBuilder, caching

logger = logging.getLogger(__name__)

class Main(object):
    builder = TriangleBuilder()

#Add decorador 2
    @caching
#End decorador 2
    def get_element_Recursively(self,i,j):
        return 1 if (j == 0 or j >= i) else \
            self.get_element_Recursively(i=i-1, j=j) + self.get_element_Recursively(i=i-1, j=j-1)

    def pascal_triangle_a(self, level, index=0):
        if index < level:
            row = [str(self.get_element_Recursively(i=index, j=j)) for j in range(index+1)]
            print(" ".join(row))
            self.pascal_triangle_a(level=level, index=index+1)

    def pascal_triangle_b(self,level, index=0):
        if index < level:
            row = self.builder.get_row(index=index)
            print(" ".join(row))
            self.pascal_triangle_b(level=level, index=index+1)

    def print_message(self, content):
        logger.info(content)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Main)
