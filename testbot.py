import os #for env vars
import sys 
from twitchio.ext import commands
from twitchio.ext import routines
from dotenv import load_dotenv
import asyncio

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

load_dotenv()

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(client_id=os.environ['CLIENT_ID'], token=os.environ['TMI_TOKEN'], prefix=os.environ['BOT_PREFIX'], initial_channels=[os.environ['CHANNEL']])
        
        self.cred = credentials.Certificate("testtwitchbot-be33d-firebase-adminsdk-mw5l2-d25319f7d0.json")
        firebase_admin.initialize_app(self.cred, {'databaseURL': 'https://testtwitchbot-be33d-default-rtdb.firebaseio.com'})
        self.data = db.reference('/Test').get()
        self.score = self.data.get('Score')
        self.metaract = self.data.get('Metaract') 
        self.interval = self.data.get('Interval') 

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        
        self.channel = self.connected_channels[0]
        #await self.channel.send(os.environ['CLIENT_ID'])

    async def event_join(self, channel, user):
        if user.name == self.nick:
            await channel.send(f"{self.nick} is now online!")    

            self.looping = True
            #loop = asyncio.get_event_loop()
            while(self.looping):
                #loop.create_task(self.channel.send(f'Newest feature: {self.metaract}'))
                try:
                    await channel.send(f'Newest feature: {self.metaract}')
                    await asyncio.sleep(int(self.interval))
                except TypeError:
                    print("Interval was not int, or could not be converted to int.")
    '''
    @routines.routine(seconds=5.0, iterations=5)
    async def promote(arg: str):
        print(f'Hello {arg}!')
        #chan = self.get_channel("channelname")
        #print(chan)
    promote.start("world")
    '''
    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo: #if message.author.name == self.nick
             return
        
        # Print the contents of our message to console...
        print(message.content)
        '''
        async def event_message(self, message):
            if message.echo:
                return

            message.content = f"#z {message.content}" # add command name before message

            await self.handle_commands(message)

        @commands.command()
        async def z(self, ctx: commands.Context):
            print(f"Original message is {ctx.message.content[3:]}\n")
        '''
        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    #async def send_message(self, message):
       # await self.channel.send(message)

    @commands.command()
    async def stop(self, ctx: commands.Context):
        self.looping = False
        await ctx.send(f'loop stopped')

    @commands.command()
    async def moblabs(self, ctx: commands.Context):
        await ctx.send(f'My newest feature is {self.metaract}')

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send("to run command, send ![command name]. run !command_list to see list of commands.")
        #await ctx.send("to see list of commands, send !command_list")

    @commands.command()
    async def command_list(self, ctx: commands.Context):
        list = ""
        for command in self.commands:
            list += command + ", "
        list = list[:-2]
        await ctx.send(list)

    @commands.command()
    async def quit(self, ctx: commands.Context):
        await self.close()
        await self.loop.shutdown_asyncgens()
        await super().close()
        sys.exit(0)


def main():
      
    bot = Bot()
    bot.run()
    #asyncio.run(bot.send_message("hi"))
    

if __name__ == "__main__":
    main()