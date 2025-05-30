const mineflayer = require('mineflayer');

const serverip = process.argv[2];
const server_port = parseInt(process.argv[3]);
const version = process.argv[4];
const bot_name = process.argv[5];
const password = process.argv[6];

function botjoining(serverip, server_port, version, bot_name, password) {
    // create bot
    let bot = mineflayer.createBot({
        host: serverip,
        port: server_port,
        username: bot_name,
        version: version || false
    });

    // log every chat message received
    bot.on('message', (message) => {
        console.log(`[Chat] ${message.toString()}`);
    });

    // when bot joins the server
    bot.on('spawn', () => {
        console.log(`Bot ${bot.username} joined. Waiting 5 seconds before sending /login...`);
        setTimeout(() => {
            bot.chat(`/login ${password}`);
            console.log(`Bot ${bot.username} sent /login ${password}`);
        }, 5000);

        // leave after 10 seconds total (5 wait + 5 more)
        setTimeout(() => {
            bot.quit();
            console.log(`Bot ${bot.username} disconnected`);
        }, 10000);
    });

    bot.on('error', err => {
        console.log(`Error in ${bot.username}:`, err.message);
    });
}

botjoining(serverip, server_port, version, bot_name, password);
