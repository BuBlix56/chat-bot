print('Привет! Я чат-бот Раян!')
mood = input('Как твоё настроение?(круто/скучно/норм/злой)').lower()
while mood != 'злоц':
    if mood == 'круто':
        play = input('Поиграем в игру?').lower()
        if play == 'да' or play == 'ага' or play == 'давай':
            play_top = input('Какие жанры игр тебе нравиться? (экшен, ранер, стратегии)?').lower()
            if play_top == 'экшен':
                print('советую поиграть в "PUBG" :D.')
            elif play_top == 'ранер' or play_top == 'ранеры':
                print('советую поиграть в "Geometry Dash" ._.')
            elif play_top == 'Стратегии':
                print('советую поиграть в "Clash Royale" !_!')
            else:
                print('Тогда можешь поиграть в "Clash Royale"')
        else:
            print('Иди гуляй на улицу!')
    elif mood == 'скучно':
        cool = input('Тогда выбирай "поесть" или "Тик Ток". Что выберешь?').lower()
        if cool == 'поесть':
            breakfast = input('Уже завтракал(а)?').lower()
            if breakfast == 'да' or breakfast == 'ага':
                print('Тогда пей чай!')
            else:
                print('Суп скоро остынет!')
        elif cool == 'Тик Ток':
            print('Заходи и листай ленту!')
        else:
            print('Заходи и листай ленту!')
    elif mood == 'норм':
        print('Ну и хорошо мемы не дадут унывать!)')
    else:
        print('Я сломался, выбирай что предлагают или иди гуляй!')
    print('Раян на связи!')
    mood = input('Как настроение?(круто/скучно/норм/злой)').lower()