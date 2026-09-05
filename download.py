from datasets import load_dataset

ds = load_dataset("allenai/reward-bench-2", split="test")

# 导出为 jsonl (每行一条json，最适合评测脚本读取)
ds.to_json("reward_bench_test.jsonl", orient="records", lines=True)

# 导出为完整json数组
ds.to_json("reward_bench_test.json", orient="records")
