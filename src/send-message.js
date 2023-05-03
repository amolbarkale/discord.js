const {
  MessageActionRow,
  Client,
  Intents,
  MessageButton,
} = require("discord.js");
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

const roles = [
  {
    id: "",
    label: "Red",
  },
  {
    id: "",
    label: "Green",
  },
  {
    id: "",
    label: "Blue",
  },
];

client.login(process.env.TOKEN);
