# slack-bot-template

slackに何らかを通知するサンプル

## example

```bash
cp config.py.sample config.py
vi config.py
```

settings -> Install Appから取得したBot User OAuth Tokenを使用する
参考: https://qiita.com/seratch/items/93714b5cf3974c2f5327

```
python3 -m pip install -t . -U slack_sdk
python3 ./notify.py
```
