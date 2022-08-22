# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

from util.sample import Util

from factory import Boto3ClientFactory as Factory

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
LOG_CONFIG_FILE = ['config', 'log_config.json']

logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(os.path.join(PYTHON_APP_HOME, *LOG_CONFIG_FILE))
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if __name__ == '__main__':
    # .envの取得
    # setting.ENV_DIC[ImportEnvKeyEnum.importenvに書いた値.value]
    
    # 起動引数の取得
    args = sys.argv
    # args[0]はpythonのファイル名。
    # 実際の引数はargs[1]から。
    args_index = 1
    message = args[args_index]
    args_index = args_index + 1

    url = setting.ENV_DIC[ImportEnvKeyEnum.SQS_URL.value]
    group_id = setting.ENV_DIC[ImportEnvKeyEnum.SQS_GROUP_ID.value]

    logger.info("url : {}".format(url))
    logger.info("group : {}".format(group_id))
    logger.info("message : {}".format(message))

    sqs_client = Factory.create('sqs')
    
    logger.info("region : {}".format(sqs_client._client_config.region_name))

    sqs_client.send_message(
        QueueUrl=url,
        MessageBody=message,
        MessageGroupId=group_id
    )
    
    