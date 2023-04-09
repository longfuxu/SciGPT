# SciGPT

## How to use:
### 一、Run with python scripts

Windows, MacOS and Ubuntu systems should be fine;

python version is best 3.9, other versixons should not have any problems

1. Copy `apikey.example` and rename it as `apikey.ini`; fill in your openai key in apikey.ini. Note that this code is a pure local project, your key is very safe!

2. The process must ensure global proxy! 

3. Install dependencies:
``` bash
pip install -r requirements.txt
```
4. Run chat_paper.py, for example:

```python
python chat_paper.py --pdf_path "pdf_path.pdf"
```

## Credit
This repo is modified based on repo[https://github.com/kaixindelele/ChatPaper]. 