class Song:
    def __init__(self, idx, play):
        self.idx = idx
        self.play = play


class Genre:
    def __init__(self, genre, play):
        self.genre = genre
        self.song_list = list()
        self.total_play = play

    def add_song_list(self, song):
        self.song_list.append(song)

    def add_play(self, play):
        self.total_play += play


def solution(genres, plays):
    genre_dict = dict()
    answer = []

    for i in range(len(genres)):
        if genres[i] in genre_dict.keys():
            this_genre = genre_dict.get(genres[i])
            this_genre.add_song_list(Song(i, plays[i]))
            this_genre.add_play(plays[i])
        else:
            genre_dict[genres[i]] = Genre(genres[i], plays[i])
            genre_dict[genres[i]].add_song_list(Song(i, plays[i]))

    sorted_key_list = sorted(genre_dict, key=lambda k: genre_dict[k].total_play, reverse=True)

    for key in sorted_key_list:
        genre_dict[key].song_list.sort(key=lambda song: song.play, reverse=True)
        for i in range(min(2, len(genre_dict[key].song_list))):
            answer.append(genre_dict[key].song_list[i].idx)

    return answer


if __name__ == '__main__':
    genres = ['classic', 'pop', 'classic', 'classic', 'pop']
    plays = [500, 600, 150, 800, 2500]
    solution(genres, plays)


'''
import operator
from collections import defaultdict

class Music:
    def __init__(self, id, g, p):
        self.id = id
        self.g = g
        self.p = p

def solution(genres, plays):
    db = []
    g_db = defaultdict(int)
    for i in range(len(genres)):
        db.append(Music(i,genres[i],plays[i]))
        g_db[genres[i]] += plays[i]
    db.sort(key=operator.attrgetter("id"))
    db.sort(key=operator.attrgetter("p"),reverse=True)

    g_db = sorted(g_db.items(),key=operator.itemgetter(1), reverse=True)

    result = []
    for g in g_db:
        idx = 0
        cnt = 0
        while cnt <2:
            if idx >= len(db):
                break
            if db[idx].g == g[0]:
                result.append(db[idx].id)
                cnt += 1
            idx += 1
    return result
'''


'''
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
'''