#Install and Import Dependencies
#pytorch to speed up process between research prototyping and deployment
# GPT3 DL model trained on 175 Billion parameters and that's good for text generation and Q&A 
!pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html

!pip install transformers 
#has alot of pipelines like convestional , Feature extraction , text generation and translation , it adoptes the mechanism of self attention , differentially weight the significance .
#allow you to leverage alot of sophsticated models
from transformers import pipeline # First line

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B') # Second line , 2.7 bilion Parameters

#Generate Text using Prompt
prompt = "How to be like Mohamed Hamisa" # Third line
res = generator(prompt, max_length=50, do_sample=True, temperature=0.9) # Fourth line result , do_samples to leverage sampling in model , Temp to model next set of Probablilites

#Output Text
print(res[0]['generated_text'])

with open('gpttext.txt', 'w') as f: #to write , to deal with it as a variable calles f
    f.writelines(res[0]['generated_text'])
