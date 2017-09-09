const { Command } = require('discord.js-commando');
const path = require('path')
const readRoots = require('readline').createInterface({
  input: require('fs').createReadStream(path.join(__dirname, '/../../info/roots.txt'))
});

var roots = [];
readRoots.on('line', function (line) {
  if (line !== "---") {
    roots.push(line);
  }
});

module.exports = class SayCommand extends Command {
  constructor(client) {
    super(client, {
      name: 'root',
      group: 'edu',
      memberName: 'root',
      description: 'Quizzes you on Latin/Greek roots',
      examples: ['~root [#] - loops certain number of times','~root _ - exits root loop'],
      args: [
        {
            key: 'option',
            prompt: '',
            default: '',
            type: 'string'
        }
      ]
    });
  }

  async run(message, args) {
    if (message.channel.type === "dm") {
      const { option } = args;
      const filter = k => k.author.id === message.author.id;
      if (option === "") {
        const rt = roots[Math.floor(Math.random()*roots.length)].toString();
        const r = {
          root: rt.substr(0,rt.indexOf("=")-1),
          def: rt.substring(rt.indexOf("=")+2,rt.indexOf("|")-1),
          ex: rt.substr(rt.indexOf("|")+2).split(", ")
        }
        message.author.send(r.ex[Math.floor(Math.random()*r.ex.length)].replace(r.root,"**"+r.root+"**"));
        await message.channel.awaitMessages(filter,{max:1})
          .then(ans => {
            if (ans.first().content == r.def) {
              return message.author.send("✅");
            } else {
              return message.author.send("❌ Correct Answer: "+r.def);
            }
          });
      } else if (!isNaN(option)) {
        var exit = 0;
        for (var i=0;i<Number(option);i++) {
          const rt = roots[Math.floor(Math.random()*roots.length)].toString();
          const r = {
            root: rt.substr(0,rt.indexOf("=")-1),
            def: rt.substring(rt.indexOf("=")+2,rt.indexOf("|")-1),
            ex: rt.substr(rt.indexOf("|")+2).split(", ")
          }
          message.author.send(r.ex[Math.floor(Math.random()*r.ex.length)].replace(r.root,"**"+r.root+"**"));
          await message.channel.awaitMessages(filter,{max:1})
            .then(ans => {
              if (ans.first().content === '_') {
                exit = 1
              } else if (ans.first().content == r.def) {
                message.author.send("✅");
              } else {
                message.author.send("❌ Correct Answer: "+r.def);
              }
            });
          if (exit === 1) {
            message.author.send("Done!");
            break;
          }
        }
        if (exit === 0) {
          message.author.send("Done!");
        }
      }
    } else {
      return message.author.send("Only available for use in DMs.")
    }
  }
};
