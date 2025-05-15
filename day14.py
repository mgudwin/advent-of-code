"""Day 14"""

_FILE = "Inputs/day14_input.txt"
# _FILE = "Inputs/day14_example.txt"


class Robots:
    """Beep boop"""

    def __init__(self) -> None:
        self.robot = {}
        # self.board_dims = [7, 11]
        self.board_dims = [103, 101]
        self.elapsed_time = 100

    def read_input(self, _file):
        """I like to read"""
        with open(_file, "r", encoding="utf-8") as _f:
            contents = _f.read()
        for i, line in enumerate(contents.split("\n")[:-1]):
            _position, _velocity = line.split(" ")
            _position = tuple([int(p) for p in _position.split("=")[1].split(",")])
            _velocity = tuple([int(v) for v in _velocity.split("=")[1].split(",")])
            self.robot[i] = {"pos": _position, "vel": _velocity}

    def print_robots(self):
        """Out of ink"""
        print("Beep Beep Boop Beep")
        for robot_id in self.robot:
            print(
                f"Robot {robot_id: < 5}  Position: {self.robot[robot_id]['pos']} Velocity: {self.robot[robot_id]['vel']}"
            )

    def get_quadrant(self, point):
        """get quadrant"""
        dims = self.board_dims
        horizontal_divider = dims[0] // 2
        vertical_divider = dims[1] // 2
        # top 2 quads
        if point[0] < horizontal_divider:
            if point[1] < vertical_divider:
                return 1
            if point[1] > vertical_divider:
                return 2
        elif point[0] > horizontal_divider:
            if point[1] < vertical_divider:
                return 3
            if point[1] > vertical_divider:
                return 4
        return None

    def calculate_position(self, robot_id, seconds):
        """Calculate position after 100s and then div by width"""
        start_position = self.robot[robot_id]["pos"]
        velocity = self.robot[robot_id]["vel"]
        end_position = (
            (start_position[0] + (velocity[0] * seconds)) % self.board_dims[0],
            (start_position[1] + (velocity[1] * seconds)) % self.board_dims[1],
        )
        quadrant = self.get_quadrant(end_position)
        self.robot[robot_id]["quadrant"] = quadrant
        print(
            f"Started at {start_position}, ended at {end_position}, in quadrant {quadrant}"
        )

    def predict_motion(self, seconds=100):
        """Put it all together"""
        q1_sum = 0
        q2_sum = 0
        q3_sum = 0
        q4_sum = 0
        for robot_id in self.robot:
            self.calculate_position(robot_id, seconds)
            quadrant = self.robot[robot_id]["quadrant"]
            match quadrant:
                case 1:
                    q1_sum += 1
                case 2:
                    q2_sum += 1
                case 3:
                    q3_sum += 1
                case 4:
                    q4_sum += 1
        print("")
        print("Calculated...Quadrant Counts are:")
        print(f"Q1:\t{q1_sum}")
        print(f"Q2:\t{q2_sum}")
        print(f"Q3:\t{q3_sum}")
        print(f"Q4:\t{q4_sum}")
        print("=============================")
        print(f"Safety Factor is {q1_sum * q2_sum * q3_sum * q4_sum}")
        print("=============================")


robot = Robots()
robot.read_input(_FILE)
robot.predict_motion()
# robot.calculate_position(0)
