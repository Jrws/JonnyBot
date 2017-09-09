const { Command } = require('discord.js-commando');
const gen = require('random-seed');
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

module.exports = class ReplyCommand extends Command {
  constructor(client) {
    super(client, {
      name: '8ball',
      group: 'fun',
      memberName: '8ball',
      description: 'Returns a yes/no/idk response for a question asked.',
      examples: ['~8ball Are you sure about that?']
    });
  }

  run(message) {
    var rand = gen.create(message.content.toLowerCase())(3);
    return message.reply(eightball[rand][Math.floor(Math.random() * eightball[rand].length)]);
  }
};
