from collections import Counter
from kiwipiepy import Kiwi

# pip install kiwipiepe
# 1. Kiwi 객체 생성
kiwi = Kiwi()

text = """

If it was my last day on Earth
If it was my last day
If it was my last day on Earth
If it was my last day
If I close my eyes
And the sun don't rise
Will I be okay?
If it was my last day on Earth
If it was my last day
If it was my last day on Earth
I wouldn't be in church
I'm sorry God, but it's my last day in this universe
I need to see birds and buzzin' bees
Green grass, evergreen trees
Not seeing people who have been mean to me
And why would I waste my time
All my favorite people need teary eyed goodbyes
Talk, laugh, hug and give a bunch of hard high fives
I did my best man
I gave this thing a good try
If it was my last day on Earth
If it was my last day
If it was my last day on Earth
If it was my last day
If I close my eyes
And the sun don't rise
Will I be okay?
If it was my last day on Earth
If it was my last day
Wait, wait, wait
You're tellin' me I got 24 of these 60 minutes things left?
Damn, I ain't get to be a billionaire yet
Fly around first class, private jet flex
Use a black Amex, get up out the duplexes
Buy a Lexus
Take a road trip to a spaceship (uh)
And I'ma get on
Blast up in the sky and I'ma get gone
Gave up too much just to see one more dawn
If it was my last day on Earth
If it was my last day
If it was my last day on Earth
If it was my last day
If I close my eyes
And the sun don't rise
Will I be okay?
If it was my last day on Earth
If it was my last day
"""

#2. 형태소 분석 진행
tokens = kiwi.tokenize(text)
word_list = []

# 3. 명사(NNG, NNP)와 형용사(VA) 추출
for token in tokens:

    if token.tag in ['NNG', 'NNP', 'VA']:

        if len(tokens.form) > 1:
            # token.form: 단어의 본래 형태
            word_list.append(token.form)

print("추출된 단어 리스트")
print(word_list)

print("\n단어 빈도수")
print(Counter(word_list))

# 4. 워드 클라우드 객체 생성
wc = Word_Cloud(
    font_path = 'malgn',
    width = 400,
    height = 400,
    backgraound_coler = 'white' # 배경색을 흰색으로 변경
)

# 5. 빈도수 데이터로 워드클라우드 생성
result = wc.generate_from_frequencies(word_list_count)

# 6. matplotlib로 출력
plt.figure(figsize = (6, 6)) # 출력 이미지 크기 설정
plt.imshow(result, interpolation = 'bilinear')
plt.axis('off') # 축 레이블 제거
plt.show()