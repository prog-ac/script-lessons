# jsonデータを読み込んでメンバーの給与をし、給与の多い順に並び替えて表示しよう

## 条件

|ランク(rank)|勤続年数|給与|
|---|---|---|
|A|5年未満|3000x勤続年数+100,000|
|A|5年以上|3000x勤続年数+120,000|
|B|-|4000x勤続年数+140,000|
|C|-|5000x勤続年数+160,000|

## ヒント

オブジェクトの操作になれよう

## 実行コマンド

JavaScript
```shell:
node main.js ./users.json
```
Ruby
```shell:
ruby main.rb ./users.json
```
Python
```shell:
python3 main.py ./users.json
```
PHP
```shell:
php main.php ./users.json
```

## 実行結果

```shell:
Takahashi:210000
Ito:168000
Tanaka:165000
Sato:156000
Yamada:135000
Suzuki:109000
```
