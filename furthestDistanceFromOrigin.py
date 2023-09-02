class Solution:
    # A bit faster but uses a bit more memory
    def furthestDistanceFromOrigin1(self, moves: str) -> int:
        currentDirection = 0
        jokerMoveCount = 0
        for i in range(len(moves)):
            if moves[i] == "L":
                currentDirection -= 1
            elif moves[i] == "R":
                currentDirection += 1
            else:
                jokerMoveCount += 1

        return abs(currentDirection) + jokerMoveCount

    # A bit slower but uses less memory
    def furthestDistanceFromOrigin2(self, moves: str) -> int:
        return abs(moves.count("R") - moves.count("L")) + moves.count("_")
