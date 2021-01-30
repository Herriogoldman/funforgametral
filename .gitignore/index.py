import discord
import os
from random import*
default_intents = discord.Intents.all()
default_intents.typing = False
client = discord.Client(intents=default_intents)


##################################################################################################################################################
##################################################################################################################################################
#                                             VARIABLES
##################################################################################################################################################
##################################################################################################################################################

couleur={"Loïc#7389":0xe74c3c,"Raionkasai#8668":0x3498db,"Masterbin35#5542":0xe67e22, "Thomas(Dest)#8382":0x9b59b6}

liste_emoji=['😀', '😁', '😂', '🤣', '😃', '😄', '😅', '😆', '😉', '😊', '😋', '😎', '😍', '😘', '🥰', '😗', '😙', '😚', '☺️', '🙂', '🤗', '🤩', '🤔', '🤨', '😐', '😑', '😶', '🙄', '😏', '😣', '😥', '😮', '🤐', '😯', '😪', '😫', '😴', '😌', '😛', '😜', '😝', '🤤', '😒', '😓', '😔', '😕', '🙃', '🤑', '😲', '☹️', '🙁', '😖', '😞', '😟', '😤', '😢', '😭', '😦', '😧', '😨', '😩', '🤯', '😬', '😰', '😱', '🥵', '🥶', '😳', '🤪', '😵', '😡', '😠', '🤬', '😷', '🤒', '🤕', '🤢', '🤮', '🤧', '😇', '🤠', '🤡', '🥳', '🥴', '🥺', '🤥', '🤫', '🤭', '🧐', '🤓', '😈', '👿', '👹', '👺', '💀', '👻', '👽', '🤖', '💩', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '👶', '👧', '🧒', '👦', '👩', '🧑', '👨', '👵', '🧓', '👴', '👲', '👳\u200d♀️', '👳\u200d♂️', '🧕', '🧔', '👱\u200d♂️', '👱\u200d♀️', '👨\u200d🦰', '👩\u200d🦰', '👨\u200d🦱', '👩\u200d🦱', '👨\u200d🦲', '👩\u200d🦲', '👨\u200d🦳', '👩\u200d🦳', '🦸\u200d♀️', '🦸\u200d♂️', '🦹\u200d♀️', '🦹\u200d♂️', '👮\u200d♀️', '👮\u200d♂️', '👷\u200d♀️', '👷\u200d♂️', '💂\u200d♀️', '💂\u200d♂️', '🕵️\u200d♀️', '🕵️\u200d♂️', '👩\u200d⚕️', '👨\u200d⚕️', '👩\u200d🌾', '👨\u200d🌾', '👩\u200d🍳', '👨\u200d🍳', '👩\u200d🎓', '👨\u200d🎓', '👩\u200d🎤', '👨\u200d🎤', '👩\u200d🏫', '👨\u200d🏫', '👩\u200d🏭', '👨\u200d🏭', '👩\u200d💻', '👨\u200d💻', '👩\u200d💼', '👨\u200d💼', '👩\u200d🔧', '👨\u200d🔧', '👩\u200d🔬', '👨\u200d🔬', '👩\u200d🎨', '👨\u200d🎨', '👩\u200d🚒', '👨\u200d🚒', '👩\u200d✈️', '👨\u200d✈️', '👩\u200d🚀', '👨\u200d🚀', '👩\u200d⚖️', '👨\u200d⚖️', '👰', '🤵', '👸', '🤴', '🤶', '🎅', '🧙\u200d♀️', '🧙\u200d♂️', '🧝\u200d♀️', '🧝\u200d♂️', '🧛\u200d♀️', '🧛\u200d♂️', '🧟\u200d♀️', '🧟\u200d♂️', '🧞\u200d♀️', '🧞\u200d♂️', '🧜\u200d♀️', '🧜\u200d♂️', '🧚\u200d♀️', '🧚\u200d♂️', '👼', '🤰', '🤱', '🙇\u200d♀️', '🙇\u200d♂️', '💁\u200d♀️', '💁\u200d♂️', '🙅\u200d♀️', '🙅\u200d♂️', '🙆\u200d♀️', '🙆\u200d♂️', '🙋\u200d♀️', '🙋\u200d♂️', '🤦\u200d♀️', '🤦\u200d♂️', '🤷\u200d♀️', '🤷\u200d♂️', '🙎\u200d♀️', '🙎\u200d♂️', '🙍\u200d♀️', '🙍\u200d♂️', '💇\u200d♀️', '💇\u200d♂️', '💆\u200d♀️', '💆\u200d♂️', '🧖\u200d♀️', '🧖\u200d♂️', '💅', '🤳', '💃', '🕺', '👯\u200d♀️', '👯\u200d♂️', '🕴', '🚶\u200d♀️', '🚶\u200d♂️', '🏃\u200d♀️', '🏃\u200d♂️', '👫', '👭', '👬', '💑', '👩\u200d❤️\u200d👩', '👨\u200d❤️\u200d👨', '💏', '👩\u200d❤️\u200d💋\u200d👩', '👨\u200d❤️\u200d💋\u200d👨', '👪', '👨\u200d👩\u200d👧', '👨\u200d👩\u200d👧\u200d👦', '👨\u200d👩\u200d👦\u200d👦', '👨\u200d👩\u200d👧\u200d👧', '👩\u200d👩\u200d👦', '👩\u200d👩\u200d👧', '👩\u200d👩\u200d👧\u200d👦', '👩\u200d👩\u200d👦\u200d👦', '👩\u200d👩\u200d👧\u200d👧', '👨\u200d👨\u200d👦', '👨\u200d👨\u200d👧', '👨\u200d👨\u200d👧\u200d👦', '👨\u200d👨\u200d👦\u200d👦', '👨\u200d👨\u200d👧\u200d👧', '👩\u200d👦', '👩\u200d👧', '👩\u200d👧\u200d👦', '👩\u200d👦\u200d👦', '👩\u200d👧\u200d👧', '👨\u200d👦', '👨\u200d👧', '👨\u200d👧\u200d👦', '👨\u200d👦\u200d👦', '👨\u200d👧\u200d👧', '🤲', '👐', '🙌', '👏', '🤝', '👍', '👎', '👊', '✊', '🤛', '🤜', '🤞', '✌️', '🤟', '🤘', '👌', '👈', '👉', '👆', '👇', '☝️', '✋', '🤚', '🖐', '🖖', '👋', '🤙', '💪', '🦵', '🦶', '🖕', '✍️', '🙏', '💍', '💄', '💋', '👄', '👅', '👂', '👃', '👣', '👁', '👀', '🧠', '🦴', '🦷', '🗣', '👤', '🧥', '👚', '👕', '👖', '👔', '👗', '👙', '👘', '👠', '👡', '👢', '👞', '👟', '🥾', '🥿', '🧦', '🧤', '🧣', '🎩', '🧢', '👒', '🎓', '⛑', '👑', '👝', '👛', '👜', '💼', '🎒', '👓', '🕶', '🥽', '🥼', '🌂', '🧵', '🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🦝', '🐻', '🐼', '🦘', '🦡', '🐨', '🐯', '🦁', '🐮', '🐷', '🐽', '🐸', '🐵', '🙈', '🙉', '🙊', '🐒', '🐔', '🐧', '🐦', '🐤', '🐣', '🐥', '🦆', '🦢', '🦅', '🦉', '🦚', '🦜', '🦇', '🐺', '🐗', '🐴', '🦄', '🐝', '🐛', '🦋', '🐌', '🐚', '🐞', '🐜', '🦗', '🕷', '🕸', '🦂', '🦟', '🦠', '🐢', '🐍', '🦎', '🦖', '🦕', '🐙', '🦑', '🦐', '🦀', '🐡', '🐠', '🐟', '🐬', '🐳', '🐋', '🦈', '🐊', '🐅', '🐆', '🦓', '🦍', '🐘', '🦏', '🦛', '🐪', '🐫', '🦙', '🦒', '🐃', '🐂', '🐄', '🐎', '🐖', '🐏', '🐑', '🐐', '🦌', '🐕', '🐩', '🐈', '🐓', '🦃', '🕊', '🐇', '🐁', '🐀', '🐿', '🦔', '🐾', '🐉', '🐲', '🌵', '🎄', '🌲', '🌳', '🌴', '🌱', '🌿', '☘️', '🍀', '🎍', '🎋', '🍃', '🍂', '🍁', '🍄', '🌾', '💐', '🌷', '🌹', '🥀', '🌺', '🌸', '🌼', '🌻', '🌞', '🌝', '🌛', '🌜', '🌚', '🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔', '🌙', '🌎', '🌍', '🌏', '💫', '⭐️', '🌟', '✨', '⚡️', '☄️', '💥', '🔥', '🌪', '🌈', '☀️', '🌤', '⛅️', '🌥', '☁️', '🌦', '🌧', '⛈', '🌩', '🌨', '❄️', '☃️', '⛄️', '🌬', '💨', '💧', '💦', '☔️', '☂️', '🌊', '🍏', '🍎', '🍐', '🍊', '🍋', '🍌', '🍉', '🍇', '🍓', '🍈', '🍒', '🍑', '🍍', '🥭', '🥥', '🥝', '🍅', '🍆', '🥑', '🥦', '🥒', '🥬', '🌶', '🌽', '🥕', '🥔', '🍠', '🥐', '🍞', '🥖', '🥨', '🥯', '🧀', '🥚', '🍳', '🥞', '🥓', '🥩', '🍗', '🍖', '🌭', '🍔', '🍟', '🍕', '🥪', '🥙', '🌮', '🌯', '🥗', '🥘', '🥫', '🍝', '🍜', '🍲', '🍛', '🍣', '🍱', '🥟', '🍤', '🍙', '🍚', '🍘', '🍥', '🥮', '🥠', '🍢', '🍡', '🍧', '🍨', '🍦', '🥧', '🍰', '🎂', '🍮', '🍭', '🍬', '🍫', '🍿', '🧂', '🍩', '🍪', '🌰', '🥜', '🍯', '🥛', '🍼', '☕️', '🍵', '🥤', '🍶', '🍺', '🍻', '🥂', '🍷', '🥃', '🍸', '🍹', '🍾', '🥄', '🍴', '🍽', '🥣', '🥡', '\u26BD', '🏀', '🏈', '⚾️', '🥎', '🏐', '🏉', '🎾', '🥏', '🎱', '🏓', '🏸', '🥅', '🏒', '🏑', '🥍', '🏏', '⛳️', '🏹', '🎣', '🥊', '🥋', '🎽', '⛸', '🥌', '🛷', '🛹', '🎿', '⛷', '🏂', '🏋️\u200d♀️', '🏋🏻\u200d♀️', '🏋🏼\u200d♀️', '🏋🏽\u200d♀️', '🏋🏾\u200d♀️', '🏋🏿\u200d♀️', '🏋️\u200d♂️', '🏋🏻\u200d♂️', '🏋🏼\u200d♂️', '🏋🏽\u200d♂️', '🏋🏾\u200d♂️', '🏋🏿\u200d♂️', '🤼\u200d♀️', '🤼\u200d♂️', '🤸\u200d♀️', '🤸🏻\u200d♀️', '🤸🏼\u200d♀️', '🤸🏽\u200d♀️', '🤸🏾\u200d♀️', '🤸🏿\u200d♀️', '🤸\u200d♂️', '🤸🏻\u200d♂️', '🤸🏼\u200d♂️', '🤸🏽\u200d♂️', '🤸🏾\u200d♂️', '🤸🏿\u200d♂️', '⛹️\u200d♀️', '⛹🏻\u200d♀️', '⛹🏼\u200d♀️', '⛹🏽\u200d♀️', '⛹🏾\u200d♀️', '⛹🏿\u200d♀️', '⛹️\u200d♂️', '⛹🏻\u200d♂️', '⛹🏼\u200d♂️', '⛹🏽\u200d♂️', '⛹🏾\u200d♂️', '⛹🏿\u200d♂️', '🤺', '🤾\u200d♀️', '🤾🏻\u200d♀️', '🤾🏼\u200d♀️', '🤾🏾\u200d♀️', '🤾🏾\u200d♀️', '🤾🏿\u200d♀️', '🤾\u200d♂️', '🤾🏻\u200d♂️', '🤾🏼\u200d♂️', '🤾🏽\u200d♂️', '🤾🏾\u200d♂️', '🤾🏿\u200d♂️', '🏌️\u200d♀️', '🏌🏻\u200d♀️', '🏌🏼\u200d♀️', '🏌🏽\u200d♀️', '🏌🏾\u200d♀️', '🏌🏿\u200d♀️', '🏌️\u200d♂️', '🏌🏻\u200d♂️', '🏌🏼\u200d♂️', '🏌🏽\u200d♂️', '🏌🏾\u200d♂️', '🏌🏿\u200d♂️', '🏇', '🏇🏻', '🏇🏼', '🏇🏽', '🏇🏾', '🏇🏿', '🧘\u200d♀️', '🧘🏻\u200d♀️', '🧘🏼\u200d♀️', '🧘🏽\u200d♀️', '🧘🏾\u200d♀️', '🧘🏿\u200d♀️', '🧘\u200d♂️', '🧘🏻\u200d♂️', '🧘🏼\u200d♂️', '🧘🏽\u200d♂️', '🧘🏾\u200d♂️', '🧘🏿\u200d♂️', '🏄\u200d♀️', '🏄🏻\u200d♀️', '🏄🏼\u200d♀️', '🏄🏽\u200d♀️', '🏄🏾\u200d♀️', '🏄🏿\u200d♀️', '🏄\u200d♂️', '🏄🏻\u200d♂️', '🏄🏼\u200d♂️', '🏄🏽\u200d♂️', '🏄🏾\u200d♂️', '🏄🏿\u200d♂️', '🏊\u200d♀️', '🏊🏻\u200d♀️', '🏊🏼\u200d♀️', '🏊🏽\u200d♀️', '🏊🏾\u200d♀️', '🏊🏿\u200d♀️', '🏊\u200d♂️', '🏊🏻\u200d♂️', '🏊🏼\u200d♂️', '🏊🏽\u200d♂️', '🏊🏾\u200d♂️', '🏊🏿\u200d♂️', '🤽\u200d♀️', '🤽🏻\u200d♀️', '🤽🏼\u200d♀️', '🤽🏽\u200d♀️', '🤽🏾\u200d♀️', '🤽🏿\u200d♀️', '🤽\u200d♂️', '🤽🏻\u200d♂️', '🤽🏼\u200d♂️', '🤽🏽\u200d♂️', '🤽🏾\u200d♂️', '🤽🏿\u200d♂️', '🚣\u200d♀️', '🚣🏻\u200d♀️', '🚣🏼\u200d♀️', '🚣🏽\u200d♀️', '🚣🏾\u200d♀️', '🚣🏿\u200d♀️', '🚣\u200d♂️', '🚣🏻\u200d♂️', '🚣🏼\u200d♂️', '🚣🏽\u200d♂️', '🚣🏾\u200d♂️', '🚣🏿\u200d♂️', '🧗\u200d♀️', '🧗🏻\u200d♀️', '🧗🏼\u200d♀️', '🧗🏽\u200d♀️', '🧗🏾\u200d♀️', '🧗🏿\u200d♀️', '🧗\u200d♂️', '🧗🏻\u200d♂️', '🧗🏼\u200d♂️', '🧗🏽\u200d♂️', '🧗🏾\u200d♂️', '🧗🏿\u200d♂️', '🚵\u200d♀️', '🚵🏻\u200d♀️', '🚵🏼\u200d♀️', '🚵🏽\u200d♀️', '🚵🏾\u200d♀️', '🚵🏿\u200d♀️', '🚵\u200d♂️', '🚵🏻\u200d♂️', '🚵🏼\u200d♂️', '🚵🏽\u200d♂️', '🚵🏾\u200d♂️', '🚵🏿\u200d♂️', '🚴\u200d♀️', '🚴🏻\u200d♀️', '🚴🏼\u200d♀️', '🚴🏽\u200d♀️', '🚴🏾\u200d♀️', '🚴🏿\u200d♀️', '🚴\u200d♂️', '🚴🏻\u200d♂️', '🚴🏼\u200d♂️', '🚴🏽\u200d♂️', '🚴🏾\u200d♂️', '🚴🏿\u200d♂️', '🏆', '🥇', '🥈', '🥉', '🏅', '🎖', '🏵', '🎗', '🎫', '🎟', '🎪', '🤹\u200d♀️', '🤹🏻\u200d♀️', '🤹🏼\u200d♀️', '🤹🏽\u200d♀️', '🤹🏾\u200d♀️', '🤹🏿\u200d♀️', '🤹\u200d♂️', '🤹🏻\u200d♂️', '🤹🏼\u200d♂️', '🤹🏽\u200d♂️', '🤹🏾\u200d♂️', '🤹🏿\u200d♂️', '🎭', '🎨', '🎬', '🎤', '🎧', '🎼', '🎹', '🥁', '🎷', '🎺', '🎸', '🎻', '🎲', '🧩', '♟', '🎯', '🎳', '🎮', '🚗', '🚕', '🚙', '🚌', '🚎', '🏎', '🚓', '🚑', '🚒', '🚐', '🚚', '🚛', '🚜', '🛴', '🚲', '🛵', '🏍', '🚨', '🚔', '🚍', '🚘', '🚖', '🚡', '🚠', '🚟', '🚃', '🚋', '🚞', '🚝', '🚄', '🚅', '🚈', '🚂', '🚆', '🚇', '🚊', '🚉', '✈️', '🛫', '🛬', '🛩', '💺', '🛰', '🚀', '🛸', '🚁', '🛶', '⛵️', '🚤', '🛥', '🛳', '⛴', '🚢', '⚓️', '⛽️', '🚧', '🚦', '🚥', '🚏', '🗺', '🗿', '🗽', '🗼', '🏰', '🏯', '🏟', '🎡', '🎢', '🎠', '⛲️', '⛱', '🏖', '🏝', '🏜', '🌋', '⛰', '🏔', '🗻', '🏕', '⛺️', '🏠', '🏡', '🏘', '🏚', '🏗', '🏭', '🏢', '🏬', '🏣', '🏤', '🏥', '🏦', '🏨', '🏪', '🏫', '🏩', '💒', '🏛', '⛪️', '🕌', '🕍', '🕋', '⛩', '🛤', '🛣', '🗾', '🎑', '🏞', '🌅', '🌄', '🌠', '🎇', '🎆', '🌇', '🌆', '🏙', '🌃', '🌌', '🌉', '⌚️', '📱', '📲', '💻', '⌨️', '🖥', '🖨', '🖱', '🖲', '🕹', '🗜', '💽', '💾', '💿', '📀', '📼', '📷', '📸', '📹', '🎥', '📽', '🎞', '📞', '☎️', '📟', '📠', '📺', '📻', '🎙', '🎚', '🎛', '⏱', '⏲', '⏰', '🕰', '⌛️', '⏳', '📡', '🔋', '🔌', '💡', '🔦', '🕯', '🗑', '🛢', '💸', '💵', '💴', '💶', '💷', '💰', '💳', '🧾', '💎', '⚖️', '🔧', '🔨', '⚒', '🛠', '⛏', '🔩', '⚙️', '⛓', '🔫', '💣', '🔪', '🗡', '⚔️', '🛡', '🚬', '⚰️', '⚱️', '🏺', '🧭', '🧱', '🔮', '🧿', '🧸', '📿', '💈', '⚗️', '🔭', '🧰', '🧲', '🧪', '🧫', '🧬', '🧯', '🔬', '🕳', '💊', '💉', '🌡', '🚽', '🚰', '🚿', '🛁', '🛀', '🛀🏻', '🛀🏼', '🛀🏽', '🛀🏾', '🛀🏿', '🧴', '🧵', '🧶', '🧷', '🧹', '🧺', '🧻', '🧼', '🧽', '🛎', '🔑', '🗝', '🚪', '🛋', '🛏', '🛌', '🖼', '🛍', '🧳', '🛒', '🎁', '🎈', '🎏', '🎀', '🎊', '🎉', '🧨', '🎎', '🏮', '🎐', '🧧', '✉️', '📩', '📨', '📧', '💌', '📥', '📤', '📦', '🏷', '📪', '📫', '📬', '📭', '📮', '📯', '📜', '📃', '📄', '📑', '📊', '📈', '📉', '🗒', '🗓', '📆', '📅', '📇', '🗃', '🗳', '🗄', '📋', '📁', '📂', '🗂', '🗞', '📰', '📓', '📔', '📒', '📕', '📗', '📘', '📙', '📚', '📖', '🔖', '🔗', '📎', '🖇', '📐', '📏', '📌', '📍', '✂️', '🖊', '🖋', '✒️', '🖌', '🖍', '📝', '✏️', '🔍', '🔎', '🔏', '🔐', '🔒', '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '💔', '❣️', '💕', '💞', '💓', '💗', '💖', '💘', '💝', '💟', '☮️', '✝️', '☪️', '🕉', '☸️', '✡️', '🔯', '🕎', '☯️', '☦️', '🛐', '⛎', '♈️', '♉️', '♊️', '♋️', '♌️', '♍️', '♎️', '♏️', '♐️', '♑️', '♒️', '♓️', '🆔', '⚛️', '🉑', '☢️', '☣️', '📴', '📳', '🈶', '🈚️', '🈸', '🈺', '🈷️', '✴️', '🆚', '💮', '🉐', '㊙️', '㊗️', '🈴', '🈵', '🈹', '🈲', '🅰️', '🅱️', '🆎', '🆑', '🅾️', '🆘', '❌', '⭕️', '🛑', '⛔️', '📛', '🚫', '💯', '💢', '♨️', '🚷', '🚯', '🚳', '🚱', '🔞', '📵', '🚭', '❗️', '❕', '❓', '❔', '‼️', '⁉️', '🔅', '🔆', '〽️', '⚠️', '🚸', '🔱', '⚜️', '🔰', '♻️', '✅', '🈯️', '💹', '❇️', '✳️', '❎', '🌐', '💠', 'Ⓜ️', '🌀', '💤', '🏧', '🚾', '♿️', '🅿️', '🈳', '🈂️', '🛂', '🛃', '🛄', '🛅', '🚹', '🚺', '🚼', '🚻', '🚮', '🎦', '📶', '🈁', '🔣', 'ℹ️', '🔤', '🔡', '🔠', '🆖', '🆗', '🆙', '🆒', '🆕', '🆓', '0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟', '🔢', '#️⃣', '*️⃣', '⏏️', '▶️', '⏸', '⏯', '⏹', '⏺', '⏭', '⏮', '⏩', '⏪', '⏫', '⏬', '◀️', '🔼', '🔽', '➡️', '⬅️', '⬆️', '⬇️', '↗️', '↘️', '↙️', '↖️', '↕️', '↔️', '↪️', '↩️', '⤴️', '⤵️', '🔀', '🔁', '🔂', '🔄', '🔃', '🎵', '🎶', '➕', '➖', '➗', '✖️', '♾', '💲', '💱', '™️', '©️', '®️', '〰️', '➰', '➿', '🔚', '🔙', '🔛', '🔝', '🔜', '✔️', '☑️', '🔘', '⚪️', '⚫️', '🔴', '🔵', '🔺', '🔻', '🔸', '🔹', '🔶', '🔷', '🔳', '🔲', '▪️', '▫️', '◾️', '◽️', '◼️', '◻️', '⬛️', '⬜️', '🔈', '🔇', '🔉', '🔊', '🔔', '🔕', '📣', '📢', '👁\u200d🗨', '💬', '💭', '🗯', '♠️', '♣️', '♥️', '♦️', '🃏', '🎴', '🀄️', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚', '🕛', '🕜', '🕝', '🕞', '🕟', '🕠', '🕡', '🕢', '🕣', '🕤', '🕥', '🕦','🏳️', '🏴', '🏁', '🚩', '🏳️\u200d🌈', '🏴\u200d☠️', '🇦🇫', '🇦🇽', '🇦🇱', '🇩🇿', '🇦🇸', '🇦🇩', '🇦🇴', '🇦🇮', '🇦🇶', '🇦🇬', '🇦🇷', '🇦🇲', '🇦🇼', '🇦🇺', '🇦🇹', '🇦🇿', '🇧🇸', '🇧🇭', '🇧🇩', '🇧🇧', '🇧🇾', '🇧🇪', '🇧🇿', '🇧🇯', '🇧🇲', '🇧🇹', '🇧🇴', '🇧🇦', '🇧🇼', '🇧🇷', '🇮🇴', '🇻🇬', '🇧🇳', '🇧🇬', '🇧🇫', '🇧🇮', '🇰🇭', '🇨🇲', '🇨🇦', '🇮🇨', '🇨🇻', '🇧🇶', '🇰🇾', '🇨🇫', '🇹🇩', '🇨🇱', '🇨🇳', '🇨🇽', '🇨🇨', '🇨🇴', '🇰🇲', '🇨🇬', '🇨🇩', '🇨🇰', '🇨🇷', '🇨🇮', '🇭🇷', '🇨🇺', '🇨🇼', '🇨🇾', '🇨🇿', '🇩🇰', '🇩🇯', '🇩🇲', '🇩🇴', '🇪🇨', '🇪🇬', '🇸🇻', '🇬🇶', '🇪🇷', '🇪🇪', '🇪🇹', '🇪🇺', '🇫🇰', '🇫🇴', '🇫🇯', '🇫🇮', '🇫🇷', '🇬🇫', '🇵🇫', '🇹🇫', '🇬🇦', '🇬🇲', '🇬🇪', '🇩🇪', '🇬🇭', '🇬🇮', '🇬🇷', '🇬🇱', '🇬🇩', '🇬🇵', '🇬🇺', '🇬🇹', '🇬🇬', '🇬🇳', '🇬🇼', '🇬🇾', '🇭🇹', '🇭🇳', '🇭🇰', '🇭🇺', '🇮🇸', '🇮🇳', '🇮🇩', '🇮🇷', '🇮🇶', '🇮🇪', '🇮🇲', '🇮🇱', '🇮🇹', '🇯🇲', '🇯🇵', '🎌', '🇯🇪', '🇯🇴', '🇰🇿', '🇰🇪', '🇰🇮', '🇽🇰', '🇰🇼', '🇰🇬', '🇱🇦', '🇱🇻', '🇱🇧', '🇱🇸', '🇱🇷', '🇱🇾', '🇱🇮', '🇱🇹', '🇱🇺', '🇲🇴', '🇲🇰', '🇲🇬', '🇲🇼', '🇲🇾', '🇲🇻', '🇲🇱', '🇲🇹', '🇲🇭', '🇲🇶', '🇲🇷', '🇲🇺', '🇾🇹', '🇲🇽', '🇫🇲', '🇲🇩', '🇲🇨', '🇲🇳', '🇲🇪', '🇲🇸', '🇲🇦', '🇲🇿', '🇲🇲', '🇳🇦', '🇳🇷', '🇳🇵', '🇳🇱', '🇳🇨', '🇳🇿', '🇳🇮', '🇳🇪', '🇳🇬', '🇳🇺', '🇳🇫', '🇰🇵', '🇲🇵', '🇳🇴', '🇴🇲', '🇵🇰', '🇵🇼', '🇵🇸', '🇵🇦', '🇵🇬', '🇵🇾', '🇵🇪', '🇵🇭', '🇵🇳', '🇵🇱', '🇵🇹', '🇵🇷', '🇶🇦', '🇷🇪', '🇷🇴', '🇷🇺', '🇷🇼', '🇼🇸', '🇸🇲', '🇸🇦', '🇸🇳', '🇷🇸', '🇸🇨', '🇸🇱', '🇸🇬', '🇸🇽', '🇸🇰', '🇸🇮', '🇬🇸', '🇸🇧', '🇸🇴', '🇿🇦', '🇰🇷', '🇸🇸', '🇪🇸', '🇱🇰', '🇧🇱', '🇸🇭', '🇰🇳', '🇱🇨', '🇵🇲', '🇻🇨', '🇸🇩', '🇸🇷', '🇸🇿', '🇸🇪', '🇨🇭', '🇸🇾', '🇹🇼', '🇹🇯', '🇹🇿', '🇹🇭', '🇹🇱', '🇹🇬', '🇹🇰', '🇹🇴', '🇹🇹', '🇹🇳', '🇹🇷', '🇹🇲', '🇹🇨', '🇹🇻', '🇻🇮', '🇺🇬', '🇺🇦', '🇦🇪', '🇬🇧', '🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f', '🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f', '🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f', '🇺🇳', '🇺🇸', '🇺🇾', '🇺🇿', '🇻🇺', '🇻🇦', '🇻🇪', '🇻🇳', '🇼🇫', '🇪🇭', '🇾🇪', '🇿🇲']

emote=['<:WTF:576870192705961986>', '<:sourireirl:577145595156758528>', '<:saoul:576876335243460608>', '<:ronangers:369209617168990208>', '<:rireirl:578273002521886739>', '<:regardfou:576873563492188160>', '<:oups:577228350762909723>', '<:OULAH:577153845101330492>', '<:MANGER:576877901308362763>', '<:gneugneu:576886801029922828>', '<:globuleux:577147819551358981>', '<:ennui:576883744980598794>', '<:doute:577160207684075532>', '<:dab:581600000983957504>', '<:choc:577174077932830770>', '<:bide:576869419490213888>']

images = [
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

message_activite = {}
jeu_en_cours = {}

############################################################################################################################################################
############################################################################################################################################################
#                                                       FONCTIONS
############################################################################################################################################################
############################################################################################################################################################

async def messageActivite():
    if after.activity.type == discord.ActivityType.playing :
        print(str(after.name) +" joue à " +str(after.activity.name) + " : "+str(after.activity.state))
        mess = await after.send("Etes-vous d'accord pour inviter les membres du serveur Gametral à venir jouer à " + str(after.activity.name) + " avec vous ?")
        await mess.add_reaction('👍')
        await mess.add_reaction('👎') 
        global id 
        id = mess.id




##################################################################################################################################################
##################################################################################################################################################
#                                                   EVENTS
##################################################################################################################################################
##################################################################################################################################################

# LE BOT EST PRET

@client.event
async def on_ready():
    global pourparler
    print('Je suis en ligne')
    pourparler=client.get_channel(415217594505625600)

# RECEPTION D'UN MESSAGE

@client.event
async def on_message(message):
    i=randint(0,len(images)-1)
    message_embed = discord.Embed(title='Tiens tes nudes \ud83d\ude09 ('+str(i)+')',type='rich').set_image(url=images[i])  

    if message.author==client.user:
        return
    if message.content.startswith('!dm'):
        contenu = message.content.split(" ")
        name = contenu[1]
        mess =''
        for i in range(len(contenu)):
            if i > 1:
                mess=mess + contenu[i] + " "
        membre = discord.utils.get(message.guild.members, name=name)
        try :
            await membre.send(mess)
        except AttributeError:
            await discord.utils.get(message.guild.members, name = 'Loïc').send("L'utilisateur n'existe pas")
        except discord.errors.Forbidden :
            await message.channel.send("L'utilisateur a fermé ses dms")
    if message.channel.type == discord.ChannelType.private:
        anonyme = discord.Embed(title = "Message d'un anonyme", description = message.content)
        await client.get_channel(376778036642578442).send(embed= anonyme)
     
    if (message.content=="sendimages"):
        await message.channel.send(embed=message_embed)

    if message.content.startswith("sendimages"):
        message_embed.set_image(url=images[int(message.content[-3]+message.content[-2]+message.content[-1])])
        await message.channel.send(embed=message_embed)
            
    if 'zinzolé' in message.content.lower():
        await message.channel.send("Ici le verbe Zinzoler = "+verbes[randint(0,len(verbes)-1)])

    if message.content.lower()=='dommage':
        await message.channel.send('A ça !')

    if message.content.lower()=='ah !':
        denis=discord.Embed().set_image(url="https://lh3.googleusercontent.com/WcSWqqt-Dq-1WhE7z7M0TMTIMVK8JSuq49xRLXYZeTrDkg9kKMGHioqe4XJJYRSMaAa0=s180")
        await message.channel.send(embed=denis)

    if 'chibre' in message.content.lower():
        await message.channel.send(chibre[randint(0,len(chibre)-1)])

    if 'ta mère' in message.content.lower():
        await message.channel.send('{0.author.mention} Elle a quoi ma mère batard ?'.format(message))    
    
    if message.content.startswith("Un avis Fun"):
        await message.channel.send(emote[randint(0,len(emote))])
        
    if message.content.startswith("Sondage :"):    
        liste_message=message.content.split(" ")
        for i in liste_message:
            if i in liste_emoji or i in emote:
                await message.add_reaction(i)

# STATUT MEMBRE ACTUALISE

@client.event
async def on_member_update(before,after):
    global id
    if after.bot:
        return
    if after.is_on_mobile() or before.is_on_mobile() :
        return
    if before.activity==None and after.activity!=None:
        if after.activity.type == discord.ActivityType.playing :
            print(str(after.name) +" joue à " +str(after.activity.name) + " : "+str(after.activity.state))
            mess = await after.send("Etes-vous d'accord pour inviter les membres du serveur Gametral à venir jouer à " + str(after.activity.name) + " avec vous ?")
            await mess.add_reaction('👍')
            await mess.add_reaction('👎') 
            id = mess.id

    elif after.activity==None and before.activity!=None:
        print(str(after.name) +" ne joue plus")    
        a=False
        for joueur,jeu in jeu_en_cours.items():
            if jeu == str(before.activity.name) and joueur!=str(after.name):
                await pourparler.get_partial_message(message_activite.get(joueur)).delete()
                del message_activite[str(after.name)]
                del message_activite[str(joueur)]
                del jeu_en_cours[str(after.name)]
                emb = discord.Embed(title= joueur + ' est en train de jouer à ' + jeu + " !", description = 'Si ça te tente de jouer avec lui, demande lui 😉', colour=couleur[str(discord.utils.get(pourparler.guild.members, name=joueur))])
                emb.set_image(url=discord.utils.get(pourparler.guild.members, name=joueur).avatar_url_as(size=128))
                mess2=await pourparler.send(embed = emb)
                message_activite[joueur]=mess2.id
                a=False
                return
            else:
                a= True

        if a :
            try:
                await pourparler.get_partial_message(message_activite.get(str(after.name))).delete()
                del message_activite[str(after.name)]
                del jeu_en_cours[str(after.name)]
            except discord.errors.HTTPException:
                return

    elif before.activity.name != after.activity.name:
        if after.activity.type == discord.ActivityType.playing :
            print(str(after.name) +" joue à " +str(after.activity.name) + " : "+str(after.activity.state))
            mess = await after.send("Etes-vous d'accord pour inviter les membres du serveur Gametral à venir jouer à " + str(after.activity.name) + " avec vous ?")
            await mess.add_reaction('👍')
            await mess.add_reaction('👎')  
            id = mess.id
            



# REACTION AJOUTE SUR UN MESSAGE

@client.event
async def on_reaction_add(reaction, user):
    if user==client.user:
        return
    if reaction.message.id == id :
        if reaction.emoji=='👍':
                a=False
                await reaction.message.delete()
                if len(jeu_en_cours) !=0:
                    print(jeu_en_cours)
                    for joueur,jeu in jeu_en_cours.items():
                        print(joueur, jeu)
                        if jeu == str(discord.utils.get(discord.utils.get(client.guilds,name='Gametral').members,name=user.name).activity.name) :
                            jeu_en_cours[str(user.name)]=str(discord.utils.get(discord.utils.get(client.guilds,name='Gametral').members,name=user.name).activity.name)
                            await pourparler.get_partial_message(message_activite.get(joueur)).delete()
                            mess2=await pourparler.send(embed=discord.Embed(title= joueur+ " et " + str(user.name) + ' sont en train de jouer à ' + jeu + " !", description = 'Si ça te tente de jouer avec eux, demande leur 😉', colour=couleur[str(discord.utils.get(pourparler.guild.members, name=joueur))]))
                            del message_activite[joueur]
                            message_activite[joueur]=mess2.id
                            message_activite[str(user.name)]=mess2.id
                            a=False
                            return
                        else :
                            a=True
                    if a:
                        jeu_en_cours[str(user.name)]=str(discord.utils.get(discord.utils.get(client.guilds,name='Gametral').members,name=user.name).activity.name)
                        emb = discord.Embed(title= str(user.name) + ' est en train de jouer à ' + str(discord.utils.get(discord.utils.get(client.guilds,name='Gametral').members,name=user.name).activity.name) + " !", description = 'Si ça te tente de jouer avec lui, demande lui 😉', colour=couleur[str(user)])
                        emb.set_image(url=user.avatar_url_as(size=128))
                        mess2=await pourparler.send(embed = emb)
                        message_activite[str(user.name)]=mess2.id
                else:
                    jeu_en_cours[str(user.name)]=str(discord.utils.get(discord.utils.get(client.guilds,name='Gametral').members,name=user.name).activity.name)
                    emb = discord.Embed(title= str(user.name) + ' est en train de jouer à ' + str(discord.utils.get(discord.utils.get(client.guilds,name='Gametral').members,name=user.name).activity.name) + " !", description = 'Si ça te tente de jouer avec lui, demande lui 😉', colour=couleur[str(user)])
                    emb.set_image(url=user.avatar_url_as(size=128))
                    mess2=await pourparler.send(embed = emb)
                    message_activite[str(user.name)]=mess2.id
        if reaction.emoji=='👎':
            await reaction.message.delete()

# UN UTILISATEUR ECRIT

@client.event
async def on_typing(channel,user,when):
    await user.send("Fais gaffe à ce que t'écris mon gars")


client.run(os.environ['TOKEN'])