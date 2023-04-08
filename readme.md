# SciGPT

This repo is modified based on repo[]. 

## How to use:
### 一、Run with python scripts

Windows, MAC and Ubuntu systems should be fine;

python version is best 3.9, other versions should not have any problems

1. Fill in your openai key in apikey.ini. Note that this code is a pure local project, your key is very safe!

2. The process must ensure global proxy! (Non-Chinese users may not have this problem)

3. Install dependencies:
``` bash
pip install -r requirements.txt
```
4. Run chat_paper.py, for example:

```python
python chat_paper.py --pdf_path "pdf_path.pdf"
```
