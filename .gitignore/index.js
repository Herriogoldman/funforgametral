const Discord = require('discord.js');

var bot = new Discord.Client();

bot.on('ready', () => {
    console.log("Bot Ready !");
});

bot.login(process.env.TOKEN);

bot.on('message', message => {  
    if (message.content.startsWith ("stp")){
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
            
        ];

        var oui = bien[Math.floor(Math.random() * bien.length)];

        var bien_embed = new Discord.RichEmbed()
        .setImage(oui)
        message.channel.send(bien_embed)
    };
});

bot.on('message', message=> {
    if (message.content.startsWith('Bonjour le bot !')){
        message.reply('Salut mec, ça va tu passes une bonne journée ?')
    }
});

bot.on('message', message=> {
    if (message.content === 'Ca va et toi ?'){
        message.reply('Bah tranquille')
    }
});

bot.on('message', message=> {
    if (message.content === '12'){
        message.channel.send('E-GREC !!!')
    }
});

bot.on('message', message=> {
    if (message.content === 'y'){
        message.channel.send('12 !!!')
    }
});

bot.on('message', message=> {
    if (message.content === 'Y'){
        message.channel.send('12 !!!')
    }
});

bot.on('message', message=> {
    if (message.content === 'e-grec'){
        message.channel.send('12 !!!')
    }
});

bot.on('message', message=> {
    if (message.content === 'E-grec'){
        message.channel.send('12 !!!')
    }
});

bot.on('message', message=> {
    if (message.content === 'E-GREC'){
        message.channel.send('12 !!!')
    }
});

bot.on('message', message=> {
    if (message.content === 'oui'){
        message.channel.send('fi')
    }
});

bot.on('message', message=> {
    if (message.content === 'OUI'){
        message.channel.send('FI')
    }
});

bot.on('message', message=> {
    if (message.content === 'Oui'){
        message.channel.send('Fi')
    }
});

bot.on('message', message=> {
    if (message.content.includes('zinzolé')){
        var verbes = [
            "Accueillir",
            "Corriger",	
            "Gérer",	
            "Proposer",
            "Acheter",	
            "Créer",              	
            "Identifier",	
            "Réaliser",
            "Analyser ",           	
            "Décliner ", 	
            "Illustrer ",          	
            "Recevoir",
            "Animer",	
            "Décrire",	
            "Informer",	
            "Rechercher",
            "Appliquer",                	
            "Défendre",
            "Interpréter",
            "Récompenser",
            "Argumenter ", 	
            "Définir",           	
            "Interroger ",          	
            "Recruter",
            "Arranger",	
            "Démontrer",	
            "Interviewer",	
            "Rédiger",
            "Assembler"	,
            "Développer ",	
            "Juger"	,
            "Réduire",
            "Associer",	
            "Ecouter",	
            "Justifier" , 	
            "Relancer",
            "Assurer",	
            "Écrire"	,
            "Lister",	
            "Réparer",
            "Auditer",	
            "Editer",	
            "Manager",	
            "Repérer",
            "Augmenter"	,
            "Elaborer",	
            "Mémoriser"	,
            "Résoudre"  ,             
            "Calculer",	
            "Elargir",
            "Mettre en place  	",
            "Résumer",
            "Choisir" ,            	
            "Encadrer",	
            "Mettre en relation",     
            "Saisir",
            "Classer",	
            "Estimer" ,           
            "Modifier"	,
            "Schématiser",
            "Collecter"  ,
            "Etablir",	
            "Montrer",	
            "Séduire" ,     
            "Communiquer",	
            "Étudier",  	
            "Motiver",	
            "Sélectionner" ,                 
            "Comparer"	,
            "Évaluer",
            "Négocier",	
            "Soutenir" , 
            "Comprendre",
            "Examiner"	,
            "Nommer"	,
            "Tenir",
            "Concevoir"   ,           
            "Expliquer"  ,              	
            "Opérer"    ,         
            "Tester" , 
            "Conduire",	
            "Fabriquer",	
            "Optimiser",	
            "Traduire",
            "Conseiller",	
            "Faire"	,
            "Organiser"	,
            "Utiliser",
            "Construire" ,  	
            "Faire avancer",	
            "Parler"	,
            "Valider"   ,            
            "Contrôler"	,
            "Faire découvrir",	
            "Piloter",	
            "Valoriser",
            "Convaincre",	
            "Faire mémoriser",	
            "Planifier"	,
            "Vendre",
            "Coordonner",	
            "Fidéliser"	,
            "Poser"	,
            "Visualiser"  ,
            "Copier"	,
            "Former"	,
            "Préparer",
            "Violer",
            "Baiser",
            "Sucer",
            "Lecher"       
        ];       
        var ok = verbes[Math.floor(Math.random() * verbes.length)];
        message.channel.send("Ici le verbe zinzoler = " + ok)
    };
});    

bot.on('message', message => {
    if (message.content === 'Dommage'){
        message.channel.send("A ça !")
    }
});

bot.on('message', message => {
    if (message.content==='Ah !'){
        var ah = "https://lh3.googleusercontent.com/WcSWqqt-Dq-1WhE7z7M0TMTIMVK8JSuq49xRLXYZeTrDkg9kKMGHioqe4XJJYRSMaAa0=s180"
        message.channel.send(ah)
    }
});
