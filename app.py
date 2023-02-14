from flask import Flask,jsonify;
# Instantiating my app
app = Flask(__name__)

# creating a route for the application
@app.route('/', methods = ['GET'])
def greet():
    return 'Hello there,we bring you some interesting articles for your review.'


@app.route('/articles', methods =['GET'])
# function read_articles
def read_articles():
    articles = {
        'article1':{
        'Id': 101,
        'Title': 'Mr. Fake Fiancé: A Second Chance Romance',
        'Body': "Love is a beautiful thing, until you bump into a wrong partner like Mr. fake fiance, there you're life can be everything miserable.",
        'More_Info': {
            'Author_name':'Annabelle Love',
            'Publisher': 'Love Lust Publishing',
            'Year':  2021
        }
        },
        'article2':{
        'Id': 102,
        'Title': 'True love exists',
        'Body': 'True love is respectful; fake love is rude. True love will respect your opinions, decisions, and even your ambitions. It will also honor you as a person. On the other hand, fake love is arrogant. It doesnot care about what you think and what you feel.Fake love is when your girlfriend/boyfriend doesnot give a fuck about you',
        'More_Info': {
            'Author_name':'Julyette',
            'publisher':'J&R Inc.' ,
            'Year': 2018 
        }
        },
        'article3':{
        'Id': 103,
        'Title': 'Roger The Dodger - Money Money Money',
        'Body': "money supply and price level in an economy are in direct proportion to one another. When there is a change in the supply of money, there is a proportional change in the price level and vice-versa",
        'More_Info': {
            'Author_name':' Kedrick Thompson',
            'Publisher': ' D.C. Thomson & Co.',
            'Year': 1995
            
        }
        }
        }
    articlesList = [{'articles':articles}]
    return jsonify(articlesList)
    