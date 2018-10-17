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
            
            
        ];

        var oui = bien[Math.floor(Math.random() * bien.length)];

        var bien_embed = new Discord.RichEmbed()
        .setImage(oui)
        message.channel.send(bien_embed)
    };
    
    if (message.content.startsWith('Bonjour le bot !')){
        message.reply('Salut mec, ça va tu passes une bonne journée ?')
    };
    
    if (message.content === 'Ca va et toi ?'){
        message.reply('Bah tranquille')
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
            "Mettre en place  	",           
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
        message.channel.send('Voilà les différentes commandes :\n - TA MERE !\n - Pour les fameuses photos, faire "sendimages" AUTORISE SEULEMENT DANS LE SALON DEDIE !')
    };
});
