#fav language

favorite_language = {
    'inna': 'c',
    'john': 'java',
    'peter': 'ruby',
    'olga': 'python'
}

friends = ['john', 'phil']

for name in favorite_language:
    print('Hi', name.title())

    if name in friends:
        language = favorite_language[name].title()
        print(name.title(), 'I see you love', language)

if 'liza' not in favorite_language.keys():
    print(f'Liza, please register!')