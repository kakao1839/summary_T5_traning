from transformers import pipeline

text2text_pipeline = pipeline(
    model="llm-book/t5-base-long-livedoor-news-corpus"
)

lyric_summ = input("Enter Text:").replace('\\n','\n')
article = lyric_summ

print(text2text_pipeline(article)[0]["generated_text"])