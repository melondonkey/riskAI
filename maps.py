#Define the graph structure of the board
classic_map = {'Alaska': ['Northwest Territory', 'Alberta', 'Kamchatka'],
         'Alberta': ['Alaska', 'Northwest Territory', 'Ontario', 'Western United States' ],
         'Central America': ['Western United States','Eastern United States' ],
         'Eastern United States': ['Ontario','Quebec','Western United States', 'Central America' ], 
         'Greenland': ['Northwest Territory','Ontario','Quebec', 'Iceland' ], 
         'Northwest Territory': ['Alaska','Greenland','Alberta','Ontario' ],
         'Ontario': ['Western United States','Northwest Territory','Greenland','Alberta','Quebec','Eastern United States' ],
         'Quebec': ['Greenland','Ontario','Eastern United States' ],
         'Western United States': ['Alberta','Ontario','Eastern United States', 'Central America' ], 
         
         'Argentina': ['Peru', 'Brazil' ],
         'Brazil': ['Venezuela', 'Peru', 'Argentina', 'North Africa' ],
         'Peru': ['Venezuela', 'Brazil', 'Argentina' ],
         'Venezuela': ['Central America', 'Peru', 'Brazil' ],
         
         'Great Britain': ['Iceland', 'Western Europe','Scandanavia', 'Northern Europe' ],
         'Iceland': ['Greenland', 'Great Britain', 'Scandanavia' ],
         'Northern Europe': ['Great Britain', 'Scandanavia', 'Ukraine','Southern Europe', 'Western Europe' ],
         'Scandanavia': ['Iceland', 'Ukraine','Northern Europe','Great Britain' ],
         'Southern Europe': ['Northern Europe','Ukraine','Middle East','Western Europe' ],
         'Ukraine': ['Scandanavia', 'Northern Europe','Middle East', 'Afghanistan','Ural','Southern Europe' ],
         'Western Europe': [ 'North Africa','Northern Europe', 'Southern Europe', 'Great Britain'],
         
         'Congo': ['North Africa', 'East Africa', 'South Africa' ],
         'East Africa': ['North Africa', 'Egypt', 'Middle East', 'Madagascar', 'Congo', 'South Africa' ],
         'Egypt': ['Southern Europe','Middle East','East Africa','North Africa' ],
         'Madagascar': ['South Africa','East Africa' ],
         'North Africa': ['Brazil','Western Europe','Egypt','East Africa','Congo' ],
         'South Africa': [ 'Madagascar','Congo','East Africa'],
         
         'Afghanistan': ['Middle East', 'Ukraine','Ural','China', 'India' ],
         'China': ['Ural', 'Siberia', 'Mongolia', 'Siam', 'India', 'Afghanistan' ],
         'India': ['Middle East', 'Afghanistan', 'China', 'Siam' ],
         'Irkutsk': ['Siberia', 'Yakutsk', 'Kamchatka', 'Mongolia' ],
         'Japan': ['Kamchatka', 'Mongolia' ],
         'Kamchatka': ['Alaska', 'Japan', 'Yakutsk', 'Irkutsk', 'Mongolia' ],
         'Middle East': ['Egypt', 'Southern Europe', 'Afghanistan', 'India', 'East Africa', 'Ukraine' ],
         'Mongolia': ['Siberia', 'Irkutsk', 'Kamchatka', 'Japan','China' ],
         'Siam': ['Indonesia', 'India', 'China' ],
         'Siberia': ['Ural','Yakutsk','Irkutsk','Mongolia', 'China' ],
         'Ural': ['Ukraine','Afghanistan','China','Siberia' ],
         'Yakutsk': ['Siberia','Irkutsk','Kamchatka' ],
         
         'Eastern Australia': ['Western Australia', 'New Guinea' ],
         'Indonesia': ['Siam','New Guinea','Western Australia' ],
         'New Guinea': ['Indonesia','Eastern Australia', 'Western Australia' ],
         'Western Australia': ['Indonesia', 'New Guninea', 'Eastern Australia' ]}
         
#Utility functions for graph traversal.  Source(http://www.python.org/doc/essays/graphs.html)
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None



def find_shortest_path(graph, start, end, path=[]):
    """Returns the shortest path from node START to node END"""
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
    
def find_all_paths(graph, start, end, path=[]):
    """Returns all paths from node START to node END"""
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
