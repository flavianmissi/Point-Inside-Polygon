class Polygon(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def get_number_of_intersected_sides(self, test_point):
        crossed_by_left = 0; crossed_by_right = 0
        for i in range(1, len(self.coordinates)):
            if test_point[1] in range(self.coordinates[i-1][1], self.coordinates[i][1]+1) or test_point[1] in range(self.coordinates[i][1], self.coordinates[i-1][1]+1):
                if test_point[0] > self.coordinates[i-1][0] and test_point[0] > self.coordinates[i][0]:
                    crossed_by_left += 1
                else:
                    crossed_by_right += 1
        return {"left" : crossed_by_left, "right" : crossed_by_right}

    def belongs_to_polygon(self, test_point):
        crossed = self.get_number_of_intersected_sides(test_point)
        return crossed["left"] % 2 != 0 and crossed["right"] % 2 != 0
