# ============================================================
# Project 2 - Music Recommendation System
# Hexasoftware Internship
# Content-Based Filtering using Cosine Similarity
# ============================================================
import math

songs = [
    {"id":1,"title":"Blinding Lights","artist":"The Weeknd","genre":"Pop","tempo":"Fast","mood":"Energetic"},
    {"id":2,"title":"Shape of You","artist":"Ed Sheeran","genre":"Pop","tempo":"Medium","mood":"Happy"},
    {"id":3,"title":"Bohemian Rhapsody","artist":"Queen","genre":"Rock","tempo":"Mixed","mood":"Dramatic"},
    {"id":4,"title":"Levitating","artist":"Dua Lipa","genre":"Pop","tempo":"Fast","mood":"Energetic"},
    {"id":5,"title":"Hotel California","artist":"Eagles","genre":"Rock","tempo":"Slow","mood":"Melancholy"},
    {"id":6,"title":"Stay With Me","artist":"Sam Smith","genre":"Soul","tempo":"Slow","mood":"Sad"},
    {"id":7,"title":"Uptown Funk","artist":"Bruno Mars","genre":"Funk","tempo":"Fast","mood":"Happy"},
    {"id":8,"title":"Someone Like You","artist":"Adele","genre":"Soul","tempo":"Slow","mood":"Sad"},
]

GENRES = ['Pop','Rock','Soul','Funk']
TEMPOS = ['Slow','Medium','Fast','Mixed']
MOODS  = ['Happy','Sad','Energetic','Dramatic','Melancholy']

def encode_song(song):
    vec = []
    for g in GENRES: vec.append(1 if song['genre']==g else 0)
    for t in TEMPOS: vec.append(1 if song['tempo']==t else 0)
    for m in MOODS:  vec.append(1 if song['mood'] ==m else 0)
    return vec

def cosine_similarity(a, b):
    dot = sum(x*y for x,y in zip(a,b))
    mag = lambda v: math.sqrt(sum(x**2 for x in v))
    return 0.0 if mag(a)==0 or mag(b)==0 else dot/(mag(a)*mag(b))

def recommend(title, top_n=3):
    target = next((s for s in songs if s['title'].lower()==title.lower()), None)
    if not target: return None, []
    tv = encode_song(target)
    scores = [(s, round(cosine_similarity(tv, encode_song(s))*100,1))
              for s in songs if s['id']!=target['id']]
    return target, sorted(scores, key=lambda x:x[1], reverse=True)[:top_n]

print("="*65)
print("PROJECT 2 - MUSIC RECOMMENDATION SYSTEM")
print("Hexasoftware Internship")
print("="*65)

for query in ['Blinding Lights','Someone Like You','Bohemian Rhapsody']:
    target, recs = recommend(query)
    print(f'\n>> You Liked: {target["title"]} by {target["artist"]}')
    print(f'   Genre: {target["genre"]} | Tempo: {target["tempo"]} | Mood: {target["mood"]}')
    print('   Top Recommendations:')
    for i,(song,score) in enumerate(recs,1):
        print(f'   {i}. {song["title"]} by {song["artist"]} | Similarity: {score}%')

print("\n" + "="*65)
