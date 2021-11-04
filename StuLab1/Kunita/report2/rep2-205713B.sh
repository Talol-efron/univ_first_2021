#!/bin/zsh
#1~9個で数字を入力してください。
#入力した数字とその要素数を返します。

list=($1 $2 $3 $4 $5 $6 $7 $8 $9)

for score in $list
do
    echo $score
done

echo "さあここで、あなたが入力した文字の要素数は何個でしょうか？"
echo -n 直感で答えてください:
read int

if [ $int -eq ${#list[@]} ]; then
    echo "大正解！"
    echo "あなたが入力した文字の要素数は"${#list[@]}"個でした"
else
    echo "不正解。。"
    echo "あなたが入力した文字の要素数は"${#list[@]}"個でした"
fi