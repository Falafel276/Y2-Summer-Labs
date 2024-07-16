def create_youtube_videos(title,description):
    Title = {'Title': title,
             'Description': description , 
             'Like': 0 , 'Dislikes': 0,
             'coments' : {'username': '','comment_txt':''}
             }
    
    
    return Title

v = create_youtube_videos( 'High' ,'I am good')
def add_a_like(dict):
    if 'Like' in dict:
        dict['Like'] += 1   

def add_a_dislike(dict):
    if 'Dislikes' in dict:
         dict['Dislikes'] += 1 
 

def add_coment(youtubevideo,username,commenttext): 
    youtubevideo["coments"]["username"] = username
    youtubevideo["coments"]["comment_txt"] = commenttext
    return

