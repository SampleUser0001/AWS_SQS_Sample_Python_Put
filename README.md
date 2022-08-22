# AWS SQS sample Python put

AWS SQSにPythonでputする。

## 準備

``` bash
ln -s ~/.aws ./.aws
```

## 実行

``` bash
# 任意のメッセージ
message=
docker-compose run sqs_put ${message}
```
