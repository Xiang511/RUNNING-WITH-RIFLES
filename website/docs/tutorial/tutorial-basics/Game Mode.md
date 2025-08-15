---
sidebar_position: 2
tags:
  - Tutorial-basics
  - Game Mode
---

## intro 

### Campaign
The campaign in RWR is a series of Invasion type maps where you conquer the continent one map at a time. Each map has you starting with only one base and having to advance through either Graycollars or Brownpants resistance, or sometimes even both at the same time.

After defeating a map, you can choose the path to go and so choose your next map from any adjacent map that is logically connected with a dashed line in the worldview (see Mapview). During the campaign, all XP, RP, and equipment are tracked throughout. You can also turn a singleplayer campaign into a campaign online through local hosting at any time by activating a server by pressing ESC>Activate server. Note: Remember to forward the port that is shown when activating your server !

### Quick Match
To jump right into a simple single player game, just select “Start new quick match” from the main menu. Unlike the campaign, you can adjust your settings freely, such as maximum numbers of bots, your starting rank, etc. The other point that differs it from the campaign is that once played online, players can join either team they want, which makes it suited for PvP sessions.

### Multiplayer Joining
To join an ongoing multiplayer game, simply head to the main menu and hit “Join online game”. You will then be presented with 2 options: “Public server list” or “Manual IP”.

### Public Server List
The public server list is a server browser that shows the open servers that are online. Simply double click a server, select a username, faction, enter a password and initial rank, and hit “Start!”. If you can't join a server, it might either run an obsolete version of the game or the host didn't forward the UDP port required (default port: 1234)

### Manual IP
To connect via a direct connection using an IP address, select “Manual IP”, enter the address and port of the host server, select a username and password, a faction, initial rank, and hit “Start!”.

The server list is mainly for open games that anyone can join. Therefore, if you wish to play with a few select friends only, when hosting, choose not to advertize the server on the server browser and connect via manual IP.

### Multiplayer Hosting
Hosting a multiplayer is as easy as setting up your own quickmatch game or campaign as shown previously, hitting “ESC” to get to the main menu, and then hitting the “Activate server” button.

1.Port number. **Please ensure this port is properly forwarded!

2.Your username. This will show up on the browser as the server name.

3.If you wish to make a public game, select yes. For private matches, select no.

4.Start the match.

5.Back to main menu.

:::tip

Once you hit “Start!” the server will be open for connections. If people are having issues connecting with your server, please check to make sure that the port is properly forwarded. 

:::

:::info

We will not go into details about how to do this. To get instructions on port forwarding, please do a Google search or check the manual of your router.

:::


## Detailed

There are 8 game modes ingame right now: Quick Match, Invasion, Classic, Dominance, Minimodes, Teddy Hunt, Team elimination and Deathmatch.

***Quick Match*** is the "sandbox" standard game mode where all stock weapons are unlocked and players are free to join whichever faction they like. The rank which you start with can be set freely. In this mode you can capture any base you want as there are no restriction rules. This mode in online can only be hosted as a client server.

***Classic*** is similar to Quick Match but has a few more defined rules like round timers and a map rotation. On most server it is also set that you can only capture 1 base (server admin can customize that) to avoid backdooring and base capture rotation. This mode in online can only be hosted as a dedicated server.

***Invasion*** is a coop campaign type game mode where everyone joins the same faction: Brownpants (as of 1.5). In the join server menu, you will be defaulted to Graycollars no matter what. Along with this game mode being coop, there are a couple major differences from the standard quick match, such as specific side missions. Another difference is that the XP progression is around 73% slower and your progression throughout the campaign is persistent (XP/RP/stash content). There is also an official invasion server realm consisting in a few servers which share the profile with each other so that you can play on one of them and switch to another one and continue with the same progression. Invasion can either be hosted as a client server (start campaign and activating your game online for others to join) or as dedicated server.

The ***Dominance*** mode is a modified version of Classic focusing more on persistency and slower progression, similar to Invasion in that regard. This mode in online can only be hosted as a dedicated server.

Main features:

1) Persistent profiles: when you leave the match, you'll still have the equipment/XP/RP/stats you had when you join again

2) FoV is enabled on default which means you won't see the enemies/items/vehicles when your soldier doesn't have a direct visual line of sight to them 

3) Overall/Match stats (on the scoreboard (default F1), you can switch between them by pressing the top banner)

4) No death penalty (No XP lost)

5) Lower equipment requirement for most items

6) Max amount of AI soldiers under your control is 4 (instead of 10 in other modes)

7) No elites, no valuables drops and no rare weapons

8) Killing a bot gives you 2XP+1RP, killing a human 20XP+20RP, capturing a base up to 50RP. Spotting and destroying of vehicles give less reward than in invasion

9) Max time a map lasts is 30 minutes. If noone won after the time ran out, the faction with the most bases will be victorious

10) extended single base capture system where sometimes you have more than one base that can be captured at time, the main objective which is the bigger red marker and optional smaller red markers. The AI commander will only target the main objective but players are free to choose which base to capture

11) Some maps have bases left out to keep the fighting territory smaller

In ***Minimodes***, a map consists in having different sub-stage modes, such as Team Deathmatch, Team Teddy Hunt, King of the Hill, Delivery (not yet), Target (not yet). The sub-stages are usually 2-3 bases, keeping the playfield tight. Leaving the battle zone is not possible as there is a death-zone around the sub-stages. In minimodes the match starts only when a set number of humans join, default being 2. There are also a few bots but those will vanish once there are enough people in. This mode in online can only be hosted as a dedicated server.

***Teddy Hunt*** is a variance of Capture the flag. You have special crates somewhere on the map (the commander will indicate you roughly where it is) that need to be destroyed and a teddy bear will be dropped. These will need to be sold at an armory (or mobile armory) to make your team score. The enemy team(s) need to do the same and also prevent you in doing so. The special crates are defended by the Teddy Guardians, an AI faction.

The winner of the round is the faction who delivered the most teddies. This mode in online can only be hosted as a dedicated server.

In ***Team elimination***, your goal is to either annihilate the entire enemy team or to destroy the enemy Comms truck. In this case, your team will score and a new round will start. There are NO bots in this mode, it's pure PVP and FoV is enabled on default (you only see enemies/vehicles when you have direct vision to them, e.g. you won't see an enemy if there is a building between you and him). When you die in this mode you won't be able to respawn until the round has ended. You will have an extended view to be able to see what your team mates are doing. There is only one map so far which has been specifically designed for this game mode. This game mode can only be hosted throughout a dedicated server. The server starts in a warmup phase and the real match starts after you type "/start" in the chat.

In ***Deathmatch***, the goal is self explanatory. You score for each kill you achieve. You can change your appearance by changing your "costume" at an armory. If you respawn, the server will choose a spawnpoint where there is no enemy around. There are NO bots in this mode, it's pure PVP. This mode in online can only be hosted as a dedicated server.

***Man vs World*** is a purely single player campaign in which the player is the sole soldier. The player has to capture all of the bases in the map in order to progress to the next map. Permadeath is enabled for both the player and AI. However, the player is able to sustain 10 shots before dying. There is also a veteran mode in which fov(field of view) is enabled.