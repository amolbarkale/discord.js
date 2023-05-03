const { MessageActionRow, Client, Intents, MessageButton } = require("discord.js");
require("dotenv").config();

const client = new Client({
  intents: [
    Intents.FLAGS.GUILDS,
    Intents.FLAGS.GUILD_MESSAGES,
    Intents.FLAGS.GUILD_MEMBERS,
  ],
});

client.on("ready", () => {
  console.log(`${client.user.tag} is online✅`);
});

client.on("messageCreate", (message) => {
  if (message.author.bot) {
    return;
  }
  if (message.content === "hello") {
    message.reply("Hey!");
  }
});

client.on("messageCreate", (message) => {
  if (message.content === "!custominput") {
    const filter = (m) => m.author.id === message.author.id;
    const collector = message.channel.createMessageCollector({
      filter,
      max: 1,
    });

    const row = new MessageActionRow().addComponents(
      new MessageButton()
        .setCustomId("inputButton")
        .setLabel("Submit")
        .setStyle("PRIMARY")
    );

    message.channel
      .send({ content: "Please enter your input:", components: [row] })
      .then(() => {
        collector.on("collect", (m) => {
          message.channel.send(`Your input: ${m.content}`);
        });
      });
  }
});

client.login(process.env.TOKEN);
