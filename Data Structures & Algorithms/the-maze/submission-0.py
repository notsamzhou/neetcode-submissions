class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        

        queue = deque([start])
        visited = set()

        while queue:
            r, c = queue.popleft()
            visited.add((r, c))

            if (r, c) == (destination[0], destination[1]):
                return True

            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + direction[0], c + direction[1]
                while 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] == 0:
                     nr, nc = nr + direction[0], nc + direction[1]

                back = (nr - direction[0], nc - direction[1])
                if back != (r, c) and back not in visited:
                    queue.append(back)

        return False

                