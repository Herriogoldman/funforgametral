import discord
import os
import asyncio
from random import*
from discord.ext import commands
client = discord.Client()
@client.event
async def on_ready():
    print("Bot en ligne")
    
liste_emoji=[':grinning:', ':grin:', ':joy:', ':rofl:', ':smiley:', ':smile:', ':sweat_smile:', ':laughing:', ':wink:', ':blush:', ':yum:', ':sunglasses:', ':heart_eyes:', ':kissing_heart:', '\U0001f970', ':kissing:', ':kissing_smiling_eyes:', ':kissing_closed_eyes:', ':relaxed:', '️', ':slight_smile:', ':hugging:', '\U0001f929', ':thinking:', '\U0001f928', ':neutral_face:', ':expressionless:', ':no_mouth:', ':rolling_eyes:', ':smirk:', ':persevere:', ':disappointed_relieved:', ':open_mouth:', ':zipper_mouth:', ':hushed:', ':sleepy:', ':tired_face:', ':sleeping:', ':relieved:', ':stuck_out_tongue:', ':stuck_out_tongue_winking_eye:', ':stuck_out_tongue_closed_eyes:', ':drooling_face:', ':unamused:', ':sweat:', ':pensive:', ':confused:', ':upside_down:', ':money_mouth:', ':astonished:', ':frowning2:', '️', ':slight_frown:', ':confounded:', ':disappointed:', ':worried:', ':triumph:', ':cry:', ':sob:', ':frowning:', ':anguished:', ':fearful:', ':weary:', '\U0001f92f', ':grimacing:', ':cold_sweat:', ':scream:', '\U0001f975', '\U0001f976', ':flushed:', '\U0001f92a', ':dizzy_face:', ':rage:', ':angry:', '\U0001f92c', ':mask:', ':thermometer_face:', ':head_bandage:', ':nauseated_face:', '\U0001f92e', ':sneezing_face:', ':innocent:', ':cowboy:', ':clown:', '\U0001f973', '\U0001f974', '\U0001f97a', ':lying_face:', '\U0001f92b', '\U0001f92d', '\U0001f9d0', ':nerd:', ':smiling_imp:', ':imp:', ':japanese_ogre:', ':japanese_goblin:', ':skull:', ':ghost:', ':alien:', ':robot:', ':poop:', ':smiley_cat:', ':smile_cat:', ':joy_cat:', ':heart_eyes_cat:', ':smirk_cat:', ':kissing_cat:', ':scream_cat:', ':crying_cat_face:', ':pouting_cat:',':baby:', ':girl:', ':child:', ':boy:', ':woman:', ':adult:', ':man:', ':older_woman:', ':older_adult:', ':older_man:', ':man_with_chinese_cap:', ':woman_wearing_turban:', ':man_wearing_turban:', ':woman_with_headscarf:', ':bearded_person:', ':blond_haired_man:', ':blond_haired_woman:', ':man_red_haired:', ':woman_red_haired:', ':man_curly_haired:', ':woman_curly_haired:', ':man_bald:', ':woman_bald:', ':man_white_haired:', ':woman_white_haired:', ':woman_superhero:', ':man_superhero:', ':woman_supervillain:', ':man_supervillain:', ':woman_police_officer:', ':man_police_officer:', ':woman_construction_worker:', ':man_construction_worker:', ':woman_guard:', ':man_guard:', ':woman_detective:', ':man_detective:', ':woman_health_worker:', ':man_health_worker:', ':woman_farmer:', ':man_farmer:', ':woman_cook:', ':man_cook:', ':woman_student:', ':man_student:', ':woman_singer:', ':man_singer:', ':woman_teacher:', ':man_teacher:', ':woman_factory_worker:', ':man_factory_worker:', ':woman_technologist:', ':man_technologist:', ':woman_office_worker:', ':man_office_worker:', ':woman_mechanic:', ':man_mechanic:', ':woman_scientist:', ':man_scientist:', ':woman_artist:', ':man_artist:', ':woman_firefighter:', ':man_firefighter:', ':woman_pilot:', ':man_pilot:', ':woman_astronaut:', ':man_astronaut:', ':woman_judge:', ':man_judge:', ':bride_with_veil:', ':man_in_tuxedo:', ':princess:', ':prince:', ':mrs_claus:', ':santa:', ':woman_mage:', ':man_mage:', ':woman_elf:', ':man_elf:', ':woman_vampire:', ':man_vampire:', ':woman_zombie:', ':man_zombie:', ':woman_genie:', ':man_genie:', ':mermaid:', ':merman:', ':woman_fairy:', ':man_fairy:', ':angel:', ':pregnant_woman:', ':breast_feeding:', ':woman_bowing:', ':man_bowing:', ':woman_tipping_hand:', ':man_tipping_hand:', ':woman_gesturing_no:', ':man_gesturing_no:', ':woman_gesturing_ok:', ':man_gesturing_ok:', ':woman_raising_hand:', ':man_raising_hand:', ':woman_facepalming:', ':man_facepalming:', ':woman_shrugging:', ':man_shrugging:', ':woman_pouting:', ':man_pouting:', ':woman_frowning:', ':man_frowning:', ':woman_getting_haircut:', ':man_getting_haircut:', ':woman_getting_face_massage:', ':man_getting_face_massage:', ':woman_in_steamy_room:', ':man_in_steamy_room:', ':nail_care:', ':selfie:', ':dancer:', ':man_dancing:', ':women_with_bunny_ears_partying:', ':men_with_bunny_ears_partying:', ':levitate:', ':woman_walking:', ':man_walking:', ':woman_running:', ':man_running:', ':couple:', ':two_women_holding_hands:', ':two_men_holding_hands:', ':couple_with_heart:', ':couple_ww:', ':couple_mm:', ':couplekiss:', ':kiss_ww:', ':kiss_mm:', ':family:', ':family_mwg:', ':family_mwgb:', ':family_mwbb:', ':family_mwgg:', ':family_wwb:', ':family_wwg:', ':family_wwgb:', ':family_wwbb:', ':family_wwgg:', ':family_mmb:', ':family_mmg:', ':family_mmgb:', ':family_mmbb:', ':family_mmgg:', ':family_woman_boy:', ':family_woman_girl:', ':family_woman_girl_boy:', ':family_woman_boy_boy:', ':family_woman_girl_girl:', ':family_man_boy:', ':family_man_girl:', ':family_man_girl_boy:', ':family_man_boy_boy:', ':family_man_girl_girl:', ':palms_up_together:', ':open_hands:', ':raised_hands:', ':clap:', ':handshake:', ':thumbsup:', ':thumbsdown:', ':punch:', ':fist:', ':left_facing_fist:', ':right_facing_fist:', ':fingers_crossed:', ':v:', ':love_you_gesture:', ':metal:', ':ok_hand:', ':point_left:', ':point_right:', ':point_up_2:', ':point_down:', ':point_up:', ':raised_hand:', ':raised_back_of_hand:', ':hand_splayed:', ':vulcan:', ':wave:', ':call_me:', ':muscle:', ':leg:', ':foot:', ':middle_finger:', ':writing_hand:', ':pray:', ':ring:', ':lipstick:', ':kiss:', ':lips:', ':coat:', ':womans_clothes:', ':shirt:', ':jeans:', ':necktie:', ':dress:', ':bikini:', ':kimono:', ':high_heel:', ':sandal:', ':boot:', ':mans_shoe:', ':athletic_shoe:', ':hiking_boot:', ':womans_flat_shoe:', ':socks:', ':gloves:', ':scarf:', ':tophat:', ':billed_cap:', ':womans_hat:', ':mortar_board:', ':helmet_with_cross:', ':crown:', ':pouch:', ':purse:', ':handbag:', ':briefcase:', ':school_satchel:', ':eyeglasses:', ':dark_sunglasses:', ':goggles:', ':lab_coat:', ':closed_umbrella:', ':thread:',':baby_tone1:', ':boy_tone1:', ':girl_tone1:', ':man_tone1:', ':woman_tone1:', ':blond_haired_woman_tone1:', ':blond_haired_person_tone1:', ':older_man_tone1:', ':older_woman_tone1:', ':man_with_chinese_cap_tone1:', ':woman_wearing_turban_tone1:', ':person_wearing_turban_tone1:', ':woman_police_officer_tone1:', ':police_officer_tone1:', ':woman_construction_worker_tone1:', ':construction_worker_tone1:', ':woman_guard_tone1:', ':guard_tone1:', ':woman_detective_tone1:', ':detective_tone1:', ':woman_health_worker_tone1:', ':man_health_worker_tone1:', ':woman_farmer_tone1:', ':man_farmer_tone1:', ':woman_cook_tone1:', ':man_cook_tone1:', ':woman_student_tone1:', ':man_student_tone1:', ':woman_singer_tone1:', ':man_singer_tone1:', ':woman_teacher_tone1:', ':man_teacher_tone1:', ':woman_factory_worker_tone1:', ':man_factory_worker_tone1:', ':woman_technologist_tone1:', ':man_technologist_tone1:', ':woman_office_worker_tone1:', ':man_office_worker_tone1:', ':woman_mechanic_tone1:', ':man_mechanic_tone1:', ':woman_scientist_tone1:', ':man_scientist_tone1:', ':woman_artist_tone1:', ':man_artist_tone1:', ':woman_firefighter_tone1:', ':man_firefighter_tone1:', ':woman_pilot_tone1:', ':man_pilot_tone1:', ':woman_astronaut_tone1:', ':man_astronaut_tone1:', ':woman_judge_tone1:', ':man_judge_tone1:', ':mrs_claus_tone1:', ':santa_tone1:', ':princess_tone1:', ':prince_tone1:', ':bride_with_veil_tone1:', ':man_in_tuxedo_tone1:', ':angel_tone1:', ':pregnant_woman_tone1:', ':woman_bowing_tone1:', ':person_bowing_tone1:', ':person_tipping_hand_tone1:', ':man_tipping_hand_tone1:', ':person_gesturing_no_tone1:', ':man_gesturing_no_tone1:', ':person_gesturing_ok_tone1:', ':man_gesturing_ok_tone1:', ':person_raising_hand_tone1:', ':man_raising_hand_tone1:', ':woman_facepalming_tone1:', ':man_facepalming_tone1:', ':woman_shrugging_tone1:', ':man_shrugging_tone1:', ':person_pouting_tone1:', ':man_pouting_tone1:', ':person_frowning_tone1:', ':man_frowning_tone1:', ':person_getting_haircut_tone1:', ':man_getting_haircut_tone1:', ':person_getting_massage_tone1:', ':man_getting_face_massage_tone1:', ':levitate_tone1:', ':dancer_tone1:', ':man_dancing_tone1:', ':woman_walking_tone1:', ':person_walking_tone1:', ':woman_running_tone1:', ':person_running_tone1:', ':palms_up_together_tone1:', ':open_hands_tone1:', ':raised_hands_tone1:', ':clap_tone1:', ':pray_tone1:', ':thumbsup_tone1:', ':thumbsdown_tone1:', ':punch_tone1:', ':fist_tone1:', ':left_facing_fist_tone1:', ':right_facing_fist_tone1:', ':fingers_crossed_tone1:', ':v_tone1:', ':love_you_gesture_tone1:', ':metal_tone1:', ':ok_hand_tone1:', ':point_left_tone1:', ':point_right_tone1:', ':point_up_2_tone1:', ':point_down_tone1:', ':point_up_tone1:', ':raised_hand_tone1:', ':raised_back_of_hand_tone1:', ':hand_splayed_tone1:', ':vulcan_tone1:', ':wave_tone1:', ':call_me_tone1:', ':muscle_tone1:', ':middle_finger_tone1:', ':writing_hand_tone1:', ':selfie_tone1:', ':nail_care_tone1:', ':ear_tone1:', ':baby_tone2:', ':boy_tone2:', ':girl_tone2:', ':man_tone2:', ':woman_tone2:', ':blond_haired_woman_tone2:', ':blond_haired_person_tone2:', ':older_man_tone2:', ':older_woman_tone2:', ':man_with_chinese_cap_tone2:', ':woman_wearing_turban_tone2:', ':person_wearing_turban_tone2:', ':woman_police_officer_tone2:', ':police_officer_tone2:', ':woman_construction_worker_tone2:', ':construction_worker_tone2:', ':woman_guard_tone2:', ':guard_tone2:', ':woman_detective_tone2:', ':detective_tone2:', ':woman_health_worker_tone2:', ':man_health_worker_tone2:', ':woman_farmer_tone2:', ':man_farmer_tone2:', ':woman_cook_tone2:', ':man_cook_tone2:', ':woman_student_tone2:', ':man_student_tone2:', ':woman_singer_tone2:', ':man_singer_tone2:', ':woman_teacher_tone2:', ':man_teacher_tone2:', ':woman_factory_worker_tone2:', ':man_factory_worker_tone2:', ':woman_technologist_tone2:', ':man_technologist_tone2:', ':woman_office_worker_tone2:', ':man_office_worker_tone2:', ':woman_mechanic_tone2:', ':man_mechanic_tone2:', ':woman_scientist_tone2:', ':man_scientist_tone2:', ':woman_artist_tone2:', ':man_artist_tone2:', ':woman_firefighter_tone2:', ':man_firefighter_tone2:', ':woman_pilot_tone2:', ':man_pilot_tone2:', ':woman_astronaut_tone2:', ':man_astronaut_tone2:', ':woman_judge_tone2:', ':man_judge_tone2:', ':mrs_claus_tone2:', ':santa_tone2:', ':princess_tone2:', ':prince_tone2:', ':bride_with_veil_tone2:', ':man_in_tuxedo_tone2:', ':angel_tone2:', ':pregnant_woman_tone2:', ':woman_bowing_tone2:', ':person_bowing_tone2:', ':person_tipping_hand_tone2:', ':man_tipping_hand_tone2:', ':person_gesturing_no_tone2:', ':man_gesturing_no_tone2:', ':person_gesturing_ok_tone2:', ':man_gesturing_ok_tone2:', ':person_raising_hand_tone2:', ':man_raising_hand_tone2:', ':woman_facepalming_tone2:', ':man_facepalming_tone2:', ':woman_shrugging_tone2:', ':man_shrugging_tone2:', ':person_pouting_tone2:', ':man_pouting_tone2:', ':person_frowning_tone2:', ':man_frowning_tone2:', ':person_getting_haircut_tone2:', ':man_getting_haircut_tone2:', ':person_getting_massage_tone2:', ':man_getting_face_massage_tone2:', ':levitate_tone2:', ':dancer_tone2:', ':man_dancing_tone2:', ':woman_walking_tone2:', ':person_walking_tone2:', ':woman_running_tone2:', ':person_running_tone2:', ':palms_up_together_tone2:', ':open_hands_tone2:', ':raised_hands_tone2:', ':clap_tone2:', ':pray_tone2:', ':thumbsup_tone2:', ':thumbsdown_tone2:', ':punch_tone2:', ':fist_tone2:', ':left_facing_fist_tone2:', ':right_facing_fist_tone2:', ':fingers_crossed_tone2:', ':v_tone2:', ':love_you_gesture_tone2:', ':metal_tone2:', ':ok_hand_tone2:', ':point_left_tone2:', ':point_right_tone2:', ':point_up_2_tone2:', ':point_down_tone2:', ':point_up_tone2:', ':raised_hand_tone2:', ':raised_back_of_hand_tone2:', ':hand_splayed_tone2:', ':vulcan_tone2:', ':wave_tone2:', ':call_me_tone2:', ':muscle_tone2:', ':middle_finger_tone2:', ':writing_hand_tone2:', ':selfie_tone2:', ':nail_care_tone2:', ':ear_tone2:', ':baby_tone3:', ':boy_tone3:', ':girl_tone3:', ':man_tone3:', ':woman_tone3:', ':blond_haired_woman_tone3:', ':blond_haired_person_tone3:', ':older_man_tone3:', ':older_woman_tone3:', ':man_with_chinese_cap_tone3:', ':woman_wearing_turban_tone3:', ':person_wearing_turban_tone3:', ':woman_police_officer_tone3:', ':police_officer_tone3:', ':woman_construction_worker_tone3:', ':construction_worker_tone3:', ':woman_guard_tone3:', ':guard_tone3:', ':woman_detective_tone3:', ':detective_tone3:', ':woman_health_worker_tone3:', ':man_health_worker_tone3:', ':woman_farmer_tone3:', ':man_farmer_tone3:', ':woman_cook_tone3:', ':man_cook_tone3:', ':woman_student_tone3:', ':man_student_tone3:', ':woman_singer_tone3:', ':man_singer_tone3:', ':woman_teacher_tone3:', ':man_teacher_tone3:', ':woman_factory_worker_tone3:', ':man_factory_worker_tone3:', ':woman_technologist_tone3:', ':man_technologist_tone3:', ':woman_office_worker_tone3:', ':man_office_worker_tone3:', ':woman_mechanic_tone3:', ':man_mechanic_tone3:', ':woman_scientist_tone3:', ':man_scientist_tone3:', ':woman_artist_tone3:', ':man_artist_tone3:', ':woman_firefighter_tone3:', ':man_firefighter_tone3:', ':woman_pilot_tone3:', ':man_pilot_tone3:', ':woman_astronaut_tone3:', ':man_astronaut_tone3:', ':woman_judge_tone3:', ':man_judge_tone3:', ':mrs_claus_tone3:', ':santa_tone3:', ':princess_tone3:', ':prince_tone3:', ':bride_with_veil_tone3:', ':man_in_tuxedo_tone3:', ':angel_tone3:', ':pregnant_woman_tone3:', ':woman_bowing_tone3:', ':person_bowing_tone3:', ':person_tipping_hand_tone3:', ':man_tipping_hand_tone3:', ':person_gesturing_no_tone3:', ':man_gesturing_no_tone3:', ':person_gesturing_ok_tone3:', ':man_gesturing_ok_tone3:', ':person_raising_hand_tone3:', ':man_raising_hand_tone3:', ':woman_facepalming_tone3:', ':man_facepalming_tone3:', ':woman_shrugging_tone3:', ':man_shrugging_tone3:', ':person_pouting_tone3:', ':man_pouting_tone3:', ':person_frowning_tone3:', ':man_frowning_tone3:', ':person_getting_haircut_tone3:', ':man_getting_haircut_tone3:', ':person_getting_massage_tone3:', ':man_getting_face_massage_tone3:', ':levitate_tone2:', ':dancer_tone3:', ':man_dancing_tone3:', ':woman_walking_tone3:', ':person_walking_tone3:', ':woman_running_tone3:', ':person_running_tone3:', ':palms_up_together_tone3:', ':open_hands_tone3:', ':raised_hands_tone3:', ':clap_tone3:', ':pray_tone3:', ':thumbsup_tone3:', ':thumbsdown_tone3:', ':punch_tone3:', ':fist_tone3:', ':left_facing_fist_tone3:', ':right_facing_fist_tone3:', ':fingers_crossed_tone3:', ':v_tone3:', ':love_you_gesture_tone3:', ':metal_tone3:', ':ok_hand_tone3:', ':point_left_tone3:', ':point_right_tone3:', ':point_up_2_tone3:', ':point_down_tone3:', ':point_up_tone3:', ':raised_hand_tone3:', ':raised_back_of_hand_tone3:', ':hand_splayed_tone3:', ':vulcan_tone3:', ':wave_tone3:', ':call_me_tone3:', ':muscle_tone3:', ':middle_finger_tone3:', ':writing_hand_tone3:', ':selfie_tone3:', ':nail_care_tone3:', ':ear_tone3:', ':baby_tone4:', ':boy_tone4:', ':girl_tone4:', ':man_tone4:', ':woman_tone4:', ':blond_haired_woman_tone4:', ':blond_haired_person_tone4:', ':older_man_tone4:', ':older_woman_tone4:', ':man_with_chinese_cap_tone4:', ':woman_wearing_turban_tone4:', ':person_wearing_turban_tone4:', ':woman_police_officer_tone4:', ':police_officer_tone4:', ':woman_construction_worker_tone4:', ':construction_worker_tone4:', ':woman_guard_tone4:', ':guard_tone4:', ':woman_detective_tone4:', ':detective_tone4:', ':woman_health_worker_tone4:', ':man_health_worker_tone4:', ':woman_farmer_tone4:', ':man_farmer_tone4:', ':woman_cook_tone4:', ':man_cook_tone4:', ':woman_student_tone4:', ':man_student_tone4:', ':woman_singer_tone4:', ':man_singer_tone4:', ':woman_teacher_tone4:', ':man_teacher_tone4:', ':woman_factory_worker_tone4:', ':man_factory_worker_tone4:', ':woman_technologist_tone4:', ':man_technologist_tone4:', ':woman_office_worker_tone4:', ':man_office_worker_tone4:', ':woman_mechanic_tone4:', ':man_mechanic_tone4:', ':woman_scientist_tone4:', ':man_scientist_tone4:', ':woman_artist_tone4:', ':man_artist_tone4:', ':woman_firefighter_tone4:', ':man_firefighter_tone4:', ':woman_pilot_tone4:', ':man_pilot_tone4:', ':woman_astronaut_tone4:', ':man_astronaut_tone4:', ':woman_judge_tone4:', ':man_judge_tone4:', ':mrs_claus_tone4:', ':santa_tone4:', ':princess_tone4:', ':prince_tone4:', ':bride_with_veil_tone4:', ':man_in_tuxedo_tone4:', ':angel_tone4:', ':pregnant_woman_tone4:', ':woman_bowing_tone4:', ':person_bowing_tone4:', ':person_tipping_hand_tone4:', ':man_tipping_hand_tone4:', ':person_gesturing_no_tone4:', ':man_gesturing_no_tone4:', ':person_gesturing_ok_tone4:', ':man_gesturing_ok_tone4:', ':person_raising_hand_tone4:', ':man_raising_hand_tone4:', ':woman_facepalming_tone4:', ':man_facepalming_tone4:', ':woman_shrugging_tone4:', ':man_shrugging_tone4:', ':person_pouting_tone4:', ':man_pouting_tone4:', ':person_frowning_tone4:', ':man_frowning_tone4:', ':person_getting_haircut_tone4:', ':man_getting_haircut_tone4:', ':person_getting_massage_tone4:', ':man_getting_face_massage_tone4:', ':levitate_tone4:', ':dancer_tone4:', ':man_dancing_tone4:', ':woman_walking_tone4:', ':person_walking_tone4:', ':woman_running_tone4:', ':person_running_tone4:', ':palms_up_together_tone4:', ':open_hands_tone4:', ':raised_hands_tone4:', ':clap_tone4:', ':pray_tone4:', ':thumbsup_tone4:', ':thumbsdown_tone4:', ':punch_tone4:', ':fist_tone4:', ':left_facing_fist_tone4:', ':right_facing_fist_tone4:', ':fingers_crossed_tone4:', ':v_tone4:', ':love_you_gesture_tone4:', ':metal_tone4:', ':ok_hand_tone4:', ':point_left_tone4:', ':point_right_tone4:', ':point_up_2_tone4:', ':point_down_tone4:', ':point_up_tone4:', ':raised_hand_tone4:', ':raised_back_of_hand_tone4:', ':hand_splayed_tone4:', ':vulcan_tone4:', ':wave_tone4:', ':call_me_tone4:', ':muscle_tone4:', ':middle_finger_tone4:', ':writing_hand_tone4:', ':selfie_tone4:', ':nail_care_tone4:', ':ear_tone4:', ':baby_tone5:', ':boy_tone5:', ':girl_tone5:', ':man_tone5:', ':woman_tone5:', ':blond_haired_woman_tone5:', ':blond_haired_person_tone5:', ':older_man_tone5:', ':older_woman_tone5:', ':man_with_chinese_cap_tone5:', ':woman_wearing_turban_tone5:', ':person_wearing_turban_tone5:', ':woman_police_officer_tone5:', ':police_officer_tone5:', ':woman_construction_worker_tone5:', ':construction_worker_tone5:', ':woman_guard_tone5:', ':guard_tone5:', ':woman_detective_tone5:', ':detective_tone5:', ':woman_health_worker_tone5:', ':man_health_worker_tone5:', ':woman_farmer_tone5:', ':man_farmer_tone5:', ':woman_cook_tone5:', ':man_cook_tone5:', ':woman_student_tone5:', ':man_student_tone5:', ':woman_singer_tone5:', ':man_singer_tone5:', ':woman_teacher_tone5:', ':man_teacher_tone5:', ':woman_factory_worker_tone5:', ':man_factory_worker_tone5:', ':woman_technologist_tone5:', ':man_technologist_tone5:', ':woman_office_worker_tone5:', ':man_office_worker_tone5:', ':woman_mechanic_tone5:', ':man_mechanic_tone5:', ':woman_scientist_tone5:', ':man_scientist_tone5:', ':woman_artist_tone5:', ':man_artist_tone5:', ':woman_firefighter_tone5:', ':man_firefighter_tone5:', ':woman_pilot_tone5:', ':man_pilot_tone5:', ':woman_astronaut_tone5:', ':man_astronaut_tone5:', ':woman_judge_tone5:', ':man_judge_tone5:', ':mrs_claus_tone5:', ':santa_tone5:', ':princess_tone5:', ':prince_tone5:', ':bride_with_veil_tone5:', ':man_in_tuxedo_tone5:', ':angel_tone5:', ':pregnant_woman_tone5:', ':woman_bowing_tone5:', ':person_bowing_tone5:', ':person_tipping_hand_tone5:', ':man_tipping_hand_tone5:', ':person_gesturing_no_tone5:', ':man_gesturing_no_tone5:', ':person_gesturing_ok_tone5:', ':man_gesturing_ok_tone5:', ':person_raising_hand_tone5:', ':man_raising_hand_tone5:', ':woman_facepalming_tone5:', ':man_facepalming_tone5:', ':woman_shrugging_tone5:', ':man_shrugging_tone5:', ':person_pouting_tone5:', ':man_pouting_tone5:', ':person_frowning_tone5:', ':man_frowning_tone5:', ':person_getting_haircut_tone5:', ':man_getting_haircut_tone5:', ':person_getting_massage_tone5:', ':man_getting_face_massage_tone5:', ':levitate_tone5:', ':dancer_tone5:', ':man_dancing_tone5:', ':woman_walking_tone5:', ':person_walking_tone5:', ':woman_running_tone5:', ':person_running_tone5:', ':palms_up_together_tone5:', ':open_hands_tone5:', ':raised_hands_tone5:', ':clap_tone5:', ':pray_tone5:', ':thumbsup_tone5:', ':thumbsdown_tone5:', ':punch_tone5:', ':fist_tone5:', ':left_facing_fist_tone5:', ':right_facing_fist_tone5:', ':fingers_crossed_tone5:', ':v_tone5:', ':love_you_gesture_tone5:', ':metal_tone5:', ':ok_hand_tone5:', ':point_left_tone5:', ':point_right_tone5:', ':point_up_2_tone5:', ':point_down_tone5:', ':point_up_tone5:', ':raised_hand_tone5:', ':raised_back_of_hand_tone5:', ':hand_splayed_tone5:', ':vulcan_tone5:', ':wave_tone5:', ':call_me_tone5:', ':muscle_tone5:', ':middle_finger_tone5:', ':writing_hand_tone5:', ':selfie_tone5:', ':nail_care_tone5:', ':ear_tone5:', ':dog:', ':cat:', ':mouse:', ':hamster:', ':rabbit:', ':fox:', ':raccoon:', ':bear:', ':panda_face:', ':kangaroo:', ':badger:', ':koala:', ':tiger:', ':lion_face:', ':cow:', ':pig:', ':pig_nose:', ':frog:', ':monkey_face:', ':see_no_evil:', ':hear_no_evil:', ':speak_no_evil:', ':monkey:', ':chicken:', ':penguin:', ':bird:', ':baby_chick:', ':hatching_chick:', ':hatched_chick:', ':duck:', ':swan:', ':eagle:', ':owl:', ':peacock:', ':parrot:', ':bat:', ':wolf:', ':boar:', ':horse:', ':unicorn:', ':bee:', ':bug:', ':butterfly:', ':snail:', ':shell:', ':beetle:', ':ant:', ':cricket:', ':spider:', ':spider_web:', ':scorpion:', ':mosquito:', ':microbe:', ':turtle:', ':snake:', ':lizard:', ':t_rex:', ':sauropod:', ':octopus:', ':squid:', ':shrimp:', ':crab:', ':blowfish:', ':tropical_fish:', ':fish:', ':dolphin:', ':whale:', ':whale2:', ':shark:', ':crocodile:', ':tiger2:', ':leopard:', ':zebra:', ':gorilla:', ':elephant:', ':rhino:', ':hippopotamus:', ':dromedary_camel:', ':camel:', ':llama:', ':giraffe:', ':water_buffalo:', ':ox:', ':cow2:', ':racehorse:', ':pig2:', ':ram:', ':sheep:', ':goat:', ':deer:', ':dog2:', ':poodle:', ':cat2:', ':rooster:', ':turkey:', ':dove:', ':rabbit2:', ':mouse2:', ':rat:', ':chipmunk:', ':hedgehog:', ':feet:', ':dragon:', ':dragon_face:', ':cactus:', ':christmas_tree:', ':evergreen_tree:', ':deciduous_tree:', ':palm_tree:', ':seedling:', ':herb:', ':shamrock:', ':four_leaf_clover:', ':bamboo:', ':tanabata_tree:', ':leaves:', ':fallen_leaf:', ':maple_leaf:', ':mushroom:', ':ear_of_rice:', ':bouquet:', ':tulip:', ':rose:', ':wilted_rose:', ':hibiscus:', ':cherry_blossom:', ':blossom:', ':sunflower:', ':sun_with_face:', ':full_moon_with_face:', ':first_quarter_moon_with_face:', ':last_quarter_moon_with_face:', ':new_moon_with_face:', ':full_moon:', ':waning_gibbous_moon:', ':last_quarter_moon:', ':waning_crescent_moon:', ':new_moon:', ':waxing_crescent_moon:', ':first_quarter_moon:', ':waxing_gibbous_moon:', ':crescent_moon:', ':earth_americas:', ':earth_africa:', ':earth_asia:', ':dizzy:', '⭐️', ':star2:', ':sparkles:', '⚡️', ':comet:', ':boom:', ':fire:', ':cloud_tornado:', ':rainbow:', ':sunny:', ':white_sun_small_cloud:', '⛅️', ':white_sun_cloud:', ':cloud:', ':white_sun_rain_cloud:', ':cloud_rain:', ':thunder_cloud_rain:', ':cloud_lightning:', ':cloud_snow:', ':snowflake:', ':snowman2:', '⛄️', ':wind_blowing_face:', ':dash:', ':droplet:', ':sweat_drops:', '☔️', ':umbrella2:', ':ocean:',':green_apple:', ':apple:', ':pear:', ':tangerine:', ':lemon:', ':banana:', ':watermelon:', ':grapes:', ':strawberry:', ':melon:', ':cherries:', ':peach:', ':pineapple:', ':mango:', ':coconut:', ':kiwi:', ':tomato:', ':eggplant:', ':avocado:', ':broccoli:', ':cucumber:', ':leafy_green:', ':hot_pepper:', ':corn:', ':carrot:', ':potato:', ':sweet_potato:', ':croissant:', ':bread:', ':french_bread:', ':pretzel:', ':bagel:', ':cheese:', ':egg:', ':cooking:', ':pancakes:', ':bacon:', ':cut_of_meat:', ':poultry_leg:', ':meat_on_bone:', ':hotdog:', ':hamburger:', ':fries:', ':pizza:', ':sandwich:', ':stuffed_flatbread:', ':taco:', ':burrito:', ':salad:', ':shallow_pan_of_food:', ':canned_food:', ':spaghetti:', ':ramen:', ':stew:', ':curry:', ':sushi:', ':bento:', ':dumpling:', ':fried_shrimp:', ':rice_ball:', ':rice:', ':rice_cracker:', ':fish_cake:', ':moon_cake:', ':fortune_cookie:', ':oden:', ':dango:', ':shaved_ice:', ':ice_cream:', ':icecream:', ':pie:', ':cake:', ':birthday:', ':custard:', ':lollipop:', ':candy:', ':chocolate_bar:', ':popcorn:', ':salt:', ':doughnut:', ':cookie:', ':chestnut:', ':peanuts:', ':honey_pot:', ':milk:', ':baby_bottle:', '☕️', ':tea:', ':cup_with_straw:', ':sake:', ':beer:', ':beers:', ':champagne_glass:', ':wine_glass:', ':tumbler_glass:', ':cocktail:', ':tropical_drink:', ':champagne:', ':spoon:', ':fork_and_knife:', ':fork_knife_plate:', ':bowl_with_spoon:', ':takeout_box:', '⚽️', ':basketball:', ':football:', '⚾️', ':softball:', ':volleyball:', ':rugby_football:', ':tennis:', ':flying_disc:', ':8ball:', ':ping_pong:', ':badminton:', ':goal:', ':hockey:', ':field_hockey:', ':lacrosse:', ':cricket_game:', '⛳️', ':bow_and_arrow:', ':fishing_pole_and_fish:', ':boxing_glove:', ':martial_arts_uniform:', ':running_shirt_with_sash:', ':ice_skate:', ':curling_stone:', ':sled:', ':skateboard:', ':ski:', ':skier:', ':snowboarder:', ':woman_lifting_weights:', ':woman_lifting_weights_tone1:', ':woman_lifting_weights_tone2:', ':woman_lifting_weights_tone3:', ':woman_lifting_weights_tone4:', ':woman_lifting_weights_tone5:', ':man_lifting_weights:', ':man_lifting_weights_tone1:', ':man_lifting_weights_tone2:', ':man_lifting_weights_tone3:', ':man_lifting_weights_tone4:', ':man_lifting_weights_tone5:', ':women_wrestling:', ':men_wrestling:', ':woman_cartwheeling:', ':woman_cartwheeling_tone1:', ':woman_cartwheeling_tone2:', ':woman_cartwheeling_tone3:', ':woman_cartwheeling_tone4:', ':woman_cartwheeling_tone5:', ':man_cartwheeling:', ':man_cartwheeling_tone1:', ':man_cartwheeling_tone2:', ':man_cartwheeling_tone3:', ':man_cartwheeling_tone4:', ':man_cartwheeling_tone5:', ':woman_bouncing_ball:', ':woman_bouncing_ball_tone1:', ':woman_bouncing_ball_tone2:', ':woman_bouncing_ball_tone3:', ':woman_bouncing_ball_tone4:', ':woman_bouncing_ball_tone5:', ':man_bouncing_ball:', ':man_bouncing_ball_tone1:', ':man_bouncing_ball_tone2:', ':man_bouncing_ball_tone3:', ':man_bouncing_ball_tone4:', ':man_bouncing_ball_tone5:', ':person_fencing:', ':woman_playing_handball:', ':woman_playing_handball_tone1:', ':woman_playing_handball_tone2:', ':woman_playing_handball_tone4:', ':woman_playing_handball_tone4:', ':woman_playing_handball_tone5:', ':man_playing_handball:', ':man_playing_handball_tone1:', ':man_playing_handball_tone2:', ':man_playing_handball_tone3:', ':man_playing_handball_tone4:', ':man_playing_handball_tone5:', ':woman_golfing:', ':woman_golfing_tone1:', ':woman_golfing_tone2:', ':woman_golfing_tone3:', ':woman_golfing_tone4:', ':woman_golfing_tone5:', ':man_golfing:', ':man_golfing_tone1:', ':man_golfing_tone2:', ':man_golfing_tone3:', ':man_golfing_tone4:', ':man_golfing_tone5:', ':horse_racing:', ':horse_racing_tone1:', ':horse_racing_tone2:', ':horse_racing_tone3:', ':horse_racing_tone4:', ':horse_racing_tone5:', ':woman_in_lotus_position:', ':woman_in_lotus_position_tone1:', ':woman_in_lotus_position_tone2:', ':woman_in_lotus_position_tone3:', ':woman_in_lotus_position_tone4:', ':woman_in_lotus_position_tone5:', ':man_in_lotus_position:', ':man_in_lotus_position_tone1:', ':man_in_lotus_position_tone2:', ':man_in_lotus_position_tone3:', ':man_in_lotus_position_tone4:', ':man_in_lotus_position_tone5:', ':woman_surfing:', ':woman_surfing_tone1:', ':woman_surfing_tone2:', ':woman_surfing_tone3:', ':woman_surfing_tone4:', ':woman_surfing_tone5:', ':man_surfing:', ':man_surfing_tone1:', ':man_surfing_tone2:', ':man_surfing_tone3:', ':man_surfing_tone4:', ':man_surfing_tone5:', ':woman_swimming:', ':woman_swimming_tone1:', ':woman_swimming_tone2:', ':woman_swimming_tone3:', ':woman_swimming_tone4:', ':woman_swimming_tone5:', ':man_swimming:', ':man_swimming_tone1:', ':man_swimming_tone2:', ':man_swimming_tone3:', ':man_swimming_tone4:', ':man_swimming_tone5:', ':woman_playing_water_polo:', ':woman_playing_water_polo_tone1:', ':woman_playing_water_polo_tone2:', ':woman_playing_water_polo_tone3:', ':woman_playing_water_polo_tone4:', ':woman_playing_water_polo_tone5:', ':man_playing_water_polo:', ':man_playing_water_polo_tone1:', ':man_playing_water_polo_tone2:', ':man_playing_water_polo_tone3:', ':man_playing_water_polo_tone4:', ':man_playing_water_polo_tone5:', ':woman_rowing_boat:', ':woman_rowing_boat_tone1:', ':woman_rowing_boat_tone2:', ':woman_rowing_boat_tone3:', ':woman_rowing_boat_tone4:', ':woman_rowing_boat_tone5:', ':man_rowing_boat:', ':man_rowing_boat_tone1:', ':man_rowing_boat_tone2:', ':man_rowing_boat_tone3:', ':man_rowing_boat_tone4:', ':man_rowing_boat_tone5:', ':woman_climbing:', ':woman_climbing_tone1:', ':woman_climbing_tone2:', ':woman_climbing_tone3:', ':woman_climbing_tone4:', ':woman_climbing_tone5:', ':man_climbing:', ':man_climbing_tone1:', ':man_climbing_tone2:', ':man_climbing_tone3:', ':man_climbing_tone4:', ':man_climbing_tone5:', ':woman_mountain_biking:', ':woman_mountain_biking_tone1:', ':woman_mountain_biking_tone2:', ':woman_mountain_biking_tone3:', ':woman_mountain_biking_tone4:', ':woman_mountain_biking_tone5:', ':man_mountain_biking:', ':man_mountain_biking_tone1:', ':man_mountain_biking_tone2:', ':man_mountain_biking_tone3:', ':man_mountain_biking_tone4:', ':man_mountain_biking_tone5:', ':woman_biking:', ':woman_biking_tone1:', ':woman_biking_tone2:', ':woman_biking_tone3:', ':woman_biking_tone4:', ':woman_biking_tone5:', ':man_biking:', ':man_biking_tone1:', ':man_biking_tone2:', ':man_biking_tone3:', ':man_biking_tone4:', ':man_biking_tone5:', ':trophy:', ':first_place:', ':second_place:', ':third_place:', ':medal:', ':military_medal:', ':rosette:', ':reminder_ribbon:', ':ticket:', ':tickets:', ':circus_tent:', ':woman_juggling:', ':woman_juggling_tone1:', ':woman_juggling_tone2:', ':woman_juggling_tone3:', ':woman_juggling_tone4:', ':woman_juggling_tone5:', ':man_juggling:', ':man_juggling_tone1:', ':man_juggling_tone2:', ':man_juggling_tone3:', ':man_juggling_tone4:', ':man_juggling_tone5:', ':performing_arts:', ':art:', ':clapper:', ':microphone:', ':headphones:', ':musical_score:', ':musical_keyboard:', ':drum:', ':saxophone:', ':trumpet:', ':guitar:', ':violin:', ':game_die:', ':jigsaw:', ':chess_pawn:', ':dart:', ':bowling:', ':video_game:', ':red_car:', ':taxi:', ':blue_car:', ':bus:', ':trolleybus:', ':race_car:', ':police_car:', ':ambulance:', ':fire_engine:', ':minibus:', ':truck:', ':articulated_lorry:', ':tractor:', ':scooter:', ':bike:', ':motor_scooter:', ':motorcycle:', ':rotating_light:', ':oncoming_police_car:', ':oncoming_bus:', ':oncoming_automobile:', ':oncoming_taxi:', ':aerial_tramway:', ':mountain_cableway:', ':suspension_railway:', ':railway_car:', ':train:', ':mountain_railway:', ':monorail:', ':bullettrain_side:', ':bullettrain_front:', ':light_rail:', ':steam_locomotive:', ':train2:', ':metro:', ':tram:', ':station:', ':airplane:', ':airplane_departure:', ':airplane_arriving:', ':airplane_small:', ':seat:', ':satellite_orbital:', ':rocket:', ':flying_saucer:', ':helicopter:', ':canoe:', '⛵️', ':speedboat:', ':motorboat:', ':cruise_ship:', ':ferry:', ':ship:', '⚓️', '⛽️', ':construction:', ':vertical_traffic_light:', ':traffic_light:', ':busstop:', ':map:', ':moyai:', ':statue_of_liberty:', ':tokyo_tower:', ':european_castle:', ':japanese_castle:', ':stadium:', ':ferris_wheel:', ':roller_coaster:', ':carousel_horse:', '⛲️', ':beach_umbrella:', ':beach:', ':island:', ':desert:', ':volcano:', ':mountain:', ':mountain_snow:', ':mount_fuji:', ':camping:', '⛺️', ':house:', ':house_with_garden:', ':homes:', ':house_abandoned:', ':construction_site:', ':factory:', ':office:', ':department_store:', ':post_office:', ':european_post_office:', ':hospital:', ':bank:', ':hotel:', ':convenience_store:', ':school:', ':love_hotel:', ':wedding:', ':classical_building:', '⛪️', ':mosque:', ':synagogue:', ':kaaba:', ':shinto_shrine:', ':railway_track:', ':motorway:', ':japan:', ':rice_scene:', ':park:', ':sunrise:', ':sunrise_over_mountains:', ':stars:', ':sparkler:', ':fireworks:', ':city_sunset:', ':city_dusk:', ':cityscape:', ':night_with_stars:', ':milky_way:', ':bridge_at_night:', '⌚️', ':iphone:', ':calling:', ':computer:', ':keyboard:', ':desktop:', ':printer:', ':mouse_three_button:', ':trackball:', ':joystick:', ':compression:', ':minidisc:', ':floppy_disk:', ':cd:', ':dvd:', ':vhs:', ':camera:', ':camera_with_flash:', ':video_camera:', ':movie_camera:', ':projector:', ':film_frames:', ':telephone_receiver:', ':telephone:', ':pager:', ':fax:', ':tv:', ':radio:', ':microphone2:', ':level_slider:', ':control_knobs:', ':stopwatch:', ':timer:', ':alarm_clock:', ':clock:', '⌛️', ':hourglass_flowing_sand:', ':satellite:', ':battery:', ':electric_plug:', ':bulb:', ':flashlight:', ':candle:', ':wastebasket:', ':oil:', ':money_with_wings:', ':dollar:', ':yen:', ':euro:', ':pound:', ':moneybag:', ':credit_card:', ':receipt:', ':gem:', ':scales:', ':wrench:', ':hammer:', ':hammer_pick:', ':tools:', ':pick:', ':nut_and_bolt:', ':gear:', ':chains:', ':gun:', ':bomb:', ':knife:', ':dagger:', ':crossed_swords:', ':shield:', ':smoking:', ':coffin:', ':urn:', ':amphora:', ':compass:', ':bricks:', ':crystal_ball:', ':nazar_amulet:', ':teddy_bear:', ':prayer_beads:', ':barber:', ':alembic:', ':telescope:', ':toolbox:', ':magnet:', ':test_tube:', ':petri_dish:', ':dna:', ':fire_extinguisher:', ':microscope:', ':hole:', ':pill:', ':syringe:', ':thermometer:', ':toilet:', ':potable_water:', ':shower:', ':bathtub:', ':bath:', ':bath_tone1:', ':bath_tone2:', ':bath_tone3:', ':bath_tone4:', ':bath_tone5:', ':squeeze_bottle:', ':thread:', ':yarn:', ':safety_pin:', ':broom:', ':basket:', ':roll_of_paper:', ':soap:', ':sponge:', ':bellhop:', ':key:', ':key2:', ':door:', ':couch:', ':bed:', ':sleeping_accommodation:', ':frame_photo:', ':shopping_bags:', ':luggage:', ':shopping_cart:', ':gift:', ':balloon:', ':flags:', ':ribbon:', ':confetti_ball:', ':tada:', ':firecracker:', ':dolls:', ':izakaya_lantern:', ':wind_chime:', ':red_envelope:', ':envelope:', ':envelope_with_arrow:', ':incoming_envelope:', ':e_mail:', ':love_letter:', ':inbox_tray:', ':outbox_tray:', ':package:', ':label:', ':mailbox_closed:', ':mailbox:', ':mailbox_with_mail:', ':mailbox_with_no_mail:', ':postbox:', ':postal_horn:', ':scroll:', ':page_with_curl:', ':page_facing_up:', ':bookmark_tabs:', ':bar_chart:', ':chart_with_upwards_trend:', ':chart_with_downwards_trend:', ':notepad_spiral:', ':calendar_spiral:', ':calendar:', ':date:', ':card_index:', ':card_box:', ':ballot_box:', ':file_cabinet:', ':clipboard:', ':file_folder:', ':open_file_folder:', ':dividers:', ':newspaper2:', ':newspaper:', ':notebook:', ':notebook_with_decorative_cover:', ':ledger:', ':closed_book:', ':green_book:', ':blue_book:', ':orange_book:', ':books:', ':book:', ':bookmark:', ':link:', ':paperclip:', ':paperclips:', ':triangular_ruler:', ':straight_ruler:', ':pushpin:', ':round_pushpin:', ':scissors:', ':pen_ballpoint:', ':pen_fountain:', ':black_nib:', ':paintbrush:', ':crayon:', ':pencil:', ':pencil2:', ':mag:', ':mag_right:', ':lock_with_ink_pen:', ':closed_lock_with_key:', ':lock:', ':heart:', ':orange_heart:', ':yellow_heart:', ':green_heart:', ':blue_heart:', ':purple_heart:', ':black_heart:', ':broken_heart:', ':heart_exclamation:', ':two_hearts:', ':revolving_hearts:', ':heartbeat:', ':heartpulse:', ':sparkling_heart:', ':cupid:', ':gift_heart:', ':heart_decoration:', ':peace:', ':cross:', ':star_and_crescent:', ':om_symbol:', ':wheel_of_dharma:', ':star_of_david:', ':six_pointed_star:', ':menorah:', ':yin_yang:', ':orthodox_cross:', ':place_of_worship:', ':ophiuchus:', '♈️', '♉️', '♊️', '♋️', '♌️', '♍️', '♎️', '♏️', '♐️', '♑️', '♒️', '♓️', ':id:', ':atom:', ':accept:', ':radioactive:', ':biohazard:', ':mobile_phone_off:', ':vibration_mode:', ':u6709:', '🈚️', ':u7533:', ':u55b6:', ':u6708:', ':eight_pointed_black_star:', ':vs:', ':white_flower:', ':ideograph_advantage:', ':secret:', ':congratulations:', ':u5408:', ':u6e80:', ':u5272:', ':u7981:', ':a:', ':b:', ':ab:', ':cl:', ':o2:', ':sos:', ':x:', '⭕️', ':octagonal_sign:', '⛔️', ':name_badge:', ':no_entry_sign:', ':100:', ':anger:', ':hotsprings:', ':no_pedestrians:', ':do_not_litter:', ':no_bicycles:', ':non_potable_water:', ':underage:', ':no_mobile_phones:', ':no_smoking:', '❗️', ':grey_exclamation:', ':question:', ':grey_question:', ':bangbang:', ':interrobang:', ':low_brightness:', ':high_brightness:', ':part_alternation_mark:', ':warning:', ':children_crossing:', ':trident:', ':fleur_de_lis:', ':beginner:', ':recycle:', ':white_check_mark:', '🈯️', ':chart:', ':sparkle:', ':eight_spoked_asterisk:', ':negative_squared_cross_mark:', ':globe_with_meridians:', ':diamond_shape_with_a_dot_inside:', ':m:', ':cyclone:', ':zzz:', ':atm:', ':wc:', '♿️', ':parking:', ':u7a7a:', ':sa:', ':passport_control:', ':customs:', ':baggage_claim:', ':left_luggage:', ':mens:', ':womens:', ':baby_symbol:', ':restroom:', ':put_litter_in_its_place:', ':cinema:', ':signal_strength:', ':koko:', ':symbols:', ':information_source:', ':abc:', ':abcd:', ':capital_abcd:', ':ng:', ':ok:', ':up:', ':cool:', ':new:', ':free:', ':zero:', ':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:', ':keycap_ten:', ':1234:', ':hash:', ':asterisk:', ':eject:', ':arrow_forward:', ':pause_button:', ':play_pause:', ':stop_button:', ':record_button:', ':track_next:', ':track_previous:', ':fast_forward:', ':rewind:', ':arrow_double_up:', ':arrow_double_down:', ':arrow_backward:', ':arrow_up_small:', ':arrow_down_small:', ':arrow_right:', ':arrow_left:', ':arrow_up:', ':arrow_down:', ':arrow_upper_right:', ':arrow_lower_right:', ':arrow_lower_left:', ':arrow_upper_left:', ':arrow_up_down:', ':left_right_arrow:', ':arrow_right_hook:', ':leftwards_arrow_with_hook:', ':arrow_heading_up:', ':arrow_heading_down:', ':twisted_rightwards_arrows:', ':repeat:', ':repeat_one:', ':arrows_counterclockwise:', ':arrows_clockwise:', ':musical_note:', ':notes:', ':heavy_plus_sign:', ':heavy_minus_sign:', ':heavy_division_sign:', ':heavy_multiplication_x:', ':infinity:', ':heavy_dollar_sign:', ':currency_exchange:', ':tm:', ':copyright:', ':registered:', ':wavy_dash:', ':curly_loop:', ':loop:', ':end:', ':back:', ':on:', ':top:', ':soon:', ':heavy_check_mark:', ':ballot_box_with_check:', ':radio_button:', '⚪️', '⚫️', ':red_circle:', ':blue_circle:', ':small_red_triangle:', ':small_red_triangle_down:', ':small_orange_diamond:', ':small_blue_diamond:', ':large_orange_diamond:', ':large_blue_diamond:', ':white_square_button:', ':black_square_button:', ':black_small_square:', ':white_small_square:', '◾️', '◽️', ':black_medium_square:', ':white_medium_square:', '⬛️', '⬜️', ':speaker:', ':mute:', ':sound:', ':loud_sound:', ':bell:', ':no_bell:', ':mega:', ':loudspeaker:', ':eye_in_speech_bubble:', ':speech_balloon:', ':thought_balloon:', ':anger_right:', ':spades:', ':clubs:', ':hearts:', ':diamonds:', ':black_joker:', ':flower_playing_cards:', '🀄️', ':clock1:', ':clock2:', ':clock3:', ':clock4:', ':clock5:', ':clock6:', ':clock7:', ':clock8:', ':clock9:', ':clock10:', ':clock11:', ':clock12:', ':clock130:', ':clock230:', ':clock330:', ':clock430:', ':clock530:', ':clock630:', ':clock730:', ':clock830:', ':clock930:', ':clock1030:', ':clock1130:', ':flag_white:', ':flag_black:', ':checkered_flag:', ':triangular_flag_on_post:', ':rainbow_flag:', ':pirate_flag:', ':flag_af:', ':flag_ax:', ':flag_al:', ':flag_dz:', ':flag_as:', ':flag_ad:', ':flag_ao:', ':flag_ai:', ':flag_aq:', ':flag_ag:', ':flag_ar:', ':flag_am:', ':flag_aw:', ':flag_au:', ':flag_at:', ':flag_az:', ':flag_bs:', ':flag_bh:', ':flag_bd:', ':flag_bb:', ':flag_by:', ':flag_be:', ':flag_bz:', ':flag_bj:', ':flag_bm:', ':flag_bt:', ':flag_bo:', ':flag_ba:', ':flag_bw:', ':flag_br:', ':flag_io:', ':flag_vg:', ':flag_bn:', ':flag_bg:', ':flag_bf:', ':flag_bi:', ':flag_kh:', ':flag_cm:', ':flag_ca:', ':flag_ic:', ':flag_cv:', ':flag_bq:', ':flag_ky:', ':flag_cf:', ':flag_td:', ':flag_cl:', ':flag_cn:', ':flag_cx:', ':flag_cc:', ':flag_co:', ':flag_km:', ':flag_cg:', ':flag_cd:', ':flag_ck:', ':flag_cr:', ':flag_ci:', ':flag_hr:', ':flag_cu:', ':flag_cw:', ':flag_cy:', ':flag_cz:', ':flag_dk:', ':flag_dj:', ':flag_dm:', ':flag_do:', ':flag_ec:', ':flag_eg:', ':flag_sv:', ':flag_gq:', ':flag_er:', ':flag_ee:', ':flag_et:', ':flag_eu:', ':flag_fk:', ':flag_fo:', ':flag_fj:', ':flag_fi:', ':flag_fr:', ':flag_gf:', ':flag_pf:', ':flag_tf:', ':flag_ga:', ':flag_gm:', ':flag_ge:', ':flag_de:', ':flag_gh:', ':flag_gi:', ':flag_gr:', ':flag_gl:', ':flag_gd:', ':flag_gp:', ':flag_gu:', ':flag_gt:', ':flag_gg:', ':flag_gn:', ':flag_gw:', ':flag_gy:', ':flag_ht:', ':flag_hn:', ':flag_hk:', ':flag_hu:', ':flag_is:', ':flag_in:', ':flag_id:', ':flag_ir:', ':flag_iq:', ':flag_ie:', ':flag_im:', ':flag_il:', ':flag_it:', ':flag_jm:', ':flag_jp:', ':crossed_flags:', ':flag_je:', ':flag_jo:', ':flag_kz:', ':flag_ke:', ':flag_ki:', ':flag_xk:', ':flag_kw:', ':flag_kg:', ':flag_la:', ':flag_lv:', ':flag_lb:', ':flag_ls:', ':flag_lr:', ':flag_ly:', ':flag_li:', ':flag_lt:', ':flag_lu:', ':flag_mo:', ':flag_mk:', ':flag_mg:', ':flag_mw:', ':flag_my:', ':flag_mv:', ':flag_ml:', ':flag_mt:', ':flag_mh:', ':flag_mq:', ':flag_mr:', ':flag_mu:', ':flag_yt:', ':flag_mx:', ':flag_fm:', ':flag_md:', ':flag_mc:', ':flag_mn:', ':flag_me:', ':flag_ms:', ':flag_ma:', ':flag_mz:', ':flag_mm:', ':flag_na:', ':flag_nr:', ':flag_np:', ':flag_nl:', ':flag_nc:', ':flag_nz:', ':flag_ni:', ':flag_ne:', ':flag_ng:', ':flag_nu:', ':flag_nf:', ':flag_kp:', ':flag_mp:', ':flag_no:', ':flag_om:', ':flag_pk:', ':flag_pw:', ':flag_ps:', ':flag_pa:', ':flag_pg:', ':flag_py:', ':flag_pe:', ':flag_ph:', ':flag_pn:', ':flag_pl:', ':flag_pt:', ':flag_pr:', ':flag_qa:', ':flag_re:', ':flag_ro:', ':flag_ru:', ':flag_rw:', ':flag_ws:', ':flag_sm:', ':flag_sa:', ':flag_sn:', ':flag_rs:', ':flag_sc:', ':flag_sl:', ':flag_sg:', ':flag_sx:', ':flag_sk:', ':flag_si:', ':flag_gs:', ':flag_sb:', ':flag_so:', ':flag_za:', ':flag_kr:', ':flag_ss:', ':flag_es:', ':flag_lk:', ':flag_bl:', ':flag_sh:', ':flag_kn:', ':flag_lc:', ':flag_pm:', ':flag_vc:', ':flag_sd:', ':flag_sr:', ':flag_sz:', ':flag_se:', ':flag_ch:', ':flag_sy:', ':flag_tw:', ':flag_tj:', ':flag_tz:', ':flag_th:', ':flag_tl:', ':flag_tg:', ':flag_tk:', ':flag_to:', ':flag_tt:', ':flag_tn:', ':flag_tr:', ':flag_tm:', ':flag_tc:', ':flag_tv:', ':flag_vi:', ':flag_ug:', ':flag_ua:', ':flag_ae:', ':flag_gb:', ':england:', ':scotland:', ':wales:', ':united_nations:', ':flag_us:', ':flag_uy:', ':flag_uz:', ':flag_vu:', ':flag_va:', ':flag_ve:', ':flag_vn:', ':flag_wf:', ':flag_eh:', ':flag_ye:', ':flag_zm:']


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
            "https://lh3.googleusercontent.com/proxy/RmbSxY0rLbunWqTvdW0OOwdEdgxHRuUmM2WPQEZ-kxaUyRz6afkZdx0OOKGGTKMhrJBJ66-DCmI60Aafok2swrhU2fZHRF5lWTy6sEiCLd-tJcI63Gfs9ehwbU4",
            "https://content6.livejasminbabes.net/arielrebel.com/0128/11.jpg",
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


@client.event
async def on_message(message):
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
    if message.content=='user':
        await message.channel.send(str(user_id))

    if message.content.startswith("Combien de fois j'ai dit le mot :"):
        mot=''
        for i in range(34,len(message.content)):
            mot+=message.content[i]
        await message.channel.send('Vous avez dit '+str(rec_mot(str(message.author)+'.txt',mot.lower()))+' fois le mot "'+mot+'"')
     
    
    
    if(message.content=="Dis nous tout Fun 2.0"):
        await message.channel.send("Bonjour tout le monde ! Je suis Fun 2.0. En gros je suis comme Fun sauf qu'on va le terminer ensemble ce putain de jeu secret ;). Sur ce, bisous et à bientôt !")
        
    if (message.content=="sendimages"):
        i=randint(0,len(biend))
        oui = biend[i]
        bien_embed = discord.Embed(title='Tiens tes nudes \ud83d\ude09 ('+str(i)+')',type='rich')
        bien_embed.set_image(url=oui)
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

    if message.content.startswith('Joueurs :'):
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
    sondage = False
    if message.content.startswith("Sondage :"):
        await message.channel.send(liste_emoji)
        sondage = True
    
    if sondage:
        liste_message=message.content.split(" ")
        for i in range(len(liste_message)):
            if liste_message[i] in liste_emoji:
                await message.add_reaction(liste_message[i])
client.run(os.environ['TOKEN'])
    
