cd content
python3 ./work/transformers/examples/seq2seq/run_summarization.py --model_name_or_path=sonoisa/t5-base-japanese --do_train --do_eval --train_file=work/train.csv --validation_file=work/dev.csv --num_train_epochs=10 --per_device_train_batch_size=4 --per_device_eval_batch_size=4 --save_steps=5000 --save_total_limit=3 --output_dir=work/output --predict_with_generate --use_fast_tokenizer=False --logging_steps=100