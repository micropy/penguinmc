const mineflayer = require('mineflayer');

const serverip = process.argv[2];
const server_port = process.argv[3];
const version = process.argv[4];
const bot_amount = parseInt(process.argv[5], 10);
const bot_name = process.argv[6];
const timein = parseInt(process.argv[7], 10); 

function botjoining(serverip, server_port, version, bot_amount, bot_name, timein) {
    // create bots
    for (let i = 0; i < bot_amount; i++) {
        let bot = mineflayer.createBot({
            host: serverip,
            port: server_port,
            username: `${bot_name}${i}`,
            version: version || false
        });
        // join bots
        bot.on('spawn', () => {
            console.log(`bot: ${bot.username} connected`);
            // stay bots in the server
            setTimeout(() => {
                bot.quit();
            }, timein * 1000);
        });

        bot.on('error', err => {
            console.log(`Error in ${bot.username}:`);
        });
    }
}

botjoining(serverip, server_port, version, bot_amount, bot_name, timein);