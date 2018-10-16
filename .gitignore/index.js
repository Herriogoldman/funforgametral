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
            "https://ftopx.com/images/201405/ftop.ru_101253.jpg"
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
        message.channel.send('E-GREC')
    }
});

bot.on('message', message=> {
    if (message.content === 'y'){
        message.reply('12 !!!')
    }
});

bot.on('message', message=> {
    if (message.content === 'Y'){
        message.reply('12 !!!')
    }
});

bot.on('message', message=> {
    if (message.content === 'e-grec'){
        message.reply('12 !!!')
    }
});
