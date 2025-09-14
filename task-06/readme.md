nitial Setup and Configuration ⚙️

The bot's implementation starts with setting up its foundation.

    Imports: It first imports necessary libraries: discord and commands for bot functionality, random for role assignment, asyncio for handling timed tasks, and os with dotenv to securely load your bot's secret token.

    Environment Variables: load_dotenv() loads variables from a .env file. This is best practice for keeping your BOT_TOKEN secret and not hardcoding it directly in the script.

    Constants: The script defines constants for key channel IDs (MAIN, ORIENTATION, ANOUNCEMENTS). This makes the code cleaner and easier to update if you ever change these channels.

    Bot Instance: The line bot = commands.Bot(command_prefix="!" , intents = discord.Intents.all()) is crucial. It creates the bot instance.

        command_prefix="!" tells the bot to listen for messages that start with !.

        intents = discord.Intents.all() grants the bot permission to receive all types of data from Discord, like member join events and message content.

Event-Driven Functions 🤖

The bot is designed to react to specific events happening on your Discord server. This is handled by functions marked with the @bot.event decorator.

    Bot Startup: on_ready()

    This function runs only once when the bot successfully connects to Discord. It prints "hello brodie!!" to your terminal to confirm it's running and sends a public "Hello! Friendly Neighbourhood Bot is activated." message to the MAIN channel.

    New Member Onboarding: on_member_join(member)

    This function is triggered automatically whenever a new user joins the server.

        It gets the ORIENTATION channel object.

        It finds the "Aspiring Hero" and "New Student" roles on your server.

        It sends a personalized welcome message, mentioning the new member (f"Welcome {member.mention}...").

        It then uses random.choice() to randomly assign one of the two roles to the new member.

    Message Moderation: on_message(message)

    This is one of the most important event handlers, as it runs for every single message sent in the server.

        It first checks if the message author is a bot (if message.author.bot: return). This is a critical step to prevent the bot from replying to itself or other bots, which could cause an infinite loop.

        It then loops through your FORBIDDEN list. If any of the forbidden words or phrases are found in the message content (converted to lowercase), it immediately deletes the message and sends a private DM to the author. The return statement stops any further action.

        If the message is clean, the code reaches await bot.process_commands(message). This line is vital because the on_message event normally overrides the bot's ability to see commands. This line tells the bot to check the message for any commands (like !wisdom) after it has been cleared by the moderation filter.

User Commands 🗣️

These are functions that users can trigger by typing a message with the ! prefix. They are defined with the @bot.command() decorator.

    !wisdom Command

    This command provides quick access to server information stored in the WISDOM dictionary.

        It accepts one argument, type (e.g., !wisdom rules).

        It checks if the type provided by the user exists as a key in the WISDOM dictionary.

        If it exists, the bot sends the corresponding value. If not, it sends an error message telling the user the valid options.

    !bugle Command

    This is a moderator-only command for making temporary announcements.

        @commands.has_role("faculty"): This decorator restricts the command's use to only those members who have the "faculty" role. If anyone else tries to use it, the bot will automatically send an error.

        The command takes all text after !bugle as a single message.

        It sends this message to the ANOUNCEMENTS channel and stores the sent message object in the announcement variable.

        It then defines an inner asynchronous function shred(). Inside shred, the bot waits for 24 hours (asyncio.sleep(24*60*60)). After the wait, it checks if the announcement message has been pinned. If it has not been pinned, it deletes the message.

        Finally, bot.loop.create_task(shred()) schedules the shred function to run in the background without pausing the rest of the bot's operations.

