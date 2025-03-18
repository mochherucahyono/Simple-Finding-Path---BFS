from collections import deque
def bfs_shortest_path(city_map, start, goal):
    queue = deque([(start,[start])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        
        if current not in visited:
            visited.add(current)
            for neighbor in city_map.get(current,[]):
                queue.append((neighbor, path + [neighbor]))

    return None

city_map = {
    'Home':['Mall','School'],
    'Mall':['Gym','Hospital'],
    'School' : ['Library'],
    'Gym':['Hospital'],
    'Library':['Hospital'],
    'Hospital':[],
}

shortest_path = bfs_shortest_path(city_map, 'Home', 'Hospital')
print("Shortest path:", shortest_path)
