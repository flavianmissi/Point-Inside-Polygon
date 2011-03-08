class Polygon(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def get_vertical_sides(self):
        vertical_coordinates = []
        for i in range(1, len(self.coordinates)):
            if self.coordinates[i][0] == self.coordinates[i-1][0]:
                vertical_coordinates.append([[self.coordinates[i-1][0], self.coordinates[i-1][1]], [self.coordinates[i][0], self.coordinates[i][1]]])
        return vertical_coordinates

    def get_number_of_intersected_sides(self, test_point):
        crossed_by_left = 0; crossed_by_right = 0
        print self.coordinates
        for i in range(1, len(self.coordinates)):
            if test_point[1] in range(self.coordinates[i-1][1], self.coordinates[i][1]+1) or test_point[1] in range(self.coordinates[i][1], self.coordinates[i-1][1]+1):
                if test_point[0] > self.coordinates[i-1][0] and test_point[0] > self.coordinates[i][0]:
                    crossed_by_left += 1
                else:
                    crossed_by_right += 1
        return {"left" : crossed_by_left, "right" : crossed_by_right}
