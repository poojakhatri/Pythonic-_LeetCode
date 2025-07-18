import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    viewers = views[views['author_id'] == views['viewer_id']][['author_id']]
    result = viewers.drop_duplicates().sort_values(by='author_id').rename(columns={'author_id':'id'})
    return result