# Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.


def points(games):

    point = 0
    for game in games:
        x, y = game.split(':')
        print(x,y)
        if x > y:
            point += 3
        elif x == y:
            point += 1

    return point
print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))