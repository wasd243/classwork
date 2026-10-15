## Class Work 2026 10 15

This is a PyO3 bridge practice class work, also resolved problem in [Canvas](https://windermereprep.instructure.com/courses/7900/assignments/242172)

### LLM disclosure
I used ChatGPT to search PyO3 documentations and help me understand APIs.

### How to execute?
This program will fail if you directly use python interpreter execute. Before execution, you should:
```bash
cd parser
maturin develop # build and install the Rust extension module

cd .. # go back to 20261015
python3 main.py
```
