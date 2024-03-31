# 文字列のハッシュ値を取得

```bash
python pyhash.py sthash --algorithm sha256 --string test        
ハッシュ値: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
```

# ファイルのハッシュ値を取得

```bash
python pyhash.py filehash --algorithm sha256 --file ./pyhash.py
ファイルのハッシュ値: aba85b466692ac19f9f851dfd773abdf69f7a3bef11dea87b26aa59dfb70c3f4
```

# ハッシュ値の比較

```bash
python pyhash.py comp --algorithm sha256 --file ./pyhash.py --hash aba85b466692ac19f9f851dfd773abdf69f7a3bef11dea87b26aa59dfb70c3f4  

ハッシュ値は一致しています
```