ted = pd.read_csv("C:/Users/CDustin/Documents/Projects/Kaggle/TedTalks/Data/ted_main.csv")
list(ted)

ted.shape
ted.info()
ted.describe()

##create table for ratings
ratings = pd.DataFrame.from_dict(ted['ratings'], orient='columns')
ratings.concat(ted['title'], inplace=True)


def GatherRatings(ratings, title):
    ratings = literal_eval(ratings)
    dfs = [pd.DataFrame([rating],columns=rating.keys()) for rating in ratings]
    df = pd.concat(dfs)
    df['Title'] = title
    df.drop(columns='id')
    return df

def CountRatings(ratings):
    ratings = literal_eval(ratings)
    return len(ratings)

rating_counts = ted.apply(lambda x: CountRatings(x.ratings),axis=1)
sum(rating_counts < 14)

ratings_df = []
for i in range(len(ted)):
	ratings_df.append(GatherRatings(ted.iloc[i,-7],ted.iloc[i,-3]))

ratings_dfs = [df.pivot_table('count',index='Title',columns='name') for df in ratings_df]
df_rate = pd.concat(ratings_dfs)

list(df_rates)
ratings = list(df_rates)
negative_ratings = ratings[1,9,10,11,13]
positive_ratings = list(set(ratings)-set(negative_ratings))

