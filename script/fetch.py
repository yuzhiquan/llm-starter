import urllib.request, pathlib, time

base = 'https://raw.githubusercontent.com/GitHubxsy/nanoAgent/claude/organize-teaching-materials-4hnRP/llm-from-scratch/'
out = pathlib.Path(r'C:\Users\益达\WorkBuddy\2026-09-18-23-06-10\materials')
out.mkdir(parents=True, exist_ok=True)

md = ['README.md'] + [f'llm-{i:02d}-{n}.md' for i, n in [
    (1, 'next-token'), (2, 'token'), (3, 'embedding'), (4, 'attention'),
    (5, 'transformer'), (6, 'training'), (7, 'inference'), (8, 'context-window'),
    (9, 'scaling-law'), (10, 'agent'), (11, 'multimodal'), (12, 'gpu'),
    (13, 'token-pricing'), (14, 'thinking-mode'), (15, 'moe'), (16, 'operators')]]

py = ['analogy.py', 'attention.py', 'bpe_demo.py', 'context_embedding.py',
      'context_window.py', 'embedding.py', 'generate.py', 'inference.py',
      'multi_head.py', 'predict.py', 'scaling_law.py', 'tiny_agent.py',
      'token_cost.py', 'tokenizer_demo.py', 'train_tiny.py',
      'transformer_anatomy.py', 'visualize.py']

fails = []
for f in md + py:
    ok = False
    for attempt in range(4):
        try:
            req = urllib.request.Request(base + f, headers={'User-Agent': 'curl'})
            data = urllib.request.urlopen(req, timeout=45).read()
            (out / f).write_bytes(data)
            print('OK', f, len(data))
            ok = True
            break
        except Exception as e:
            time.sleep(1.5)
    if not ok:
        fails.append(f)
        print('FAIL', f)

print('FAILED:', fails)
