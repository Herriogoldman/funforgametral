import discord
import os
import asyncio
import typing
import random
from random import*
from discord.ext import commands
client = discord.Client()
@client.event
async def on_ready():
    print("Bot en ligne")
    channel=client.get_channel(687014490793050114)
    await channel.send('Je suis en ligne') 
    
liste_emoji=['😀', '😁', '😂', '🤣', '😃', '😄', '😅', '😆', '😉', '😊', '😋', '😎', '😍', '😘', '🥰', '😗', '😙', '😚', '☺️', '🙂', '🤗', '🤩', '🤔', '🤨', '😐', '😑', '😶', '🙄', '😏', '😣', '😥', '😮', '🤐', '😯', '😪', '😫', '😴', '😌', '😛', '😜', '😝', '🤤', '😒', '😓', '😔', '😕', '🙃', '🤑', '😲', '☹️', '🙁', '😖', '😞', '😟', '😤', '😢', '😭', '😦', '😧', '😨', '😩', '🤯', '😬', '😰', '😱', '🥵', '🥶', '😳', '🤪', '😵', '😡', '😠', '🤬', '😷', '🤒', '🤕', '🤢', '🤮', '🤧', '😇', '🤠', '🤡', '🥳', '🥴', '🥺', '🤥', '🤫', '🤭', '🧐', '🤓', '😈', '👿', '👹', '👺', '💀', '👻', '👽', '🤖', '💩', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '👶', '👧', '🧒', '👦', '👩', '🧑', '👨', '👵', '🧓', '👴', '👲', '👳\u200d♀️', '👳\u200d♂️', '🧕', '🧔', '👱\u200d♂️', '👱\u200d♀️', '👨\u200d🦰', '👩\u200d🦰', '👨\u200d🦱', '👩\u200d🦱', '👨\u200d🦲', '👩\u200d🦲', '👨\u200d🦳', '👩\u200d🦳', '🦸\u200d♀️', '🦸\u200d♂️', '🦹\u200d♀️', '🦹\u200d♂️', '👮\u200d♀️', '👮\u200d♂️', '👷\u200d♀️', '👷\u200d♂️', '💂\u200d♀️', '💂\u200d♂️', '🕵️\u200d♀️', '🕵️\u200d♂️', '👩\u200d⚕️', '👨\u200d⚕️', '👩\u200d🌾', '👨\u200d🌾', '👩\u200d🍳', '👨\u200d🍳', '👩\u200d🎓', '👨\u200d🎓', '👩\u200d🎤', '👨\u200d🎤', '👩\u200d🏫', '👨\u200d🏫', '👩\u200d🏭', '👨\u200d🏭', '👩\u200d💻', '👨\u200d💻', '👩\u200d💼', '👨\u200d💼', '👩\u200d🔧', '👨\u200d🔧', '👩\u200d🔬', '👨\u200d🔬', '👩\u200d🎨', '👨\u200d🎨', '👩\u200d🚒', '👨\u200d🚒', '👩\u200d✈️', '👨\u200d✈️', '👩\u200d🚀', '👨\u200d🚀', '👩\u200d⚖️', '👨\u200d⚖️', '👰', '🤵', '👸', '🤴', '🤶', '🎅', '🧙\u200d♀️', '🧙\u200d♂️', '🧝\u200d♀️', '🧝\u200d♂️', '🧛\u200d♀️', '🧛\u200d♂️', '🧟\u200d♀️', '🧟\u200d♂️', '🧞\u200d♀️', '🧞\u200d♂️', '🧜\u200d♀️', '🧜\u200d♂️', '🧚\u200d♀️', '🧚\u200d♂️', '👼', '🤰', '🤱', '🙇\u200d♀️', '🙇\u200d♂️', '💁\u200d♀️', '💁\u200d♂️', '🙅\u200d♀️', '🙅\u200d♂️', '🙆\u200d♀️', '🙆\u200d♂️', '🙋\u200d♀️', '🙋\u200d♂️', '🤦\u200d♀️', '🤦\u200d♂️', '🤷\u200d♀️', '🤷\u200d♂️', '🙎\u200d♀️', '🙎\u200d♂️', '🙍\u200d♀️', '🙍\u200d♂️', '💇\u200d♀️', '💇\u200d♂️', '💆\u200d♀️', '💆\u200d♂️', '🧖\u200d♀️', '🧖\u200d♂️', '💅', '🤳', '💃', '🕺', '👯\u200d♀️', '👯\u200d♂️', '🕴', '🚶\u200d♀️', '🚶\u200d♂️', '🏃\u200d♀️', '🏃\u200d♂️', '👫', '👭', '👬', '💑', '👩\u200d❤️\u200d👩', '👨\u200d❤️\u200d👨', '💏', '👩\u200d❤️\u200d💋\u200d👩', '👨\u200d❤️\u200d💋\u200d👨', '👪', '👨\u200d👩\u200d👧', '👨\u200d👩\u200d👧\u200d👦', '👨\u200d👩\u200d👦\u200d👦', '👨\u200d👩\u200d👧\u200d👧', '👩\u200d👩\u200d👦', '👩\u200d👩\u200d👧', '👩\u200d👩\u200d👧\u200d👦', '👩\u200d👩\u200d👦\u200d👦', '👩\u200d👩\u200d👧\u200d👧', '👨\u200d👨\u200d👦', '👨\u200d👨\u200d👧', '👨\u200d👨\u200d👧\u200d👦', '👨\u200d👨\u200d👦\u200d👦', '👨\u200d👨\u200d👧\u200d👧', '👩\u200d👦', '👩\u200d👧', '👩\u200d👧\u200d👦', '👩\u200d👦\u200d👦', '👩\u200d👧\u200d👧', '👨\u200d👦', '👨\u200d👧', '👨\u200d👧\u200d👦', '👨\u200d👦\u200d👦', '👨\u200d👧\u200d👧', '🤲', '👐', '🙌', '👏', '🤝', '👍', '👎', '👊', '✊', '🤛', '🤜', '🤞', '✌️', '🤟', '🤘', '👌', '👈', '👉', '👆', '👇', '☝️', '✋', '🤚', '🖐', '🖖', '👋', '🤙', '💪', '🦵', '🦶', '🖕', '✍️', '🙏', '💍', '💄', '💋', '👄', '👅', '👂', '👃', '👣', '👁', '👀', '🧠', '🦴', '🦷', '🗣', '👤', '🧥', '👚', '👕', '👖', '👔', '👗', '👙', '👘', '👠', '👡', '👢', '👞', '👟', '🥾', '🥿', '🧦', '🧤', '🧣', '🎩', '🧢', '👒', '🎓', '⛑', '👑', '👝', '👛', '👜', '💼', '🎒', '👓', '🕶', '🥽', '🥼', '🌂', '🧵', '🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🦝', '🐻', '🐼', '🦘', '🦡', '🐨', '🐯', '🦁', '🐮', '🐷', '🐽', '🐸', '🐵', '🙈', '🙉', '🙊', '🐒', '🐔', '🐧', '🐦', '🐤', '🐣', '🐥', '🦆', '🦢', '🦅', '🦉', '🦚', '🦜', '🦇', '🐺', '🐗', '🐴', '🦄', '🐝', '🐛', '🦋', '🐌', '🐚', '🐞', '🐜', '🦗', '🕷', '🕸', '🦂', '🦟', '🦠', '🐢', '🐍', '🦎', '🦖', '🦕', '🐙', '🦑', '🦐', '🦀', '🐡', '🐠', '🐟', '🐬', '🐳', '🐋', '🦈', '🐊', '🐅', '🐆', '🦓', '🦍', '🐘', '🦏', '🦛', '🐪', '🐫', '🦙', '🦒', '🐃', '🐂', '🐄', '🐎', '🐖', '🐏', '🐑', '🐐', '🦌', '🐕', '🐩', '🐈', '🐓', '🦃', '🕊', '🐇', '🐁', '🐀', '🐿', '🦔', '🐾', '🐉', '🐲', '🌵', '🎄', '🌲', '🌳', '🌴', '🌱', '🌿', '☘️', '🍀', '🎍', '🎋', '🍃', '🍂', '🍁', '🍄', '🌾', '💐', '🌷', '🌹', '🥀', '🌺', '🌸', '🌼', '🌻', '🌞', '🌝', '🌛', '🌜', '🌚', '🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔', '🌙', '🌎', '🌍', '🌏', '💫', '⭐️', '🌟', '✨', '⚡️', '☄️', '💥', '🔥', '🌪', '🌈', '☀️', '🌤', '⛅️', '🌥', '☁️', '🌦', '🌧', '⛈', '🌩', '🌨', '❄️', '☃️', '⛄️', '🌬', '💨', '💧', '💦', '☔️', '☂️', '🌊', '🍏', '🍎', '🍐', '🍊', '🍋', '🍌', '🍉', '🍇', '🍓', '🍈', '🍒', '🍑', '🍍', '🥭', '🥥', '🥝', '🍅', '🍆', '🥑', '🥦', '🥒', '🥬', '🌶', '🌽', '🥕', '🥔', '🍠', '🥐', '🍞', '🥖', '🥨', '🥯', '🧀', '🥚', '🍳', '🥞', '🥓', '🥩', '🍗', '🍖', '🌭', '🍔', '🍟', '🍕', '🥪', '🥙', '🌮', '🌯', '🥗', '🥘', '🥫', '🍝', '🍜', '🍲', '🍛', '🍣', '🍱', '🥟', '🍤', '🍙', '🍚', '🍘', '🍥', '🥮', '🥠', '🍢', '🍡', '🍧', '🍨', '🍦', '🥧', '🍰', '🎂', '🍮', '🍭', '🍬', '🍫', '🍿', '🧂', '🍩', '🍪', '🌰', '🥜', '🍯', '🥛', '🍼', '☕️', '🍵', '🥤', '🍶', '🍺', '🍻', '🥂', '🍷', '🥃', '🍸', '🍹', '🍾', '🥄', '🍴', '🍽', '🥣', '🥡', '\u26BD', '🏀', '🏈', '⚾️', '🥎', '🏐', '🏉', '🎾', '🥏', '🎱', '🏓', '🏸', '🥅', '🏒', '🏑', '🥍', '🏏', '⛳️', '🏹', '🎣', '🥊', '🥋', '🎽', '⛸', '🥌', '🛷', '🛹', '🎿', '⛷', '🏂', '🏋️\u200d♀️', '🏋🏻\u200d♀️', '🏋🏼\u200d♀️', '🏋🏽\u200d♀️', '🏋🏾\u200d♀️', '🏋🏿\u200d♀️', '🏋️\u200d♂️', '🏋🏻\u200d♂️', '🏋🏼\u200d♂️', '🏋🏽\u200d♂️', '🏋🏾\u200d♂️', '🏋🏿\u200d♂️', '🤼\u200d♀️', '🤼\u200d♂️', '🤸\u200d♀️', '🤸🏻\u200d♀️', '🤸🏼\u200d♀️', '🤸🏽\u200d♀️', '🤸🏾\u200d♀️', '🤸🏿\u200d♀️', '🤸\u200d♂️', '🤸🏻\u200d♂️', '🤸🏼\u200d♂️', '🤸🏽\u200d♂️', '🤸🏾\u200d♂️', '🤸🏿\u200d♂️', '⛹️\u200d♀️', '⛹🏻\u200d♀️', '⛹🏼\u200d♀️', '⛹🏽\u200d♀️', '⛹🏾\u200d♀️', '⛹🏿\u200d♀️', '⛹️\u200d♂️', '⛹🏻\u200d♂️', '⛹🏼\u200d♂️', '⛹🏽\u200d♂️', '⛹🏾\u200d♂️', '⛹🏿\u200d♂️', '🤺', '🤾\u200d♀️', '🤾🏻\u200d♀️', '🤾🏼\u200d♀️', '🤾🏾\u200d♀️', '🤾🏾\u200d♀️', '🤾🏿\u200d♀️', '🤾\u200d♂️', '🤾🏻\u200d♂️', '🤾🏼\u200d♂️', '🤾🏽\u200d♂️', '🤾🏾\u200d♂️', '🤾🏿\u200d♂️', '🏌️\u200d♀️', '🏌🏻\u200d♀️', '🏌🏼\u200d♀️', '🏌🏽\u200d♀️', '🏌🏾\u200d♀️', '🏌🏿\u200d♀️', '🏌️\u200d♂️', '🏌🏻\u200d♂️', '🏌🏼\u200d♂️', '🏌🏽\u200d♂️', '🏌🏾\u200d♂️', '🏌🏿\u200d♂️', '🏇', '🏇🏻', '🏇🏼', '🏇🏽', '🏇🏾', '🏇🏿', '🧘\u200d♀️', '🧘🏻\u200d♀️', '🧘🏼\u200d♀️', '🧘🏽\u200d♀️', '🧘🏾\u200d♀️', '🧘🏿\u200d♀️', '🧘\u200d♂️', '🧘🏻\u200d♂️', '🧘🏼\u200d♂️', '🧘🏽\u200d♂️', '🧘🏾\u200d♂️', '🧘🏿\u200d♂️', '🏄\u200d♀️', '🏄🏻\u200d♀️', '🏄🏼\u200d♀️', '🏄🏽\u200d♀️', '🏄🏾\u200d♀️', '🏄🏿\u200d♀️', '🏄\u200d♂️', '🏄🏻\u200d♂️', '🏄🏼\u200d♂️', '🏄🏽\u200d♂️', '🏄🏾\u200d♂️', '🏄🏿\u200d♂️', '🏊\u200d♀️', '🏊🏻\u200d♀️', '🏊🏼\u200d♀️', '🏊🏽\u200d♀️', '🏊🏾\u200d♀️', '🏊🏿\u200d♀️', '🏊\u200d♂️', '🏊🏻\u200d♂️', '🏊🏼\u200d♂️', '🏊🏽\u200d♂️', '🏊🏾\u200d♂️', '🏊🏿\u200d♂️', '🤽\u200d♀️', '🤽🏻\u200d♀️', '🤽🏼\u200d♀️', '🤽🏽\u200d♀️', '🤽🏾\u200d♀️', '🤽🏿\u200d♀️', '🤽\u200d♂️', '🤽🏻\u200d♂️', '🤽🏼\u200d♂️', '🤽🏽\u200d♂️', '🤽🏾\u200d♂️', '🤽🏿\u200d♂️', '🚣\u200d♀️', '🚣🏻\u200d♀️', '🚣🏼\u200d♀️', '🚣🏽\u200d♀️', '🚣🏾\u200d♀️', '🚣🏿\u200d♀️', '🚣\u200d♂️', '🚣🏻\u200d♂️', '🚣🏼\u200d♂️', '🚣🏽\u200d♂️', '🚣🏾\u200d♂️', '🚣🏿\u200d♂️', '🧗\u200d♀️', '🧗🏻\u200d♀️', '🧗🏼\u200d♀️', '🧗🏽\u200d♀️', '🧗🏾\u200d♀️', '🧗🏿\u200d♀️', '🧗\u200d♂️', '🧗🏻\u200d♂️', '🧗🏼\u200d♂️', '🧗🏽\u200d♂️', '🧗🏾\u200d♂️', '🧗🏿\u200d♂️', '🚵\u200d♀️', '🚵🏻\u200d♀️', '🚵🏼\u200d♀️', '🚵🏽\u200d♀️', '🚵🏾\u200d♀️', '🚵🏿\u200d♀️', '🚵\u200d♂️', '🚵🏻\u200d♂️', '🚵🏼\u200d♂️', '🚵🏽\u200d♂️', '🚵🏾\u200d♂️', '🚵🏿\u200d♂️', '🚴\u200d♀️', '🚴🏻\u200d♀️', '🚴🏼\u200d♀️', '🚴🏽\u200d♀️', '🚴🏾\u200d♀️', '🚴🏿\u200d♀️', '🚴\u200d♂️', '🚴🏻\u200d♂️', '🚴🏼\u200d♂️', '🚴🏽\u200d♂️', '🚴🏾\u200d♂️', '🚴🏿\u200d♂️', '🏆', '🥇', '🥈', '🥉', '🏅', '🎖', '🏵', '🎗', '🎫', '🎟', '🎪', '🤹\u200d♀️', '🤹🏻\u200d♀️', '🤹🏼\u200d♀️', '🤹🏽\u200d♀️', '🤹🏾\u200d♀️', '🤹🏿\u200d♀️', '🤹\u200d♂️', '🤹🏻\u200d♂️', '🤹🏼\u200d♂️', '🤹🏽\u200d♂️', '🤹🏾\u200d♂️', '🤹🏿\u200d♂️', '🎭', '🎨', '🎬', '🎤', '🎧', '🎼', '🎹', '🥁', '🎷', '🎺', '🎸', '🎻', '🎲', '🧩', '♟', '🎯', '🎳', '🎮', '🚗', '🚕', '🚙', '🚌', '🚎', '🏎', '🚓', '🚑', '🚒', '🚐', '🚚', '🚛', '🚜', '🛴', '🚲', '🛵', '🏍', '🚨', '🚔', '🚍', '🚘', '🚖', '🚡', '🚠', '🚟', '🚃', '🚋', '🚞', '🚝', '🚄', '🚅', '🚈', '🚂', '🚆', '🚇', '🚊', '🚉', '✈️', '🛫', '🛬', '🛩', '💺', '🛰', '🚀', '🛸', '🚁', '🛶', '⛵️', '🚤', '🛥', '🛳', '⛴', '🚢', '⚓️', '⛽️', '🚧', '🚦', '🚥', '🚏', '🗺', '🗿', '🗽', '🗼', '🏰', '🏯', '🏟', '🎡', '🎢', '🎠', '⛲️', '⛱', '🏖', '🏝', '🏜', '🌋', '⛰', '🏔', '🗻', '🏕', '⛺️', '🏠', '🏡', '🏘', '🏚', '🏗', '🏭', '🏢', '🏬', '🏣', '🏤', '🏥', '🏦', '🏨', '🏪', '🏫', '🏩', '💒', '🏛', '⛪️', '🕌', '🕍', '🕋', '⛩', '🛤', '🛣', '🗾', '🎑', '🏞', '🌅', '🌄', '🌠', '🎇', '🎆', '🌇', '🌆', '🏙', '🌃', '🌌', '🌉', '⌚️', '📱', '📲', '💻', '⌨️', '🖥', '🖨', '🖱', '🖲', '🕹', '🗜', '💽', '💾', '💿', '📀', '📼', '📷', '📸', '📹', '🎥', '📽', '🎞', '📞', '☎️', '📟', '📠', '📺', '📻', '🎙', '🎚', '🎛', '⏱', '⏲', '⏰', '🕰', '⌛️', '⏳', '📡', '🔋', '🔌', '💡', '🔦', '🕯', '🗑', '🛢', '💸', '💵', '💴', '💶', '💷', '💰', '💳', '🧾', '💎', '⚖️', '🔧', '🔨', '⚒', '🛠', '⛏', '🔩', '⚙️', '⛓', '🔫', '💣', '🔪', '🗡', '⚔️', '🛡', '🚬', '⚰️', '⚱️', '🏺', '🧭', '🧱', '🔮', '🧿', '🧸', '📿', '💈', '⚗️', '🔭', '🧰', '🧲', '🧪', '🧫', '🧬', '🧯', '🔬', '🕳', '💊', '💉', '🌡', '🚽', '🚰', '🚿', '🛁', '🛀', '🛀🏻', '🛀🏼', '🛀🏽', '🛀🏾', '🛀🏿', '🧴', '🧵', '🧶', '🧷', '🧹', '🧺', '🧻', '🧼', '🧽', '🛎', '🔑', '🗝', '🚪', '🛋', '🛏', '🛌', '🖼', '🛍', '🧳', '🛒', '🎁', '🎈', '🎏', '🎀', '🎊', '🎉', '🧨', '🎎', '🏮', '🎐', '🧧', '✉️', '📩', '📨', '📧', '💌', '📥', '📤', '📦', '🏷', '📪', '📫', '📬', '📭', '📮', '📯', '📜', '📃', '📄', '📑', '📊', '📈', '📉', '🗒', '🗓', '📆', '📅', '📇', '🗃', '🗳', '🗄', '📋', '📁', '📂', '🗂', '🗞', '📰', '📓', '📔', '📒', '📕', '📗', '📘', '📙', '📚', '📖', '🔖', '🔗', '📎', '🖇', '📐', '📏', '📌', '📍', '✂️', '🖊', '🖋', '✒️', '🖌', '🖍', '📝', '✏️', '🔍', '🔎', '🔏', '🔐', '🔒', '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '💔', '❣️', '💕', '💞', '💓', '💗', '💖', '💘', '💝', '💟', '☮️', '✝️', '☪️', '🕉', '☸️', '✡️', '🔯', '🕎', '☯️', '☦️', '🛐', '⛎', '♈️', '♉️', '♊️', '♋️', '♌️', '♍️', '♎️', '♏️', '♐️', '♑️', '♒️', '♓️', '🆔', '⚛️', '🉑', '☢️', '☣️', '📴', '📳', '🈶', '🈚️', '🈸', '🈺', '🈷️', '✴️', '🆚', '💮', '🉐', '㊙️', '㊗️', '🈴', '🈵', '🈹', '🈲', '🅰️', '🅱️', '🆎', '🆑', '🅾️', '🆘', '❌', '⭕️', '🛑', '⛔️', '📛', '🚫', '💯', '💢', '♨️', '🚷', '🚯', '🚳', '🚱', '🔞', '📵', '🚭', '❗️', '❕', '❓', '❔', '‼️', '⁉️', '🔅', '🔆', '〽️', '⚠️', '🚸', '🔱', '⚜️', '🔰', '♻️', '✅', '🈯️', '💹', '❇️', '✳️', '❎', '🌐', '💠', 'Ⓜ️', '🌀', '💤', '🏧', '🚾', '♿️', '🅿️', '🈳', '🈂️', '🛂', '🛃', '🛄', '🛅', '🚹', '🚺', '🚼', '🚻', '🚮', '🎦', '📶', '🈁', '🔣', 'ℹ️', '🔤', '🔡', '🔠', '🆖', '🆗', '🆙', '🆒', '🆕', '🆓', '0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟', '🔢', '#️⃣', '*️⃣', '⏏️', '▶️', '⏸', '⏯', '⏹', '⏺', '⏭', '⏮', '⏩', '⏪', '⏫', '⏬', '◀️', '🔼', '🔽', '➡️', '⬅️', '⬆️', '⬇️', '↗️', '↘️', '↙️', '↖️', '↕️', '↔️', '↪️', '↩️', '⤴️', '⤵️', '🔀', '🔁', '🔂', '🔄', '🔃', '🎵', '🎶', '➕', '➖', '➗', '✖️', '♾', '💲', '💱', '™️', '©️', '®️', '〰️', '➰', '➿', '🔚', '🔙', '🔛', '🔝', '🔜', '✔️', '☑️', '🔘', '⚪️', '⚫️', '🔴', '🔵', '🔺', '🔻', '🔸', '🔹', '🔶', '🔷', '🔳', '🔲', '▪️', '▫️', '◾️', '◽️', '◼️', '◻️', '⬛️', '⬜️', '🔈', '🔇', '🔉', '🔊', '🔔', '🔕', '📣', '📢', '👁\u200d🗨', '💬', '💭', '🗯', '♠️', '♣️', '♥️', '♦️', '🃏', '🎴', '🀄️', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚', '🕛', '🕜', '🕝', '🕞', '🕟', '🕠', '🕡', '🕢', '🕣', '🕤', '🕥', '🕦','🏳️', '🏴', '🏁', '🚩', '🏳️\u200d🌈', '🏴\u200d☠️', '🇦🇫', '🇦🇽', '🇦🇱', '🇩🇿', '🇦🇸', '🇦🇩', '🇦🇴', '🇦🇮', '🇦🇶', '🇦🇬', '🇦🇷', '🇦🇲', '🇦🇼', '🇦🇺', '🇦🇹', '🇦🇿', '🇧🇸', '🇧🇭', '🇧🇩', '🇧🇧', '🇧🇾', '🇧🇪', '🇧🇿', '🇧🇯', '🇧🇲', '🇧🇹', '🇧🇴', '🇧🇦', '🇧🇼', '🇧🇷', '🇮🇴', '🇻🇬', '🇧🇳', '🇧🇬', '🇧🇫', '🇧🇮', '🇰🇭', '🇨🇲', '🇨🇦', '🇮🇨', '🇨🇻', '🇧🇶', '🇰🇾', '🇨🇫', '🇹🇩', '🇨🇱', '🇨🇳', '🇨🇽', '🇨🇨', '🇨🇴', '🇰🇲', '🇨🇬', '🇨🇩', '🇨🇰', '🇨🇷', '🇨🇮', '🇭🇷', '🇨🇺', '🇨🇼', '🇨🇾', '🇨🇿', '🇩🇰', '🇩🇯', '🇩🇲', '🇩🇴', '🇪🇨', '🇪🇬', '🇸🇻', '🇬🇶', '🇪🇷', '🇪🇪', '🇪🇹', '🇪🇺', '🇫🇰', '🇫🇴', '🇫🇯', '🇫🇮', '🇫🇷', '🇬🇫', '🇵🇫', '🇹🇫', '🇬🇦', '🇬🇲', '🇬🇪', '🇩🇪', '🇬🇭', '🇬🇮', '🇬🇷', '🇬🇱', '🇬🇩', '🇬🇵', '🇬🇺', '🇬🇹', '🇬🇬', '🇬🇳', '🇬🇼', '🇬🇾', '🇭🇹', '🇭🇳', '🇭🇰', '🇭🇺', '🇮🇸', '🇮🇳', '🇮🇩', '🇮🇷', '🇮🇶', '🇮🇪', '🇮🇲', '🇮🇱', '🇮🇹', '🇯🇲', '🇯🇵', '🎌', '🇯🇪', '🇯🇴', '🇰🇿', '🇰🇪', '🇰🇮', '🇽🇰', '🇰🇼', '🇰🇬', '🇱🇦', '🇱🇻', '🇱🇧', '🇱🇸', '🇱🇷', '🇱🇾', '🇱🇮', '🇱🇹', '🇱🇺', '🇲🇴', '🇲🇰', '🇲🇬', '🇲🇼', '🇲🇾', '🇲🇻', '🇲🇱', '🇲🇹', '🇲🇭', '🇲🇶', '🇲🇷', '🇲🇺', '🇾🇹', '🇲🇽', '🇫🇲', '🇲🇩', '🇲🇨', '🇲🇳', '🇲🇪', '🇲🇸', '🇲🇦', '🇲🇿', '🇲🇲', '🇳🇦', '🇳🇷', '🇳🇵', '🇳🇱', '🇳🇨', '🇳🇿', '🇳🇮', '🇳🇪', '🇳🇬', '🇳🇺', '🇳🇫', '🇰🇵', '🇲🇵', '🇳🇴', '🇴🇲', '🇵🇰', '🇵🇼', '🇵🇸', '🇵🇦', '🇵🇬', '🇵🇾', '🇵🇪', '🇵🇭', '🇵🇳', '🇵🇱', '🇵🇹', '🇵🇷', '🇶🇦', '🇷🇪', '🇷🇴', '🇷🇺', '🇷🇼', '🇼🇸', '🇸🇲', '🇸🇦', '🇸🇳', '🇷🇸', '🇸🇨', '🇸🇱', '🇸🇬', '🇸🇽', '🇸🇰', '🇸🇮', '🇬🇸', '🇸🇧', '🇸🇴', '🇿🇦', '🇰🇷', '🇸🇸', '🇪🇸', '🇱🇰', '🇧🇱', '🇸🇭', '🇰🇳', '🇱🇨', '🇵🇲', '🇻🇨', '🇸🇩', '🇸🇷', '🇸🇿', '🇸🇪', '🇨🇭', '🇸🇾', '🇹🇼', '🇹🇯', '🇹🇿', '🇹🇭', '🇹🇱', '🇹🇬', '🇹🇰', '🇹🇴', '🇹🇹', '🇹🇳', '🇹🇷', '🇹🇲', '🇹🇨', '🇹🇻', '🇻🇮', '🇺🇬', '🇺🇦', '🇦🇪', '🇬🇧', '🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f', '🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f', '🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f', '🇺🇳', '🇺🇸', '🇺🇾', '🇺🇿', '🇻🇺', '🇻🇦', '🇻🇪', '🇻🇳', '🇼🇫', '🇪🇭', '🇾🇪', '🇿🇲']

emote=['<:WTF:576870192705961986>', '<:sourireirl:577145595156758528>', '<:saoul:576876335243460608>', '<:ronangers:369209617168990208>', '<:rireirl:578273002521886739>', '<:regardfou:576873563492188160>', '<:oups:577228350762909723>', '<:OULAH:577153845101330492>', '<:MANGER:576877901308362763>', '<:gneugneu:576886801029922828>', '<:globuleux:577147819551358981>', '<:ennui:576883744980598794>', '<:doute:577160207684075532>', '<:dab:581600000983957504>', '<:choc:577174077932830770>', '<:bide:576869419490213888>']

biend = [
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZT0E0MTcJpcLYChSljSd3kagEzqcHgP0cvEzlvcf8olU3nWjStA",
            "https://www.tout-bon.com/newpics/40106.jpg",
            "http://www.hotfemmenue.xyz/wp-content/uploads/2017/03/exhib-de-femme-nue-du-70-chaude-et-salope-736x1024.jpg",
            "https://www.bonsoirmademoiselle.fr/wp-content/uploads/2018/04/belle-femme-nue-plus-belle-du-monde.jpg",
            "http://jolies.filles.nues.free.fr/jolies-filles-nues.jpg",
            "http://cdn.hotnakedgirls.net/2015-12-30/330251_06.jpg",
            "https://stunnershq.com/images/414/thumb/super-sexy-teen-girl-mila-azul-nude-outside-showing-her-perfect-ass-5.jpg",
            "http://cdn.nudesexporn.com/2018-06-04/527865_08.jpg",
            "http://video.damplips.com/pics/wp-content/uploads/2015/02/naked-girl-masturbates.jpg",
            "https://ftopx.com/images/201405/ftop.ru_101253.jpg",
            "https://i.pinimg.com/474x/5a/89/9a/5a899af65e8b10ce836fb1468850b470--girls-girls-girls-sexy-girls.jpg",
            "http://revalsheva.com/367/918451.jpg",
            "http://sexsagar.net/wp-content/uploads/2016/01/sunny-leone-naked-erotic-without-clothes-hd-images.jpg",
            "http://cdn.hotnudegirls.net/2015-05-20/288686_12.jpg",
            "http://xxxpicz.com/xxx/naked-japanese-teen-portal-real-sexiest-clips-women-mega-world.jpg",
            "http://viparea.com/images/samples/img02_large.jpg",
            "https://i.pinimg.com/originals/5c/84/91/5c8491d7d34d5a4f29cc8fcc8098f984.jpg",
            "http://1.bp.blogspot.com/-R3ZIrog0BrE/Ufp5pDUllQI/AAAAAAACQZc/r68ex4bazm4/s1600/Hawaiian+Tropic+Girls_provatina_com_2.jpg",
            "http://31.media.tumblr.com/065fafce58c3164307658a464c9bf542/tumblr_nnbvojHXhO1tjd582o1_400.gif",
            "https://media.tits-guru.com/images?uuid=03d1aa18-9a77-4b96-816d-60ae5a2056da",
            "http://pornpictures.xxx/wp-content/uploads/2016/01/naked-perfect-teen-boobs-gif-xxx-girls-free-porn-teen-tits-pussy-pic-gif-video-1452046128plc48.gif",
            "https://78.media.tumblr.com/167d638cebe2fff0217e6473043d76d3/tumblr_o53mlds8ma1s2wsdzo1_400.gif",
            "https://www.livexxx.me/wp-content/uploads/2014/11/Sexy-big-titted-black-haired-babe-shows-dildo1.gif",
            "http://gfpics.com/wp-content/uploads/2-69.gif",
            "http://38.media.tumblr.com/42309cd26437609dda2d2a1d2b8f1bd6/tumblr_nohib8cLDE1tv5llvo1_500.gif",
            "http://68.media.tumblr.com/f0161ab24a8072cb65992320646874d2/tumblr_inline_of5vkgFLbF1sw8ada_500.gif",
            "http://dm.damcdn.net/pics/wp-content/uploads/2012/07/sexy-girl-strip-17.jpg",
            "https://www.classy-girls.com/main/btD0W4ulod.jpg",
            "https://contenta.nakedneighbour.com/sexart.com/0941/11.jpg",
            "https://cdn.pornpics.com/pics/2017-05-18/267919_03big.jpg",
            "http://cdn1.teennudegirls.com/da/2/da226ce9c.jpg",
            "http://www.adultwalls.com/web/wallpapers/sexy-pussy-hd-nude-girl-naked-wallpaper/thumbnail/lg.jpg",
            "https://pbs.twimg.com/profile_images/450146843859906560/vjhPacVU.jpeg",
            "http://zapatosadidas.info/images/56b55460d476e6fb99176f474371c1e3.jpg",
            "https://i.pinimg.com/originals/f9/62/e0/f962e07c4828d50abdc77ec671273266.jpg",
            "https://content4.morazzia.com/playboyplus.com/5302/06.jpg",
            "https://celeb.gate.cc/media/cache/original/upload/4/e/4e383bde13.jpg",
            "http://qpornx.com/xxx/naked-girls-fingering-pussy.jpg",
            "https://cdn.pornpics.com/pics/2017-01-22/255186_01big.jpg",
            "http://cdn.hotnudegirls.net/2013-06-18/265880_08.jpg",
            "https://ftopx.com/large/201203/31476.jpg",
            "http://www.met-nude.com/MNPics/MN20130102_Met-Art-Volere-Caprice-A-Indiana-A/img/Met-Art_Volere_Caprice-A--Indiana-A_by_Luca-Helios_medium_0029.jpg",
            "https://gallery-of-nudes.com/wp-content/uploads/2016/04/Playboy-Playmate-Regina-Deutinger-Pictures-02.jpg",
            "https://i.imagepost.com/wp-content/uploads/2015/10/ana-cheri-for-pb.jpg",
            "https://www.morbomodelospics.com/wp-content/uploads/2015/10/Lindsey-Vuolo-para-Playboy-10.jpg",
            "https://www.tribute-to.com/playboy/2016/01/kristy-garett-an-american-dream-nude/h/kristy-garett-an-american-dream-nude07.jpg",
            "https://gallery-of-nudes.com/wp-content/uploads/2017/02/Playboy-Cybergirl-Jessica-Workman-Nude-03.jpg",
            "http://qpornx.com/xxx/playboy-playmate-centerfold-naked-nude.jpg",
            "http://2.bp.blogspot.com/-vyAvLu4zN4U/UALudgfqcXI/AAAAAAAAIsc/xyjS3J06eHo/s1600/entrou%20model%20sex.jpg",
            "http://xxxpornozone.com/xxx/caprice-x-art-porn.jpg",
            "https://www.cherrynudes.com/roberta-vasquez-classic-playmate/2.jpg",
            "https://www.tribute-to.com/playboy/2015/10/rachel-harris-a-creative-force-nude/h/rachel-harris-a-creative-force-nude09.jpg",
            "http://3.bp.blogspot.com/_pTyKeFv2GpM/Sa1kyS4KnFI/AAAAAAAAAxE/SvI1OX-dDsI/s400/US+Playboy+-+January+2009+%28Carmen+Electra%29+%2811%29.jpg",
            "http://assets.mrstiff.com/uploads/pornstar/jennifer-walcott/jennifer-walcott-106.jpg",
            "https://gallery-of-nudes.com/wp-content/uploads/2016/08/Playboy-Playmate-Amberleigh-West-Nude-Pictures-02-1046x697.jpg",
            "http://siaxleebi.info/imgs/f4d54ffc7f7c87435be61bae12eec1e2.jpg",
            "https://cdn4.images.motherlessmedia.com/images/8DB0EC5.jpg?fs=opencloud",
            "http://www.randomnude.com/wp-content/uploads/sites/39/tdomf/4054/ccde_WorldSoccerTeam_GroupShoots_02.jpg",
            "https://thumb-p2.xhcdn.com/a/eMgR7NfKayRSDbvSZ5UfFA/000/069/074/652_1000.jpg",
            "https://www.curvyerotic.com/thumbs/sasha6.jpg",
            "http://bestplayboy.com/sr/thumbs/0/646.jpg",
            "https://www.tribute-to.com/playboy/wp-content/uploads/2015/06/vanessa-alvar-latin-adultery-nude-365x235.jpg",
            "https://www.spicybunnies.com/gals/playboy_cyber_girls/2016/11/playboy_playmate_olivia_paige_nude/playboy_playmate_olivia_paige_nude-5.jpg",
            "http://gratuitescolaire.info/imgs/7e589c0c10a356c026512a271debf069.jpg",
            "http://xxxpornozone.com/xxx/playmate-playboy-girls-naked.jpg",
            "http://snadgy.com/wp-content/uploads/2015/08/Monica-Sims-nude-Playmate-of-the-month-September-2015-Playboy-Magazine-07.jpg",
            "http://snadgy.com/wp-content/uploads/2014/09/Sherlyn-Chopra-playboy-part2-18-667x1000.jpg",
            "https://gallery-of-nudes.com/wp-content/uploads/2016/03/playboy-Playmate-Vanessa-Hoelsher-Nude-Photos-04.jpg",
            "http://redbust.com/stuff/regina-deutinger-german-blonde/regina-deutinger-german-nude-playboy-11.jpg",
            "https://content4.babesandgirls.com/playboy-plus/0495/12.jpg",
            "http://imagepost.com/wp-content/uploads/2015/01/31.jpg",
            "http://www.drsnysvet.cz/wp-content/gallery/dd-candace-leilani-2/15.jpg",
            "https://thumb-p0.xhcdn.com/a/fiX95SSMuQsEe7nJ48G7Bw/000/048/992/970_1000.jpg",
            "https://gals.kindgirls.com/d3/zafira776/zafira776_15.jpg",
            "https://ftopx.com/images/201207/ftop.ru_36975.jpg",
            "https://contenta.babesandgirls.com/babesandgirls.com/playboy-sexy-wives/0002/04.jpg",
            "https://sozosblog.com/images/8f2d37e3621b9e377d410bf988cae148.jpg",
            "http://qpornx.com/xxx/playboy-college-girls-whitney-leigh-nude.jpg",
            "https://content4.babesandgirls.com/playboy-plus/0540/07.jpg",
            "https://i.pinimg.com/originals/6c/79/76/6c797658158c361362e3ea1c5b3a6656.jpg",
            "https://media.tits-guru.com/images?uuid=f6959fe9-7323-4a72-92c1-c16e13fa4719",
            "http://images.fuskator.com/large/eyapCVcWLbN/Brande+Roderick_goddess_pbgals_playboy_playmate_playmates_3.jpg",
            "https://gallery-of-nudes.com/wp-content/uploads/2016/03/playboy-Playmate-Vanessa-Hoelsher-Nude-Photos-05.jpg",
            "https://www.tribute-to.com/playboy/wp-content/uploads/2015/10/ana-cheri-strong-woman-nude.jpg",
            "https://content4.morazzia.com/playboyplus.com/4456/07.jpg",
            "http://thefappening2015.com/wp-content/uploads/2015/08/Joana-Plankl-nude-in-the-pages-of-Playboy-Germany-%E2%80%93-September-2015-3.jpg",
            "http://www.phun.org/specials/courtney_culkin/courtney_culkin_11.jpg",
            "http://www.epilepsy-brain-mind2014.eu/image/char-naked-in-playboy-4.jpg",
            "https://contenta.morazzia.com/playboyplus.com/0538/06.jpg",
            "http://www.centerfoldsblog.com/wp-content/uploads/2014/06/playboy-playmate-dani-mathers-at-the-beach-posing-her-sexy-curves7.jpg",
            "http://egotasticcom.files.wordpress.com/2009/08/jayde-nicole-nude-playboy-03.jpg",
            "https://content4.morazzia.com/playboyplus.com/6282/08.jpg",
            "http://www.radioaktywni.eu/image/playboy-mansion-twins-naked.jpg",
            "http://gratuitescolaire.info/imgs/effe957ba05d558d701c028a442b08c4.jpg",
            "https://thumb-p7.xhcdn.com/a/KMtgblUCohJ-r0n67nTJxw/000/048/992/977_1000.jpg",
            "http://snadgy.com/wp-content/uploads/2015/06/kayla-rae-reid-playboy-playmate-of-the-month-july-nude-in-in-eternal-sunshine-07.jpg",
            "https://gallery-of-nudes.com/wp-content/uploads/2016/02/playboy-playmate-val-keil-nude-01.jpg",
            "http://www.tribute-to.com/playboy/2015/01/meghan-leopard-model-month-january-2015-nude/h/meghan-leopard-model-month-january-2015-nude03.jpg",
            "https://i.pinimg.com/236x/c4/f6/ab/c4f6ab12b379b6140d159e5489101efd--playboy-girls-sexy-women.jpg",
            "https://www.tribute-to.com/playboy/2014/07/maggie-may-miss-august-2014-nude/h/maggie-may-miss-august-2014-nude12.jpg",
            "http://www.teenageslut.net/lesbians/hot-teen-lesbian-sex/teen-lesbian-sex-16.jpg",
            "http://qpornx.com/xxx/lesbian-sex-fingering-orgasm.jpg",
            "http://dm.damcdn.net/pics/wp-content/uploads/2014/03/naked-girls-lesbian-sex.jpg",
            "https://www.nakedgirls.mobi/contents/videos_screenshots/1000/1422/preview.mp4.jpg",
            "https://www.celebjihad.com/celeb-jihad/images/selena_gomez_lesbian_sex.jpg",
            "http://ftop.ru/large/201502/141110.jpg",
            "http://images.nubilefilms.com/films/impeccable_with_sophie_lynx/screenshots/9.jpg",
            "http://xxxlibz.com/wp-content/uploads/2017/06/12101011-8299-xxxlibz.com.jpg",   
            "http://ftop.ru/images/201210/ftop.ru_41569.jpg",
            "https://i.ytimg.com/vi/pD9fAHo2wSw/maxresdefault.jpg",
            "https://cdn.pichunter.com/365/1/3651070/3651070_13_o.jpg",
            "https://cdn.pichunter.com/366/1/3661023/3661023_10_o.jpg",
            "https://cdn.pichunter.com/364/8/3648684/3648684_14_o.jpg",
            "https://88gals.com/content/X%20Cash/X%20Art/Adria%20Rae%20All%20I%20Want%20For%20Christmas/x-art-10.jpg",
            "https://i.imgur.com/uLQYOFq.jpg",
            "https://www.girlznation.com/galleries/ariel_rebel_nude_tease/ariel_rebel_nude_tease_1.jpg",
            "https://lh3.googleusercontent.com/proxy/4xWQpdDmXoxnjn78DI-L_recaxoMPi98wqH5-hbLJvdCW7aXdnYbNHNFMxUuRkidk2KB8Tpm7yBfkX3_sp9m9zNTB4kSytK0",
            "https://teengirlserotica.com/eroticax/wp-content/uploads/sites/5/nggallery/melody-marks/melody-marks1.jpg"]




verbes = [
            "Cueillir",           
            "Gérer",	           
            "Acheter",                                  	          	                     	                   	                                                       	                                          	                     	                   	
            "Recruter",
            "Arranger",            	           	                                
            "Juger"	,
            "Réduire",                                	                                             	
            "Réparer",                                                                                                         
            "Elargir",
            "Mettre en place",           
            "Choisir" ,            	         
            "Mettre en relation",     
            "Saisir",                                         
            "Schématiser",
            "Collectionner"  ,           
            "Montrer",	
            "Séduire" ,                
            "Étudier",
            "Sélectionner" ,                 
            "Négocier",
            "Soutenir",
            "Examiner",      
            "Tenir",                                            	                                       
            "Fabriquer",	                      
            "Conseiller",	
            "Faire"	,            
            "Utiliser",            	
            "Faire avancer",	           
            "Valider"   ,        
            "Contrôler"	,
            "Faire découvrir",	
            "Piloter",           
            "Convaincre",
            "Faire mémoriser",	           
            "Vendre",
            "Coordonner",
            "Fidéliser"	,          
            "Visualiser"  ,           
            "Former"	,
            "Préparer",
            "Violer",
            "Baiser",
            "Sucer",
            "Lecher",
            "Monter",
            "Sauter",
            "Démonter",
            "Charger",
            "Planter",
            "Fourrer",
            "Soulever",
            "Niquer",
            "Enculer",
            "Empaler",
            "Piquer",
            "Défoncer",
            "Péter",
            "Exploser",
            "Pilonner",
            "Vider"]

chibre = [
            "250 kg de chibre, ça te fait pas peur ?",
            "24/24 7j/7 j'ai qu'un seul objectif, avoir le meilleur chibre de toute la ville",
            "Le matin je pense au chibre, le midi c'est chibre, le soir chibre, même la nuit quand je dors, c'est chibre",
            "Parfois j'fais des rêves autour de plusieurs thématiques, et généralement c'est celle du chibre",
            "Chibre, chibre, chibre, chibre, chibre, chibre ,chibre, chibre, chibre, chibre",
            "Parfois j'pense à rien, parfois j'pense au chibre",
            "Attend une seconde... chibre"]

open('nbjoueurs.txt','w').write('0')

def rec_mot(fichier,mot_cherché):
    f=open(fichier,'r') #On ouvre le fichier
    contenu=f.read() #On récupère son contenu
    res=0
    mot=''
    liste=[]
    for i in contenu:
        if i == " " or i=='\n':
            liste.append(mot)
            mot=""
        else:
            mot+=i
    for i in liste: #La boucle compte le nombre de fois où le caractère donné en paramètre apparait
        if i==mot_cherché:
            res+=1
    return res

def tout_mot(fichier):
    f=open(fichier,'r')
    contenu=f.read()
    liste=[]
    mot=""
    res={}
    for i in contenu:
        if i == " " or i=='\n':
            liste.append(mot)
            mot=""
        else:
            mot+=i
    for i in liste:
        res[i]=rec_mot(fichier,i)
    print(res)

liste_commande=['dossier',"combien de fois j'ai dit le mot :","dis nous tout fun 2.0",
                'début du jeu','joueurs :','jeu fini','zinzolé','dommage','ah !']

c=False
a=False
b=False
v=False
nb=0
messagepv={}
react=0
membres=[]
personnes=[]
personnes2=[]

@client.event
async def on_raw_reaction_add(payload):
    global nb, react, a,membres,v,messagepv,w,personnes,personnes2
    i=randint(0,len(biend))
    oui = biend[i]
    bien_embed = discord.Embed(title='Tiens tes nudes \ud83d\ude09 ('+str(i)+')',type='rich')
    bien_embed.set_image(url=oui)
    
    if payload.user_id==client.user.id:
        return
    
    debutid=int(open('debut.txt','r').readline())
    if payload.message_id==debutid and payload.emoji.name=='😎':
        if str(payload.member) in membres:
            return
        v=True
        membres.append(str(payload.member))
        open('score'+str(payload.member)+'.txt','w').write('0')
        channel=client.get_channel(462231061842100225)
        nb+=1

    if payload.message_id==debutid and payload.emoji.name=='✅' and v and w:
        v=False
        w=False
        a=True
        channel=client.get_channel(462231061842100225)
        await channel.send('Ok, il y a '+str(nb)+" joueurs ! Je vais mettre des images, vous allez devoir m'envoyer en mp des légendes drôles à ces images, vous n'aurez qu'à voter pour votre préférée grâce à la réaction !")       
        await channel.send(embed=bien_embed)
        
    channel=client.get_channel(462231061842100225)
    for i in range(0,nb):
        f=open('msg'+str(i)+'.txt', 'r').read()
        final=f.split(' ')
        idmsg=int(final[0])
        gars=str(final[1])
        if payload.message_id==idmsg and payload.emoji.name=='👍':
            if str(payload.member) in personnes:
                return
            personnes.append(str(payload.member))
            messagepv={}
            a=True
            f=open('score'+str(gars)+'.txt','r')
            score=round(float(f.readline()))
            f.close()
            score+=1
            f=open('score'+str(gars)+'.txt','w')
            f.write(str(score))
            f.close()
            react+=1
            if react==nb:
                personnes2=[]
                react=0
                channel=client.get_channel(462231061842100225)
                await channel.send(embed=bien_embed)
                
                
            
            
@client.event
async def on_message(message):
    global a,b,c,nb,messagepv,w,personnes, personnes2,membres
    
    i=randint(0,len(biend))
    oui = biend[i]
    bien_embed = discord.Embed(title='Tiens tes nudes \ud83d\ude09 ('+str(i)+')',type='rich')
    bien_embed.set_image(url=oui)   
    
    channel=client.get_channel(462231061842100225)
    if message.content=='Légende party':
        membres=[]
        w=True
        nb=0
        debut=await channel.send("Combien de joueurs les bros ? Cliquez sur la réaction pour vous inscrire 😎. Lorsque tout le monde s'est inscrit, cliquez sur la réaction ✅ (trollez pas, attendez tout le monde svp)")
        await debut.add_reaction('😎')
        await debut.add_reaction('✅')
        f=open('debut.txt','w')
        f.write(str(debut.id))
        f.close()
                        
    if message.channel.type==discord.ChannelType.private and a:   
        if str(message.author) in personnes2:
                return
        personnes2.append(str(message.author))
        messagepv[message.content]=str(message.author)
        if len(messagepv)==nb:
            personnes=[]
            channel=client.get_channel(462231061842100225)
            liste2=[]
            for f in messagepv.keys():
                liste2.append(f+" "+messagepv.get(f))
            shuffle(liste2)
            messagepv={}
            for i in liste2:
                tout=str(i)
                lettre=0
                mot=''
                tout2=[]
                fini=False
                while not fini:
                    if lettre==len(tout):
                        tout2.append(mot)
                        mot=''
                        fini=True
                    elif tout[lettre]==' ':
                        tout2.append(mot)
                        mot=''
                        lettre+=1
                    else:
                        mot+=tout[lettre]
                        lettre+=1
                clé=''
                for j in range(len(tout2)-1):
                    clé += tout2[j]+" "
                auteur= tout2[-1]
                messagepv[clé]=auteur
            i=0
            for key in messagepv.keys():
                i+=1
                propal=discord.Embed(description="Proposition "+str(i),title=str(key), type='rich', colour=discord.Colour.blue())
                channel=client.get_channel(462231061842100225)
                msg = await channel.send(embed=propal)
                await msg.add_reaction('👍')
                f=open('msg'+str(i-1)+'.txt','w')
                f.write(str(msg.id)+" "+str(messagepv.get(key)))
                f.close()
            
                
    if message.content=='Party over':
        a=False
        liste=[]
        cor=-1
        egalite=False
        for i in range(0,nb):
            score=int(open('score'+str(membres[i])+'.txt','r').readline())
            if score>cor:
                cor=score
                joueur=membres[i]
                scorefinal=score
            elif score==cor:
                liste.append(membres[i])
                egalite=True
                
        if egalite:
            complement_message=''
            for i in range(len(liste)):
                complement_message+=', '+str(liste[i])
            await message.channel.send('Bravo aux joueurs '+str(joueur)+complement_message+ ' qui finissent avec le même score de ' +str(scorefinal)+' points.')
        else:
            await message.channel.send('Bravo au joueur '+str(joueur)+' qui finit avec un score de ' +str(scorefinal)+' points.')
 
    
    
    
    if message.author==client.user:
        return
    oui=True
    for i in liste_commande:
        if i in message.content.lower():
            oui=False
    if oui:        
        open(str(message.author)+'.txt','a').write(message.content.lower()+' ')
    if message.content=='dossier':
        await message.channel.send(open(str(message.author)+'.txt','r').read())

    if message.content.startswith("Combien de fois j'ai dit le mot :"):
        mot=''
        for i in range(34,len(message.content)):
            mot+=message.content[i]
        await message.channel.send('Vous avez dit '+str(rec_mot(str(message.author)+'.txt',mot.lower()))+' fois le mot "'+mot+'"')
     
    
    
    if(message.content=="Dis nous tout Fun 2.0"):
        await message.channel.send("Bonjour tout le monde ! Je suis Fun 2.0. En gros je suis comme Fun sauf qu'on va le terminer ensemble ce putain de jeu secret ;). Sur ce, bisous et à bientôt !") 
    
    if (message.content=="sendimages"):
        await message.channel.send(embed=bien_embed)

    if message.content.startswith("sendimages"):
        a=message.content[-3]
        b=message.content[-2]
        c=message.content[-1]
        oui = biend[int(a+b+c)]
        bien_embed = discord.Embed(title='Tiens tes nudes \ud83d\ude09',type='rich')
        bien_embed.set_image(url=oui)
        await message.channel.send(embed=bien_embed)
        
    if message.content=='Début du jeu':   
        await message.channel.send('Commençons le jeu')
        await message.channel.send('Combien de joueurs ?')
        c=True
   
    if (message.content.startswith('Joueurs :')) and c:
        c=False
        nbjoueurs=message.content[-1]
        await message.channel.send('Ok, il y a '+nbjoueurs+" joueurs ! Donnez un numéro allant de 1 à "+nbjoueurs+' à chaque joueur puis votez pour le gagnant à chaque round grâce à la commande "!<numéro joueur>". Bonne chance !')
        f=open('nbjoueurs.txt','w')
        f.write(nbjoueurs)
        f.close()
        for i in range(int(nbjoueurs)+1):
            open('score'+str(i)+'.txt','w').write('0')
    nbjoueurs=int(open('nbjoueurs.txt','r').readline())
    for i in range(nbjoueurs+1):
        if message.content=='!'+str(i):  
            f=open('score'+str(i)+'.txt','r')
            score=round(float(f.readline()))
            f.close()
            score+=1
            f=open('score'+str(i)+'.txt','w')
            f.write(str(score))
            f.close()
        if message.content=='Score '+str(i):
            await message.channel.send(open('score'+str(i)+'.txt','r').readline())
            
    if message.content=='Jeu fini':
        liste=[]
        a=-1
        egalite=False
        for i in range(1,nbjoueurs+1):
            score=int(open('score'+str(i)+'.txt','r').readline())
            if score>a:
                a=score
                joueur=i
                scorefinal=score
            elif score==a:
                liste.append(i)
                egalite=True
                
        if egalite:
            complement_message=''
            for i in range(len(liste)):
                complement_message+=', '+str(liste[i])
            await message.channel.send('Bravo aux joueurs '+str(joueur)+complement_message+ ' qui finnissent avec le même score de ' +str(scorefinal)+' points. Si les autres veulent voir leurs scores, utilisez la commande "Score <numéro joueur>".')
        else:
            await message.channel.send('Bravo au joueur '+str(joueur)+' qui finit avec un score de ' +str(scorefinal)+' points. Si les autres veulent voir leurs scores, utilisez la commande "Score <numéro joueur>".')
          
    if 'zinzolé' in message.content.lower():
        aleatoire=randint(0,len(verbes))
        verbe=verbes[aleatoire]
        await message.channel.send("Ici le verbe Zinzoler = "+verbe)

    if message.content.lower()=='dommage':
        await message.channel.send('A ça !')

    if message.content.lower()=='ah !':
        embed=discord.Embed()
        embed.set_image(url="https://lh3.googleusercontent.com/WcSWqqt-Dq-1WhE7z7M0TMTIMVK8JSuq49xRLXYZeTrDkg9kKMGHioqe4XJJYRSMaAa0=s180")
        await message.channel.send(embed=embed)

    if 'chibre' in message.content.lower():
        i = randint(0,len(chibre))
        chibre2=chibre[i]
        await message.channel.send(chibre2)

    if 'ta mère' in message.content.lower():
        await message.channel.send('{0.author.mention} Elle a quoi ma mère batard ?'.format(message))    
    
    if message.content.startswith("Un avis Fun"):
        i=randint(0,len(emote))
        await message.channel.send(emote[i])
        
    sondage = False
    if message.content.startswith("Sondage :"):    
        sondage = True
    
    if sondage:
        liste_message=message.content.split(" ")
        for i in liste_message:
            if i in liste_emoji:
                await message.add_reaction(i)

    if message.content == 'Dis nous tout Fun':
        await message.channel.send("Je suis de retour mais attention ! Je n'ai aucune nouvelle fonctionnalité... Loïc à juste enfin compris pourquoi je marchais plus ce trouduc... La bise.")
   


client.run(os.environ['TOKEN'])
    
