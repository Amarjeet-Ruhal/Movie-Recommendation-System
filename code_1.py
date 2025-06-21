import pickle
import sys
import json

movies=pickle.load(open('artifacts/movie_list.pkl','rb'))
similarity=pickle.load(open('artifacts/similarity.pkl','rb'))

def recommend(movie):
    index=movies[movies['movie_id']==movie].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x: x[1])
    recommended_movie_name=[]
    # recommended_movie_poster=[]
    for i in distances[1:41]:
        mov_id=movies.iloc[i[0]].movie_id
        # recommended_movie_poster=
        recommended_movie_name.append(mov_id)
    return recommended_movie_name

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Insufficient input provided"}))
        sys.exit(1)

    # The first argument is the JSON string representing the movie list
    user_input = json.loads(sys.argv[1])
    recently_watched = sys.argv[2]

    # Process the input
    output = recommend(user_input, recently_watched)

    # Return the processed movie list as a JSON array
    print(json.dumps(output))
