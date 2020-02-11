from pathlib import Path

path = Path("ecommerce")

for p in path.iterdir():
    print(p)
