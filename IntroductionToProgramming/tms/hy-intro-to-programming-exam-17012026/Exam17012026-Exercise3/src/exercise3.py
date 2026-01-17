# Write your solution to exercise 3 here
def read_points():
    result: list[tuple] = []
    with open("./statistics.txt", "r") as file:
        for line in file:
            line = line.strip()
            team, points = line.split(":")
            try:
                points = [int(point) for point in points.split("-")]
            except:
                raise ValueError(f"Invalid format in the file: {line}")
            total = 3 * points[0] + points[2]
            result.append((team, total))
    return result


print(read_points())
