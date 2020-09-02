# Status notifications in Zulip

Python script to:
 * check all messages in Zulip Source Stream
 * if a message contains the :fire: or :warning: emoticon, send notification to Zulip Target Stream Topic

```
docker run \
  -e ZULIP_SITE=https://zulip.example.com \
  -e ZULIP_EMAIL=picimaci-proba-bot@zulip.example.com \
  -e ZULIP_API_KEY=secret \
  -e ZULIP_SOURCE_STREAM=Status \
  -e ZULIP_TARGET_STREAM=Transformers \
  -e ZULIP_TARGET_TOPIC=hello \
  picimaci/status-notifications-zulip
```