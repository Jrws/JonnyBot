const Commando = require('discord.js-commando');
const gen = require('random-seed');
const path = require('path');
const deadline = require('readline');
const fs = require('fs');

const config = require(path.join(__dirname, '/info/config.json'));
const bot = new Commando.Client({
  commandPrefix: '~',
  owner: config.owner,
  unknownCommandResponse: false
});
bot.registry
  .registerDefaultTypes()
  .registerGroups([
    ['fun','Fun commands'],
    ['edu','Commands for learning']
  ])
  .registerDefaultGroups()
  .registerDefaultCommands()
  .registerCommandsIn(path.join(__dirname, "commands"))

const readRoots = require('readline').createInterface({
  input: require('fs').createReadStream(path.join(__dirname, '/info/roots.txt'))
});

var roots = [];
readRoots.on('line', function (line) {
  roots.push(line);
});

const eightball = [
                    ["It is almost certain.",
                    "Without a doubt.",
                    "Yes definitely.",
                    "Outlook good.",
                    "Most likely."],

                    ["Reply hazy.",
                    "ERROR 404: Answer not found.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Maybe, maybe not."],

                    ["Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
                  ];

/*bot.on("message", message => {
    var msg = message.content.toLowerCase();
    var prefix = "~";

});*/

bot.on("ready", () => {
    console.log("======");
    console.log("Logged in as");
    console.log(bot.user.username);
    console.log(bot.user.id);
    console.log("======");
});

bot.login(config.token);
