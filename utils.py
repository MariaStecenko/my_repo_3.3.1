from figures import *

def parse_figure(line: str) -> Figure:
    tokens = line.strip().split()
    name, params = tokens[0], list(map(float, tokens[1:]))

    match name:
        case 'Triangle': return Triangle(*params)
        case 'Rectangle': return Rectangle(*params)
        case 'Trapeze': return Trapeze(*params)
        case 'Parallelogram': return Parallelogram(*params)
        case 'Circle': return Circle(*params)
        case 'Ball': return Ball(*params)
        case 'TriangularPyramid': return TriangularPyramid(*params)
        case 'QuadrangularPyramid': return QuadrangularPyramid(*params)
        case 'RectangularParallelepiped': return RectangularParallelepiped(*params)
        case 'Cone': return Cone(*params)
        case 'TriangularPrism': return TriangularPrism(*params)
        case _: raise ValueError(f"Unknown figure: {name}")

