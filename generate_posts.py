import random
from datetime import date

works = [
    {
        "title": "おすすめ作品A",
        "genre": "ストーリー重視",
        "point": "ストーリーをじっくり楽しみたい人向け",
        "url": "ここにアフィリエイトリンク"
    },
    {
        "title": "おすすめ作品B",
        "genre": "絵が綺麗",
        "point": "作画重視で作品を選びたい人向け",
        "url": "ここにアフィリエイトリンク"
    }
]

work = random.choice(works)

post = f"""📚 今日のおすすめ

「{work["title"]}」

{work["genre"]}で探しているならチェックしたい作品。

{work["point"]}

詳細・サンプルはこちら👇
{work["url"]}

#おすすめ漫画
"""

print(post)
