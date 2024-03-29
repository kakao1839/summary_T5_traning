import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained('Gou1839/Live-Door-3Line-Summary')
tokenizer = AutoTokenizer.from_pretrained('sonoisa/t5-base-japanese')



text = r"""
いつもどおりのある日の事 君は突然立ち上がり言った
「今夜星を見に行こう」
「たまには良いこと言うんだね」 なんてみんなして言って笑った
明かりもない道を
バカみたいにはしゃいで歩いた
抱え込んだ孤独や不安に 押しつぶされないように
真っ暗な世界から見上げた 夜空は星が降るようで
いつからだろう 君の事を 追いかける私がいた
どうかお願い 驚かないで聞いてよ
私のこの想いを
「あれがデネブ、アルタイル、ベガ」
君は指さす夏の大三角 覚えて空を見る
やっと見つけた織姫様 だけどどこだろう彦星様
これじゃひとりぼっち
楽しげなひとつ隣の君 私は何も言えなくて
本当はずっと君の事を どこかでわかっていた
見つかったって 届きはしない
だめだよ 泣かないで
そう言い聞かせた
強がる私は臆病で 興味がないようなふりをしてた
だけど
胸を刺す痛みは増してく
ああそうか 好きになるって こういう事なんだね
どうしたい？ 言ってごらん
心の声がする
君の隣がいい 真実は残酷だ
言わなかった
言えなかった
二度と戻れない
あの夏の日 きらめく星
今でも思い出せるよ
笑った顔も 怒った顔も
大好きでした おかしいよね わかってたのに
君の知らない 私だけの秘密
夜を越えて 遠い思い出の君が
指をさす 無邪気な声で"""

inputs = tokenizer(text, return_tensors="pt", max_length=512,truncation=True)

outputs = model.generate(inputs["input_ids"], max_length=40, min_length=10,num_beams=4, early_stopping=True)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))