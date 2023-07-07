from matplotlib import pyplot as plt
import re
from shapely import Polygon
import geopandas as gpd
from shapely.ops import unary_union

test = False
range_limit = 20 if test else 4000000
bounding_box = Polygon(
    ((0, 0), (0, range_limit), (range_limit, range_limit), (range_limit, 0))
)
input_file = "test_input.txt" if test else "input.txt"
puzzle_input = open(input_file, "r").read().splitlines()


def calculate_manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


polygons = []
for line in puzzle_input:
    sx, sy, bx, by = map(
        int,
        re.findall(
            r".*x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)",
            line,
        )[0],
    )
    s, b = (sx, sy), (bx, by)
    distance = calculate_manhattan_distance(s, b)

    coordinates = (
        (s[0] - distance, s[1]),
        (s[0], s[1] - distance),
        (s[0] + distance, s[1]),
        (s[0], s[1] + distance),
    )
    polygons.append(Polygon(coordinates))

polygon_union = unary_union(polygons)

difference = bounding_box.difference(polygon_union)

gpd.GeoSeries(polygons).boundary.plot()
gpd.GeoSeries([polygon_union, bounding_box]).boundary.plot()
gpd.GeoSeries(difference).boundary.plot()
centroid = difference.centroid
print("centroid:", centroid.x, centroid.y)
print("tuning frequency: ", centroid.x * 4000000 + centroid.y)


plt.show()
