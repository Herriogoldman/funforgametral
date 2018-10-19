const Discord = require('discord.js');

var bot = new Discord.Client();

bot.on('ready', () => {
    console.log("Bot Ready !");
});

bot.login(process.env.TOKEN);

bot.on('message', message => {  
    if (message.content.startsWith ("sendimages")){
        var bien = [
            
            "http://img.over-blog-kiwi.com/0/62/06/01/20140701/ob_03acc5_les-plus-belles-femmes-nues-de-l-ete-4.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZT0E0MTcJpcLYChSljSd3kagEzqcHgP0cvEzlvcf8olU3nWjStA",
            "https://www.tout-bon.com/newpics/40106.jpg",
            "http://www.hotfemmenue.xyz/wp-content/uploads/2017/03/exhib-de-femme-nue-du-70-chaude-et-salope-736x1024.jpg",
            "https://www.bonsoirmademoiselle.fr/wp-content/uploads/2018/04/belle-femme-nue-plus-belle-du-monde.jpg",
            "http://jolies.filles.nues.free.fr/jolies-filles-nues.jpg",
            "http://img.over-blog-kiwi.com/0/62/06/01/20140630/ob_dd29d8_les-plus-belles-femmes-nues-de-l-ete-0.jpg",
            "http://cdn.hotnakedgirls.net/2015-12-30/330251_06.jpg",
            "https://stunnershq.com/images/414/thumb/super-sexy-teen-girl-mila-azul-nude-outside-showing-her-perfect-ass-5.jpg",
            "http://hamadvision.com/376/naked-white-hot-girls.jpg",
            "http://cdn.nudesexporn.com/2018-06-04/527865_08.jpg",
            "http://video.damplips.com/pics/wp-content/uploads/2015/02/naked-girl-masturbates.jpg",
            "https://i2.wp.com/fracturedelaretine.com/wp-content/uploads/2016/01/97183241171.jpg?resize=710%2C1065",
            "http://bonheurdusoir.com/wp-content/uploads/2016/12/42575688-e1480599886800.jpg",
            "https://ftopx.com/images/201405/ftop.ru_101253.jpg",
            "https://i.pinimg.com/474x/5a/89/9a/5a899af65e8b10ce836fb1468850b470--girls-girls-girls-sexy-girls.jpg",
            "http://revalsheva.com/367/918451.jpg",
            "https://shikokuweb.com/images/ed22ececd4f4abaebee0ed4a3baf4e74.jpg",
            "https://madonie.info/images/40267205512a4e3811ea6607f96dce58.jpg",
            "http://tooxme.com/images/147682.jpg",
            "http://mincirfacilement.com/429/sexy-nude-women-tumblr-3.jpg",
            "http://www.bustyteengallery.com/images/016hg/sexy-lesbian-sluts.jpg",
            "http://www.eightminutedeadline.com/img/sexiest-nude-woman-in-the-world-3.jpg",
            "http://www.leonelkaplan.com/img/big-boobs-of-sexy-women-2.jpg",
            "http://salocallowdown.com/393/best-sexy-naked-women.jpg",
            "https://tabrat.info/images/bee2f0cfcb25a6f5aac9b87248c86a67.jpg",
            "http://sexsagar.net/wp-content/uploads/2016/01/sunny-leone-naked-erotic-without-clothes-hd-images.jpg",
            "http://cdn.hotnudegirls.net/2015-05-20/288686_12.jpg",
            "http://kauacademy.com/425/nude-girl-fit-2.jpg",
            "http://coed.cosmosexy.com/ph7/0f72c6915664299d3b39f26761b32dfb.jpg",
            "http://xxxpicz.com/xxx/naked-japanese-teen-portal-real-sexiest-clips-women-mega-world.jpg",
            "http://wm-job.info/images/9e9a0a932b530a4062b11e4cec37aba8.jpg",
            "http://viparea.com/images/samples/img02_large.jpg",
            "https://i.pinimg.com/originals/5c/84/91/5c8491d7d34d5a4f29cc8fcc8098f984.jpg",
            "http://www.acromegalyanswerswebinar.com/img/free-hot-sexy-nude-girls.jpg",
            "https://lastscore.info/images/11f12743d8a548bf31df042f869fcce0.jpg",
            "https://y2.pichunter.com/3415560_9_o.jpg",
            "http://psychologyprogress.com/images/15e8a13e76be70c9b03477b3d37b5918.jpg",
            "http://1.bp.blogspot.com/-R3ZIrog0BrE/Ufp5pDUllQI/AAAAAAACQZc/r68ex4bazm4/s1600/Hawaiian+Tropic+Girls_provatina_com_2.jpg",
            "https://shikokuweb.com/images/c457c498e2e90bbc51868b33dd73480f.gif",
            "http://31.media.tumblr.com/065fafce58c3164307658a464c9bf542/tumblr_nnbvojHXhO1tjd582o1_400.gif",
            "https://media.tits-guru.com/images?uuid=03d1aa18-9a77-4b96-816d-60ae5a2056da",
            "http://pornpictures.xxx/wp-content/uploads/2016/01/naked-perfect-teen-boobs-gif-xxx-girls-free-porn-teen-tits-pussy-pic-gif-video-1452046128plc48.gif",
            "https://78.media.tumblr.com/167d638cebe2fff0217e6473043d76d3/tumblr_o53mlds8ma1s2wsdzo1_400.gif",
            "https://www.livexxx.me/wp-content/uploads/2014/11/Sexy-big-titted-black-haired-babe-shows-dildo1.gif",
            "http://gfpics.com/wp-content/uploads/2-69.gif",
            "http://teen-sex-photos.eu/wp-content/uploads/2016/03/tumblr_nj0hh0ofgJ1tbywgho1_500.gif",
            "http://38.media.tumblr.com/42309cd26437609dda2d2a1d2b8f1bd6/tumblr_nohib8cLDE1tv5llvo1_500.gif",
            "http://68.media.tumblr.com/f0161ab24a8072cb65992320646874d2/tumblr_inline_of5vkgFLbF1sw8ada_500.gif",
            "http://dm.damcdn.net/pics/wp-content/uploads/2012/07/sexy-girl-strip-17.jpg",
            "https://lh3.googleusercontent.com/-eNXlqg9t24k/WyDi7peqt1I/AAAAAAAAAdM/WA6qIbxm_g8t8jr6erIk3xfGVne9MsIdACJoC/w1076-h1437/gplus1238947832.png",
            "https://s9v7j7a4.ssl.hwcdn.net/galleries/new_big/79/1d/13/791d1360ce727d3d9fcad62280f827d5/10.jpg",
            "https://www.classy-girls.com/main/btD0W4ulod.jpg",
            "https://contenta.nakedneighbour.com/sexart.com/0941/11.jpg",
            "https://cdn.pornpics.com/pics/2017-05-18/267919_03big.jpg",
            "http://cdn1.teennudegirls.com/da/2/da226ce9c.jpg",
            "https://pbs.twimg.com/profile_images/824015421154140160/4M0SNK2n_400x400.jpg",
            "http://www.adultwalls.com/web/wallpapers/sexy-pussy-hd-nude-girl-naked-wallpaper/thumbnail/lg.jpg",
            "https://pbs.twimg.com/profile_images/450146843859906560/vjhPacVU.jpeg",
            "http://20muleteammuseum.org/img/hot-sexy-naked-girls-picture-2.jpg",
            "http://zapatosadidas.info/images/56b55460d476e6fb99176f474371c1e3.jpg",
            "http://www.its-nano.eu/image/259161.jpg",
            "https://i.pinimg.com/originals/f9/62/e0/f962e07c4828d50abdc77ec671273266.jpg",
            "http://cantrellandcochrane.com/imgs/16f141214aa3c00311fd150c7e287960.jpg",
            "http://algysbar.com/369/e336f3708b337dca4fe640999e39d636.jpg",
            "http://thekingsleyreport.com/407/637293.jpg",
            "https://content4.morazzia.com/playboyplus.com/5302/06.jpg",
            "https://celeb.gate.cc/media/cache/original/upload/4/e/4e383bde13.jpg",
            "http://qpornx.com/xxx/naked-girls-fingering-pussy.jpg",
            "https://cdn.pornpics.com/pics/2017-01-22/255186_01big.jpg",
            "http://cdn.hotnudegirls.net/2013-06-18/265880_08.jpg",
            "https://dissykosmetik.info/images/77730f334c8a27a6cc109d7587955310.jpg",
            "https://ftopx.com/large/201203/31476.jpg",
            "http://www.met-nude.com/MNPics/MN20130102_Met-Art-Volere-Caprice-A-Indiana-A/img/Met-Art_Volere_Caprice-A--Indiana-A_by_Luca-Helios_medium_0029.jpg",
            "http://sean-rowe.com/412/5f6669f89d69a3e9cfaa01d981536a23.jpg",
            "https://gallery-of-nudes.com/wp-content/uploads/2016/04/Playboy-Playmate-Regina-Deutinger-Pictures-02.jpg",
            "https://i.imagepost.com/wp-content/uploads/2015/10/ana-cheri-for-pb.jpg",
            "https://www.morbomodelospics.com/wp-content/uploads/2015/10/Lindsey-Vuolo-para-Playboy-10.jpg",
            "https://www.tribute-to.com/playboy/2016/01/kristy-garett-an-american-dream-nude/h/kristy-garett-an-american-dream-nude07.jpg",
            "https://gallery-of-nudes.com/wp-content/uploads/2017/02/Playboy-Cybergirl-Jessica-Workman-Nude-03.jpg",
            "http://qpornx.com/xxx/playboy-playmate-centerfold-naked-nude.jpg",
            "http://2.bp.blogspot.com/-vyAvLu4zN4U/UALudgfqcXI/AAAAAAAAIsc/xyjS3J06eHo/s1600/entrou%20model%20sex.jpg",
            "http://xxxpornozone.com/xxx/caprice-x-art-porn.jpg",
            "https://sqmf.info/images/18242d9791d8af51f81eb33acdb22095.jpg",
            "http://www.alafoto.com/wp-content/uploads/2017/02/Playboy-Playmate-Calendar-2014-07.jpg",
            "https://www.cherrynudes.com/roberta-vasquez-classic-playmate/2.jpg",
            "https://www.tribute-to.com/playboy/2015/10/rachel-harris-a-creative-force-nude/h/rachel-harris-a-creative-force-nude09.jpg",
            "http://3.bp.blogspot.com/_pTyKeFv2GpM/Sa1kyS4KnFI/AAAAAAAAAxE/SvI1OX-dDsI/s400/US+Playboy+-+January+2009+%28Carmen+Electra%29+%2811%29.jpg",
            "http://assets.mrstiff.com/uploads/pornstar/jennifer-walcott/jennifer-walcott-106.jpg",
            "https://sqmf.info/images/043fc12deff1cae1adc00c986ecb28bf.jpg",
            "https://lamacchinadeltempo.info/imgs/eff7e659cd0a8911c404692523594413.jpg",
            "http://brasseriepdx.com/imgs/29c2cf42d1d20b09e3a81eb13be7335a.jpg",
            "http://dagenspost.com/413/celebrity-playmates-nude.jpg",
            "https://gallery-of-nudes.com/wp-content/uploads/2016/08/Playboy-Playmate-Amberleigh-West-Nude-Pictures-02-1046x697.jpg",
            "https://celeb.gate.cc/media/cache/original/upload/a/m/amanda-cerny-naked-846963.jpeg",
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
            "http://sutekh.info/images/74ade4548fd970f4a6ba15b265d6ec10.jpg",
            "https://gallery-of-nudes.com/wp-content/uploads/2016/03/playboy-Playmate-Vanessa-Hoelsher-Nude-Photos-04.jpg",
            "http://redbust.com/stuff/regina-deutinger-german-blonde/regina-deutinger-german-nude-playboy-11.jpg",
            "https://content4.babesandgirls.com/playboy-plus/0495/12.jpg",
            "http://greencoffeebeanmaxx.com/418/hot-naked-playmates.jpg",
            "http://imagepost.com/wp-content/uploads/2015/01/31.jpg",
            "https://europeonbike.info/images/be45f111d57c87c3b5b278ec65070108.jpg",
            "http://www.drsnysvet.cz/wp-content/gallery/dd-candace-leilani-2/15.jpg",
            "https://thumb-p0.xhcdn.com/a/fiX95SSMuQsEe7nJ48G7Bw/000/048/992/970_1000.jpg",
            "https://gals.kindgirls.com/d3/zafira776/zafira776_15.jpg",
            "https://ftopx.com/images/201207/ftop.ru_36975.jpg",
            "http://maheev-promo.ru/wp-content/uploads/2016/01/naked-brazilian-models.jpg",
            "http://vpicz.com/pics/1386/lesbian-playboy-girls-nude.jpg",
            "http://campus-online.ru/uploads/posts/porno-lesbiyanki-blondinki-bolshaya-grud.jpg",
            "https://contenta.babesandgirls.com/babesandgirls.com/playboy-sexy-wives/0002/04.jpg",
            "http://vodice-kraljevic.com/379/nude-sexy-playmates.jpg",
            "https://sozosblog.com/images/8f2d37e3621b9e377d410bf988cae148.jpg",
            "http://www.lettherebeporn.com/galleries/2011/3/kelliesmith/kelliesmith_002.jpg",
            "http://qpornx.com/xxx/playboy-college-girls-whitney-leigh-nude.jpg",
            "http://www.momochihama.org/img/sexy-naked-play-boy-girls-2.jpg",
            "https://content4.babesandgirls.com/playboy-plus/0540/07.jpg",
            "https://i.pinimg.com/originals/6c/79/76/6c797658158c361362e3ea1c5b3a6656.jpg",
            "https://media.tits-guru.com/images?uuid=f6959fe9-7323-4a72-92c1-c16e13fa4719",
            "http://images.fuskator.com/large/eyapCVcWLbN/Brande+Roderick_goddess_pbgals_playboy_playmate_playmates_3.jpg",
            "https://rankly.com/images/listitems/6633586.jpg",
            "https://gallery-of-nudes.com/wp-content/uploads/2016/03/playboy-Playmate-Vanessa-Hoelsher-Nude-Photos-05.jpg",
            "https://www.tribute-to.com/playboy/wp-content/uploads/2015/10/ana-cheri-strong-woman-nude.jpg",
            "http://salocallowdown.com/393/045c4d510c435495ab7514ee92b5e846.jpg",
            "https://media.tits-guru.com/images?uuid=dd22f114-8708-46b9-897a-610654d92531",
            "https://content4.morazzia.com/playboyplus.com/4456/07.jpg",
            "http://afroblue.info/images/1a63a3ebf66288da2c1a54e481cee06f.jpg",
            "http://thefappening2015.com/wp-content/uploads/2015/08/Joana-Plankl-nude-in-the-pages-of-Playboy-Germany-%E2%80%93-September-2015-3.jpg",
            "http://www.phun.org/specials/courtney_culkin/courtney_culkin_11.jpg",
            "http://www.epilepsy-brain-mind2014.eu/image/char-naked-in-playboy-4.jpg",
            "https://contenta.morazzia.com/playboyplus.com/0538/06.jpg",
            "http://www.centerfoldsblog.com/wp-content/uploads/2014/06/playboy-playmate-dani-mathers-at-the-beach-posing-her-sexy-curves7.jpg",
            "http://egotasticcom.files.wordpress.com/2009/08/jayde-nicole-nude-playboy-03.jpg",
            "https://content4.morazzia.com/playboyplus.com/6282/08.jpg",
            "http://www.radioaktywni.eu/image/playboy-mansion-twins-naked.jpg",
            "http://www.momochihama.org/img/sexy-naked-play-boy-girls-5.jpg",
            "http://3dtelevisie.info/imgs/046dba5d6359ea299a1cf1bc44649427.jpg",
            "http://nych.info/images/65f93ef1144facf15c631b7c75fd0432.jpg",
            "http://gratuitescolaire.info/imgs/effe957ba05d558d701c028a442b08c4.jpg",
            "http://puuinfo.info/imgs/3e61ba70f7581fe2c4a0de298cffe05b.jpg",
            "https://thumb-p7.xhcdn.com/a/KMtgblUCohJ-r0n67nTJxw/000/048/992/977_1000.jpg",
            "http://snadgy.com/wp-content/uploads/2015/06/kayla-rae-reid-playboy-playmate-of-the-month-july-nude-in-in-eternal-sunshine-07.jpg",
            "https://gallery-of-nudes.com/wp-content/uploads/2016/02/playboy-playmate-val-keil-nude-01.jpg",
            "http://www.tribute-to.com/playboy/2015/01/meghan-leopard-model-month-january-2015-nude/h/meghan-leopard-model-month-january-2015-nude03.jpg",
            "https://i.pinimg.com/236x/c4/f6/ab/c4f6ab12b379b6140d159e5489101efd--playboy-girls-sexy-women.jpg",
            "https://www.tribute-to.com/playboy/2014/07/maggie-may-miss-august-2014-nude/h/maggie-may-miss-august-2014-nude12.jpg",
            "http://www.teenageslut.net/lesbians/hot-teen-lesbian-sex/teen-lesbian-sex-16.jpg",
            "http://qpornx.com/xxx/lesbian-sex-fingering-orgasm.jpg",
            "https://lamacchinadeltempo.info/imgs/6b33606b801497b4046d0689359ab562.jpg",
            "http://dm.damcdn.net/pics/wp-content/uploads/2014/03/naked-girls-lesbian-sex.jpg",
            "https://www.nakedgirls.mobi/contents/videos_screenshots/1000/1422/preview.mp4.jpg",
            "https://www.celebjihad.com/celeb-jihad/images/selena_gomez_lesbian_sex.jpg",
            "http://ftop.ru/large/201502/141110.jpg",
            "http://images.nubilefilms.com/films/impeccable_with_sophie_lynx/screenshots/9.jpg",
            "http://www.bustyteengallery.com/images/10n1q/pussy-wide-open-for-photos.jpg",
            "http://xxxlibz.com/wp-content/uploads/2017/06/12101011-8299-xxxlibz.com.jpg",
            "https://www.thehearingstop.com/images/alabama-hot-kn.jpg",
            "http://ftop.ru/images/201210/ftop.ru_41569.jpg",
            "https://i.ytimg.com/vi/pD9fAHo2wSw/maxresdefault.jpg"
            
        ];

        var oui = bien[Math.floor(Math.random() * bien.length)];

        var bien_embed = new Discord.RichEmbed()
        .setImage(oui)
        .setTitle('Tiens tes nudes \ud83d\ude09')
        message.channel.send(bien_embed)
    };
    
    if (message.content === 'Bonjour le bot !'){
        message.reply('Salut mec, ça va tu passes une bonne journée ?')
    };
    
    if (message.content === 'Ca va le bot ?'){
        message.reply("Ah bah pas ouf, en ce moment y'a vraiment plus de saisons !")
    };
    
    if (message.content === 'Ça va le bot ?'){
        message.reply("Ah bah pas ouf, en ce moment y'a vraiment plus de saisons !")
    };
    
    if (message.content === '12'){
        message.channel.send('E-GREC !!!')
    };
    
    if (message.content === 'y'){
        message.channel.send('12 !!!')
    };
    
    if (message.content === 'Y'){
        message.channel.send('12 !!!')
    };
    
    if (message.content === 'e-grec'){
        message.channel.send('12 !!!')
    };
    
    if (message.content === 'E-grec'){
        message.channel.send('12 !!!')
    };
    
    if (message.content === 'E-GREC'){
        message.channel.send('12 !!!')
    };
    
    if (message.content === 'oui'){
        message.channel.send('fi')
    };
    
    if (message.content === 'OUI'){
        message.channel.send('FI')
    };
    
    if (message.content === 'Oui'){
        message.channel.send('Fi')
    };
    
    if (message.content === 'Celle'){
        message.channel.send('Oh !')
    };
    
    if (message.content.includes('zinzolé')){
        var verbes = [
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
            "Vider"

        ];       
        var ok = verbes[Math.floor(Math.random() * verbes.length)];
        message.channel.send("Ici le verbe Zinzoler = " + ok)
    };
    
    if (message.content === 'Dommage'){
        message.channel.send("A ça !")
    };
    
    if (message.content === 'Ah !'){
        var ah = "https://lh3.googleusercontent.com/WcSWqqt-Dq-1WhE7z7M0TMTIMVK8JSuq49xRLXYZeTrDkg9kKMGHioqe4XJJYRSMaAa0=s180"
        var ah_embed = new Discord.RichEmbed()
        .setImage(ah)
        message.channel.send(ah_embed)
    };
    
    if (message.content === 'aide'){
        message.channel.send('Voilà les différentes commandes :\n - TA MERE !\n - Le bot pourrait étonnement vous répondre si vous lui adressez ce gentil message "Bonjour le bot !" (oubliez pas de lui demander comment il se porte)\n - 12, Y et MDR ne sont pas a zinzolé, Ah ! Dommage ! Et oui !\n - Il se pourrait que "Ce qui" et "veut dire ?" rassemblés mettent en colère le bot !\n - Chibre ?\n - Les prénoms peuvent parfois être utilisés à mauvais essiens\n - Pour les fameuses photos, faire "sendimages" (AUTORISE SEULEMENT DANS LE SALON DEDIE) !')
    };
    
    if (message.content.includes('Ce qui veut dire ?')){
        message.channel.send("La prochaine fois que tu me demandes ce qui veut dire, J'TE RETROUVE ET JE TE NIQUE TA MERE !")
    };
    
    if (message.content.includes('ce qui veut dire ?')){
        message.channel.send("La prochaine fois que tu me demandes ce qui veut dire, J'TE RETROUVE ET JE TE NIQUE TA MERE !")
    };
    
    if (message.content.startsWith('MDR')){
        message.channel.send('Trop drôle !')
    };
    
    if (message.content.includes('Albin')){
        message.channel.send("Albdeux, Albtrois, Albquattre, Albcinq, Albsix")
        message.channel.send('Ordonnées !')        
    };
    
    if (message.content.includes('Loïc')){
        message.channel.send('Loic pas logique, ya pas de g !')
    };
    
    if (message.content.includes('Thomas')){
        message.channel.send('Thommage !')
    };
    
    if (message.content.includes('Ludo ')){
        message.channel.send('VIC')
    };
    
    if (message.content.includes('Ronan')){
        message.channel.send('RHOO NAN, pas un croche-pattes !')
    };
    
    if (message.content === 'Chibre'){
        var chibre = [
            "250 kg de chibre, ça te fait pas peur ?",
            "24/24 7j/7 j'ai qu'un seul objectif, avoir le meilleur chibre de toute la ville",
            "Le matin je pense au chibre, le midi c'est chibre, le soir chibre, même la nuit quand je dors,c'est chibre",
            "Parfois j'fais des rêves autour de plusieurs thématiques, et généralement c'est celle du chibre",
            "Chibre, chibre, chibre, chibre, chibre, chibre ,chibre, chibre, chibre, chibre",
            "Parfois j'pense à rien, parfois j'pense au chibre",
            "Attend une seconde... chibre"
        ];
        
        var chibre2 = chibre[Math.floor(Math.random() * chibre.length)];
        message.channel.send(chibre2)
    };
    
    if (message.content.includes('TA MERE')){
        message.reply('Elle a quoi ma mère batard ?')
    };
    
    if (message.content === 'Bisous'){
        message.channel.send('Bisous poutou \ud83d\ude17')
    };
});
