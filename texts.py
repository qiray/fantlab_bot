# -*- coding: utf-8 -*-

helpText = '/help - выводит этот текст\n/book - переходит к рекомендации книг\n/top100 - Интерактивный путеводитель по Top-100 фантастических книг [Перевод интерактивной версии от сайта sfsignal.com, основанный на 100 Лучших НФ и Фэнтези книг (NPR Top 100)] '
botErrorText = 'Произошла ошибка. Пожалуйста, начните работу с ботом заново и сообщите разработчику (@qiray) о случившемся.'
pleaseWaitText = "Пожалуйста, подождите, выбираем книгу специально для вас..."
showRecomendsText = "Перейти к рекомендациям"
showtop100Text = "Перейти к путеводителю Top-100"
startText = 'Этот бот предназначен для получения жанровых рекомендаций книг из базы Фантлаба (https://fantlab.ru/).\nДля начала работы введите команду /book или нажмите на кнопку "' + showRecomendsText + '"\nДля выбора книга из списка Топ-100 введите команду /top100 или нажмите на кнопку "' + showtop100Text + '"'
iwantmoreText = "Хочу еще такого же"
startagainText= "Не, давай по новой"
pleaseWaitTheSameText = "Хорошо, подбираем еще парочку похожих книг"

requestStepsArray = [
	[
		["Фэнтези", "wg19=on", 0], 
		["Фантастика", "wg1=on", 0],
		['Не важно', "NONE", 0]
	],
	[
		["На Земле", "&wg69=on&wg89=on", 1], 
		["Где-то в другом мире", "&wg78=on&wg88=on&wg91=on&wg92=on&wg129=on&wg213=on", 1],
		['Не важно', "NONE", 1]
	], 
	[
		["Далеко в прошлом", "&wg93=on&wg94=on&wg95=on&wg96=on&wg97=on&wg98=on&wg99=on", 2], 
		["В наши дни", "&wg100=on&wg101=on", 2],
		["В будущем", "&wg102=on&wg103=on&wg104=on", 2],
		['Не важно', "NONE", 2]
	],
	[
		["Наши", "&lang=rus", 3], 
		["Зарубежные", "&lang=for", 3],
		['Не важно', "NONE", 3]
	],
	[
		["Роман", "&form=nov", 4], 
		["Повесть или рассказ", "&form=sto", 4],
		['Не важно', "NONE", 4]
	]
]
	
requestNamesArray = ["Что читаем?", "Где разворачивается действие?", "Когда происходят события?", "И кто же авторы?", "А размер имеет значение?"]

fixRequestString = "wg1=on&wg19=on&wg33=on&wg30=on&wg31=on&wg32=on&wg34=on&wg35=on&wg225=on&wg36=on&wg37=on&wg38=on&wg39=on&wg160=on&wg116=on&lang=&form="

goback = 'Назад'

top100questions = [
	[
		'С чего хотите начать?', 
		0,
		[
			['Фантастика', 2],
			['Фэнтези', 3],
			['И того, и другого', 50],
			['Я предпочитаю книжки с картинками', 51],
			['Как насчёт ужасов?', 52],
			['Откланиваюсь. Пойду-ка лучше в раздел с Донцовой.', 53]
		],
		'q1'
	],
	[
		'Вам нравится киберпанк?',
		1,
		[
			['Да. Панки, хой!', 4],
			['Не, спасибо, я с ними пару раз в автобусе ехал.', 5],
			['Можно. Тогда лучше что-то весёлое про киберпространство', '9769', 'Криптономикон', 'Нил Стивенсон']
		],
		'q2'
	],
	[
		'Вас расстроит, если в книге не будет *шрамированного подростка в магической школе*?',
		1,
		[
			['Да. Без Поттера и книга не книга, и фильм не фильм!', '188170', 'Имя ветра', 'Патрик Ротфусс'],
			['Нет. К Вольдемору Поттера!', 6]
		],
		'q3'
	],
	[
		'Суровый нуар, викторианская Англия или катаны и самураи?',
		2,
		[
			['Суровый нуар. Да, я не хочу быть пай-мальчиком.', '2654', 'Нейромант', 'Уильям Гибсон'],
			['Викторианская Англия. Ах, этот незабываемый хруст викторианских булок!', '9767', 'Алмазная эпоха', 'Нил Стивенсон'],
			['Самураи. Только настоящий Путь Самурая.', '9765', 'Лавина', 'Нил Стивенсон']
		],
		'q4'
	],
	[
		'Как насчёт громких взрывов в вакууме?',
		2,
		[
			['О да! Будет скафандр, будут путешествия (через тернии к звёздам)', 7],
			['Нет. Я предпочитаю держать ноги не вакууме, а на какой-нибудь твёрдой опоре, вроде Земли', 8],
			['Ну может быть. Хотя меня терзают смутные сомнения. А можно не покидать Солнечную систему?', 9]
		],
		'q5'
	],
	[
		'А вы с фэнтези хорошо знакомы?',
		3,
		[
			['Неа. Мои бедные стальные нервы её переносят с трудом.', 69],
			['Да. О, Элберет и Земноморье!', 10],
			['Немного. Я чего-то такое про Тотошку и дорогу из жёлтого кирпича в детстве читал.', '81650', 'Ведьма. Жизнь и времена Западной колдуньи из страны Оз', 'Грегори Магуайр']
		],
		'q6'
	],
	[
		'Как насчёт военной фантастики?',
		5,
		[
			['О да! Я этих зергов накрошил немеренно!', 11],
			['Спасибо, не надо. А нет ли у вас что-нибудь про первый контакт?', 12],
			['Можно. Хотя мне бы до войны космос поисследовать.', 13]
		],
		'q7'
	],
	[
		'А как насчёт приключений внутри Земли?',
		5,
		[
			['Да. Звучит интересно. Дайте два!', 14],
			['Нет. Эй, умник, я сказал на поверхности, а не под ней.', 15]
		],
		'q8'
	],
	[
		'ОК. А от Земли отлетать будем?',
		5,
		[
			['Ну нет. У меня боязнь открытого пространства. Ну вот разве что Марс?', 16],
			['Конечно же', '9957', '2001: Космическая одиссея', 'Артур Кларк']
		],
		'q9'
	],
	[
		'Как Артуриана?',
		6,
		[
			['Да я даже "Янки при дворе короля Артура" только из-за Артура и прочёл.', 17],
			['Нет', 18]
		],
		'q10'
	],
	[
		'И кого укрощать будем?',
		7,
		[
			['Жуков', '2796', 'Звёздный десант', 'Роберт Хайнлайн'],
			['Жуков. Но из глубин Космоса.', '4670', 'Игра Эндера', 'Орсон Скотт Кард'],
			['Гуманоидов. Чтобы две руки, две ноги были', '15912', 'Бесконечная война', 'Джо Холдеман'],
			['Империю', '4325', 'Дюна', 'Фрэнк Герберт'],
			['Землян. Вернее, колиниальную администрацию, угнетающую свободолюбивых лунян.', '2802', 'Луна жёстко стелет', 'Роберт Хайнлайн'],
			['Всех. Кого встретим, с тем и воюем.', '29460', 'Война старика', 'Джон Скальци']
		],
		'q11'
	],
	[
		'И с какими пришельцами Вам бы хотелось повстречаться?',
		7,
		[
			['Воинственными.', '9457', 'Война миров', 'Герберт Уэллс'],
			['Равнодушными. Которым безразлична Земля и её обитатели.', '9961', 'Свидание с Рамой', 'Артур Кларк'],
			['Мирными', '10140', 'Конец детства', 'Артур Кларк'],
			['Мудрыми. Которые хотят позаботиться о человечестве.', '106908', 'Контакт', 'Карл Саган'],
			['Быстроразмножающимися.', '23283', 'Мошка в зенице Господней', 'Ларри Нивен и Джерри Пурнелл']
		],
		'q12'
	],
	[
		'Далёкая-предалёкая Галактика?',
		7,
		[
			['Да. И лучше бы ещё и давным давно.', '14938', 'Наследник Империи', 'Тимоти Зан'],
			['Нет. Знаю, что хотите предложить.', 19]
		],
		'q13'
	],
	[
		'Под сушей или под морем?',
		8,
		[
			['Под землёй, конечно же.', '7189', 'Путешествие к центру Земли', 'Жюль Верн'],
			['Под водой. Ах, море-море', '7182', 'Двадцать тысяч лье под водой', 'Жюль Верн']
		],
		'q14'
	],
	[
		'Ну раз я - умник, скажите, что больше интересно: политика, религия или философия?',
		8,
		[
			['Анархия - мать порядка.', 20],
			['Религия - опиум для народа.', 21],
			['Я мыслю - следовательно, существую.', '5353', 'Мечтают ли андроиды об электроовцах?', 'Филипп К. Дик'],
			['Ну уж нет. В прошлый раз с приятелями про Сталина заговорили, так у меня теперь зуба нет. А чего-нибудь про путешествия во времени есть или ещё чего интересненькое?', 22]
		],
		'q15'
	],
	[
		'Хм, Марс. А как бы Вам хотелось увидеть Красную планету?',
		9,
		[
			['Через окошко, причём земляничное.', '5149', 'Марсианские хроники', 'Рей Брэдбери'],
			['Глазами специалиста по терроформированию.', '18286', 'Красный Марс', 'Ким Стенли Робинсон'],
			['Сквозь волшебное зеркало.', '11139', 'Космическая трилогия', 'Клайв Льюис'],
		],
		'q16'
	],
	[
		'А кто из героев самый-самый?',
		10,
		[
			['Моргана', '16699', 'Туманы Авалона', 'Мэрион Брэдли'],
			['Мерлин', '10805', 'Хрустальный грот', 'Мэри Стюарт'],
			['Артур', '22020', 'Король Былого и Грядущего', 'Теренс Х. Уайт']
		],
		'q17'
	],
	[
		'А действие в нашем мире?',
		10,
		[
			['Да. Ну да, я - городской ребёнок.', 23],
			['Нет. Тут скучно и уныло, мне бы другой глобус.', 24],
			['Можно и так. Каждое лето в детстве я проводил в маленьком городке, где жила бабушка.', '5219', 'Что-то страшное грядёт', 'Рэй Брэдбери'],
		],
		'q18'
	],
	[
		'Любите хорошую шутку?',
		13,
		[
			['А то. Я - испытанный остряк.', '2076', 'Путеводитель по галактике для путешествующих автостопом', 'Дуглас Адамс'],
			['Не в книгах. Да и вообще, у меня некоторые проблемы с чувством юмора.', 25],
			['Можно. Только чтобы: взрывы, стрельба, пара весёлых моментов, и снова стрельба.', '13789', 'Культура', 'Иен Бэнкс']
		],
		'q19'
	],
	[
		'Что вам интереснее?',
		15,
		[
			['Феминизм', '2051', 'Левая рука Тьмы', 'Урсула Ле гуин'],
			['Коммунизм', 'Обделённые', 'Урсула Ле Гуин']
		],
		'q20'
	],
	[
		'Чем будем дурманить голову?',
		15,
		[
			['Христианством', '13076', 'Страсти по Лейбовицу', 'Уолтер Миллер младший'],
			['Гуманизмом', '2797', 'Чужак в чужой стране', 'Роберт Хайнлайн']
		],
		'q21'
	],
	[
		'Олично. А лучше что-нибудь классическое или наоборот посовременнее?',
		15,
		[
			['Современное', '33826', 'Doomsday Book', 'Конни Уиллис'],
			['Классику', '9452', 'Машина времени', 'Герберт Уэллс'],
			['Ой, не надо лучше. Чего-то я заговорился уже. Лучше мистику какую-нибудь или триллер посоветуйте.', 26]
		],
		'q22'
	],
	[
		'А под городом можно повстречаться с богами?',
		18,
		[
			['Да. С одной стороны, чтобы что-то мифологическое, но с другой, чтобы про современность', '10134', 'Американские боги', 'Нил Гейман'],
			['Нет. Чтобы и без богов там целый мир был.', '10133', 'Задверье', 'Нил Гейман']
		],
		'q23'
	],
	[
		'А вестерны нравятся?',
		18,
		[
			['А то! У меня и шляпа есть как у Клинт Иствуда.', '424', 'Тёмная башня', 'Стивен Кинг'],
			['Нет. Старьё. Да и в карты постоянно режутся, а я не очень в этом деле разбираюсь.', 27]
		],
		'q24'
	],
	[
		'Ага, чувствуется закваска настоящего учёного, не так ли?',
		19,
		[
			['Да. А если уж и приходится лирику читать, то предпочитаю твёрдую научную фантастику.', 28],
			['Не угадали. Просто предпочитаю, когда экшена побольше.', 29]
		],
		'q25'
	],
	[
		'Уверены? Так мистика или триллер?',
		22,
		[
			['Мистика', '779', 'Стальные пещеры', 'Айзек Азимов'],
			['Триллер', '23432', 'Молот Люцифера', 'Ларри Нивен и Джереми Пурнелл']
		],
		'q26'
	],
	[
		'Животные больше интересны?',
		24,
		[
			['Да. Я когда рекламу фонда диких животных вижу, у меня слёзы на глазах наворачиваются.', 30],
			['Нет. У меня на них аллергия.', 31]
		],
		'q27'
	],
	[
		'Что изучаете?',
		25,
		[
			['Историю', '95', 'Основание', 'Айзек Азимов'],
			['Я - инженер', '23276', 'Мир-кольцо', 'Ларри Нивен'],
			['IT-технологии', '7019', 'Пламя над бездной', 'Вернон Виндж']
		],
		'q28'
	],
	[
		'А к сериалам как относитесь?',
		25,
		[
			['Нормально', '5385', 'Барраярский цикл', 'Лоис Макмастер Буджолд'],
			['Плохо. Ни за какие коврижки.', 32]
		],
		'q29'
	],
	[
		'Кого бы с удовольствием дома завели?',
		27,
		[
			['Единорога', '11022', 'Последний единорог', 'Питер Бигль'],
			['Кролика', '37490', 'Обитатели холмов', 'Ричард Адамс'],
			['Дракона', '9869', 'Полёт дракона', 'Энн Маккефри']
		],
		'q30'
	],
	[
		'А к альтернативной истории как относитесь?',
		27,
		[
			['Люблю. Ой, жа я пикейный жилет в глубине души, бывает как сяду рассуждать: а что если бы...', 33],
			['Без восторга. Я и в школе уроки истории просто прогуливал.', 34]
		],
		'q31'
	],
	[
		'А ну тогда рассказы, и это замечательно! Роботы или марсиане?',
		29,
		[
			['Роботы', '7078', 'Я, робот', 'Айзек Азимов'],
			['Марсиане', '5042', 'Человек в картинках', 'Рэй Брэдбери']
		],
		'q32'
	],
	[
		'Любовь и магия или вражда между волшебниками?',
		31,
		[
			['Любовь и магия', '189062', 'Kushiel\'s Legacy Series', 'Жаклин Кэри'],
			['Вражда', '21260', 'Джонатан Стрендж и мистер Норрелл', 'Сюзанна Кларк']
		],
		'q33'
	],
	[
		'Готовы зарыться в цикл?',
		31,
		[
			['Да. Я дважды уже выбирал, сколько можно?', 35],
			['Нет. Не хочу, чтобы чтение становилось одноообразным.', 36],
			['Можно попробовать. А вот чтобы отдельные книги каких-то циклов можно?', 37]
		],
		'q34'
	],
	[
		'А цикл должен иметь окончание?',
		34,
		[
			['Да', 38],
			['Не обязательно. Мне нравится чувство ожидания, так что пусть оно длится годами.', 39]
		],
		'q35'
	],
	[
		'Пираты должны быть?',
		34,
		[
			['Да. Конечно с пиратами!', '286966', 'Принцесса-невеста', 'Уильям Голдман'],
			['Нет. К морским чертям пиратов.', '10825', 'Звёздная пыль', 'Нил Гейман']
		],
		'q36'
	],
	[
		'А что вам больше нравится',
		34,
		[
			['Сатира на бюрократические организации', '1951', 'Опочтарение', 'Терри Пратчетт'],
			['Сатира на церковь', '1722', 'Мелкие боги', 'Терри Пратчетт'],
			['Комедия положений', '35756', 'Заклинание для Хамелеона', 'Пирс Энтони']
		],
		'q37'
	],
	[
		'Словосочетание "фантастика меча и магии" вам заставляют вспомнить что-то хорошее?',
		35,
		[
			['О, да! Варвары и маги? Да, как это может не нравится?', 40],
			['Нет', 41]
		],
		'q38'
	],
	[
		'Красивые вершки или вкусные корешки?',
		35,
		[
			['Высокое фэнтези',  '224233', 'The Way of Kings', 'Брендон Сандерсон'],
			['Релистическое фэнтези', '4133', 'Песня Льда и Огня', 'Джордж Р. Р. Мартин']
		],
		'q39'
	],
	[
		'Любите ролевые игры?',
		38,
		[
			['Да', '3972', 'Дзирт До\'Урден', 'Роберт Сальваторе'],
			['Нет', 42]
		],
		'q40'
	],
	[
		'Какую-нибудь трилогию в старом добром духе?',
		38,
		[
			['Да. Три - моё любимое число.', 43],
			['Нет. В таких случаях я обычно говорю "Семи смертям не бывать, а одной не миновать".', 44],
			['Можно. А чтобы трилогия трилогий можно?', '53650', 'Хроники Томаса Ковенанта, Неверующего', 'Стивен Р. Дональдсон']
		],
		'q41'
	],
	[
		'Вавары или маги?',
		40,
		[
			['Маги',  '3378', 'Элрик из Мелнибонэ', 'Майкл Муркок'],
			['Варвары', '1382', 'Конан-варвар', 'Роберт Говард']
		],
		'q42'
	],
	[
		'Значит будете читать о',
		41,
		[
			['ворах', '46393', 'Рожденный туманом', 'Брендон Сандерсон'],
			['волшебных артефактах', '4960', 'Меч Шаннары', 'Терри Брукс'],
			['убийцах', '3607', 'Сага о Видящих', 'Робин Хобб'],
			['магах', '3580', 'Имперские войны', 'Раймонд Фэйст']
		],
		'q43'
	],
	[
		'Ну а пяти-шести книг-то для Вас достаточно?',
		41,
		[
			['Да. Мне надолго хватит.', 45],
			['Нет. Мне нужно как минимум 10.', 46]
		],
		'q44'
	],
	[
		'Вам нравятся истории о сиротах, выросших у крестьян?',
		44,
		[
			['Да/Нет. Как ни печально, но здесь не из чего выбирать.', 47]
		],
		'q45'
	],
	[
		'Как насчёт квеста по спасению мира от зла?',
		44,
		[
			['Да. Эпическое противостоя Добра и Зла, пожалуйста.', 48],
			['Нет. Хотелось бы чего-то посложнее.', 49]
		],
		'q46'
	],
	[
		'Современное или классическое?',
		45,
		[
			['Современное', '40684', 'Кодекс Алеры', 'Джим Батчер'],
			['Классику', '4741', 'Белгариад', 'Дэвид Эддингс']
		],
		'q47'
	],
	[
		'И кто же спасёт мир?',
		46,
		[
			['Искатель Истины', '3616', 'Меч Истины', 'Терри Гудкайнд'],
			['Возрождённый Дракон', '2699', 'Колесо Времени', 'Роберт Джордан']
		],
		'q48'
	],
	[
		'Сделайте взвешанный выбор, это последнее, что мы Вас спрашиваем.',
		46,
		[
			['Земля - одна из Теней, которые отбрасывает Амбер.', '72', 'Хроники Амбера', 'Роджер Желязны'],
			['Волнообразное повествование. Хотелось бы чего-то посложнее.', '31518', 'Малазанская <Книга Павших>', 'Стивен Эриксон']
		],
		'q49'
	],
	[
		'Ура, Вы сделали это. Куда отправимся: в будущее или в прошлое?',
		1,
		[
			['В будущее', 54],
			['В прошлое', 55]
		],
		'q50'
	],
	[
		'Супергерои или божество, пережившее пытки?',
		1,
		[
			['Супергерои', '216554', 'Хранители', 'Алан Мур'],
			['Бог сновидений', '163035', 'The Sandman. Песочный человек', 'Нил Гейман']
		],
		'q51'
	],
	[
		'Почти не из чего выбирать. Как Вы к вампирам относитесь?',
		1,
		[
			['Нормально', '121279', 'Солнечный свет', 'Робин Мак-Кинли'],
			['Не очень. Мне зомби больше по душе.', 56]
		],
		'q52'
	],
	[
		'Мы никому не расскажем. Нравятся трагические истории?',
		1,
		[
			['Да. Я люблю поплакать над книгой.', 57],
			['Нет. Я прошлой ночью в очередной раз посмотрел "Титаник". Так что обойдусь', 58]
		],
		'q53'
	],
	[
		'Вы часом не слегка тронувшийся математик?',
		50,
		[
			['Да', '74823', 'Анафем', 'Нил Стивенсон'],
			['Нет', 59]
		],
		'q54'
	],
	[
		'А монстров любите?',
		50,
		[
			['Да', '36265', 'Вокзал потерянных снов', 'Чайна Мьевиль'],
			['Нет', '33814', 'Дело Джен, или Эйра немилосердия']
		],
		'q55'
	],
	[
		'Полноценная война с зомби, или одиночка против орд ходячих мервецов?',
		52,
		[
			['Оба мимо. Пожалуй, подумав, я бы предпочёл что-то классическое.', '80310', 'Франкенштейн', 'Мэри Шелли'],
			['Война. С компанией, хоть на край света, а хоть крошить трупы.', '121626', 'Мировая война Z', 'Макс Брукс'],
			['Одиночка. Я - мизантроп.', '18643', 'Я - легенда', 'Ричард Матесон']
		],
		'q56'
	],
	[
		'Любовная история или человек, преодолевающий свой интеллектуальную немощь?',
		53,
		[
			['Любовная история', 60],
			['Второе. Мне всегда было очень жалко умственно-отсталых.', '52178', 'Цветы для Элджернона', 'Дэниел Киз']
		],
		'q57'
	],
	[
		'Что-то постмодернистское и психоделическое?',
		53,
		[
			['Да', 61],
			['Нет. Если кто-то начинает рассматривать нео-культурное повествование, он встаёт перед выбором: либо принять субтекстуальную парадигму выражения или придти к заключению, что повествование должно возникнуть в процессе общения. Это диалектическая парадигма содержания содержится в нём самом...', 62]
		],
		'q58'
	],
	[
		'Что звучит интереснее: умирающее Солнце или монстр, состоящий из колючей проволоки, лезвий, шипов и других острых предметов?',
		54,
		[
			['Умирающее Солнце. Это звучит поэтично.', '31459', 'Книга Нового Солнца', 'Джин Вулф'],
			['Монстр. Дайте мне уже Шрайка!', '1', 'Гиперион', 'Дэн Симмонс']
		],
		'q59'
	],
	[
		'Как насчёт путешествия во времени, сопряжённое с любовной историей?',
		57,
		[
			['Жмите. Увы и увы. Здесь не из чего больше выбирать.', 63]
		],
		'q60'
	],
	[
		'Может ещё небольшое путешествие во времени?',
		58,
		[
			['Да', '3799', 'Бойня номер пять', 'Курт Воннегут'],
			['Нет', '1435', 'Колыбель для кошки', 'Курт Воннегут']
		],
		'q61'
	],
	[
		'Как относитесь к мрачным безысходным фантазиям?',
		58,
		[
			['Давайте. Мне нравятся самые мрачные сценарии.', 64],
			['Нет, спасибо. Мир и так не сахар.', '9633', 'Скотный двор', 'Джордж Оруэлл']
		],
		'q62'
	],
	[
		'Классическая или современная?',
		60,
		[
			['Классическая', '145088', 'Чужестранка', 'Диана Гэблдон'],
			['Современная', '40342', 'Жена путешественника во времени', 'Одри Ниффенеггер']
		],
		'q63'
	],
	[
		'Тоталитарная антиутопия или мир, погружающийся в глубины безумия?',
		62,
		[
			['Диктатура', 65],
			['Сумасшествие', 66]
		],
		'q64'
	],
	[
		'И какая диктатура?',
		64,
		[
			['Религиозная', '54723', 'Рассказ служанки', 'Маргарет Этвуд'],
			['Военный коммунизм', '9632', '1984', 'Джордж Оруэлл']
		],
		'q65'
	],
	[
		'Как бы Вы отнеслись к миру, где людей изготавливают на фабриках?',
		64,
		[
			['Заинтересовало бы', '31535', 'О дивный новый мир', 'Олдос Хаксли'],
			['Не интересно', 67]
		],
		'q66'
	],
	[
		'Какой вопрос пугает Вас больше?',
		66,
		[
			['Книги, кому они нужны?', '5039', '451° по Фаренгейту', 'Рэй Брэдбери'],
			['Свободная воля, кому нужна?', '16230', 'Заводной апельсин', 'Энтони Бёрджесс'],
			['Никакой. Хочется чего-то более постапокалиптического.', 68]
		],
		'q67'
	],
	[
		'Как будто мир обратился в пепел?',
		67,
		[
			['Да. Тем более, что в истории люди, которые были готовы сжечь Землю в ядерной войне.', '140298', 'Дорога', 'Кормак Маккарти'],
			['Нет. Прикольнее было бы про пандемию почитать.', '293', 'Противостояние', 'Стивен Кинг']
		],
		'q68'
	],
	[
		'Но хоть как-то Вы с фэнтези знакомы?',
		6,
		[
			['Да. Это же про эльфов!', '1678', 'Сильмариллион', 'Дж. Р. Р. Толкин'],
			['Нет. У меня даже единорожье молоко на губах не обсохло.', '1693', 'Властелин Колец', 'Дж. Р. Р. Толкин']
		],
		'q69'
	]
]
