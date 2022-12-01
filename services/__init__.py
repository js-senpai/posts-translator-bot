import bleach
from aiogram import types
from deep_translator import GoogleTranslator

from config import BaseConfig

get_config = BaseConfig()


async def post_service(bot, data: types.Message):
    # Get group id
    group_id = data["chat"]["id"]
    # Get group title
    group_title = data["chat"]["title"]
    # Get text and remove all links
    text = bleach.clean(data.html_text, tags=['b', 'i', 'strong', 'i', 'em', 'code', 's', 'strike', 'del', 'pre'],
                        strip=True)
    print(f'New post from group "{group_title}" with id {group_id}')
    # Get settings from json
    get_groups = get_config.get_json_configs()
    # Get ids for "from groups"
    from_groups_ids = get_groups["groups_from"]
    # Get ids for "to groups"
    to_groups_ids = get_groups["groups_to"]
    check_id = False
    group_language = 'uk'
    # Check if group id exist in "from groups"
    for item in from_groups_ids:
        if item["id"] == group_id:
            check_id = True
            group_language = item["lang"]
            break
    if check_id:
        for item in to_groups_ids:
            translated_text = GoogleTranslator(source=group_language, target=item["lang"]).translate(text)
            if translated_text:
                for group in to_groups_ids:
                    if group["id"] != group_id:
                        await bot.send_message(group["id"], translated_text, parse_mode="HTML")
