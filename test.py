from textblob import TextBlob

sentence = '''Over the next years, Starr struggled with drug addiction, he was repeatedly arrested for possession of illegal drugs and other offenses. In 2010 he became a participant in the reality show "Rehabilitation of the Stars", where celebrities were helped to overcome addictions. After that, the musician briefly returned to normal life, but soon resumed taking drugs.'''

analysis = TextBlob(sentence).sentiment
print(analysis)