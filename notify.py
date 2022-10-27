import config
from slack_sdk.web import WebClient

# settings
slack_api_token = config.slack_api_token
slack_channel_name = config.slack_channel_name


def post_to_slack(slack_description):
    # TODO Exceptionの処理をしたい
    slack_client = WebClient(slack_api_token)
    response = slack_client.chat_postMessage(
        text=slack_description,
        channel=slack_channel_name
    )
    print('slack_response: {}'.format(response))


def main():
    post_to_slack("hoge")


main()
