# Tractatus Logico-Codicus

ウィトゲンシュタインが好むコーディングスタイル

> 語りえぬものは、コメントするな。

---

## 1. 語りえぬものは、コメントするな。

コードが明晰に語れないなら、沈黙しなければならない。

```haskell
-- 悪い例: 語りえぬものをコメントで語ろうとしている
x = x + 1  -- x をインクリメントする

-- 良い例: コードがそれ自体で語る
increment :: Int -> Int
increment x = x + 1
```

## 2. 「考えるな。見よ。」

コードは一目で分かるように。

```python
# 悪い: 考える必要がある
r = [x for xs in nested for x in xs if x > 0]

# 良い: 見れば分かる
def flatten_positive(nested):
    result = []
    for xs in nested:
        for x in xs:
            if x > 0:
                result.append(x)
    return result
```

## 3. 言語ゲーム

問題に合わせて言語を発明せよ。DSL を恐れるな。

```python
# 悪い: 汎用言語で全てを語ろうとする
if status == "active" and user.role == "admin" and not user.suspended:
    grant_access()

# 良い: 問題の言語で語る
match (user.role, status):
    case (Admin(), Active()): grant_access()
```

## 4. 家族類似性

継承より構成。カテゴリよりプロトコル。

```haskell
-- 悪い: 本質主義的な継承
class Animal { virtual void speak(); }
class Dog : Animal { void speak() override { print "bow"; } }

-- 良い: 家族類似性としての型クラス
class Speakable a where
    speak :: a -> String

data Dog = Dog
instance Speakable Dog where
    speak _ = "bow"
```

## 5. 治療としての哲学

複雑さは解体するものであり、構築するものではない。

```python
# 悪い: 問題を「解決」する（さらに複雑にする）
class AbstractFactoryProviderBuilderFactory: ...

# 良い: 問題を「溶解」する
def build(): ...
```

## 6. ハシゴ

登り終えたら捨てよ。

```python
# 理解のために書いたコメント → 理解したら消せ
# プロトタイプのコード → 本番では捨てよ
# フレームワーク → 理解したら不要になる
```

> 私の命題を明らかにした者は、最終的にそれらが無意味であることを理解する。
> ハシゴを登り終えたなら、ハシゴを捨てなければならない。

## 7. 沈黙

語りえぬものについては、沈黙しなければならない。

```haskell
-- 最後のファイルは空でもよい。
-- 全てが明晰になったなら、書くことは何もない。
```

---

## 結論

```haskell
data Code = Code
  { clarity :: Clear
  , silence :: Mute
  , therapy :: Refactor
  }
```

コードは世界の論理像である。
像の正しさは、コードが語ることではなく、コードが沈黙することにある。

---

## 関連

- [SANDBOX #281](https://github.com/bonsai/SANDBOX/issues/281) — 元になった Issue
- [SANDBOX #270](https://github.com/bonsai/SANDBOX/issues/270) — Agent = DB -> DB
- [SANDBOX #269](https://github.com/bonsai/SANDBOX/issues/269) — データは世界を抽象したものである

## License

MIT
